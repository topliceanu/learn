# Tutorials

Secure MPC can model any cryptographic task!

## Security requirements:
- Privacy - parties shouldn't learn more than their input and the output of the MPC.
- Correctness - the computation is correct!
- Independence of inputs - parties can't figure out the other inputs and can't reuse them even without knowing them.
- Fairness - guaranteed output delivery: if one party gets the output then all parties get the output.

Privacy and correctness can't be separated, ie. there is no protocol that is correct with loss of privacy and vice-versa.
Same is true for independence of inputs and privacy.

## Types of adversaries

- semi-honest: follows the protocol, but tries to learn more by inspecting the transcript.
  By looking at the transcript you can learn nothing whatsoever.
- malicious: follows an arbitrary strategy
- covert: follows any arbitrary strategy, but is averse to being caught.

## Notation
- n - security parameter
- miu - we allow failure with negligible probability. miu is small in the inverse of every polynomial.

For every _semi-honest A_, there exists a _simulator S_ such that for every set of corrupted
parties I and every vector of inputs x, the following are computationally indistinguishabe.

## Oblivious Transfer

- Notation: OT(1,2) - one out of two oblivious transfer: Bob will get only one of Alice's two inputs.
- you can get OT(k, n) given OT(1, 2) efficiently
- OT is symmetric
- variants: Random OT, Rabin OT, Weak OT

Example of constructing OT(1,2) from DHH (decisional diffie-helman) and El-gamal encryption
- Alice sends Bob a group element w.
- Bob picks two public keys h0 and h1 such that `h0*h1=w`. It does this by finding
an h(sigma) that it knows the Private key to, computing h(1-sigma)=h(sigma)/w which
it won't know the private key of.
- Bob sends the public keys to Alice
- Alice encrypts x0 with h0 and x1 with h1 and sends the cypher texts back to Bob
- Bob decrypts the value that matches his choice sigma using h(sigma) private key.

## ElGamal encryption

## Blum's two party coin tossing algorithm
- using ElGamal encryption instead of commitment schemes
- challenge: how to generate a random, unbiased, random bit, given two mutually distrustful parties.
- party P1 chooses a random big b in {0,1} and two random number r and s.
  - computes h = g^r, u = g^s and v = h^s * g^b (v is the product of r and s in the group)
  - send (h, u, v) to party P2. This works like a commitment.
- party P2 chooses a random bit b' in {0, 1}
  - send b' to P1
- party P1 sends r, s, b to P2
- party P2 verifies that h=g^r and u=g^s, v=g^s * g^b
- both parties P1 and P2 compute b * b' as the shared random bit.
