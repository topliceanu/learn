# Chapter 13: References

- the assignment operator `:=` changes the value in the reference cell, not the cell reference
```
r = ref 5    - type is Ref Nat
r := 7       - type is Unit, changed the value of r to 7
```

EX.13.1.1.Draw a similar diagram showing the effects of evaluating the expressions
a = {ref 0, ref 0} and b = (λx:Ref Nat. {x,x}) (ref 0).
```
a.1     a.2        b.1       b.2
 |       |          |         |
 v       v          |         |
ref 0  ref 0        +->ref 0<-+
```

- update function of an array
```
update = \a:NatArray.
          \m:Nat.
           \v:Nat.
            let oldf = !a in
            a := (\n:Nat.if equal m n then v else oldf n);
```

EX.13.1.2. If we defined update more compactly like this
```
update = λa:NatArray.
          λm:Nat.
            λv:Nat.
              a := (λn:Nat. if equal m n then v else (!a) n);
```
would it behave the same?
No, because this version is overriding the function reference.

- automatic garbage collection is required because a manual deallocation would violate type safety! Why?

13.1.3.Show how deallocation can lead to a violation of type safety.
```
Safety_ = progress + preservation
Progress = if t:T then either t is a value or (E) a t' such that t->t'
Preservation = if t:T and t->t' then t':T

I think it breaks preseration:
t =
  r = ref 10;   - r: Ref nat
  dealloc r;    - what's the type of r? Should be removed from the typing context
  s = ref true; - assume this operation reuses the same memory chunk.
  !r            - this should not type check!
```

- rules
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

(\x:T11.t12) v2|μ -> [x->v3]t12|μ  (E-AppAbs) - function application does not change the store!

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
