# Quantum Computing Resource Estimates for Breaking ECC

**Date:** 2026-03-15
**Topic:** Citing quantum resource papers accurately — distinguishing inference from proven claims.

## Reusable Pattern

When researching quantum threat timelines and resource estimates, the literature provides **specific claims** about qubit counts and runtimes, but does NOT provide formal proofs of theoretical lower bounds on circuit depth. Be careful to distinguish:

- **Proven:** specific resource estimates (qubits, gates, time) under stated assumptions.
- **Demonstrated:** space-time tradeoffs showing diminishing returns from more qubits.
- **Inferred but not proven:** the existence of a hard "circuit depth floor" or formal lower bound.

## Trigger Conditions

- Answering questions about how fast a quantum computer can break cryptography.
- Citing papers on quantum resource estimates.
- Discussing whether "more qubits = faster" has limits.

## Key Papers and What They Actually Claim

| Paper | Claims | Does NOT Claim |
|-------|--------|----------------|
| Roetteler et al. (2017) | ~2,330 logical qubits for 256-bit ECC | Runtime or physical qubit count |
| Ha, Lee & Heo (2024) | More logical qubits doesn't always reduce N_phy; ~5.68M physical qubits for P-256 | A formal time ceiling or circuit depth lower bound |
| Häner et al. (2020) | Three optimisation strategies with different qubit-depth tradeoffs | That the depth-optimised version is the theoretical minimum |
| Banegas et al. (2026) | 2.8× more qubits → 2.8× faster (P-224); P-256 in ~2 hours | A formal lower bound on depth |

## Failure Modes

1. **Conflating cost ceiling with time ceiling:** Ha, Lee & Heo prove more qubits can increase physical cost, but don't directly prove a time floor.
2. **Attributing analogies to papers:** "Amdahl's Law for quantum computing" is a useful analogy but not a formal concept — don't present it as if it comes from a paper.
3. **Mixing up logical vs physical qubit estimates:** Always state which level the estimate refers to.
4. **Citing web search summaries as paper claims:** Always verify against the actual paper text. Web summaries can misattribute or misstate figures.
