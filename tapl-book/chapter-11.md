# Chapter 11: Simple Extensions

- _derived form_ or _syntactic sugar_ - terms that are simplified versions of equivalent terms.
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
- `t1;t2` can be derived as `(\x:Unit.t2) t1`
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
(\_:T1.t2) v1 -> t2 (A-AppWildcard)
```

## Ascribing

_ascribing_ written as `t as T` - verifies the type of term t is indeed T

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

_let binding_  a let expression gives names to some of its subexpressions.

```
Definition:
let x=t1 in t2  ===  (\x:T1.t2) t1

Typing:

Γ|-t1:T1         Γ,x:T1|-t2:T2
------------------------------ (T-Let)
        Γ|-let x=t1 in t2:T2
```

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
