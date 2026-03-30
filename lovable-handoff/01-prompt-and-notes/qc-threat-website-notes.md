# QC Threat to Bitcoin Website Notes

This document is the source-of-truth content handoff for the website version of the project. It expands the current slide deck into website-ready copy for a mixed audience: Bitcoin beginners through advanced users, and quantum newcomers through technically curious readers.

Primary inputs for this draft are `quantum-threat-bitcoin-bushbash.odp` (slides 1-30), `qc-threat-pres-v1.md`, `qc-threat-log.md`, the local research extracts in `assets/research/`, and a small targeted research pass for the Deutsch-Jozsa and quantum-physics explainer sections.

Lovable should treat each section below as a content module. The `Core narrative` is the default on-page copy. The `Expandable deep dives` are optional accordions, tabs, side panels, or secondary pages.

## 1. Framing the problem (ODP slides 1-4)

**Website heading**

Quantum computing is a real threat to Bitcoin, but it is not game over.

**Purpose / key takeaway**

Open by replacing fear with a sharper frame: this is not a story about Bitcoin failing overnight. It is a story about whether Bitcoin can finish a cryptographic migration before a cryptographically relevant quantum computer arrives.

**Core narrative**

The most useful way to frame the quantum threat is not "Will Bitcoin suddenly die?" but "Can Bitcoin migrate in time?" That difference matters. A lot of public discussion collapses everything into one catastrophic headline, but the real picture is more staged than that. Different parts of Bitcoin are exposed in different ways, and some of those exposures depend on how people use addresses and wallets.

The signature problem is the main problem. Bitcoin relies on elliptic curve cryptography for ownership and spending authorization. If a future fault-tolerant quantum computer can run Shor's algorithm at useful scale, then public keys become much more dangerous to expose. That does not mean every coin gets stolen at once. It means exposed coins become vulnerable on different timelines depending on output type, reuse behavior, and how long a public key sits in the open.

The more grounded framing is a migration race. Bitcoin wins if it can ship practical post-quantum defenses, coordinate adoption across wallets and exchanges, and handle the legacy coin problem before a CRQC becomes practical. That is why this topic is partly cryptography, partly engineering, and partly governance.

The newer industry framing in the repo is useful here: Galaxy Digital's March 19, 2026 report treats the threat as genuine but not imminent, and it argues that governance around non-migrated coins may be harder than the cryptographic upgrade itself. That tone is the right one for the website. Serious, not hysterical.

**Expandable deep dives**

- Why the answer to "Is Bitcoin fucked?" is still "No"
- Why "migration race" is a better mental model than "overnight collapse"
- The difference between a real threat and an imminent threat
- Why governance may become the hardest part of the problem

**Relevant assets**

- `assets/images/ibm-100-qubits-title-pic.jpg`
- `assets/images/project-eleven-exposed-bitcoin.png`
- `assets/images/gri-timeline-2025.png`

**Sources**

- Bitcoin Magazine, "The Quantum Bitcoin Summit: A Grounded Look at the Issues"  
  https://bitcoinmagazine.com/technical/the-quantum-bitcoin-summit-a-grounded-look-at-the-issues
- Repo working note: `qc-threat-log.md`
- Atlas21 summary of Galaxy Digital, "The Quantum Risk to Bitcoin is Real, but the Network is Preparing"  
  https://atlas21.com/galaxy-digital-the-quantum-risk-to-bitcoin-is-real-but-the-network-is-preparing/

## 2. How quantum computing actually gets an advantage (ODP slides 5-6)

**Website heading**

Quantum computers are not magic. Their speedup comes from superposition, interference, and brutal engineering.

**Purpose / key takeaway**

Explain quantum computing clearly enough that non-specialists can follow the Bitcoin threat without falling back on vague "parallel universes" language. The key idea is that quantum advantage comes from preparing quantum states, transforming them with gates, and using interference so measurement is likely to return a useful answer.

**Core narrative**

A qubit is not just a faster bit. A classical bit is either 0 or 1. A qubit is a quantum state that can be prepared in a superposition, meaning the system carries amplitudes associated with both outcomes until it is measured. Quantum gates do not simply flip bits. They rotate and entangle quantum states. Measurement then turns those amplitudes into an ordinary classical result.

That still does not explain the advantage by itself. The cleanest beginner-friendly example is the Deutsch or Deutsch-Jozsa oracle problem. The promise problem is simple: determine whether a hidden function is constant or balanced. A deterministic classical approach needs multiple queries. The quantum approach places the input into superposition, lets the oracle write information into phase, and then uses interference so one measurement reveals the answer. The lesson is not that a quantum computer "reads all answers at once." The lesson is that it can shape probability amplitudes so the right answer is more likely to survive measurement.

That algorithmic intuition should then be tied back to physics. Quantum computers work because nature itself allows superposition, interference, entanglement, and measurement effects at microscopic scales. Qubits do not have to be photons. Different hardware platforms encode quantum information in different physical systems, including superconducting circuits, trapped ions, neutral atoms, quantum dots, and photonic systems. The software story is abstract, but the machine is always a physical device fighting decoherence and noise.

That is why physical qubits and logical qubits must be separated in the copy. Physical qubits are the messy hardware. Logical qubits are the error-corrected qubits you wish you had. A CRQC is not just "a lot of qubits." It is a machine with enough logical qubits, low enough error rates, and enough runtime to finish something like Shor's algorithm against real key sizes. That is the engineering wall, and fault tolerance is the reason the wall is so high.

**Expandable deep dives**

- Deutsch vs Deutsch-Jozsa: the simplest quantum speedup story
- Phase kickback and why the oracle matters
- Why measurement prevents a quantum computer from simply dumping all 2^n answers at once
- Physical qubits vs logical qubits vs fault tolerance
- What "CRQC" means in practical terms

**Relevant assets**

- `assets/images/ibm-100-qubits-title-pic.jpg`
- `assets/images/mit-peter-shor.png`
- `assets/images/lov-grover.png`

**Sources**

- IBM Quantum Learning, "Bits, Gates, and Circuits"  
  https://quantum.cloud.ibm.com/learning/en/courses/utility-scale-quantum-computing/bits-gates-and-circuits
- IBM Quantum Learning, "The Deutsch-Jozsa Algorithm"  
  https://quantum.cloud.ibm.com/learning/en/modules/computer-science/deutsch-jozsa
- IBM, "What is a qubit?"  
  https://www.ibm.com/think/topics/qubit
- IBM, "What Is Quantum Computing?"  
  https://www.ibm.com/think/topics/quantum-computing
- IBM Quantum Learning, "Approach to fault tolerance"  
  https://quantum.cloud.ibm.com/learning/en/courses/foundations-of-quantum-error-correction/fault-tolerant-quantum-computing/approach-to-fault-tolerance
- Roetteler et al. (2017), "Quantum Resource Estimates for Computing Elliptic Curve Discrete Logarithms"  
  https://arxiv.org/abs/1706.06752
- Ha, Lee, and Heo (2024), "Resource analysis for ECDLP with noisy qubits"  
  https://www.nature.com/articles/s41598-024-54434-w

## 3. Why Bitcoin is exposed (ODP slides 7-16)

**Website heading**

Bitcoin is exposed unevenly: signatures are the real problem, mining is a secondary problem.

**Purpose / key takeaway**

Show that the quantum threat is not uniform across Bitcoin. Shor's algorithm targets public-key cryptography directly. Grover's algorithm does not "break Bitcoin mining" in the same way; it changes search economics and may increase centralization pressure.

**Core narrative**

Bitcoin relies on two broad families of cryptography: public-key signatures and hash functions. Quantum computers interact with those very differently. Shor's algorithm attacks the discrete logarithm problem behind ECDSA and Schnorr signatures. If a CRQC can run it at practical scale, then a public key can become a route back to the private key. That is why public-key exposure is the center of gravity in this discussion.

The most important practical concept for the website is exposure type. Some outputs reveal the public key early, while others only reveal it at spend time. In the repo's current framing, legacy P2PK and Taproot key-path spends are long-exposure cases because the public key is visible on-chain before the coin moves. P2PKH, P2SH, P2WPKH, and P2WSH are much safer until the first spend, but address reuse turns them into long-lived targets too. Short exposure is different again: once a transaction enters the mempool, a fast enough quantum attacker could try to recover the key and race a competing spend before confirmation.

Taproot deserves a specific callout because it changed Bitcoin's privacy and scripting surface in a way that matters here. A P2TR output commits to a tweaked public key on-chain. In the repo research notes, the key point is that a quantum attacker does not need to reverse back to the untweaked internal key first. They can target the exposed tweaked key directly. That makes Taproot excellent for many current purposes, but awkward in a post-quantum threat model if the key-path remains available.

Mining is a real but different issue. Grover's algorithm provides a quadratic speedup for unstructured search. It does not cause a neat cryptographic collapse the way Shor does against signatures. The likely effect is on cost curves and mining economics, not on Bitcoin's basic ability to use SHA-256 at all. That still matters, especially for centralization, but it belongs in a separate bucket from quantum key recovery.

**Expandable deep dives**

- Long exposure vs short exposure
- Why address reuse is a quiet but important risk multiplier
- The mempool race window and what a short-exposure attack would look like
- Taproot tweak math in plain English
- Why Grover changes mining economics without "breaking SHA-256"

**Relevant assets**

- `assets/charts/exposure-risk.png`
- `assets/images/learn-me-a-bitcoin-taproot-diagram.png`
- `assets/images/mit-peter-shor.png`
- `assets/images/lov-grover.png`

**Sources**

- Learn Me A Bitcoin, "Elliptic Curve Cryptography"  
  https://learnmeabitcoin.com/technical/cryptography/elliptic-curve/
- Learn Me A Bitcoin, "Digital Signatures"  
  https://learnmeabitcoin.com/beginners/guide/digital-signatures/
- Learn Me A Bitcoin, "Hash Functions"  
  https://learnmeabitcoin.com/technical/cryptography/hash-function/
- Learn Me A Bitcoin, "Memory Pool"  
  https://learnmeabitcoin.com/technical/mining/memory-pool/
- Learn Me A Bitcoin, "Taproot (P2TR)"  
  https://learnmeabitcoin.com/technical/script/p2tr/
- Roetteler et al. (2017), "Quantum Resource Estimates for Computing Elliptic Curve Discrete Logarithms"  
  https://arxiv.org/abs/1706.06752
- Repo research note: `notes/thread-memory/qc-threat-presentation-research.md`

## 4. When it starts to matter (ODP slides 11-15, 25, 29)

**Website heading**

No one knows Q-Day, so the right question is probability, not prophecy.

**Purpose / key takeaway**

Anchor the timeline section in uncertainty ranges, not false precision. The website should make it clear that nobody can give an exact arrival date for a CRQC, but the probability bands are now large enough that Bitcoin cannot treat this as a problem for "sometime later."

**Core narrative**

Quantum timelines are hard because they depend on many moving parts at once: hardware quality, error correction, architecture, algorithmic progress, and funding. That is why the site should avoid single-date predictions. A better framing is probability under uncertainty. The GRI Quantum Threat Timeline Report 2025 surveyed 26 experts across academia and industry and found a wide spread of views, but even its pessimistic interpretation still puts the risk within ten years at roughly 28 percent. Its optimistic interpretation puts the number at roughly 49 percent by around 2035.

That uncertainty does not make the problem smaller. It makes early preparation more important. Bitcoin is not the only system watching these dates. Government and standards bodies are already planning around post-quantum migration. NIST released the first core PQC standards in August 2024 and says organizations should begin migration now. Under the current draft transition timeline described in NIST IR 8547, quantum-vulnerable public-key algorithms are expected to be deprecated and ultimately removed from NIST standards by 2035, with high-risk systems moving earlier.

The strategic point for Bitcoin is that quantum spending risk will not wait for Bitcoin-specific deadlines. Nation-state incentives already exist outside Bitcoin. "Harvest now, decrypt later" is the clearest example: adversaries can capture valuable encrypted traffic today and hold it for a future machine. That means progress toward a CRQC can be driven by intelligence, defense, cloud, and scientific incentives even if Bitcoin were not part of the story at all.

The copy in this section should therefore feel like a tightening window, not a countdown clock. The uncertainty is real. The policy signal is real. The external incentives are real. Those facts together justify starting sooner rather than later.

**Expandable deep dives**

- How to read the optimistic and pessimistic GRI curves
- Why probability ranges matter more than a single Q-Day prediction
- Why NIST timelines matter even though NIST does not set Bitcoin policy
- Why HNDL makes quantum risk urgent before the first public Bitcoin theft

**Relevant assets**

- `assets/images/gri-timeline-2025.png`
- `assets/charts/migration-vs-qday.png`
- `assets/charts/gri-curve.png`

**Sources**

- GRI, "Quantum Threat Timeline 2025: Executive Perspectives on Barriers to Action"  
  https://globalriskinstitute.org/publication/quantum-threat-timeline-2025-executive-perspectives-on-barriers-to-action/
- Local extract: `assets/research/pdf-quantum-threat-timeline-report-2025.txt`
- NIST PQC project page  
  https://csrc.nist.gov/projects/post-quantum-cryptography
- NIST IR 8547, "Transition to Post-Quantum Cryptography Standards"  
  https://csrc.nist.gov/pubs/ir/8547/ipd
- Federal Reserve, "Harvest Now, Decrypt Later: Examining Post-Quantum Cryptography and the Data Privacy Risks for Distributed Ledger Networks"  
  https://www.federalreserve.gov/econres/feds/harvest-now-decrypt-later-examining-post-quantum-cryptography-and-the-data-privacy-risks-for-distributed-ledger-networks.htm

## 5. The technical response: PQC, BIP-360, and the migration race (ODP slides 17-25)

**Website heading**

Bitcoin's technical path is not "flip a switch." It is staged migration with hard tradeoffs.

**Purpose / key takeaway**

Show that the technical response has two layers: reduce today's exposure where possible, and build a migration path toward quantum-resistant spending without breaking Bitcoin's social and operational reality.

**Core narrative**

There is no single post-quantum patch that drops cleanly into Bitcoin without tradeoffs. Post-quantum signatures are larger, often slower, and still evolving. Some once-prominent candidates have already failed, which is why the website should present caution as a feature, not a weakness. Bitcoin is right to be conservative here.

The broad family picture is helpful for readers. Hash-based, lattice-based, code-based, multivariate, and isogeny-based schemes have all been studied. For practical near-term discussion, the important standardized names are ML-DSA and SLH-DSA, which NIST finalized in 2024. They give the website something concrete to talk about, but the copy should emphasize tradeoffs rather than imply that Bitcoin has already chosen its final signature scheme.

BIP-360 is the most important Bitcoin-specific mitigation path already in the repo. Its core idea is simple: remove the Taproot key-path spend and commit to a Merkle root of the script tree instead of a tweaked public key. That means a P2MR output does not expose the long-lived key material that makes P2TR awkward in a quantum setting. It is not a complete post-quantum solution, because it does not solve short-exposure attacks by itself, but it does eliminate a major long-exposure surface and creates a cleaner path for future PQC integration.

The website should explain BIP-360 as a pragmatic engineering move. It minimizes network changes, preserves tapscript-like structure, and leaves room for later post-quantum signature opcodes. It also has costs. Witnesses are larger than P2TR key-path spends, privacy differs from the best Taproot case because script-path use is explicit, and the path still requires broad implementation work across wallets, infrastructure, and policy.

The migration race belongs here too. A standard upgrade path may take years. The current repo notes use a rough seven-year figure from a BIP-360 co-author as a reference point for broad adoption under normal conditions. That is exactly why the newer BTQ update matters: it shows that BIP-360 is no longer only a draft on paper. According to the March 2026 repo log, BTQ has running code on its Bitcoin Quantum testnet, more than 50 active miners, more than 100,000 processed blocks, end-to-end wallet tooling, and compatibility claims for Lightning, BitVM, and Ark. That does not mean Bitcoin mainnet is solved. It does mean the conversation has moved from theory toward implementation.

**Expandable deep dives**

- PQC signature families and why Bitcoin should stay conservative
- ML-DSA vs SLH-DSA in practical Bitcoin terms
- BIP-360 witness structure and why `bc1z` matters
- P2MR size and privacy tradeoffs vs P2TR
- Standard migration path vs urgent migration path
- BitMEX dual-path Taproot idea as an intermediate design

**Relevant assets**

- `assets/images/signiture-comparison.png`
- `assets/images/bip360-address-type-vulnerability.png`
- `assets/images/bip360-merkletree.png`
- `assets/charts/bip360-witness-size.png`
- `assets/charts/witness-cmp.png`

**Sources**

- BIP360.org overview  
  https://bip360.org/bip360.html
- BIP-360 draft specification  
  https://github.com/bitcoin/bips/blob/master/bip-0360.mediawiki
- BitMEX Research, "Taproot Quantum Spend Paths"  
  https://www.bitmex.com/blog/Taproot-Quantum-Spend-Paths
- TradingView / Cointelegraph, "Bitcoin may take 7 years to upgrade to post-quantum BIP-360: co-author"  
  https://www.tradingview.com/news/cointelegraph%253A30729863f094b%253A0-bitcoin-may-take-7-years-to-upgrade-to-post-quantum-bip-360-co-author/
- Chaincode Labs, "Bitcoin Post-Quantum"  
  https://chaincode.com/bitcoin-post-quantum.pdf
- NIST FIPS 204, ML-DSA  
  https://csrc.nist.gov/pubs/fips/204/final
- NIST FIPS 205, SLH-DSA  
  https://csrc.nist.gov/pubs/fips/205/final
- Repo working note: `qc-threat-log.md`
- Atlas21 summary of BTQ implementation progress  
  https://atlas21.com/bip-360-btq-launches-the-first-implementation-to-protect-bitcoin-from-quantum-computers/

## 6. The governance response: legacy coins, freezes, and Hourglass (ODP slides 16, 26, 30)

**Website heading**

The hardest Bitcoin problem may not be the new cryptography. It may be the old coins.

**Purpose / key takeaway**

Explain that post-quantum Bitcoin is not only a wallet-upgrade problem. It is also a legitimacy problem around coins that never migrate. Any credible website treatment needs to show why this debate cuts across censorship resistance, market stability, and social consensus.

**Core narrative**

Even if Bitcoin ships a good technical migration path, a second problem remains: what happens to coins that never upgrade? If a future CRQC can steal from exposed legacy outputs, then doing nothing preserves Bitcoin's current rules but risks theft and a severe market shock. On the other hand, freezing or invalidating vulnerable coins might reduce theft but would directly challenge assumptions about property rights, censorship resistance, and the social contract.

That is why the social layer matters so much here. The debate is not really "security vs insecurity." It is a three-way tension among security, legitimacy, and continuity. A hard freeze could protect the market while damaging Bitcoin's political credibility. A status-quo approach could protect that credibility while accepting theft and price dislocation. Hourglass-style proposals try to sit in the middle by rate-limiting the movement of quantum-exposed coins rather than simply ignoring the issue or banning those coins outright.

This is also where Satoshi's coins become the symbolic center of the debate. If the most famous unspent coins are considered vulnerable, then any intervention around them will be interpreted as a precedent for the rest of the network. That is part of why the governance problem can be harder than the cryptographic problem. Code can be drafted in a BIP. Legitimacy has to survive a political fight.

The website should not pretend there is already consensus here. It should present the main positions fairly, show what each one protects and sacrifices, and make it clear that a quantum event could drive a wedge into Bitcoin even if the technical fixes are available.

**Expandable deep dives**

- Status quo vs freeze vs Hourglass
- What "rate limiting" tries to preserve that freezing does not
- Satoshi's coins as the hardest governance edge case
- Why a quantum response could still cause a chain split

**Relevant assets**

- `assets/images/project-eleven-exposed-bitcoin.png`
- `assets/charts/migration.png`
- `assets/charts/exposure-risk.png`

**Sources**

- Hourglass v2 draft  
  https://github.com/cryptoquick/bips/blob/hourglass-v2/bip-hourglass-v2.mediawiki
- Jameson Lopp, "Against Quantum Recovery of Bitcoin"  
  https://blog.lopp.net/against-quantum-recovery-of-bitcoin/
- CoinDesk, "To Freeze or Not to Freeze - Satoshi and the $440B in Bitcoin Threatened by Quantum Computing"  
  https://www.coindesk.com/business/2026/02/22/to-freeze-or-not-to-freeze-satoshi-and-the-usd440-billion-in-bitcoin-threatened-by-quantum-computing
- Cointelegraph Magazine, "Bitcoin may face hard fork over any attempt to freeze Satoshi's coins"  
  https://cointelegraph-magazine.com/bitcoin-may-face-hard-fork-over-any-attempt-to-freeze-satoshis-coins/
- Repo working note: `qc-threat-log.md`

## 7. What users can do now (ODP slides 27, 30)

**Website heading**

You cannot solve the entire problem today, but you can reduce avoidable exposure.

**Purpose / key takeaway**

Turn the topic into practical guidance. The best current advice is mostly about exposure hygiene, operational awareness, and being ready to migrate when the ecosystem has credible tools.

**Core narrative**

The first practical rule is simple: do not create unnecessary long-term public-key exposure. Avoid address reuse. Be cautious about output types that reveal public keys earlier in their lifecycle if quantum long exposure is part of your threat model. In the repo's current framing, P2PK and Taproot key-path exposure deserve extra caution here because the public key is already sitting on-chain before a future spend.

The second rule is to think beyond addresses. Public information leakage matters too. Extended public keys can reveal wallet structure and future address derivation paths, which is why the existing project notes call out xpub sharing in contexts such as SMSF auditing and public node use. That is not the same thing as a quantum break, but it can enlarge the map an attacker works from.

The third rule is to prepare for migration rather than improvise during panic. When credible post-quantum standards, wallet support, and Bitcoin-specific conventions arrive, the goal will be orderly movement, not last-minute scrambling. That matters for individuals, but even more for exchanges, custodians, multisig setups, and Lightning-related infrastructure.

The website should make room for participation too. People can fund research, test implementations, run nodes, follow BIP discussions, and help normalize calm technical discussion instead of fear. "Satoshi's shield" can be mentioned here as a game-theoretic idea, but not as a primary defense plan.

**Expandable deep dives**

- Address hygiene by output type
- Why xpub exposure matters
- What users should not overreact to yet
- What institutions should inventory before a migration wave
- How to participate without pretending to be a cryptographer

**Relevant assets**

- `assets/charts/exposure-risk.png`
- `assets/images/project-eleven-exposed-bitcoin.png`

**Sources**

- Learn Me A Bitcoin, "Memory Pool"  
  https://learnmeabitcoin.com/technical/mining/memory-pool/
- Learn Me A Bitcoin, "Taproot (P2TR)"  
  https://learnmeabitcoin.com/technical/script/p2tr/
- Repo source-of-truth draft: `qc-threat-pres-v1.md`
- Repo research note: `notes/thread-memory/qc-threat-presentation-research.md`

## 8. Mythbusters and perspective (ODP slides 28-30)

**Website heading**

The quantum threat is real, staged, and much bigger than Bitcoin.

**Purpose / key takeaway**

End by calibrating the audience. This section should kill the most common misunderstandings while showing why quantum investment will continue with or without Bitcoin.

**Core narrative**

The first myth to kill is that a CRQC would instantly drain every Bitcoin address. It would not. Exposure type matters. Time window matters. Address behavior matters. That does not make the threat trivial. It makes it more specific.

The second myth is that Grover's algorithm "kills SHA-256." It does not. A quadratic speedup is significant, but it is not the same category of failure as Shor's attack on signatures. The right mental model is shifting cost curves, not magical collapse.

The third myth is that this is only a Bitcoin problem. It is not. The same quantum progress that worries Bitcoin is also relevant to state intelligence, encrypted archives, enterprise infrastructure, and scientific computing. That broader context matters because it explains why large-scale investment in quantum computing will continue even if Bitcoin itself is not the top priority for the organizations building these machines.

That is also why the positive case for quantum computing belongs on the website. Materials science, chemistry, pharmaceutical research, optimization, and experimental physics all help explain why the field is moving forward. The goal of this section is not to market quantum computing. It is to show that Bitcoin sits inside a much larger technological and geopolitical story.

**Expandable deep dives**

- Why "genuine but not imminent" is the right tone
- The difference between Shor panic and Grover panic
- Harvest now, decrypt later as a non-Bitcoin pressure source
- The most plausible first uses of a CRQC outside Bitcoin

**Relevant assets**

- `assets/images/lov-grover.png`
- `assets/images/mit-peter-shor.png`
- `assets/images/ibm-100-qubits-title-pic.jpg`

**Sources**

- Federal Reserve, "Harvest Now, Decrypt Later: Examining Post-Quantum Cryptography and the Data Privacy Risks for Distributed Ledger Networks"  
  https://www.federalreserve.gov/econres/feds/harvest-now-decrypt-later-examining-post-quantum-cryptography-and-the-data-privacy-risks-for-distributed-ledger-networks.htm
- Frontiers, "Quantum Computing - Foundations, Algorithms, and Emerging Applications"  
  https://www.frontiersin.org/journals/quantum-science-and-technology/articles/10.3389/frqst.2025.1723319/full
- Nature, "Quantum-machine-assisted drug discovery"  
  https://www.nature.com/articles/s44386-025-00033-2
- Repo working note: `qc-threat-log.md`

## Appendix A: Bibliography grouped by website section

### Framing the problem

- Bitcoin Magazine, "The Quantum Bitcoin Summit: A Grounded Look at the Issues"  
  https://bitcoinmagazine.com/technical/the-quantum-bitcoin-summit-a-grounded-look-at-the-issues
- Repo working note: `qc-threat-log.md`
- Atlas21 summary of Galaxy Digital  
  https://atlas21.com/galaxy-digital-the-quantum-risk-to-bitcoin-is-real-but-the-network-is-preparing/

### How quantum computing actually gets an advantage

- IBM Quantum Learning, "Bits, Gates, and Circuits"  
  https://quantum.cloud.ibm.com/learning/en/courses/utility-scale-quantum-computing/bits-gates-and-circuits
- IBM Quantum Learning, "The Deutsch-Jozsa Algorithm"  
  https://quantum.cloud.ibm.com/learning/en/modules/computer-science/deutsch-jozsa
- IBM, "What is a qubit?"  
  https://www.ibm.com/think/topics/qubit
- IBM, "What Is Quantum Computing?"  
  https://www.ibm.com/think/topics/quantum-computing
- IBM Quantum Learning, "Approach to fault tolerance"  
  https://quantum.cloud.ibm.com/learning/en/courses/foundations-of-quantum-error-correction/fault-tolerant-quantum-computing/approach-to-fault-tolerance
- Roetteler et al. (2017)  
  https://arxiv.org/abs/1706.06752
- Ha, Lee, and Heo (2024)  
  https://www.nature.com/articles/s41598-024-54434-w

### Why Bitcoin is exposed

- Learn Me A Bitcoin, "Elliptic Curve Cryptography"  
  https://learnmeabitcoin.com/technical/cryptography/elliptic-curve/
- Learn Me A Bitcoin, "Digital Signatures"  
  https://learnmeabitcoin.com/beginners/guide/digital-signatures/
- Learn Me A Bitcoin, "Hash Functions"  
  https://learnmeabitcoin.com/technical/cryptography/hash-function/
- Learn Me A Bitcoin, "Memory Pool"  
  https://learnmeabitcoin.com/technical/mining/memory-pool/
- Learn Me A Bitcoin, "Taproot (P2TR)"  
  https://learnmeabitcoin.com/technical/script/p2tr/
- Roetteler et al. (2017)  
  https://arxiv.org/abs/1706.06752
- Repo research note: `notes/thread-memory/qc-threat-presentation-research.md`

### When it starts to matter

- GRI, "Quantum Threat Timeline 2025: Executive Perspectives on Barriers to Action"  
  https://globalriskinstitute.org/publication/quantum-threat-timeline-2025-executive-perspectives-on-barriers-to-action/
- Local extract: `assets/research/pdf-quantum-threat-timeline-report-2025.txt`
- NIST PQC project page  
  https://csrc.nist.gov/projects/post-quantum-cryptography
- NIST IR 8547  
  https://csrc.nist.gov/pubs/ir/8547/ipd
- Federal Reserve HNDL paper  
  https://www.federalreserve.gov/econres/feds/harvest-now-decrypt-later-examining-post-quantum-cryptography-and-the-data-privacy-risks-for-distributed-ledger-networks.htm

### The technical response

- BIP360.org overview  
  https://bip360.org/bip360.html
- BIP-360 draft specification  
  https://github.com/bitcoin/bips/blob/master/bip-0360.mediawiki
- BitMEX Research, "Taproot Quantum Spend Paths"  
  https://www.bitmex.com/blog/Taproot-Quantum-Spend-Paths
- TradingView / Cointelegraph BIP-360 timeline article  
  https://www.tradingview.com/news/cointelegraph%253A30729863f094b%253A0-bitcoin-may-take-7-years-to-upgrade-to-post-quantum-bip-360-co-author/
- Chaincode Labs, "Bitcoin Post-Quantum"  
  https://chaincode.com/bitcoin-post-quantum.pdf
- NIST FIPS 204  
  https://csrc.nist.gov/pubs/fips/204/final
- NIST FIPS 205  
  https://csrc.nist.gov/pubs/fips/205/final
- Repo working note: `qc-threat-log.md`
- Atlas21 summary of BTQ implementation progress  
  https://atlas21.com/bip-360-btq-launches-the-first-implementation-to-protect-bitcoin-from-quantum-computers/

### The governance response

- Hourglass v2 draft  
  https://github.com/cryptoquick/bips/blob/hourglass-v2/bip-hourglass-v2.mediawiki
- Jameson Lopp, "Against Quantum Recovery of Bitcoin"  
  https://blog.lopp.net/against-quantum-recovery-of-bitcoin/
- CoinDesk freeze debate  
  https://www.coindesk.com/business/2026/02/22/to-freeze-or-not-to-freeze-satoshi-and-the-usd440-billion-in-bitcoin-threatened-by-quantum-computing
- Cointelegraph Magazine hard fork article  
  https://cointelegraph-magazine.com/bitcoin-may-face-hard-fork-over-any-attempt-to-freeze-satoshis-coins/
- Repo working note: `qc-threat-log.md`

### What users can do now

- Learn Me A Bitcoin, "Memory Pool"  
  https://learnmeabitcoin.com/technical/mining/memory-pool/
- Learn Me A Bitcoin, "Taproot (P2TR)"  
  https://learnmeabitcoin.com/technical/script/p2tr/
- Repo source-of-truth draft: `qc-threat-pres-v1.md`
- Repo research note: `notes/thread-memory/qc-threat-presentation-research.md`

### Mythbusters and perspective

- Federal Reserve HNDL paper  
  https://www.federalreserve.gov/econres/feds/harvest-now-decrypt-later-examining-post-quantum-cryptography-and-the-data-privacy-risks-for-distributed-ledger-networks.htm
- Frontiers, "Quantum Computing - Foundations, Algorithms, and Emerging Applications"  
  https://www.frontiersin.org/journals/quantum-science-and-technology/articles/10.3389/frqst.2025.1723319/full
- Nature, "Quantum-machine-assisted drug discovery"  
  https://www.nature.com/articles/s44386-025-00033-2
- Repo working note: `qc-threat-log.md`

## Appendix B: Asset index for Lovable

| Asset | Recommended use | Section |
| --- | --- | --- |
| `assets/images/ibm-100-qubits-title-pic.jpg` | Hero or background image for opening and QC basics | 1, 2, 8 |
| `assets/images/project-eleven-exposed-bitcoin.png` | Framing visual for exposed coins and risk awareness | 1, 6, 7 |
| `assets/images/gri-timeline-2025.png` | Primary timeline visual | 1, 4 |
| `assets/images/mit-peter-shor.png` | Visual anchor for Shor / signature threat | 2, 3, 8 |
| `assets/images/lov-grover.png` | Visual anchor for Grover / mining discussion | 2, 3, 8 |
| `assets/images/learn-me-a-bitcoin-taproot-diagram.png` | Taproot explainer support image | 3 |
| `assets/charts/exposure-risk.png` | Exposure-type chart | 3, 6, 7 |
| `assets/charts/migration-vs-qday.png` | Migration race visual | 4 |
| `assets/charts/gri-curve.png` | Secondary timeline visual if labels are checked before publish | 4 |
| `assets/images/signiture-comparison.png` | Signature tradeoff comparison | 5 |
| `assets/images/bip360-address-type-vulnerability.png` | Long-exposure comparison by output type | 5 |
| `assets/images/bip360-merkletree.png` | P2MR architecture visual | 5 |
| `assets/charts/bip360-witness-size.png` | Witness-size tradeoff chart | 5 |
| `assets/charts/witness-cmp.png` | Alternate witness-size comparison | 5 |
| `assets/charts/migration.png` | Governance / migration support chart | 6 |

## Appendix C: Later-phase website features

Do not fold these into the first content build. Treat them as phase-two additions after the core notes are turned into a stable website.

- Podcasts section: curate episodes, summaries, metadata, and a lightweight ingestion workflow for later updates.
- Cron-based update layer: fetch new articles, podcasts, and implementation milestones after the editorial model is stable.
- Inline AI panel: restrict the retrieval corpus to vetted local markdown and source notes so the assistant answers from the project's own material first.
