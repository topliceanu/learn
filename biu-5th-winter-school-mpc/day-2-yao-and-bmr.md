# The Yao and the BMR multi-party computation

## Yao's protocol

- general secure computation, constant number of rounds, secure agains semi-honest adversaries
- represent the function as a boolean circuits (ie. formed with gates - 2 input and one output wire, a "truth" table)
  - AES - 30k gates
  - indirect addressing is hard with gates, eg. A[i]
  - billions of gates are easily computed

- garbled circuit: each gate is encrypted
  - for every "wire" in the circuit, we assign two random keys associated with the 0 and 1 values of that wire, (k0, k1). The keys are also called _garbled values_.
  - every gate, given one key for each input wire (corresponding to a 0 or 1 value on each wire), will compute the key corresponding to the gate's output and nothing else.
  Q: So, we're computing keys?! instead of values
  - this is done using OT (oblivious transfer).
  Q: are we using symmetric keys. That's why we talked about AES before?

Eg. a garbled AND gate

```
  k(u,0)  +-----\
u --------+      \
  k(u,1)  |       \   k(w,0)
          |        )---------- w
  k(v,0)  |       /   k(w,1)
v --------+      /
  k(v,1)  +-----/
```

-------+---------+------------------------------
u      | v       | w = u AND v
-------+---------+------------------------------
k(u,0) | k(v, 0) | E(k(u,0), E(k(v,0), k(w, 0)))
k(u,1) | k(v, 0) | E(k(u,1), E(k(v,0), k(w, 0)))
k(u,0) | k(v, 1) | E(k(u,0), E(k(v,1), k(w, 0)))
k(u,1) | k(v, 1) | E(k(u,1), E(k(v,1), k(w, 1)))

  - the party evaluating this circuit will only be able to decypt just a single entry of this table
  - we permute the truth table otherwise decrypting an entry immediately reveals what this entry corresponds to.
  - to use the output, we also provide a translation table for the garbled values: [(0, k(w, 0)), (1, k(w, 1))]
  - if the output is used as input to other gates, we provide a translation table with hash values.
