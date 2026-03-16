# QC Threat to Bitcoin — Presentation Research & Build

**Date:** 2026-03-15
**Goal:** Research quantum computing threats to Bitcoin, build reference material, and create presentation slides for a 25-minute talk at Bitcoin Bush Bash.

## Repo-Specific Context

- Presentation file: `quantum-threat-bitcoin-bushbash.odp` (LibreOffice Impress, 39 slides)
- Presentation notes: `qc-threat-pres.md` (outline, references 1–36, supporting notes)
- Research PDFs and text versions: `assets/research/`
- Impress editing skill created at: `~/.claude/skills/impress-edit.md`

## Key Findings

### Quantum Computing Fundamentals
- Three pillars: superposition (2^n states), entanglement (linked qubits), interference (amplify right, cancel wrong).
- Key gates: Hadamard (superposition), CNOT (entanglement), Rx/Ry/Rz (rotation).
- Deutsch's algorithm circuit explained as simplest quantum speedup demonstration.
- Fault tolerance is the biggest engineering challenge — qubits decohere in microseconds.

### Threat to Bitcoin
- **Shor's algorithm** provides exponential speedup against ECC (ECDSA/Schnorr) — fundamentally broken, no key size is safe.
- **Grover's algorithm** provides only quadratic speedup against SHA-256 — halves security bits, mitigated by doubling key size.
- Taproot (P2TR) exposes tweaked public key on-chain. Tweaked key Q = P + hash(P || m) * G. A quantum attacker can run Shor's directly on Q to find q (tweaked private key) — doesn't need to recover P first.

### Resource Estimates for Breaking 256-bit ECC
- **Roetteler et al. (2017):** ~2,330 logical qubits, ~1.29 × 10^11 Toffoli gates.
- **Ha, Lee & Heo (2024):** ~2,586 logical qubits → ~5.68M physical qubits, ~62 days runtime (error rate 10^-3, cycle time 200 ns).
- **Häner et al. (2020):** Three strategies — Low Width (2,124 qubits), Low T-count (2,619), Low Depth (2,871). Depth-optimized achieves 6,000× depth reduction for 22% more qubits.
- **Banegas et al. (2026):** P-224 breakable in 34 min (19.1M qubits) or 96 min (6.9M qubits). P-256 qubit-optimized: ~7.7M qubits, ~2 hours.

### Logical Qubit Ceiling Question (Loyd's question)
**Question:** Is there a limit to adding more logical qubits to speed up solving ECDLP?
**Answer:** Yes, evidence strongly supports a ceiling, but no paper formally proves a hard floor.

**Evidence:**
1. Ha, Lee & Heo (2024): *"the use of more logical qubits in quantum algorithms does not always lead to the use of more physical qubits"* — more qubits can increase error correction overhead (magic-state factories) without reducing runtime.
2. Häner et al. (2020): depth-optimized circuit at 2,871 qubits achieves the practical depth limit — gains plateau.
3. Banegas et al. (2026): 2.8× more qubits → 2.8× faster (linear, not exponential returns).
4. Structural constraint: Shor's requires 2n sequential point additions to an accumulator; windowing reduces to 2n/w but at exponential cost per window.

**What is NOT proven:** No paper formally proves a lower bound on circuit depth for ECDLP. "Circuit depth floor" is an inference, not a cited term.

### Once parallelism is maxed, faster runtime requires:
- Faster gate speeds (below 200 ns cycle time)
- Lower physical error rates (below 10^-3)
- Algorithmic breakthroughs (reduce circuit depth itself)
- Better error correction codes (beyond surface codes)

### GRI Quantum Threat Timeline 2025
- 26 global experts surveyed (not 32 as in 2024 report).
- Optimistic: ~49% chance of CRQC within 10 years; Pessimistic: ~28%.
- Optimistic/pessimistic = upper/lower end of experts' chosen likelihood bins.
- Notable upward shift from prior years. Report on page 4-6 of `assets/research/pdf-quantum-threat-timeline-report-2025.pdf`.

### QC and Bitcoin Mining Centralisation
- Grover's quadratic speedup doesn't break SHA-256 but gives a mining advantage.
- QC mining CAN be distributed (assign different nonce ranges to different QCs — same as classical pools).
- The real centralisation risk is economic: QCs cost hundreds of millions, only a few entities will have them.

### PQC Signature Comparison (ECDSA vs ML-DSA-44 vs SLH-DSA-128s)
- ECDSA: 33B pubkey, 71B sig, ~0.01ms sign/verify.
- ML-DSA-44: 1,312B pubkey, 2,420B sig, ~0.24ms sign, ~0.05ms verify.
- SLH-DSA-128s: 32B pubkey, 7,856B sig, ~94ms sign, ~6ms verify.

### Legacy Coins / Social Problem
- Status quo (don't freeze): preserves censorship resistance, risks market crash from stolen coins.
- Freeze: prevents crash but violates property rights, could cause chain split.
- Hourglass: rate-limiting movement of quantum-vulnerable coins as middle ground.

## Decisions Made

1. References reorganised from unnumbered to numbered 1–36 across 7 categories.
2. Bitcoin revision links condensed from 16 to 5 (ECC, Digital Signatures, Hash Functions, Mempool, Taproot).
3. GRI 2025 report and Bitcoin Fundamentals podcast moved to QC Timeline section.
4. Chaincode Labs paper moved to Technical Fixes section.
5. 9 reference slides added to ODP presentation programmatically via Python/XML.
6. Impress editing skill created documenting ODP XML structure and pitfalls.

## Files Created/Modified

- `qc-threat-pres.md` — major reference reorganisation and descriptions added.
- `quantum-threat-bitcoin-bushbash.odp` — 9 reference slides added (slides 31–39).
- `quantum-threat-bitcoin-bushbash.pdf` — PDF export of presentation.
- `~/.claude/skills/impress-edit.md` — skill for editing ODP files.
- `assets/research/roetteler-2017-quantum-resource-estimates-ecdlp.pdf` + `.txt`
- `assets/research/chaincode-bitcoin-post-quantum.pdf` + `.txt`
- `assets/research/fed-reserve-hndl-pqc-distributed-ledger.pdf` + `.txt`
- `assets/research/pdf-quantum-threat-timeline-report-2025.txt` (text conversion)
- `assets/research/haner-2020-improved-quantum-circuits-ecdlp.pdf`
- `assets/research/banegas-2026-new-quantum-circuits-ecdlp.pdf`

## Risks / Open Questions

1. **No formal lower bound proven** for circuit depth on ECDLP — the "ceiling" claim is well-supported by evidence but not formally proven in any cited paper.
2. **Ha, Lee & Heo 21-hour figure** — appeared in web search summaries but could not be verified from the paper's full text. The paper's Table 3 shows ~62 days for 256-bit ECC, not 21 hours. The 21 hours may have been misattributed.
3. **PQC signature benchmarks** — the exact numbers for ML-DSA and SLH-DSA were stated from general knowledge, not benchmarked from a specific source. Should be verified against refs 23/24.
4. **ODP hyperlinks** — fixed format to match existing presentation style but not visually verified in Impress.
5. **Banegas 2026 paper** — text file at `/tmp/banegas2026.txt` needs to be moved to `assets/research/`.

## Next Steps

1. **Complete Banegas 2026 analysis:** Read full Table 6 for P-256/P-384/P-521 qubit-time tradeoff data. Move text file to `assets/research/`.
2. **Search for formal lower bounds:** Look for papers proving theoretical minimum circuit depth for Shor's/ECDLP. Search: "lower bound circuit depth discrete logarithm quantum."
3. **Plot qubit-time tradeoff curve:** Using Banegas data points, visualise where the curve flattens.
4. **Write up Loyd's answer** in `increasing-qubit-size.md` with exact quotes, evidence chain, and caveats about what is inference vs proven.
5. **Verify ODP slides** in LibreOffice Impress — check hyperlinks work, descriptions render, formatting on all 9 reference slides.
6. **Verify PQC benchmark numbers** against refs 23/24.
7. **Generate text version** of Ha, Lee & Heo PDF (`assets/research/`).
