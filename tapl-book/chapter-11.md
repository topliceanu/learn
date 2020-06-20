# Chapter 11: Simple Extensions

- _derived form_ or _syntactic sugar_: the typing and evaluation rules of derived
forms must be derived from application and abstraction! Derived forms should not
introduce new language constructs, which have to be proven.

"The advantage of introducing features like sequencing as derived forms rather
than as full-fledged language constructs is that we can exend the surface syntax
(i.e., the language that the programmer actually uses to write programs) without
adding any complexity to the internal language about which theorems such as type
safety must be proved."

- _base types_ or _atomic types_ - simple unstructured values - booleans, numbers, characters - with associated primitive operations.
- _uninterpreted_ or _unknown_ base types - types that have no primitives on them at all.

## Unit

- the _unit type_ or _Unit_ - a singleton type with only one inhabitant: _unit_
- _unit_ is the only possible result of evaluating an expression of type _Unit_.
- unit is most useful in languages with side-effects, where the side-effect of an
expression, not the result of the expression, is what we care about. These expressions
usually return Unit.
- the Bottom type (⊥) is a type with no inhabitants.

```
Typing:
Γ|-unit:Unit (T-Unit)

Definition:
t1;t2  ===  (\x:Unit.t2) t1, where x is not in FV(t2)
```

EX.11.2.1. Is there a way of constructing a sequence of terms t1, t2,... in the simply
typed lambda-calculus with only the base type Unit, such that, for each n, the term tn has size
at most O(n) but requires at least O(2^n) steps of evaluation to reach a normal form?

```
Is there an expression that has length n and evaluates in 2^n steps?
What is the length of an expression?
```

## Sequencing and Wildcards

- _sequencing notation_ - t1;t2 - evaluates t1, throws away the result, then evaluates t2.
- t1 has to have type Unit for the sequencing term to be legal
- `t1;t2` can be derived from `(\x:Unit.t2) t1`
```
Evaluation:
   t1 -> t1'
--------------- (E-Seq)
t1;t2 -> t1';t2

unit;t2 -> t2 (E-SeqNext)

Typing:
Γ|-t1:Unit   Γ|-t2:T2
--------------------- (T-Seq)
    Γ|-t1;t2:T2
```
- wildcards relace variable names that we don't need, so it's annoying to give them names.
- `\_:S.t` is used to abbreviate `\x:S.t` where x does not occur in t

Ex.11.3.2 Give typing and evaluation rules for wildcard abstractions, and
prove that they can be derived from the abbreviation stated

```
The typing an evaluation rules are the same as the simply typed lambda calculus.
The difference is that in the case of abstractions, _ stands for a variable that does not occur in t

Evaluation:

(\_.t) t' -> t (E-AppWildcard)

      Γ|-t1:T1
-------------------- (T-Abs) ***
Γ|-(\_:T2.t1):T2->T1
```

## Ascribing

- _ascribing_ written as `t as T` - verifies the type of term t is indeed T at compile time.
- it's useful for documentation, debugging, making the code more readable.
- when a term t may have many different types - in languages with subtyping - ascribing can
be used to restrict the set of types the compiler has to consider.

```
Syntactic forms:
t ::= t as T

Evaluation:
v1 as T -> v1 (E-Ascribe)

     t1 -> t1'
------------------- (E-Ascribe1)
t1 as T -> t1' as T

Typing:
   Γ|-t1:T
-------------- (T-Ascribe)
Γ|-t1 as T : T

```

Ex.11.4.1. (1) Show how to formulate ascription as a derived form.
Prove that the “official” typing and evaluation rules given here correspond to
your definition in a suitable sense. (2) Suppose that, instead of the pair of
evaluation rules E-Ascribe and E-Ascribe1, we had given an "eager" rule
```
t1 as T -> t1 (E-AscribeEager)
```
that throws away an ascription as soon as it is reached. Can ascription still
be considered as a derived form?

Solution:
```
The only place where we introduce new types are abstractions,
so `t as T` can be derived from `(\x:T.x) t`

For E-Ascribe, `v1 as T -> v1`

(\x:T.x) v1 -> [x->v1]x -> v1 (E-AppAbs)

For E-Ascribe1,
     t1 -> t1'
--------------------
t1 as T -> t1' as T

t1 as T = (\x:T.x) t1 -> [x->t1]x -> t1 (E-AppAbs) -> t1'

The problem here is we evaluate the ascription before the term t1!!

For T-Ascribe
   Γ|-t1:T
-------------- (T-Ascribe)
Γ|-t1 as T : T

Given
Γ_0 = t:T
Γ_1 = Γ_0,x:T

Type derivation is
    x:T in Γ_1
   ------------
     Γ_1|-x:T                        t:T in Γ_0
--------------------- (T-Abs)        ----------- (T-Var)
  Γ_0|-(\x:T.x):T->T                  Γ_0|-t:T
------------------------------------------------- (T-App)
     Γ_0|-(\x:T.x) t : T

For E-AscribeEager, t1 as T -> t1.
To mee, these "eager" evaluation rules are just like derived forms, they don't
introduce any new language construct, they are just syntactic sugar.
```

## Let Binding

- a let expression gives names to some of its subexpressions.
- evaluation is `call-by-value`: the let-bound term must be fully evaluated before
evaluation of the let body can begin.

```
Syntax:
t ::= ....
      let x=t in t - let binding

Evaluation:
let x = v1 in t2 -> [x->v1]t2 (E-LetV)

                t1->t1'
------------------------------------- (E-Let)
let x = t1 in t2 -> let x = t1' in t2

Typing:
Γ|-t1:T1         Γ,x:T1|-t2:T2
------------------------------ (T-Let)
        Γ|-let x=t1 in t2:T2

Definition as a derived form:
let x=t1 in t2  ===  (\x:T1.t2) t1
```
- we can derive let's evaluation behaviour by desugaring it, but it's typing
behaviour must be built into the internal language.

EX.11.5.2  Does let x=t1 in t2 === [x->t1]t2 work?
```
I would say no, you can only do that with values, like in E-LetV.
We have to evaluate t1 first, that's the key of a let expression.
```

## Pairs

_pairs_ are groups of two values of any type. They only support projections,
ie. accessing one of the elements in the pair.

```
Syntax:
t ::= ...
      {t, t} - pair
      t.1 - first projection
      t.2 - second projection

Values:
v ::= ...
      {v, v} - pair value
```

## Questions
- Ex.11.2.1 What?
- Q: If Haskell a purely functional language?
- Q: In sequencing, t1;t2, does t1 HAVE to evaluate to unit?!
