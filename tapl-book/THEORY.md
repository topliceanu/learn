# BOOK: Types and Programming Languages

## Chapter 9: Simple Typed Lambda-Calculus

- introduces a type for functions: T1->T2
- EX.9.2.1


## Curry-Howard equivalence: for every proposition you can associate a type.

+--------------------------+------------------------+
| mathematical logic       | programming languages  |
+--------------------------+------------------------+
| propositions             | types                  |
+--------------------------+------------------------+
| proofs                   | terms (programs)       |
+--------------------------+------------------------+
| simplification of proofs | evaluation of programs |
+--------------------------+------------------------+

Product types == records == structs (carthesian products)
Sum types == union types

## Resources
1. Church encodings used in TaPL [wiki](https://en.wikipedia.org/wiki/Church_encoding#List_encodings)
2. System F, a typed lambda calculus [wiki](https://en.wikipedia.org/wiki/System_F)
3. Impl of lambda calculus in Racket [link](http://matt.might.net/articles/compiling-up-to-lambda-calculus/)
4. Computerfile videos on this:
  - [Lambda calculus](https://www.youtube.com/watch?v=eis11j_iGMs)
  - [Y combinator](https://www.youtube.com/watch?v=9T8A89jgeTI) - good intuition on recursion in lambda calculus
  - [What is a monad](https://www.youtube.com/watch?v=t1e8gqXLbsU)
  - [Functional parsing](https://www.youtube.com/watch?v=dDtZLm7HIJs)
  - [What is Functional Programming](https://www.youtube.com/watch?v=LnX3B9oaKzw)
5. Impl of lambda calculus in Haskell [link](http://dev.stephendiehl.com/fun/lambda_calculus.html)
6. Propositions as Types:
  - [computerphile](https://www.youtube.com/watch?v=SknxggwRPzU)
  - [Philip Wadler](https://www.youtube.com/watch?v=IOiZatlZtGU) ***
7. Homotropy theory:
  - [Computerphile - computer science and mathemathics](https://www.youtube.com/watch?v=qT8NyyRgLDQ)
  - [Computerphile - homotropy theory](https://www.youtube.com/watch?v=Ft8R3-kPDdk)
8. Category theory for the working hacker [link](https://www.youtube.com/watch?v=gui_SE8rJUM)
