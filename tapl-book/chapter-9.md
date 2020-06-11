# Chapter 9: Simply Typed Lambda-Calculus

Obs. this book taught me to read every single sentence and proof very carefully,
because I will need that in the exercises. This book is surprisingly precise and
careful in the statements that it makes.

`->` is _right associative_, ie t1 -> t2 -> t3 === t1 -> (t2 -> t3)

Languages in which type annotations in terms are used to help guide the type
checker are called _explicitly typed_. Languages in which the type checker _infers_
or _reconstructs_ the type information are called _implicitly typed_ (also used
is the term _type assignment systems_).

## Typing rules for lambda calculus

```
x:T in Γ
--------- (T-Var)
 Γ|-x:T

 Γ,x:T1|-t2:T2
--------------- (T-Abs)
Γ|-\x:T1.t2:T1->T2

Γ|-t1:T11->T12  Γ|-t2:T11
------------------------- (T-App)
      Γ|-t1 t2:T12
```

A _typing context_ (Or _type environment_) is a set of variables and their types.
The empty type context is omited. Uses the greek letter capital Gamma.Γ

## Typing rules for boolean terms
```
Γ|-t1:Bool Γ|-t2:T Γ|-t3:T
-------------------------- (T-If)
Γ|-if t1 then t2 else t3:T
```

## Evaluation and typing rules rules
```
Syntax:

t := x - variable
     \x:T.t - abstraction
     t t - application

Values:

v ::= \x:T.t - abstraction value

Types:

T ::= T->T - type of function

Contexts:

Γ ::= ∅ - empty context
      Γ,x:T - term variable binding

Evaluation:

    t1->t1'
--------------- (E-App1)
t1 t2 -> t1' t2

   t2->t2'
------------- (E-App2)
v1 t2 -> v1 t2'

(\x:T11.t2) v2 -> [x->v2]t12 (E-AppAbs)

Typing:

x:T in Γ
--------- (T-Var)
 Γ|-x:T

  Γ,x:T1|-t2:T2
------------------ (T-Abs)
Γ|-\x:T1.t2:T1->T2

Γ|-t1:T11->T12 Γ|-t2:T11
------------------------ (T-App)
      Γ|-t1 t2:T12
```

Note that only abstractions introduce a new variable in the typing context.

EX.9.2.1 The pure simply typed lambda-calculus with no base types is
actually degenerate, in the sense that it has no well-typed terms at all. Why?

```
Q: are the base types Bool and Nat?
Q: does pure lambda calculus have any values?

A language is ill-typed if terms reach a stuck state.
For pure lambda calculus, terms evaluate to abstractions, there are no values.
```

EX.9.2.2 Show (by drawing derivation trees) that the following terms have the
indicated types:
```
1. f:Bool->Bool|-f (if false then true else false) : Bool

G_0 = f:Bool->Bool

                                 ---------------- (T-False)      --------------- (T-True)   ---------------- (T-False)
 f:Bool->Bool in G_0             G_0 |-false:Bool                G_0 |-true:Bool            G_0 |-false:Bool
--------------------- (T-Var)    ------------------------------------------------------------------------------ (T-If)
 G_0 |- f:Bool->Bool                         G_0 |-if false then true else false : Bool
--------------------------------------------------------------------------------------------- (T-App)
                G_0|-f (if false then true else false) : Bool

2. f:Bool->Bool|-\x:Bool.f (if x then false else x) : Bool -> Bool

G_0 = f:Bool->Bool
G_1 = f:Bool->Bool, x : Bool

                                 ------------- (T-Var)     ---------------- (T-False)    ------------- (T-Var)
   f:Bool->Bool in G_1            G_1|- x:Bool             G_1 |-false:Bool                G_1|- x:Bool
  ------------------- (T-Var)    ------------------------------------------------------------------------------ (T-If)
   G_1|-f:Bool->Bool                 G_1 |- if x then false else x: Bool
  -------------------------------------------------------------------------- (T-App)
                  G_1|-f (if x then false else x): Bool
   ------------------------------------------------------------------- (T-Abs)
        G_0|-\x:Bool.f (if x then false else x) : Bool -> Bool

```

EX.9.2.3 Find a context Γ under which the term f x y has type Bool.
Can you give a simple description of the set of all such contexts
```
                    Γ|-(f x y):Bool
   ------------------------------------------------- (T-App)
    Γ|-(f x):T1->Bool                       Γ|-y:T1
---------------------------- (T-App)
Γ|-f:T2->T1->Bool   Γ|-x:T2

So Γ,f:T2->T1->Bool,x:T2,y:T1|-(f x y):Bool
```

## Inversion lemma - inversions of the typing relation
```
1. If Γ|-x:R, then x:R in Γ
2. If Γ|-\x:T1.t2:R, then R=T1->R2, for some R2 in with Γ,x:T1|-t2:R2
3. If Γ|-t1 t2:R, then there is some type T11 such that Γ|-t1:T11->R and Γ|-t2:T11
4. If Γ|-true:R, then R=Bool
5. If Γ|-false:R, then R=Bool
6. If Γ|-if t1 then t2 else t3:R, then Γ|-t1:Bool, Γ|-t2,t3:R
```

EX.9.3.2. Is there any context Γ and type T such that Γ|-x x:T?
If so, give Γ and T and show a typing derivation for Γ|-x x:T; if not, prove it.
```
G0=Γ,
G1=Γ,x:T11->T12,x:T11

x:T11->T12 in Γ                 x:T11 in Γ
--------------- (T-Var)        ------------ (T-Var)
G0|-x:T11->T12                   G0|-x:T11
------------------------------------------- (T-App)
                G0|-x x:T12

```
The context G1, x has type T11 and x:T11->T12. This contradicts the uniqueness of types theorem.
However, if I do `id id` evaluates to id. What is the type of id? `id: 'a -> 'a`. `id` is polymorphic.

## Uniqueness of Types Theorem

Given Γ and all free variables of t are in Γ, then t has at most one type, call it T.
Moreover, there is only one derivation that justifies t:T

## Canonical forms Lemma:
1. if v:Bool, then v is either true or false.
2. if v:T1->T2, then v=\x:T1.t:T2

## Progress
If t is a closed, well-typed term, Γ|-t:T then t is a value or there exists t' such that t->t'.

## Permutation Lemma:
If Γ|-t:T and ∆ is a permutation of Γ, then ∆|-t:T

## Weakening Lemma:
If Γ|-t:T and x not in dom(Γ), then Γ,x:S|-t:T. In other words we can extend the
typing context with another variable independent of T and then the type of t stays T.

## Preservation of types under substitution (OR Substitution Lemma):
If Γ,x:S|-t:T and Γ|-s:S, then Γ|-[x->s]t:T

## Preservation Theorem:
If Γ|-t:T and t -> t' then Γ|-t':T

Ex.9.3.10. In Exercise 8.3.6 we investigated the subject expansion property for
our simple calculus of typed arithmetic expressions. Does it hold for the "functional part"
of the simply typed lambda-calculus? That is, suppose t does not contain any
conditional expressions. Do t->t' and Γ|-t':T imply Γ|-t:T?

```
It's similar to 8.3.6. We iterate through all the typing rules.
For all the typing rules, we find matching evaluation rules
There is no reason why a function type would break subject expansion.
```

## Curry-Howard correspondence
- an _introduction rule_ describes how elements of the type can be created (T-Abs)
- a _reduction rule_ describes how elements of the type can be used (T-Abs)

EX.9.4.1 Which of the rules for the type Bool in Figure 8-1 are introduction rules
and which are elimination rules? What about the rules for Nat in Figure 8-2?
```
- in both 8-1 and 8-2 they are all introduction rules.
```

```
Logic               | Programming languages
--------------------+------------------------
propositions        | types
P included in Q     | type P->Q
P and Q             | type PxQ
proof of P          | term t has type P
P is provable       | type P is inhabited by at least one term.
```

- a term of the simply-types lambda calculus is a proof of a logical proposition corresponding to its type.
- computation - reduction of lambda terms - corresponds to the logical operation of proof simplification by cut elimination.


## Questions:
- Is 9.3.2 correct?
- Is 9.4.1 correct?
- Prove the preservation theorem
Old
- Can a term have different types under different typing contexts? Yes
- Evaluation rules are left-to-right/top-to-bottom, typing rules right-to-left/bottom-up? Yes

## Definitions:
- lemma: a minor, proven proposition which is used as a stepping stone to a larger result.
- axiom or postulate: a statement that is regarded as being established, accepted or self-evidently true.
- theorem: a non-self-evident statement that has been proven to be true, either on the bases of axioms or other theorems

## Todo
1. https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus
2. https://byorgey.wordpress.com/2009/01/12/abstraction-intuition-and-the-monad-tutorial-fallacy/
