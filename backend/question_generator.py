# backend/question_generator.py

from typing import Tuple
from rag_engine import get_qa_chain


def generate_question(qtype: str, topic: str, difficulty: str) -> Tuple[str, str]:
    """
    Returns (metadata_json, question_and_solution_text).
    If the LLM fails, metadata_json == "{}".
    """
    prompt = (
        f"{qtype}: {topic}, {difficulty}.\n"
        "Return exactly TWO parts:\n"
        "PART-1: one-line JSON with keys "
        "\"type\",\"topic\",\"difficulty\",\"format\".\n"
        "PART-2: the AP-style question plus a six-step solution."
    )

    qa_chain = get_qa_chain()

    try:
        result = qa_chain({"query": prompt})
        text = result["result"]

        if text.strip().startswith("{"):
            meta_line, body = text.split("\n", 1)
            return meta_line, body.strip()
        else:
            return "{}", text.strip()

    except Exception as e:
        return "{}", f"LLM error: {e}"


def main() -> None:
    samples = [
        ("MCQ", "Unit 5: Momentum", "Medium"),
        ("FRQ", "Unit 10: Conductors & Capacitors", "Hard"),
    ]
    for qtype, topic, diff in samples:
        meta, body = generate_question(qtype, topic, diff)
        print("METADATA:", meta)
        print(body)
        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()

