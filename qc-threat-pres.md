# Quantum Computing Threat to Bitcoin

## Presentation Length
* 25 minutes including quesitons

## Audience

* Bitcoin: beginner to advance on bitcoin  
* QC: no knowledge to intermediate

## Objective

* Overview the threat, what can we do, what can you do.

## Topic Intro
- Interesting and difficult topic to present on because it lies at the intersection of four disciplinary pillars
  1. the strange world of quantum mechanics,
  2. the intricate mathematics of cyrptography,
  3. the elegant structures of computer science, and
  4. the innovative functions of Bitcoin.
- The presenter is currently studying the first three: physics, math, and computer science; and has had a keen interest in the technical aspects of Bitcoin for many years.
- This topic has a lot of FUD around and one of the presentations aims is to reduce that:
  - Understanding a threat and what is being done can eleviate fear,
  - Uncertainty is a big thing in the QC space and won't be going away, so learn to live with it
  - Doubt exists on both sides of people underselling and overselling the risk. I hope to clear up some of those doubts
- Explore further as not much time here to explain.


## Outline

* ### What is Quantum Computing (QC) — ORIGINAL

  * What makes it work:
    * Three components: qubits, quantum gates, measurement
    * Physical qubits → error correction → logical qubits
    * logical qubits \+ runtime → “can it run Shor fast enough?”
    * Fault tolerance: the key engineering challenge
  * Definitions:
    * Cryptographic Relevant Quantum Computer (CRQC): a QC with enough logical qubits to break cryptography
    * Q-Day: the day a CRQC arrives
  * What we currently have
    * Current uses: drug discovery, optimisation
  * What’s getting built ([ref](https://bitcoinmagazine.com/technical/the-quantum-bitcoin-summit-a-grounded-look-at-the-issues))


* ### What is the QC threat to Bitcoin

  * Digital signatures: Shor’s algorithm  
    * Long exposure attack:
      * P2PK/P2TR immediatly exposed,
      * P2PKH/P2SH/P2WPKH/P2WSH exposed after first spend (address reuse)
    * Short exposure attack: mempool window  
  * Mining: Grover’s algorithm

* ### Revision
 
 (typing) . (door opens) . (door closes) (typing)

* ### When is it coming

  * Q-day likelihoods (GRI Quantum Threat Timeline Report 2025)  
  * Government policy timelines

* ### The two big problems to Bitcoin

  * 1\. Technical problem: adding PQC to bitcoin  
  * 2\. Social problem: legacy coins (UTXOs that don’t upgrade)

* ### Problem 1 \- PQC

  * Attack types:  
    * Long exposure attack: Show tables of amounts  
    * Short exposure attack: Show table of all bitcoin  
  * Quantum resistant signatures  
    * 5 main families: hash, lattice, isogeny, codes, multivariate
    * Lattice based: Dilithium
      *[ML-DSA](https://csrc.nist.gov/pubs/fips/204/final)* Latice-based (derived from CRYSTALS-Dilithium) NIST FIPS 204
    * Hash based: SPHINCS+
      *[SLH-DSA](https://csrc.nist.gov/pubs/fips/204/final)* Hash-based (derived from SPHINCS+) NIST FIPS 205  
    * Isogeny: experimental and risky
  * Impacts
    * Size, verification & signing times  
    * Lightning channels  
    * Multisign wallets  
    * Exchanges & custody services  
  * P2TR mitigation path [BIP360](https://github.com/bitcoin/bips/blob/master/bip-0360.mediawiki) P2MR
  * Timeline for implementation ([Bitmex ref](https://www.bitmex.com/blog/Taproot-Quantum-Spend-Paths))([TradingView ref](https://www.tradingview.com/news/cointelegraph%253A30729863f094b%253A0-bitcoin-may-take-7-years-to-upgrade-to-post-quantum-bip-360-co-author/))  
    * Standard vs urgent upgrade timelines  
    * Side by side timeline with Q-Day likelihood  
    * “We win if migration finishes before Q-Day”

* ### Problem 2 \- Legacy Coins

  * The problem: do nothing and a CRQC can spend & crash the market, or restrict spending somehow and violate bitcoin’s censorship resistance.  
  * Solutions:  
    * Status quo: preserves censorship resistance but could collapse price  
    * Freeze: prevents market crash but violates censorship resistance and legitimacy  
    * Hourglass: middle path of rate-limiting movement of quantum-exposed coins.  
  * Timeline issues with freezing  
  * Likely outcomes: chain split, external forces will use this to drive a wedge in bitcoin.

* ### What can you do
  * Today:
    * Don’t reuse addresses 
    * Avoid P2TR/P2PK (larger addresses more so)
    * Avoid sharing your XPUB (SMSF auditing & public nodes)  
  * Later:
    * Move to PQC upgrade when standards and wallets exist
  * Satoshi's shield: game theory effect
  * Participate in the solution  
    * Grants for dev and crypto research  
    * Other: run a node, understand the problems/solutions, influence direction.

* ### Mythbusters

  * “CRQC breaks all addresses instantly” → no, *exposure type* and *time window* matters.  
  * “Grover kills SHA-256” → no, it’s a quadratic speedup and doesn’t magically break hashing; it changes cost curves.  
  * “This is only a Bitcoin problem” → no, breaking ECDSA/RSA is an internet-and-nation-state problem. 

* ###  Perspective: A CRQC most likely use cases

  * SIGINT: cracking the store now / decrypt later vault  
  * Materials science and engineering  
  * Pharmaceutical development  
  * Disease prevention research  
  * Experimental physics modeling and research: find the boundary of QFT

## References

### What is QC
1. [IBM Quantum Learning: Bits, Gates, and Circuits](https://quantum.cloud.ibm.com/learning/en/courses/utility-scale-quantum-computing/bits-gates-and-circuits)
   IBM's technical introduction to qubits, quantum gates, and circuits — aimed at people with a computing background, no physics degree required.
2. [Classiq: The Deutsch-Jozsa Algorithm Explained](https://www.classiq.io/insights/the-deutsch-jozsa-algorithm-explained)
   Step-by-step walkthrough of the Deutsch oracle problem and circuit — the simplest demonstration that a quantum computer can outperform a classical one.
3. [Bitcoin Magazine: Quantum Bitcoin Summit](https://bitcoinmagazine.com/technical/the-quantum-bitcoin-summit-a-grounded-look-at-the-issues)
   Summary of a summit bringing together quantum computing and Bitcoin experts to examine the real threats and separate hype from substance.

### What is the threat
4. [Grover's Search Algorithm Overview](https://learn.microsoft.com/en-us/azure/quantum/concepts-grovers)
   Microsoft's explanation of Grover's quantum search algorithm, which provides a quadratic speedup for unstructured search problems.
5. [Quantum Resource Estimates for ECDLP](https://arxiv.org/abs/1706.06752)
   Roetteler et al. (2017) foundational paper estimating ~2,330 logical qubits and ~1.29 × 10¹¹ Toffoli gates to break 256-bit ECC using Shor's algorithm.
6. [Ha, Lee & Heo (2024) — Resource analysis for ECDLP with noisy qubits](https://www.nature.com/articles/s41598-024-54434-w)
   First comprehensive physical qubit estimate for ECDLP under surface codes: ~5.87 million physical qubits for P-256 at 10⁻³ error rate with 200 ns cycle time.
7. [Ed25519 Optimisation (2025)](https://link.springer.com/article/10.1007/s11128-025-04916-1)
   Achieves 97% reduction in T-count, 60% reduction in T-depth, and 16% fewer qubits for quantum attacks on Ed25519 by exploiting its specific finite field structure.

### Bitcoin revision
8. [Elliptic Curve Cryptography](https://learnmeabitcoin.com/technical/cryptography/elliptic-curve/)
   How Bitcoin uses the secp256k1 elliptic curve for key generation and digital signatures — the operation Shor's algorithm can reverse.
9. [Digital Signatures](https://learnmeabitcoin.com/beginners/guide/digital-signatures/)
   How ECDSA and Schnorr signatures work in Bitcoin to authorise spending without revealing the private key.
10. [Hash Functions](https://learnmeabitcoin.com/technical/cryptography/hash-function/)
    Overview of SHA-256 and RIPEMD-160 as used in Bitcoin for mining, addresses, and data integrity — Grover's algorithm provides only a quadratic speedup against these.
11. [Memory Pool](https://learnmeabitcoin.com/technical/mining/memory-pool/)
    The mempool where unconfirmed transactions wait — the window during which a short exposure quantum attack could occur.
12. [Taproot (P2TR)](https://learnmeabitcoin.com/technical/script/p2tr/)
    Pay-to-Taproot: exposes a tweaked public key on-chain, making unspent P2TR outputs vulnerable to long exposure quantum attacks.

### QC timeline
13. [GRI Quantum Threat Timeline Report 2025](https://globalriskinstitute.org/publication/quantum-threat-timeline-2025-executive-perspectives-on-barriers-to-action/)
    Annual survey of 26 global quantum experts. Optimistic interpretation: ~49% chance of a CRQC within 10 years; pessimistic: ~28%. Notable upward shift from prior years.
14. [Bitcoin Fundamentals: Quantum Computing and Bitcoin](https://www.theinvestorspodcast.com/bitcoin-fundamentals/quantum-computing-and-bitcoin-w-charles-edwards/)
    Podcast episode discussing the quantum threat to Bitcoin with Charles Edwards, covering timelines, risk assessment, and what bitcoiners should know.
15. [Cointelegraph: BIP-360 Upgrade Timeline](https://www.tradingview.com/news/cointelegraph%253A30729863f094b%253A0-bitcoin-may-take-7-years-to-upgrade-to-post-quantum-bip-360-co-author/)
    BIP-360 co-author estimates Bitcoin may take up to 7 years to fully upgrade to post-quantum signatures under a standard timeline.

### Technical problem and fixes
16. [BIP360.org Overview](https://bip360.org/bip360.html)
    Overview of Pay-to-Merkle-Root (P2MR), a new output type that removes the quantum-vulnerable key path spend from Taproot while preserving script tree functionality.
17. [BIP-360 Draft: Pay-to-Merkle-Root](https://github.com/bitcoin/bips/blob/master/bip-0360.mediawiki)
    The formal BIP specification for P2MR, detailing address format (bc1z...), witness structure, and security rationale against long exposure quantum attacks.
18. [BitMEX Research: Taproot Quantum Spend Paths](https://www.bitmex.com/blog/Taproot-Quantum-Spend-Paths)
    Proposes dual-path Taproot wallets with both quantum-safe and classical spend paths, arguing these wallets should be exempt from any future coin freeze.
19. [Cointelegraph: Six Quantum Security Challenges](https://www.tradingview.com/news/cointelegraph:d4cc2ff14094b:0-bitcoin-faces-6-massive-challenges-to-become-quantum-secure/)
    Outlines six major hurdles Bitcoin faces in becoming quantum-resistant, including signature size bloat, consensus changes, and migration logistics.
20. [Bitcoin Magazine: Bitcoin Advances Toward Quantum Resistance](https://bitcoinmagazine.com/news/bitcoin-advances-toward-quantum-resistance)
    Reports on recent development progress toward quantum-resistant Bitcoin, including BIP-360 and related proposals.
21. [NIST FIPS 204: ML-DSA](https://csrc.nist.gov/pubs/fips/204/final)
    NIST's finalised standard for ML-DSA (derived from CRYSTALS-Dilithium), a lattice-based post-quantum digital signature algorithm.
22. [NIST FIPS 205: SLH-DSA](https://csrc.nist.gov/pubs/fips/205/final)
    NIST's finalised standard for SLH-DSA (derived from SPHINCS+), a stateless hash-based post-quantum digital signature algorithm.
23. [Post-Quantum Digital Signatures Benchmark: ML-DSA vs ECDSA](https://pqc.metamui.id/signatures/ecc_dss)
    Side-by-side performance benchmarks comparing ML-DSA signature sizes, signing times, and verification times against classical ECDSA.
24. [ASecuritySite: Digital Signature Benchmark](https://asecuritysite.com/pqc/dilbenchmark)
    Interactive benchmarking tool for post-quantum signature schemes including Dilithium/ML-DSA across different security levels.
25. [Making SLH-DSA 10x-100x Faster](https://huelsing.net/wordpress/?page_id=1474)
    Research by SLH-DSA co-designer Andreas Huelsing on optimisation techniques to dramatically improve SLH-DSA signing and verification performance.
26. [SLotH GitHub: SLH-DSA Performance](https://github.com/slh-dsa/sloth)
    Reference implementation and benchmarks for optimised SLH-DSA, targeting hardware acceleration to close the performance gap with lattice-based schemes.
27. [Chaincode: Bitcoin Post-Quantum](https://chaincode.com/bitcoin-post-quantum.pdf)
    Chaincode Labs research paper analysing post-quantum migration strategies for Bitcoin, including signature scheme selection and upgrade paths.

### Social problem and fixes
28. [Hourglass v2 Draft](https://github.com/cryptoquick/bips/blob/hourglass-v2/bip-hourglass-v2.mediawiki)
    Proposes a middle-ground approach to quantum-vulnerable coins: rate-limiting their movement rather than freezing or ignoring them entirely.
29. [Lopp: Against Quantum Recovery of Bitcoin](https://blog.lopp.net/against-quantum-recovery-of-bitcoin/)
    Jameson Lopp argues Bitcoin should permanently burn funds in quantum-vulnerable addresses rather than allow quantum-capable entities to steal them.
30. [CoinDesk: To Freeze or Not to Freeze — Satoshi and the $440B in Bitcoin Threatened by Quantum Computing](https://www.coindesk.com/business/2026/02/22/to-freeze-or-not-to-freeze-satoshi-and-the-usd440-billion-in-bitcoin-threatened-by-quantum-computing)
    Examines the debate over ~7 million BTC in quantum-vulnerable addresses including Satoshi's ~1 million coins, weighing immutability against market stability.
31. [Cointelegraph Magazine: Bitcoin may face hard fork over any attempt to freeze Satoshi's coins](https://cointelegraph-magazine.com/bitcoin-may-face-hard-fork-over-any-attempt-to-freeze-satoshis-coins/)
    Argues that freezing quantum-vulnerable coins would violate Bitcoin's core property rights, potentially splitting the network in a contentious hard fork.

### Other uses of QC
32. [Frontiers: Quantum Computing — Foundations, Algorithms, and Emerging Applications (2025)](https://www.frontiersin.org/journals/quantum-science-and-technology/articles/10.3389/frqst.2025.1723319/full)
    Comprehensive review covering quantum algorithms and their emerging applications across materials science, chemistry, optimisation, and physics simulation.
33. [Wikipedia: Harvest Now, Decrypt Later](https://en.wikipedia.org/wiki/Harvest_now,_decrypt_later)
    Overview of the HNDL strategy where adversaries intercept and store encrypted communications today for decryption once quantum computers become available.
34. [Federal Reserve: HNDL and Post-Quantum Cryptography Risks for Distributed Ledger Networks](https://www.federalreserve.gov/econres/feds/harvest-now-decrypt-later-examining-post-quantum-cryptography-and-the-data-privacy-risks-for-distributed-ledger-networks.htm)
    Federal Reserve research examining how harvest-now-decrypt-later attacks pose data privacy risks specifically for blockchain and distributed ledger networks.
35. [McKinsey: The Quantum Revolution in Pharma (2025)](https://www.mckinsey.com/industries/life-sciences/our-insights/the-quantum-revolution-in-pharma-faster-smarter-and-more-precise)
    McKinsey analysis of how quantum computing is accelerating drug discovery by simulating molecular interactions at the quantum level, compressing timelines from years to weeks.
36. [Nature: Quantum-Machine-Assisted Drug Discovery (2025)](https://www.nature.com/articles/s44386-025-00033-2)
    Nature paper on combining quantum computing with machine learning for biomarker discovery, genomic data processing, and cancer detection via liquid biopsy.



## Notes to support the presentation

### Summary of [BIP360 Pay-to_Markle-Root (P2MR)](https://github.com/bitcoin/bips/blob/master/bip-0360.mediawiki)

- Pay-to-Merkle-Root (P2MR) output is similar to Pay-to-Taproot (P2TR) but with the *key path spend* removed.

- Uses *script trees* and *tapscript* in a manner that makes it resistant to:
  1. long exposure attacks by CRQCs, and
  2. future cryptanalytic approaches that compromise ECC.

- Protection against short exposure attacks requires PQC, which this BIP doesn't propose.

#### Motivation
- Shor's on CRQC solves the DLP exponentially faster then a classical computer -> derives k from K, known as *quantum key recovery*

- Timelines of GOs:
  - Commercial National Security Algorithm Suite (CNSA) 2.0 PQC in software & networking by 2030, and browsers & OS by 2033
  - NIST disallow ECC within US federal government after 2035.

#### Long exposure attack vulnerability of all output types
  ![BIP360 Address Type Vulnerability](assets/images/bip360-address-type-vulnerability.png)

#### Design
- P2MR witness consists of:
  - script inputs + leaf script + *control block* (same as P2TR script path spend), however
  - control block doesn't contain the public key for the taproot derivation, therefore consists of
  - control byte + *Merkle path*

- Script tree with Merkle root, and input/output diagram
  ![BIP360 script tree with inputs and outputs](assets/images/bip360-merkletree.png)


#### Rationale
1. minimizes changes to the network
2. supports tapscript which assists in implementing PQC required opcodes
3. Facilitates gradual integration of PQC without negative impacts before Q-Day.

#### Trade-offs
- Size: the witness to a P2MR is always > P2TR key path spend
  - The smallest witness size P2MR is 103 bytes to 66 bytes for P2TR key path spend, however
  - The witness to a P2MR is always < an equivalent P2TR script path spend, due no requirement of the internal public key in the control block
- Privacy: comparing P2MR to P2TR key path spent: with P2MR there is no way to conceal you have other script path spends.
  - Note: P2MR and P2TR script path spend offer the same level of privacy, and both are better than P2SH because unused script paths are not revealed.

#### Specifications

- Address format: Bech32m encoding maps version 2 to prifix *z* -> P2MR address begin with bc1z...

- ScriptPubKey: OP_2 OP_PUSHBYTES_32 <hash>
  - where OP_2 indicates SegWit version 2
  - <hash> is the 32-byte Markle root of the *script tree*

#### Security
- P2MR uses 256-bit hash output -> 128 bits of collision resitance and 256 bits of preimage resistance; same as P2WSH.
- P2MR does not, byt itself, protect against short exposure attacks, however
  - Later plug-in PQC can provide resistance for this attack.
- Preparing against long exposure attacks is more time-crucial as early CRQCs are unlikely to be fast enought for short exposure attacks.


### Notes on Quantum Computing
  * **Qubits**: the basic unit — like a bit but can be in superposition (both 0 and 1 simultaneously). Superposition is what gives QC its parallelism.
  * **Quantum gates**: operations that manipulate qubits, analogous to logic gates in classical computing. They exploit superposition and entanglement to perform computations across many states at once.
  * **Measurement**: collapses a qubit’s superposition into a definite 0 or 1. Quantum algorithms are designed so that measuring at the end gives the correct answer with high probability.
  * **Physical vs logical qubits**: physical qubits are the actual hardware (superconducting circuits, trapped ions, etc.) and are extremely error-prone. Multiple physical qubits are combined via quantum error correction codes to form one reliable logical qubit. Current ratios are roughly 1,000:1 or worse.
  * **Fault tolerance**: the ability to perform long computations despite individual qubit errors. Without fault tolerance a QC can only run very short, noisy circuits. Achieving fault tolerance at scale is the single biggest engineering barrier to a CRQC.
  * **CRQC (Cryptographically Relevant Quantum Computer)**: a fault-tolerant QC with enough logical qubits and sufficient runtime to execute Shor’s algorithm against real-world key sizes (e.g. ECDSA-256). Estimates range from ~2,000–4,000 logical qubits, which translates to millions of physical qubits with current error rates.
  * **Current commercial uses**: Pharmaceutical companies are paying for QC time to simulate molecular interactions for drug discovery. Logistics and finance firms use quantum annealers and hybrid algorithms for combinatorial optimisation problems (routing, portfolio optimisation). These are the applications attracting real revenue today, which signals where the technology is genuinely useful right now. (sizzling)
