# Chapter 8: Typed arithmetic expressions

## Definitions:
- a term t is _typable_ - or _well typed_ - if there is a type T such that t:T.
- What it means for a term to be _ill-typed_ or not well-typed:
  - terms whose evaluation reaches a stuck state: it is not a final
  value but the evaluation rules do not tell us what to do next.
  Eg. `if 0 then 1 else 2` breaks E-IF
  - terms that behave well under evaluation but fail the static type check.
  Eg. `if true then 0 else false` breaks T-IF because 0 and false are of different types

- a _typing relation_ is the smallest binary relation between terms and types satisfying
the Typing Rules:
```
T ::= Bool
true:Bool (T-True)
false:Bool (T-False)

t1:Bool t2:Bool t3:Bool
-----------------------  (T-If)
 if t1 then t2 else t3

T ::= Nat
0:Nat (T-Zero)

  t1:Nat
----------- (T-Succ)
succ t1:Nat

  t1:Nat
----------- (T-Pred)
pred t1:Nat

    t1:Nat
-------------- (T-IsZero)
iszero t1:Bool
```

- the _inversion lemma_:
```
If true:R then R = Bool
If false:R then R = Bool
If if t1 then t2 else t3:R then t1:Bool, t2:R and t3:R
If 0:R, then R=Nat
If succ t1:R, then R=Nat
If pred t1:R, then R=Nat
If iszero t1:R, then R=Bool and t1:Nat
```

- Uniqueness of types: each term t has at most one type T: if t is typable, then its type is unique.
- _statements_ are formal assertions about the typing of programs
- _typing rules_ are implications between statements
- _derivations_ are deductions based on typing rules.

Ex.8.2.3. Prove that every subterm of a well typed term is well typed.
```
Solution: we iterate through all the term forms allowed.
Case T-True: t=True, no subterms
Case T-False: t=False, no subterms
Case T-If: t=if t1 then t2 else t3, t1:Bool, t2:T, t3:T, t:T
  Suppose t is well typed but t1 is ill-typed. So t1's evaluation is stuck: it is
  not a value - so we can't use E-IfTrue/E-IfFalse to evaluate t - nor is there
  an evaluation rule that can reduce it - so we can't use E-If to reduce t.
  So t is ill-typed. Contradicts the hypothesis.
  Suppose t2 is ill-typed and t1 evaluates to true. By E-IfTrue, t=t2.
  So t is ill-typed. Contradiction. Same logic applies for t3.
Case T-Zero: t=0, no subterms
Case T-Succ: t=succ nv, by T-Succ, t:Nat.
  Similar to T-If, if nv is ill-typed, we can't evaluate t so t is ill-typed. Contradiction!
Case T-Pred: similar to T-Succ
Case T-IsZero: similar to T-Succ
```

- _Safety_ = progress + preservation. Safety - also called _soundness_ - well-typed
systems do not "go wrong", ie. don't end up in a wrong state: not a value but we also
can't evaluate further based on the rules we have.

- _Progress_ = a well-typed term is either a value or it can take an evaluation step
acording to evaluation rules:
```
  If t:T then either t=value or (E) t' so that t->t'
```

- _Preservation_ = all intermediate terms in the evaluation of a well-typed term are
also well-typed. Also know as _subject reduction_ or _subject evaluation_:
```
  If t:T and t->t' then t':T
```

- _Canonical forms lemma_
If v:Bool then v is either true or false
If v:Nat, then v is either `0` or `succ n`

## Evaluation rules from Ch3:
```
t ::= true | false | if t then t else t (terms)
v ::= true | false  (values)

if true then t2 else t3 -> t2 (E-IfTrue)
if false then t2 else t3 -> t3 (E-IfFalse)

                 t1 -> t1'
----------------------------------------------- (E-If)
if t1 then t2 else t3 -> if t1' then t2 else t3

t ::= 0 | succ t | pred t | iszero t (terms)
v ::= nv (values)
nv ::= 0 | succ nv

     t1 -> t1'
------------------ (E-Succ)
succ t1 -> succ t1'

     t1 -> t1'
------------------- (E-Pred)
pred t1 -> pred t1'

pred 0 -> 0 (E-PredZero)

pred (succ nv1) -> nv1 (E-PredSucc)

iszero 0 -> true (E-IsZeroZero)

iszero (succ nv1) -> false (E-IsZeroSucc)

       t1 -> t1'
----------------------- (E-IsZero)
iszero t1 -> iszero t1'
```

- The _cannonical forms_ lemma: if v is a Bool then v is either True or False.
If v is a Nat, then v is either 0 or succ nv

EX 8.3.4 Restructure the proof (of the preservation theorem) so that it goes
by induction on evaluation derivations rather than by typing derivations.

```
Theorem: If t:T and t -> t' then t':T
Solution: for each Evaluation rule we find all the Typing rules that match it.

Case E-If: t=if t1 then t2 else t3
  Which typing rule matches t? It's only T-If
  By T-If, t1:Bool, t2:T and T3:T, t:T
  By cannonical forms lemma, t1 can only be True or False
  For t1=True, By E-IfTrue, t' = t2 and t2:T -> t':T
  For t1=False, by E-IfTrue, t' = t3 and t3:T -> t':T

Case E-IfTrue: t=if true then t2 else t3
  Which typing rule matches t? T-If with t1=True, t:T, t2:T, t3:T
  By E-IfTrue, t'=t2, since t2:T => t':T

Case E-IfFalse: t=if false then t2 else t3
  What typing rule matches t? T-If with t1=False, t:T, t2:T, t3:T
  By E-IfFalse, t'=t3 => t':T

Case E-Succ: t=succ t1
  Which typing rule matches t? T-Succ, so t:Nat and t1:Nat
  Case t1=0, by T-Succ, t=succ 0:T
  Case t1=succ t2, by
  Case t1=pred t2, t1' can only be derived by E-Pred, E-PredZero and E-PredSucc
    Case t1=pred 0. By E-PredZero, t1'=0. By T-Zero, 0:Nat -> t1':Nat
    Case t1=pred (succ nv_1). By E-PredSucc, t1'=nv_1. Since nv_1 can only be 0:Nat or succ nv1' : Nat -> t1':Nat
    Case t1=pred nv1 ....

E-Pred: t=pred t1. By T-Pred, t1:Nat, t:Nat
  Which typing rule cand derive to t?

E-PredZero
E-PredSucc
E-IsZeroZero
E-IsZeroSucc

Case E-IsZero: t=iszero nv1
  From T-IsZero, t:Bool, nv1:Nat
  Case nv1=0, By E-IsZeroZero, t=iszero 0 -> t'=true. true:Bool->t':Bool
```

EX 8.3.5  The evaluation rule E-PredZero (Figure 3-2) is a bit counterintuitive:
we might feel that it makes more sense for the predecessor of zero to be undefined,
rather than being defined to be zero. Can we achieve this simply by removing the
rule from the definition of single-step evaluation?

```
Tl;dr: no.
Suppose E-PredZero is not part of the evaluation rule.
The term t=pred 0 has type t:Nat, by T-Pred.
Since we removed E-PredZero, there is no other evaluation rule that can reduce t.
So t must be a value. But pred 0 is not one of the Nat values in the typed language.
We've broken the progress property and our types system is no longer safe!
So, if we remove E-PredZero, we have to introduce pred 0 as a value.
```

EX.8.3.6. Having seen the subject reduction property, it is reasonable to wonder
whether the opposite property—subject expansion—also holds.
Is it always the case that, if t -> t' and t':T, then t:T?
If so, prove it. If not, give a counterexample.

```
Problem: If t -> t' and t':T then t:T
Solution: we know t' has type T. we iterate through all typing rules.
For each typing rule, find matching evaluation rules.

Case T-True: t'=True, T=Bool
  Which evaluation rules can produce a True value?
  Case E-IsZeroZero: t=iszero 0. By T-IsZero, t:Bool
  Case E-IfTrue: t=if true then t2 else t3 AND t2=True. By T-If, t:Bool
  Case E-IfFalse: t=if false then t2 else t3 AND t3=True, By T-If, t:Bool

Case T-False: similar to Case T-True

Case T-If: t'=if t1' then t2 else t3; t':T, t1':Bool, t2:T, t3:T.
  Which evaluation rule can produce form t'? Only E-If
  Case E-If: t=if t1 then t2 else t3 AND t1->t1', t1:Bool
    By T-If, the type of t is the same as type of t2 and t3, ie. t:T

Case T-Zero: t'=0, t':Nat
  Which evaluation rules can produce 0? E-PredZero
  Case E-PredZero: t=pred 0. By T-Pred, t:Nat

Case T-Succ: t'=succ t4', t':Nat, t4':Nat
  Which evaluation rules can product succ t1? E-IfTrue, E-IfFalse, E-Succ, E-PredSucc
  Case E-IfTrue: t=if True then t2 else t3 AND t2=succ t4', t2:Nat, t3:Nat
    By T-If, the type of t is the type of t2, so t:Nat
  Case E-IfFalse, similar to Case E-IfTrue
  Case E-Succ: t=succ t5 AND t4=pred (succ t4'). By T-Succ, t:Nat
  Case E-PredSucc: t=pred (succ t4) AND t4=succ t4'. By T-Pred, t:Nat

Case T-Pred: t'=pred t4', t':Nat, t4':Nat
  Which evaluation rules can produce a pred? E-IfTrue, E-IfFalse, E-Pred, E-PredSucc
  Case E-IfTrue: t=if True then t2 else t3 AND t2=pred t4'.
    From T-If, the type of t is the type of t2, so t:T
  Case E-IfFalse: Similar to the above
  Case E-Pred: t=pred t4 AND t4=succ (pred t4'), t4:Nat. By T-Pred, t:Nat
  Case E-PredSucc: t=pred succ t4 AND t4=pred t4', t4:Nat. By T-Pred, t:Nat

Case T-IsZero: t'=0, 0:Nat, t':Nat
  Which evaluation rules can product 0? E-IfTrue, E-IfFalse, E-PredZero, E-PredSucc
  Case E-IfTrue: t=if true then 0 else t3, t3:Nat. By T-If, t:Nat
  Case E-IfFalse: t=if false then t2 else 0, t2:Nat. By T-if, t:Nat
  Case E-PredZero: t=pred 0. By T-Pred, t:Nat
  Case E-PredSucc: t=pred (succ 0). By T-Pred, t:Nat
```

## Alternative "big-step" evaluation rules (See 3.5.17):
```
v => v (B-Value)

  t1 => true    t2 => v2
--------------------------- (B-IfTrue)
if t1 then t2 else t3 => v2

  t1 => false   t3 => v3
--------------------------- (B-IfFalse)
if t1 then t2 else t3 => v3

    b1 => nv1
------------------- (B-Succ)
succ t1 => succ nv1

  b1 => 0
------------ (B-PredZero)
pred t1 => 0

   t1 => succ nv1
------------------- (B-PredSucc)
pred succ t1 => nv1

     t1 => 0
----------------- (B-IsZerorZero)
iszero t1 => True

  t1 => succ nv1
------------------ (B-IsZeroSucc)
iszero t1 => False
```

Ex 8.3.7. Suppose our evaluation relation is defined in the big-step style,
as in Exercise 3.5.17. How should the intuitive property of type safety be
formalized?

```
safety = progress + preservation
progress: if t:T then t is a value or (E) a value v such that t=>v
preservation: if t:T and t => v then v:T
```

## Alternative "meaninless" states (see 3.5.16):
```
badnat ::= wrong | true | false # Non-numeric form
badbool ::= wrong | nv # Non-bool form

if badbool then t2 else t3 -> wrong
succ badnat -> wrong
pred badnat -> wrong
pred badnat -> wrong
```

Ex.8.3.8 Suppose our evaluation relation is augmented with rules for reducing
nonsensical terms to an explicit wrong state, as in Exercise 3.5.16.
Now how should type safety be formalized?
```
Safety = progress + preservation
Based on Ex.8.3.7, we use big-step evaluation to redefined progress and preservation:
* progress: if t:T then t is a value v or (E) a value v' such that t=>v' and v and v' are != wrong
* preservation: if t:T and t=>v' then v':T and v' != wrong.
```

## Questions for Ch8.
* How do you know the type of t if you haven't fully evaluated t. Related to preservation.
By a process called type inference, where the type systems looks at signatures it knows in infers the rest

* Is my solution to Ex.8.2.3. correct?
* Is my solution to Ex.8.3.7. correct?
