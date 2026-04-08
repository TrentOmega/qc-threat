# Quantum Computing Threat — Running Log

Running log of new quantum computing threat articles and developments.
Cross-referenced against existing presentation material in `qc-threat-pres-v1.md` (36 references) to avoid duplication.

---

## New Information

### Quantum FUD / Narrative Risk

Atlas21 reported on April 1, 2026 that media coverage around a new Google quantum paper escalated into fresh Bitcoin quantum alarmism, while the article argues the engineering gap remains very large and that post-quantum migration work such as BIP-360 is already progressing [[4]](#ref-4). This source is less useful as a primary technical reference and more useful as evidence of how quantum-risk narratives are being framed in public discourse [[4]](#ref-4).

The main value for future presentation use is rhetorical rather than technical: it gives a concrete example of how sensational headlines can outrun the practical state of fault-tolerant quantum hardware, and it surfaces the political or ecosystem incentives around quantum messaging [[4]](#ref-4).

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
