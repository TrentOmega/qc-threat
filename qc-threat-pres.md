# Quantum Computing Threat to Bitcoin

## Presentation Length
* 30 minutes including quesitons

## Audience

* Bitcoin: beginner to advance on bitcoin  
* QC: no knowledge to intermediate

## Objective

* Overview the threat, what can we do, what can you do.

## Outline

* ### What is Quantum Computing (QC)

  * What makes it work: superposition and entanglement  
  * What we currently have   
  * What’s getting built ([ref](https://bitcoinmagazine.com/technical/the-quantum-bitcoin-summit-a-grounded-look-at-the-issues))  
  * Cryptographic Relevant Quantum Computer (CRQC)  
    * physical qubits → error correction → logical qubits  
    * logical qubits \+ runtime → “can it run Shor fast enough?”

* ### What is the QC threat to Bitcoin

  * Digital signatures: Shor’s algorithm  
    * Long exposure attack:
      * P2PK/P2TR immediatly exposed,
      * P2PKH/P2SH/P2WPKH/P2WSH exposed after first spend (address reuse)
    * Short exposure attack: mempool window  
  * Mining: Grover’s algorithm

* ### Revision

  * Digital signatures and hashing  
  * How digital signatures are used in Bitcoin  
  * How hashing is used in Bitcoin  
    * Mining  
    * Compressing and concealing public keys  
  * Spending bitcoin and the mempool

* ### When is it coming

  * Q-day likelihoods (GRI Quantum Threat Timeline Report 2024)  
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
    * Hash based: SPHINCS+  
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
    * Steal: preserves censorship resistance but could collapse price  
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

1. [https://bip360.org/bip360.html](https://bip360.org/bip360.html)  
2. [https://github.com/bitcoin/bips/blob/master/bip-0360.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0360.mediawiki)  
3. [https://www.bitmex.com/blog/Taproot-Quantum-Spend-Paths](https://www.bitmex.com/blog/Taproot-Quantum-Spend-Paths)  
4. [https://www.tradingview.com/news/cointelegraph%253A30729863f094b%253A0-bitcoin-may-take-7-years-to-upgrade-to-post-quantum-bip-360-co-author/](https://www.tradingview.com/news/cointelegraph%253A30729863f094b%253A0-bitcoin-may-take-7-years-to-upgrade-to-post-quantum-bip-360-co-author/)  
5. [https://www.tradingview.com/news/cointelegraph:d4cc2ff14094b:0-bitcoin-faces-6-massive-challenges-to-become-quantum-secure/](https://www.tradingview.com/news/cointelegraph:d4cc2ff14094b:0-bitcoin-faces-6-massive-challenges-to-become-quantum-secure/)  
6. [https://bitcoinmagazine.com/news/bitcoin-advances-toward-quantum-resistance](https://bitcoinmagazine.com/news/bitcoin-advances-toward-quantum-resistance)  
7. [https://bitcoinmagazine.com/technical/the-quantum-bitcoin-summit-a-grounded-look-at-the-issues](https://bitcoinmagazine.com/technical/the-quantum-bitcoin-summit-a-grounded-look-at-the-issues)  
8. [https://github.com/cryptoquick/bips/blob/hourglass-v2/bip-hourglass-v2.mediawiki](https://github.com/cryptoquick/bips/blob/hourglass-v2/bip-hourglass-v2.mediawiki)  
9. [https://blog.lopp.net/against-quantum-recovery-of-bitcoin/](https://blog.lopp.net/against-quantum-recovery-of-bitcoin/)

