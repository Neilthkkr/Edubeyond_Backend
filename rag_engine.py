# rag_engine.py  — local flan-t5 backend (no OpenAI key needed)

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline


def get_qa_chain():
    """
    Build and return a RetrievalQA chain that uses:
      • your FAISS vector store (Tutor_Guidelines chunks)
      • a local FLAN-T5 small text-generation model
    """

    # 1) Load vector store (allows pickle)
    db = FAISS.load_local(
        "data/vector_db",
        HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
        allow_dangerous_deserialization=True,
    )

    # 2) Retriever wrapper
    retriever = db.as_retriever(search_kwargs={"k": 2})

    # 3) Local text-generation pipeline → LangChain LLM wrapper

    hf_pipe = pipeline(
        "text2text-generation",
        model="google/flan-t5-small",      # ≈250 MB, CPU/GPU/MPS friendly
        tokenizer="google/flan-t5-small",
        max_length=512,        # model's absolute limit
        max_new_tokens=128,    # cap generated text
        truncation=True,       # truncate long prompts automatically
    )
    

    llm = HuggingFacePipeline(pipeline=hf_pipe)

    # 4) Retrieval-augmented QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm,                      # positional arg = LLM
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
    )

    return qa_chain

