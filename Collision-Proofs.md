# Demonstrating Hash Collisions
## Overview

This document provides formal proofs of hash collisions using two distinct examples.
A hash collision occurs when two different inputs produce the same hash output, violating the principle of uniqueness in hashing functions.
While hash functions are designed to minimize collisions, due to limited output space, collisions are mathematically inevitable (as proven by the Pigeonhole Principle).

### Example 1 — Hash Collision in a Simple Modular Hash Function
Hash Function Definition
    Let the hash function be:
    h(x) = x mod 10
    This function maps any integer x to the remainder when divided by 10.

Proof of Collision

Let’s consider:
        Input A = 27
        Input B = 37

Compute hashes
        h(27) = 27 mod 10 = 7
        h(37) = 37 mod 10 = 7

Result
        h(27) == h(37)
        Yet, 27 ≠ 37 — hence, a collision has occurred.

Explanation
- The hash space (0–9) has only 10 possible outputs, but there are infinitely many integers.
- By the Pigeonhole Principle, at least two distinct integers must share the same hash value.

Impact
In real-world hash tables:
  - Collisions reduce efficiency (O(1) → O(n) lookup time).
  - Require collision resolution techniques like chaining or open addressing.
  - If not handled, data may overwrite or become inaccessible.

### Example 2 — Collision in the Real MD5 Hash Function
Hash Function

MD5 (Message Digest 5) is a popular cryptographic hash function that outputs a 128-bit digest.
However, MD5 is cryptographically broken — collisions can be constructed intentionally.

Known Collision Example
Two different files (binary inputs) produce the same MD5 hash.
    
```
    import hashlib, binascii
    
    hex_a = (
        "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5be2aa8f5e4a8aa3b4e1e4a0544c4e72e0a27afccfa6cfc79f1b91efda45a7fc5f664b6117ba6f7fbf8"
        "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5be2aa8f5e4a8aa3b4e1e4a0544c4e72e0a27afccfa6cfc79f1b91efda45a7fc5f664b6117ba6f7fbf8"
    )
    
    hex_b = (
        "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5be2aa8f5e4a8aa3b4e1e4a0544c4e72e0a27afccfa6cfc79f1b91efda45a7fc5f664b60f7ba6f7fbf8"
        "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5be2aa8f5e4a8aa3b4e1e4a0544c4e72e0a27afccfa6cfc79f1b91efda45a7fc5f664b60f7ba6f7fbf8"
    )
    
    a = binascii.unhexlify(hex_a)
    b = binascii.unhexlify(hex_b)
    
    print("Length(hex_a):", len(hex_a))
    print("Even length?", len(hex_a) % 2 == 0)
    print("A == B?", a == b)
    print("MD5(A):", hashlib.md5(a).hexdigest())
    print("MD5(B):", hashlib.md5(b).hexdigest())

```
    
Impact
- Cryptographic trust is broken.
- Attackers can create two different files (for example, contracts or certificates) with the same MD5 hash.
- Modern systems have deprecated MD5 and moved to SHA-256 or SHA-3.

#### Significance
Hash collisions demonstrate that:
    Perfect hashing is impossible for unbounded input domains.
    Collision resistance is critical in cryptographic systems.
    Developers must choose appropriate hash algorithms based on use cases — performance versus security.
