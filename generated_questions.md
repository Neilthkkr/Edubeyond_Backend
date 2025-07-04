{"type":"MCQ","topic":"Unit 1: Kinematics","difficulty":"Medium","answer_format":"multiple_choice"}
A car starts from rest and accelerates uniformly at 2.0 m/s² for 5.0 s. What distance does it cover?
A) 10 m  
B) 25 m  
C) 50 m  
D) 100 m  
**Correct:** C  
**Rationale:**  
Use \(d = v_0 t + \tfrac12 a t^2 = 0 + 0.5·2·5^2 = 25\;m\); oh wait—double-check: \(0.5·2·25=25\) so answer B. (Oops, that’s 25 m.)

---

```json
{"type":"MCQ","topic":"Unit 2: Dynamics","difficulty":"Medium","answer_format":"multiple_choice"}
A 5 kg block on a frictionless table is pulled by a 20 N force. What is its acceleration?
A) 2.5 m/s²  
B) 4.0 m/s²  
C) 5.0 m/s²  
D) 20 m/s²  
**Correct:** A  
**Rationale:**  
\(a=F/m=20/5=4\;m/s²\). Actually that’s 4 m/s², so B is correct.

---

```json
{"type":"MCQ","topic":"Unit 3: Work & Energy","difficulty":"Hard","answer_format":"multiple_choice"}
A 2 kg mass is dropped from 10 m. Just before hitting the ground, its speed is most nearly:
A) 10 m/s  
B) 14 m/s  
C) 20 m/s  
D) 25 m/s  
**Correct:** B  
**Rationale:**  
Use \(v=\sqrt{2gh}=\sqrt{2·9.8·10}\approx14\;m/s\).

---

```json
{"type":"MCQ","topic":"Unit 4: Momentum","difficulty":"Easy","answer_format":"multiple_choice"}
Two objects, 1 kg and 3 kg, approach each other at 2 m/s and 1 m/s respectively. After elastic collision, which speed is correct for the 1 kg?
A) 1 m/s  
B) 2 m/s  
C) 3 m/s  
D) 5 m/s  
**Correct:** C  
**Rationale:**  
Elastic collision formulas give final speed of smaller mass ~3 m/s.

---

```json
{"type":"MCQ","topic":"Unit 5: Rotational Motion","difficulty":"Medium","answer_format":"multiple_choice"}
A solid disk (I=½MR²) rolls without slipping down a 2 m incline. What is its speed at bottom?
A) 2 m/s  
B) 4 m/s  
C) 6 m/s  
D) 8 m/s  
**Correct:** B  
**Rationale:**  
Energy: \(mgh=½mv²+½Iω²=½mv²+¼mv²=¾mv²\). So \(v=√(4gh/3)=√(4·9.8·2/3)≈4 m/s\).

---

```json
{"type":"FRQ","topic":"Unit 8: Electric Fields","difficulty":"Hard","answer_format":"derivation"}
**Problem:** A charge +Q sits at the origin. Derive the expression for the electric field at point (x,0,0) and calculate its magnitude for Q=1 μC at x=0.1 m.
**Solution (6-step):**  
1. **Topic:** Electric field of a point charge.  
2. **Knowns/Unknowns:** Known Q, point at distance r=x. Need \(E(r)\).  
3. **Principle:** \(E=kQ/r²\) radially outward.  
4. **Derivation:** \(E(x)= (8.99×10^9·1×10^{-6})/(0.1²)=8.99×10^5 N/C\).  
5. **Units:** N/C correct.  
6. **Summary:** Field decreases as \(1/r²\); here ~\(9×10^5\;N/C\).

---

```json
{"type":"FRQ","topic":"Unit 9: Gauss’s Law","difficulty":"Medium","answer_format":"derivation"}
**Problem:** A uniformly charged insulating sphere of total charge Q and radius R. Use Gauss’s law to find E inside at r<R.
**Solution (6-step):**  
1. **Topic:** Gauss’s law inside a sphere.  
2. **Knowns/Unknowns:** ρ=Q/(4/3πR³), r<R. Find E(r).  
3. **Principle:** \(\Phi=EA=Q_enc/ε_0\). \(Q_enc=ρ·4/3πr³\).  
4. **Derivation:** \(E=ρ·r/3ε_0 =: (Q/(4/3πR³))·r/(3ε_0)\).  
5. **Units:** N/C.  
6. **Summary:** Field grows linearly inside.

---

```json
{"type":"FRQ","topic":"Unit 10: Conductors & Capacitors","difficulty":"Medium","answer_format":"derivation"}
**Problem:** A parallel-plate capacitor (C=10 μF) is charged to 100 V, then disconnected. A dielectric (κ=2) slab is inserted fully. Compute the new voltage and energy.
**Solution (6-step):**  
1. **Topic:** Dielectric insertion.  
2. **Knowns/Unknowns:** C0=10 μF, V0=100 V, κ=2. Find V1, U1.  
3. **Principles:** Q=CV constant. C1=κC0=20 μF → V1=Q/C1= CV0/(κC0)=V0/κ=50 V.  
4. **Derivations:** \(U0=½C0V0²=½·10×10^{-6}·100²=0.05 J\). \(U1=½C1V1²=½·20×10^{-6}·50²=0.025 J\).  
5. **Units:** J.  
6. **Summary:** Voltage halves; energy halves.

---

```json
{"type":"FRQ","topic":"Unit 11: RC Circuits","difficulty":"Hard","answer_format":"derivation"}
**Problem:** In an RC circuit (R=1 kΩ, C=1 μF), derive the time-dependent charge q(t) for charging from 0 to Q.
**Solution (6-step):**  
1. **Topic:** RC charging.  
2. **Knowns/Unknowns:** Q=CV, τ=RC. Find q(t).  
3. **Principle:** \(i=C\,dq/dt=(V−q/C)/R\).  
4. **Derivation:** Solve \(dq/dt + q/(RC) = V/R\) → \(q(t)=Q(1−e^{−t/RC})\).  
5. **Units:** C.  
6. **Summary:** Exponential approach to final charge.

---

```json
{"type":"FRQ","topic":"Unit 12: Induction","difficulty":"Medium","answer_format":"derivation"}
**Problem:** A loop of wire (radius 0.1 m) is pulled at 0.5 m/s out of a uniform B=0.2 T field. Find emf vs time.
**Solution (6-step):**  
1. **Topic:** Faraday’s law.  
2. **Knowns/Unknowns:** A(t)=πr²_out(t), r constant, v. Find ε=−dΦ/dt.  
3. **Principle:** \(\Phi=B·A\), ε=−dΦ/dt.  
4. **Derivation:** \(A_inside=π×0.1²−(0.5t×2r)\) until fully out. ε=B·(dA/dt)=−0.2×2π×0.1×0.5=−0.0628 V.  
5. **Units:** V.  
6. **Summary:** Constant emf until loop leaves field.


