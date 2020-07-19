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
- sometimes T1xT2 is referred to as a product type or carthesian product.
- in {t1, t2} you need to first t1 down to a value, then t2 down to a value, then you can project!

```
Syntax:
t ::= ...
      {t, t} - pair
      t.1 - first projection
      t.2 - second projection

Values:
v ::= ...
      {v, v} - pair value

Types:
T ::= ...
      {TxT} - product type

Evaluation:
{v1,v2}.1 -> v1 (E-PairBeta1)
{v1,v2}.2 -> v2 (E-PairBeta2)

  t1 -> t1'
-------------- (E-PairProj1)
t1.1 -> t1'.1

  t1 -> t1'
-------------- (E-PairProj2)
t1.2 -> t1'.2

    t1 -> t1'
------------------- (E-Pair1)
{t1,t2} -> {t1',t2}

    t2 -> t2'
------------------- (E-Pair2)
{t1,t2} -> {t1,t2'}

Typing
Γ|-t1:T1   Γ|-t2:T2
-------------------- (T-Pair) - introduction rule, introduces T1xT2
 Γ|-{t1,t2}:T1xT2

Γ|-t:T1xT2
---------- (T-Proj1) - elimination rule
 Γ|-t.1:T1

Γ|-t:T1xT2
---------- (T-Proj2) - elimination rule
 Γ|-t.2:T2
```

## Tuples

- generalization on pairs
- you can have an empty tuple, {}

```
Syntax:
t ::= ...
      {ti,i=1..n} - tuple
      t.i - projection

Values:
v ::= ...
      {vi,i=1..n} - tuple value

Types:
T ::= ...
      {Ti,i=1..n} - tuple type

Evaluation:
{vi,i=1..n}.j -> vj (E-ProjTuple)

  t1 -> t1'
------------- (E-Proj)
t1.i -> t1'.i

                            tj -> tj'
----------------------------------------------------------------- (E-Tuple)
{vi,i=1..j-1, tj, vk,k=j+1..n} -> {vi,i=1..j-1, tj', vk,k=j+1..n}

Typing:
   for each i Γ|-ti:Ti
--------------------------- (T-Tuple)
Γ|-(ti,i=1..n):{Ti,i=1..n}

Γ|-t1:{Ti,i=1..n}
----------------- (T-Proj)
   Γ|-t1.j:Tj
```

## Records

- records are labeled tuples. Tuples can be seen as a Records where labes are positional numbers and can be omitted.
- pairs are also records with only two elements and with numeric labels. This applies to pattern matching.
- {x:Nat,y:Bool} != {y:Bool,x:Nat} in their definition

```
Syntax:
t ::= ...
      {li=ti,i=1..n} - record
      t.l - projection

Values:
v ::= ...
      {li=vi,i=1..n} - record value

Types:
T ::= ...
      {li:Ti,i=1..n} - record type

Evaluation:
{li=vi,i=1..n}.j -> vj (E-ProjTuple)

  t1 -> t1'
------------- (E-Proj)
t1.l -> t1'.l

                                     tj -> tj'
---------------------------------------------------------------------------------- (E-Record)
{li=vi,i=1..j-1, lj=tj, lk=vk,k=j+1..n} -> {li=vi,i=1..j-1, lj=tj', lk=vk,k=j+1..n}

Typing:
      for each i Γ|-ti:Ti
-------------------------------- (T-Rcd)
Γ|-(li=ti,i=1..n):{li:Ti,i=1..n}

Γ|-t1:{li:Ti,i=1..n}
-------------------- (T-Proj)
   Γ|-t1.lj:Tj

```

EX.11.8.1.Write E-ProjRcd more explicitly, for comparison.
```
{li=vi,i=1..n}.lj -> vj

becomes:
{li=vi,i=1..j-1, lj=vj, lk=vk,k=j+1,n}.lj -> vj
```

Ex.11.8.2 Pattern matching

```
Patterns:
p ::= x              - variable pattern
      {li=pi,i=1..n} - record pattern

Terms:
t ::= ...
      let p=t in t   - pattern binding

Matching:
match(x, v) = [x->v]  (M-Var)               - match is a substitution of x with v

              for each i match(pi,vi) = σi
------------------------------------------------------ (M-Rcd)
match({li=pi,i=1..n}, {li=vi,i=1..n}) = σ1.σ2.σ3...σn

- if we match a record pattern against a record we get a series of substitutions.
- the pattern and the record must have the same labels and same length, otherwise matching will fail!

New evaluation rules:
let p=v1 in t2 -> match(p,v1) t2 (E-LetV) - apply all substitution from match(p,v1) in t2

            t1 -> t1'
---------------------------------- (E-Let)
let p=t1 in t2 -> let p=t1' in t2
```

Add typing rules to this system.

```
- Typing rules are supposed to prevent bad evaluation situations.

Γ|-p:T1       Γ|-v1:T1        Γ|-t2:T2
-------------------------------------- (T-LetV)
      Γ|- let p=v1:T1 in t2 : T2
```

## Sums types

- Sum types are variant types with only two variants.
- we say that `inl` and `inr` _inject_ types T1 and T2 into type T1+T2.
They are not functions, but tags.
- the only way to use sum types is through a case expression which strips the tags.
- sums break unique typing unless ascribing is used.

```
Syntax:
t ::= ...
      inl t as T - left tagging or injecting
      inr t as T - right tagging or injecting
v ::= ...
      inl v as T - tagged value (left)
      inr v as T - tagged value (right)
T ::= ...
      T+T - sum type
Evaluation:
case (inl v0 as T0) of inl x1 => t1 | inr x2 => t2 -> [x1->v0]t1 (E-CaseInl)

case (inr v0 as T0) of inl x1 => t2 | inr x2 => t2 -> [x2->v0]t2 (E-CaseInr)

                    t0 -> t0'
------------------------------------------------ (E-Case)
case (inl t0 as T0) of inl x1 => t1 | inr x2 => t2 ->
case (inl t0' as T0) of inl x1 => t1 | inr x2 => t2

          t1 -> t1'
----------------------------- (E-Inl)
inl t1 as T1 -> inl t1' as T1

          t1 -> t1'
----------------------------- (E-Inr)
inr t1 as T1 -> inr t1' as T1

Typing:
      Γ|-t1:T1
--------------------- (T-Inl)
inl t1 as T1+T1:T1+T2

      Γ|-t2:T2
--------------------- (T-Inr)
inr t2 as T1+T2:T1+T2

        Γ|-t0:T1+T2      Γ,x1:T1|-t1:T      Γ,x2:T2|-t2:T
----------------------------------------------------------------- (T-Case)
 Γ|- case t0 of inl x1 as T1+T2 => t1 | inr x2 as T1+T2 => t2 : T
```

EX.11.9.1 Derive true, false and if from sums and Unit.
```
True = inl unit : Unit+Unit
False = inr unit : Unit+Unit

if t0 then t1 else t2 === \t0:Unit+Unit.\t1:T.\t2:T.case t0 of inl _ => t1 | inr _ => t2 : T
```

## Variant types
- generalize sum types to multiple user-defined labels.
- also called _disjoint unions_

```
Syntax:
t ::= ...
      <l=t> as T                       - tagging
      case t of <li=xi> => ti,i=1..n   - case expression
T ::= ...
      <li:Ti,i=1..n>                   - type of variants

Evaluation:
case (<lj=vj> as T) of <li=xi> => ti,i=1..n -> [xi -> vj]tj  (E-CaseVariant)

            t0 -> t0'
------------------------------------ (E-Case)
case t0  of <li=xi> => ti, i=1..n ->
case t0' of <li=xi> => ti, i=1..n

          ti -> ti'
------------------------------ (E-Variant)
<li=ti> as T -> <li=ti'> as T

Typing:
                  Γ|-tj:Tj
---------------------------------------------- (T-Variant)
Γ|- <lj=tj> as <li:Ti,i=1..n> : <li:Ti,i=1..n>

       Γ|- t0:<li:Ti,i=1..n>
     for each i  Γ,xi:Ti|-ti:T
--------------------------------------- (T-Case)
Γ|- case t0 of <li=xi> => ti,i=1..n : T

```

- degenerate cases:
 - Options: one variant wraps a type, the other variant marks the absense of it
 - Enumeration: multiple labels of type Unit,
 - Single-field variants: tagging an existing type, like aliases
 - Dynamic: an infinite disjoint union, whose labels are types!


## General Recursion

- `fix` cannot be defined in simply typed lambda calculus, because it doesn't type check.
Instead we define it as a language construct.
- `PCF` = simply typed lambda calculus with numbers and fix.

```
Syntax:
t ::= ....
      fix t  - fixed point of t

Evaluation:
fix (\x:T1.t2) -> [x->(fix (\x:T1.t2))]t2 (E-FixBeta)

    t1 -> t1'
----------------- (E-Fix)
fix t1 -> fix t1'

Typing:
 Γ|- t1: T1->T1
---------------- (T-Fix)
Γ|- fix t1 : T1

Derived forms:
letrec x:T1 = t1 in t2 === let x = fix (\x:T1.t1) in t2
```

For example, the `iseven` recursive method is:
```
ff = \ie:Nat->Bool.
        \x.Nat.
            if iszero x then true
            else if iszero (pred x) then false
            else ie (pred (pred x))
iseven = fix ff
```

Ex.11.11.1 Define equal, plus, times, and factorial using fix.
```
equal' = \ie:{Nat, Nat} -> Bool.
          \p:{Nat, Nat}.
            if (iszero p.1) then (iszero p.2)
            else if (iszero p.2) then (iszero p.1)
            else ie {(pred p.1), (pred p.2)}
equal = fix equal'

plus' = \ie:{Nat, Nat} -> Nat.
          \p:{Nat, Nat}.
            if (equal p.2 0) then p.1
            else ie {(succ p.1), (pred p.2)}
plus = fix plus'

times' = \ie:{Nat, Nat} -> Nat.
            \p:{Nat, Nat}.
              if (equal p.2 1) then p.1
              else ie {(plus p.1 p.1), (pred p.2)}
times = fix times'

factorial' = \ie:Nat -> Nat.
               \n.Nat.
                 if or (equal n 0) (equal n 1) then 1
                 else times n (ie (pred n))
factorial = fix factorial'
```

EX.11.11.2 Rewrite your definitions of plus, times, and factorial from Exercise 11.11.1 using letrec instead of fix.
```
letrec equal:{Nat, Nat} -> Nat =
  \p:{Nat, Nat}.
    if (iszero p.1) then (iszero p.2)
    else if (iszero p.2) then (iszero p.1)
    else equal {pred(p.1), pred(p.2)}

letrec plus:{Nat, Nat} -> Nat =
  \p:{Nat, Nat}.
    if (equal p.2 0) then p.1
    else plus {(succ p.1), (pred p.2)}

letrec times:{Nat,Nat} -> Nat =
  \p:{Nat, Nat}.
    if (equal p.2 1) then p.1
    else times {(plus {p.1, p.1}), (pred p.2)}

letrec factorial:Nat -> Nat =
  \n:Nat.
    if (equal n 0) then 1
    else times n (factorial (pred n))
```

## List
- constructor is `List T`, it defines the type of all finite lists with elements of type T.
- the empty list that contains instances of T is `nil[T]`

```
Syntax:
t ::= ...
      nil[T]            - empty list
      cons[T] t t       - list constructor
      isnil[T] t        - test for empty list
      head[T] t         - head of a list
      tail[T] t         - tail of a list
v ::= ...
      nil[T] - empty list
      const[T] v v - list constructor
T ::= ...
      List T  - type of lists

Evaluation:
            t1 -> t1'
--------------------------------- (E-Cons1)
const[T] t1 t2 -> const[T] t1' t2
```

EX.11.12.2. Which typing rule is cannot be derived from the context?
I think it's (T-Cons), there's nothing in the conclussion to suggest t2 is a List T.

## Questions
- Q: Why don't all mainstream languages have variants if it's soo fundamental and easy to implement?
- Q: Any other way to represent equal plus and times without using pairs?
- Q: How do you get from fix to letrec?
- Q: Why is there so much new syntax for lists? Surely we can defined them using Sums already? (ie. type a list = Empty | Cons (a, a list)) Is it because we don't have recursive types yet?
- Q: How do we know for sure that every recursive expression that uses the `fix` operator will halt if it type checks? What makes this `fix` different from the one in chapter 5?

Old:
- Q: I have never seen this Dynamic type?
  A: It's similar to the `interface{}` type.
- Q: Can I have a sum of the same two types, eg Bool+Bool?
  A: Yes, that is permitted.
- Q: Where is the intuition behind the sum types
  A: they are more common than you might originally think.
- Q: How is the empty tuple {} different from unit () ?
  A: they are differen types
- Q: From the evaluation rule, it seems that to extract a value from a pair you have to evaluate both expressions.
  A: Yes, it's eager evaluation of data structures.
  Also, it seems we now evaluate arguments of an abstraction before we evaluate the abstraction.
- Q: In sequencing, t1;t2, does t1 HAVE to evaluate to unit?!
  A: The way we defined ';' it won't typecheck. If t1 can be any other type, the compiler should complain.
- Q: If Haskell a purely functional language? A: No
- Ex.11.2.1 What!?!? This is a *** exercise, we decided to now work on those anymore.
