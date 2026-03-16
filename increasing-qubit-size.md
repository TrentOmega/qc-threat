I had a follow up question from Loyd that I didn't answer yesterday, after a little more digging I came across a few references that seem to contradict what I thought. So Loyds question/statement was along the lines of "is there a limit to adding more logical qubits to get a solving speed up for a given key size?". Loyd was in the positive camp, which I belive is correct.

Adding more logical qubits speeds things up only until you hit the circuit depth floor, the minimum number of sequential gate operations that can't be parallelised. Beyond that point, extra qubits just add error correction overhead without reducing runtime — Ha, Lee & Heo (2024) confirmed this directly, showing that more logical qubits "does not always lead to" fewer physical qubits or faster execution.

Ha, Lee & Heo (2024) estimate that breaking 256-bit ECC requires ~2,586 logical qubits, which under realistic surface code conditions (error rate 10⁻³, cycle time 200 ns) translates to ~5.68 million physical qubits and ~62 days of runtime.

How to get a faster runtime then? Once you've hit the circuit depth floor, the only ways to reduce runtime are:

-Faster gate speeds: reducing the cycle time below 200 ns means each sequential operation completes sooner
- Lower physical error rates: below 10⁻³ means less error correction overhead per logical qubit, freeing up physical qubits and reducing correction cycles
- Algorithmic breakthroughs: reducing the circuit depth itself — e.g., Ha, Lee & Heo's Mod 2 (Takahashi adders) reduced the T depth from O(n³ log n) to O(n³), and the 2025 Ed25519 paper achieved a 60% T-depth reduction by exploiting specific field structure
- Better error correction codes: alternatives to surface codes that achieve the same logical error rates with fewer physical qubits per logical qubit

In short, once parallelism is maxed out, the path to faster runtime is better hardware, better codes, or fewer sequential steps — not more qubits.