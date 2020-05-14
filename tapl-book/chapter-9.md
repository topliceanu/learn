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
    t1->t1'
--------------- (E-App1)
t1 t2 -> t1' t2

   t2->t2'
------------- (T-App2)
v1 t2 -> v1 t2'

(\x:T11.t2) v2 -> [x->v2]t12 (E-AppAbs)

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

                                          ------------ (T-False)      ------------- (T-True)   -------------------- (T-False)
 f:Bool->Bool in f:Bool->Bool             f:Bool->Bool |-false:Bool   f:Bool->Bool |-true:Bool f:Bool->Bool |-false:Bool
----------------------------- (T-Var)    ---------------------------------------------------------------------- (T-If)
 f:Bool->Bool |- f:Bool->Bool             f:Bool->Bool |-if false then true else false : Bool
--------------------------------------------------------------------------------------------- (T-App)
    f:Bool->Bool|-f (if false then true else false) : Bool

2. f:Bool->Bool|-\x:Bool.f (if x then false else x) : Bool -> Bool


                                 ------------T-Var     ---------------- (T-False)
   f:Bool->Bool in G_1            G_1|- x:Bool         G_1 |-false:Bool                (T-Var)
          -------------- T-Var   ------------------------------------------------------------ (T-If)
        G_1|-f:Bool->Bool        G_1 |- if x then false else x: Bool
             --------------------------------------------------------------- (T-App)
                  G_1|-f (if x then false else x): Bool
------------------------------------------------------------------------------ (T-Abs)
    G_0|-\x:Bool.f (if x then false else x) : Bool -> Bool

G_0 = f:Bool->Bool
G_1 = f:Bool->Bool, x : Bool
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

## Questions:
- Can a term have different types under different typing contexts?
- Evaluation rules are left-to-right/top-to-bottom, typing rules right-to-left/bottom-up?
