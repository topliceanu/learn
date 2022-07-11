# Snarks

## HH (homomorphic hiding)
E(x) is HH if:
- hard to reverse: for most xs, give E(x) it's hard to find x
- different inputs lead to different outputs: x!=y then E(x)!=E(y)
- given E(x) and E(y) you can compute E(x + y) and E(x * y) without knowing x and y.

`Zp*` - the cyclic group of pozitive integers module p over the multiplication operation.

## Blind evaluation of Polinomials

- given E(X) a HH known by prover and verifier and polynomial `P(X) = a0 + a1*X + a2*X^2 + ... + ad*X^d` that the prover needs to prove to the verifier that it knows:
  - verifier sends over hidings for E(1), E(s), ... E(s^d) without knowing P.
  - prover computes E(P(s)) without knowing s. She can do this becase E(x) is HH.
- prover will give the wrong answer with high probability if their polynomial is not the correct one.

## Knowledge of coeficient (KC) Test

- Bob chooses alpha and a and computes b = alpha * a, then sends (a, b) to Alice. We call (a, b) an _alpha pair_.
- Alice must respond with a different pair (a', b') that is also an alpha pair without knowing alpha


If Alice returns a valid (a', b') to Bob's challenge (a, b) with non-neglijable probability over Bob's choise of alpha and a,
then she knows gamma, such that a' = gamma * a

## Resources
- [Explaining SNARKs](https://electriccoin.co/blog/snark-explain/) by Ariel Gabizon from ZCash


