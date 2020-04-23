# Chapter 8: Typed arithmetic expressions

## Definitions:
- a term t is _typable_ (Or well typed) if there is a type T such that t:T.
- What it means for a term to be ill-typed or not well-typed:
  - terms whose evaluation reaches a stuck state. Eg. `if 0 then 1 else 2` breaks T-IF
  - terms that behave well under evaluation but fail the static type check. Eg. `if true then 0 else false` breaks T-IF
- a typing relation is the smallest binary relation between terms and types satisfying:
```
T ::= Nat
0:Nat (T-ZERO)

t1:Nat -> succ t1:Nat
t1:Nat -> pred t1:Nat
t1:Nat -> iszero t1: Bool
```
- Uniqueness of types: each term t has at most one type T: if t is typable, then its type is unique.
- _statements_ are formal assertions about the typing of programs
- _typing rules_ are implications between statements
- _derivations_ are deductions based on typing rules.

Ex.8.2.3. Prove that every subterm of a well typed term is well typed.
Q: Isn't this part of the definition of the language in 8-1 and 8-2?! Isn't this preservation?
There are three types of terms: x; \x.t; and (t1 t1). A variable term x has not subterms.
The abstraction \x.t has type T than t is of type T because that's what \x.t returns.
The application (t1 t2) has type T than subterm t1 has type T. Q: what can we say about t2?!
Same as Ex.8.3.6

- _Safety_ = progress + preservation. Safety - also called _soundness_ - well-typed
systems do not "go wrong", ie. don't end up in a wrong state: not a value but we also
can't evaluate further based on the rules we have.
- _Progress_ = a well-typed term is either a value or it can take an evaluation step
acording to evaluation rules.
- _Preservation_ = all intermediate terms in the evaluation of a well-typed term are
also well-typed. Also know as _subject reduction_ or _subject evaluation_.
  Theorem: if t:T and t->t' then t':T

## Questions for Ch8.
* How do you know the type of t if you haven't fully evaluated t. Related to preservation.
