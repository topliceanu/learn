# Chapter 13: References

- the assignment operator `:=` changes the value in the reference cell, not the reference
```
r = ref 5    - type is Ref Nat
r := 7       - type is Unit, changed the value of r to 7
!r           - type Nat, value 7
```

EX.13.1.1.Draw a similar diagram showing the effects of evaluating the expressions
a = {ref 0, ref 0} and b = (λx:Ref Nat. {x,x}) (ref 0).
```
a.1     a.2        b.1       b.2
 |       |          |         |
 v       v          |         |
ref 0  ref 0        +->ref 0<-+
```

## Encoding arrays as function references
- create a new array of type NatArray = Ref (Nat -> Nat)
```
newarray : Unit -> NatArray
newarray = \_:Unit ref (\n:Nat.0)
```

- lookup array
```
lookup : NatArray -> Nat -> Nat
lookup = \a:NatArray.\n:Nat.(!a) n
```

- update function of an array
```
update : NatArray -> Nat -> Nat -> Unit
update = \a:NatArray.\m:Nat.\v:Nat.
            let oldf = !a in
            a := (\n:Nat.if equal m n then v else oldf n);
```
Example of creating an array, adding values to it with update and doing a lookup:
```
let a = newarray () in
  a = newarray () = ref (\n:Nat.0)
let () = update a 0 10 in
  a = \n:Nat.if n 0 then 10 else ((\n:Nat.0) n)
let () = update a 1 11 in a
  a = \n:Nat.if n 1 then 11 else ((\n:Nat.if n 0 then 10 else ((\n:Nat.0) n)) n)
lookup a 0
  returns 10
lookup a 5
  returns 0
```

EX.13.1.2. If we defined update more compactly like this
```
update : NatArray -> Nat -> Nat -> Unit
update = \a:NatArray.\m:Nat.\v:Nat.
              a := (λn:Nat. if equal m n then v else (!a) n);

let a = newarray () in
  a := newarray () = ref (\n:Nat.0)
let () = update a 0 10 in
  a := \n:Nat.if n 0 then 10 else ((!a) n)
let () = update a 1 11 in a
  a := \n:Nat.if n 1 then 11 else ((!a) n)
lookup a 1
  returns 11
lookup a 0
  will continuously loop ?!
lookup a 5
  will continuously loop ?!
```
Would it behave the same?
No. In the first version, the let binding is evaluated before the reference assignment; see E-LetV, E-Let in Ch.11.
The value corresponding to an index is captured in the let deferefencing `let oldf = !a`.
In the second version the dereference `(!a)` is evaluated after if is evaluated; see E-If, E-IfTrue, E-IfFalse in Ch.8.
At lookup, `a` will hold a reference to the last function.
This means that when looking up an index other than the last one, the execution will not terminate.

## Garbage collection

- automatic garbage collection is required because a manual deallocation would violate type safety! Why?

13.1.3.Show how deallocation can lead to a violation of type safety.
```
Safety_ = progress + preservation
Progress = if t:T then either t is a value or (E) a t' such that t->t'
Preservation = if t:T and t->t' then t':T

Assume there is a `dealloc` operator with

        Γ,r:Ref T|Σ,l=T|- r:Ref T
-------------------------------------------- (T-Dealloc)
Γ|Σ no longer has l|-dealloc r:Ref T -> Unit

there are two variations of the typing rules
- you can change the variable to point to two values of different types
- you can change the value pointed by two variables of different types.
A potential solution is to have the memory cell hold some type information.
```

## Typing and Evaluation Rules

- consider the memory as a large array of values, the `store`. The `ref` operator
allocates a value in the store and returns its location. The store is a function
from locations to values.
- all the evaluation rules are extended to include the initial state of the store
and the result state of the store. Likewise

```
Syntax:
t ::= ...
      ref t     - reference creation
      !t        - dereference
      t := t    - assignment
      l         - a location in the store array, a pseudo-reference

Values:
v ::= ...
      l     - a store location

Types:
T ::= ...
      Ref T  - type of reference cells holding data of type T

Stores:
μ ::= ∅     - the empty store
      μ,l=v - location binding

Evaluation:

   t1|μ -> t1'|μ'
-------------------- (E-App1)
t1 t2|μ -> t1' t2|μ'

  t2|-μ -> t2'|μ'
-------------------- (E-App2)
v1 t2|μ -> v1 t2'|μ'

(\x:T11.t12) v2|μ -> [x->v3]t12|μ  (E-AppAbs) - function application in itself has no side-events: it does not change the store!

t1|μ -> t1'|μ'
---------------- (E-Deref)  - evaluation potentially updates the store
!t1|μ -> !t1'|μ'

 μ(l) = v
----------- (E-DerefLoc)
!l|μ -> v|μ

    t1|μ -> t1'|μ'
--------------------- (E-Assign1)
t1:=t2|μ -> v1:=t2|μ'

    t2|μ -> t2'|μ
--------------------- (E-Assign2)
v1:=t2|μ -> v1:=t2'|μ

l := v2|μ -> unit|[l->v2]μ (E-Assign)  - update the store to make location l contain v2 instead of v1

     l not in dom(μ)
------------------------ (E-RefV)
ref v1|μ -> l|(μ, l->v1)

    t1|μ -> t1'|μ'
--------------------- (E-Ref)
ref t1|μ -> ref t1'|μ

Typing:

  Σ(l) = T1
-------------- (T-Loc)
Γ|Σ-l : Ref T1

   Γ|-t1:T1
-------------- (T-Ref)
 Γ|-t1:Ref T1

Γ|-t1:Ref T1
------------ (T-Deref)
 Γ|-!t1:T1

Γ|-t1:Ref T1  Γ|-t2:T1
---------------------- (T-Assign)
    Γ|-t1:=t2:Unit
```
