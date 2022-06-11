# Review of "Zero Knowledge Proofs: An illustrated primer"

[Blog post](https://blog.cryptographyengineering.com/2014/11/27/zero-knowledge-proofs-illustrated-primer/)
[Followup](https://blog.cryptographyengineering.com/2017/01/21/zero-knowledge-proofs-an-illustrated-primer-part-2/)

[Wikipedia](https://en.wikipedia.org/wiki/Zero-knowledge_proof)

- A password hash is a proof that the user really know their password. Unfortunately, it also reveals the password in clear to the server.

Properties of a zero-knowledge protocol:
1. completeness: if the prover is honest, she will eventually convince the verifier.
2. soundness: the prover can only convince the verifier if the statement is true.
3. zero knowledgeness: the verifier learns no new information from the prover beyond the fact that the statement is true.


- If there exists any decision problem (that is, a problem with a yes/no answer)
whose witness (solution) can be verified in polynomial time, then we can prove
that said solution exists by (1) translating the problem into an instance of the
graph three-coloring problem, and (2) running the GMW protocol.

- _soundness error_ - the probability that a cheating prover will be able to convince the verifier of a false statement.
- _witness_ - the solution.

## Resources

- Vitalik's blog post on [QAP](https://medium.com/@VitalikButerin/quadratic-arithmetic-programs-from-zero-to-hero-f6d558cea649)
