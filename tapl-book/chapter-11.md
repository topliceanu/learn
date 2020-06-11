# Chapter 11: Simple Extensions

_derived form_ or _syntactic sugar_ -

_base types_ or _atomic types_ - simple unstructured values - booleans, numbers, characters - with associated primitive operations.

_unit type_ or _Unit_ - a singleton type with only one value _unit_

```
Typing:
Γ|-unit:Unit (T-Unit)

Definition:
t1;t2  ===  (\x:Unit.t2) t1, where x is not in FV(t2)
```

_sequencing notation_ - t1;t2 - evaluates t1, throws away the result, then evaluates t2.
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
