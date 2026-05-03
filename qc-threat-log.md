# Quantum Computing Threat — Running Log

Running log of new quantum computing threat articles and developments.
Cross-referenced against existing presentation material in `qc-threat-pres-v1.md` (36 references) to avoid duplication.

---

## New Information

### Google Responsible Disclosure of Quantum Vulnerabilities

Google Research published a March 31, 2026 post explaining its approach to responsible disclosure for quantum vulnerabilities in cryptocurrency systems [[9]](#ref-9). The post says Google's new whitepaper gives updated ECDLP-256 attack resource estimates, including circuits using fewer than 1,200 logical qubits and 90 million Toffoli gates, or fewer than 1,450 logical qubits and 70 million Toffoli gates [[9]](#ref-9).

For future presentation use, this is a strong primary source for the "serious but disclose carefully" framing. Google explicitly warns that unscientific quantum break estimates can become FUD, says it is using zero-knowledge proofs to substantiate claims without publishing sensitive circuit details, and recommends cryptocurrency communities move toward post-quantum cryptography while reducing avoidable exposure such as address reuse [[9]](#ref-9).

### QSB Proposal Without Consensus Changes

Atlas21 reported on a new Bitcoin QSB proposal that claims to improve quantum resistance for Bitcoin transactions without requiring protocol changes [[6]](#ref-6). This is useful to track because it sits in a different design space from BIP-360: wallet- or transaction-level mitigation that may be deployable earlier, even if it comes with tradeoffs in assumptions, UX, or security model [[6]](#ref-6).

For future presentation use, this is worth comparing against BIP-360 and post-quantum signature proposals as a "what can be done without consensus changes?" branch of the solution space [[6]](#ref-6).

### First Wallet Anti-Quantum Prototype

Atlas21 also reported the first working prototype of an anti-quantum tool for Bitcoin wallets [[7]](#ref-7). That makes it a practical progress marker rather than a purely conceptual proposal, and it strengthens the case that wallet-layer experimentation is already underway alongside protocol-level work such as BIP-360 [[7]](#ref-7).

This source is useful in the progress report because it shows implementation momentum: not just standards discussion, but actual prototype software for wallet defenses [[7]](#ref-7).

### Adam Back: Decades, Not Immediate Crisis

Bitcoin Magazine reported on April 8, 2026 that Adam Back argued the quantum threat to Bitcoin is still decades away, while still urging gradual migration toward post-quantum security [[8]](#ref-8). This is useful because it sharpens the presentation's framing: the threat is real, preparation should begin now, but the situation is not an immediate break-glass emergency [[8]](#ref-8).

For future presentation use, this source helps balance the more alarmist narratives and supports a "serious but not imminent" position from a widely recognised Bitcoin technical voice [[8]](#ref-8).

### Quantum FUD / Narrative Risk

Atlas21 reported on April 1, 2026 that media coverage around a new Google quantum paper escalated into fresh Bitcoin quantum alarmism, while the article argues the engineering gap remains very large and that post-quantum migration work such as BIP-360 is already progressing [[4]](#ref-4). This source is less useful as a primary technical reference and more useful as evidence of how quantum-risk narratives are being framed in public discourse [[4]](#ref-4).

The main value for future presentation use is rhetorical rather than technical: it gives a concrete example of how sensational headlines can outrun the practical state of fault-tolerant quantum hardware, and it surfaces the political or ecosystem incentives around quantum messaging [[4]](#ref-4).

### BIP-360 Testnet Deployment Coverage

Bitcoin Magazine reported last week that Google's new quantum research renewed pressure to harden Bitcoin, and the piece explicitly highlighted that developers already have a BIP-360 testnet deployment to work with [[5]](#ref-5). That makes this a useful supporting source for the claim that Bitcoin's quantum response is no longer purely theoretical and now includes deployed test infrastructure [[5]](#ref-5).

For future presentation use, the main value is not the Google angle itself but the fact that a mainstream Bitcoin publication is now tying the broader quantum discussion directly to the Bitcoin Quantum testnet and active BIP-360 implementation work [[5]](#ref-5).

### SHRIMPS Post-Quantum Signature Scheme

Atlas21 reported on April 2, 2026 that Blockstream researcher Jonas Nick presented SHRIMPS, a hash-based post-quantum signature scheme designed for multi-device signing with signatures of approximately 2.5 KB [[3]](#ref-3). The proposal was published on March 30, 2026 and positions itself as a more practical fit for wallet setups that need multiple devices sharing a seed-derived signing configuration [[3]](#ref-3).

The article highlights the contrast with stateless hash-based alternatives such as SLH-DSA, where signatures are materially larger, and with SHRINCS, which is smaller but constrained by single-device state management [[3]](#ref-3). For Bitcoin, the notable angle is wallet usability: the scheme is explicitly framed around limited-signature, multi-device environments rather than generic enterprise signing [[3]](#ref-3).

### BIP-360 Implementation Progress

BTQ Technologies has released the first working implementation of BIP-360 (Pay-to-Merkle-Root), moving it from proposal to running code on a dedicated testnet [[2]](#ref-2). The Bitcoin Quantum testnet (v0.3.0) has over 50 active miners and has processed more than 100,000 blocks [[2]](#ref-2). The implementation includes full wallet tooling — users can create, fund, sign, and broadcast P2MR transactions end-to-end [[2]](#ref-2).

P2MR has been confirmed compatible with Lightning Network scripting, as well as emerging frameworks BitVM and Ark [[2]](#ref-2). The architecture removes the key-path spend mechanism introduced with Taproot, which in a quantum attack scenario exposes public keys [[2]](#ref-2).

BTQ CEO Olivier Roussy Newton: *"BIP 360 represents the Bitcoin community's most significant step toward quantum resistance and we've turned it from a proposal into running code."* [[2]](#ref-2)

### Galaxy Digital Report

Galaxy Digital published a formal report (March 19, 2026) framing the quantum threat as "genuine but not imminent" and characterising it as a long-term engineering and governance challenge [[1]](#ref-1). Most content overlaps existing presentation material, but the report provides a useful consolidated industry perspective. Galaxy frames the governance problem — deciding what happens to non-migrated coins — as potentially harder than the cryptographic upgrade itself [[1]](#ref-1).

---

## References

### <a id="ref-1"></a>[1] Galaxy Digital: The Quantum Risk to Bitcoin is Real, but the Network is Preparing
https://atlas21.com/galaxy-digital-the-quantum-risk-to-bitcoin-is-real-but-the-network-is-preparing/

Galaxy Digital report (March 19, 2026) concluding the quantum threat is genuine but not imminent, covering BIP-360, Hourglass, exposed coins, and PQC signature schemes.

**New information:** Mostly overlaps existing presentation references. Useful as a consolidated industry reference framing governance as the harder problem.

### <a id="ref-2"></a>[2] BIP 360: BTQ Launches the First Implementation to Protect Bitcoin from Quantum Computers
https://atlas21.com/bip-360-btq-launches-the-first-implementation-to-protect-bitcoin-from-quantum-computers/

BTQ Technologies releases the first working BIP-360 implementation on the Bitcoin Quantum testnet v0.3.0, with full P2MR wallet tooling and confirmed compatibility with Lightning, BitVM, and Ark.

**New information:** First working BIP-360 code. Testnet has 50+ miners and 100k+ blocks. P2MR compatibility with Lightning/BitVM/Ark confirmed. Full end-to-end wallet tooling available.

### <a id="ref-3"></a>[3] Blockstream: Jonas Nick presents SHRIMPS, a post-quantum signature scheme for Bitcoin
https://atlas21.com/blockstream-jonas-nick-presents-shrimps-a-post-quantum-signature-scheme-for-bitcoin/

Atlas21 article (April 2, 2026) on Jonas Nick's March 30, 2026 SHRIMPS proposal: a hash-based post-quantum signature scheme targeting multi-device signing with signatures of approximately 2.5 KB.

**New information:** Adds a concrete Bitcoin-oriented PQ signature design to track. Relevant because it focuses on wallet-friendly multi-device operation rather than only generic PQC benchmarks.

### <a id="ref-4"></a>[4] Bitcoin and quantum computing: FUD courtesy of Google and the Ethereum Foundation
https://atlas21.com/bitcoin-and-quantum-computing-fud-courtesy-of-google-and-the-ethereum-foundation/

Atlas21 article (April 1, 2026) arguing that recent media reactions to a Google quantum paper overstated the near-term risk to Bitcoin and that engineering reality remains far from practical secp256k1-breaking machines.

**New information:** Useful as a future presentation source on narrative risk, media framing, and quantum FUD rather than as a primary technical source.

### <a id="ref-5"></a>[5] Google’s New Quantum Research Reignites Push to Harden Bitcoin
https://bitcoinmagazine.com/news/googles-quantum-research-harden-bitcoin

Bitcoin Magazine article published last week connecting Google's latest quantum research to Bitcoin's migration planning and explicitly pointing to the already-deployed BIP-360 Bitcoin Quantum testnet as evidence of active implementation progress.

**New information:** Strong supporting source for the BIP-360 testnet deployment point because it frames deployed quantum-resistance work as already underway, not merely proposed.

### <a id="ref-6"></a>[6] Bitcoin QSB proposal offers quantum resistance without protocol changes
https://atlas21.com/bitcoin-qsb-proposal-offers-quantum-resistance-without-protocol-changes/

Atlas21 article on a Bitcoin QSB proposal positioned as a way to add quantum resistance without changing Bitcoin's consensus rules.

**New information:** Useful for tracking wallet- or transaction-layer mitigation ideas that do not depend on a protocol upgrade.

### <a id="ref-7"></a>[7] Bitcoin: first working prototype of anti-quantum tool for wallets
https://atlas21.com/bitcoin-first-working-prototype-of-anti-quantum-tool-for-wallets/

Atlas21 article on the first working prototype of an anti-quantum tool for Bitcoin wallets.

**New information:** Important implementation signal. Shows wallet-layer anti-quantum work moving from concept into prototype.

### <a id="ref-8"></a>[8] Adam Back Says Quantum Threat to Bitcoin Is Decades Away, Urges Gradual Migration to Post-Quantum Security
https://bitcoinmagazine.com/news/adam-back-says-quantum-threat-to-bitcoin

Bitcoin Magazine article published April 8, 2026 reporting Adam Back's view that quantum risk is real but still decades away, paired with a recommendation to migrate gradually toward post-quantum security.

**New information:** Strong source for a balanced framing: prepare now, but avoid treating current quantum progress as an immediate existential break of Bitcoin.

### <a id="ref-9"></a>[9] Safeguarding cryptocurrency by disclosing quantum vulnerabilities responsibly
https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/

Google Research article (March 31, 2026) by Ryan Babbush and Hartmut Neven describing updated quantum resource estimates for ECDLP-256, recommendations for cryptocurrency PQC migration, and a responsible disclosure model based on zero-knowledge proof verification rather than publishing attack circuits.

**New information:** Primary-source support for updated ECDLP-256 estimates, responsible disclosure norms, FUD-aware communication, and Google's recommendation that cryptocurrency systems transition to post-quantum cryptography.
