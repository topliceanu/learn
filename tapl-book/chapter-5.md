# Chapter 5: Lambda Calculus

## Concepts

* term:
  - either a variable (x)
  - an abstraction (\x.t, or function definition, t is the body of the abstraction) - or an application (t t, t applied to t)
* concrete syntax (or surface syntax): the source text
* abstract syntax: simpler internal representation of the program as ASTs
* application associates to the left: eg. s t u == (s t) u
* bodies of abstractions are extended as far to the right as possible (they are as long as possible)
  Eg. \x.\y.x y x == \x.(\y.((x y) x))
* metavariables,
  Eg. in \x.\y.x y == \z.s, where z = x, x = \y.x y are metavariables
* \x.t - the variable x is bound by the abstraction t; \x is the binder whose scope is term t.
* \y.x y - the variable x is free. (\x.x) x - the first x is bound, the second is free.
* a term with no free variable is _closed_, also called combinator
  Eg. simplest combinator is the identity function id=\x.x
* an _open term_ is a term that is not closed, ie. it has at least one free variable.
* an evaluation: (\x.t1) t2 -> [x:=t2]t1 - substituting the right-hand components (t2) for the bound variable (x) in t1.
  [x:=t2]t1is a term obtained by replacing all bound occurances of x in t1 with t2
* _redex_ - reducible expression, eg. (\x.t1) t2 = [x:=t2]t1
* beta-reduction - the operation of reducing a redex to simpler form
* types of evaluation
- full beta-reduction: pick any redex to evaluate first.
- normal strategy: leftmost, outermost redex is always reduced first
- call by name strategy: no reduction inside abstractions is allowed
  - call by need: instead of re-evaluating a term every time it's used, overwrite
    all occurrences with its value the first time it is evaluated.
    Ie. lazy evaluation!
- call by value strategy: outermost redexes are reduced first; a redex is reduced
  only when it's right-hand side has already been reduced to a value.
  Ie. strict evaluation!
* value - a term that is finished computing and cannot be reduced anymore.
* normal form - a term that cannot be evaluated anymore.
  - divergent term do not have a normal form.

## Church booleans
```
tru=\t.\f.t
fls=\t.\f.f

test=\b.\v.\w.b v w # similar to if
and=\b.\c.b c fls
or=\b.\c.b tru c # EX.5.2.1
not=\b.b fls tru # EX.5.2.1
xor=\b.\c.b (not c) c
```

### Pairs
```
pair=\f.\s.\b.b f s # encoded as a func which takes a boolean.
fst=\p.p tru
snd=\p.p fls
```

### Church numerals
A numeral cn is encoded as functions which take a function s and a value z and
applies s to z n times
```
c0=\s.\z.z
c1=\s.\z.s z
c2=\s.\z.s (s z)
# ...
```
Successor
```
scc=\n.\s.\z.s (n s z)
scc=\n.\s.\z.n s (s z) # alternative impl. # EX.5.2.2
scc=\n.\s.s (n s) # EX.5.2.2 Works!
```
Addition
```
plus=\n.\m.\s.\z.n s (m s z)
# Trying out plus.
plus c2 c3 =
(\n.\m.\s.\z. n s (m s z)) c2 c3 =
\s.\z.c2 s (c3 s z) =
\s.\z.c2 s ((\s'.\z'.s' (s' (s' z'))) s z) =
\s.\z.c2 s (s (s (s z))) =
\s.\z.(\s'.\z'.s' (s' z')) s (s (s (s z))) =
\s.\z.s (s (s (s (s z))))
c5
```
Multiplication
```
times=\n.\m.m (plus n) c0 # adds n to 0, m times!
times'=\n.\m.\s.\z.n (m s) z # EX.5.2.3 alternative implementation.
# Trying out times'
times' c2 c3 =
(\n.\m.\s.\z.n (m s) z) c2 c3 =
(\n.\m.\s.\z.n (m s) z) (\s'.\z'.s' (s' z')) (\s".\z".s" (s" (s" z"))) =
\m.\s.\z.(\s'.\z'.s' (s' z')) (m s) z =
\m.\s.\z.(m s) ((m s) z)) =
\s.\z.((\s".\z".s" (s" (s" z")) s) (((\s".\z".s" (s" (s" z"))) s) z)) =
\s.\z.(\z".s (s (s z")) (s (s (s z)) =
\s.\z.s (s (s (s (s (s z))))) = c6
```
Power
```
pow=\n.\m.m (times n) c1 # n^m=n*n*..*n*c1, m times. EX.5.2.4.
# Trying out pow. I'll not expand times.
pow c2 c3 =
(\n.\m.m (times n) c1) c2 c3 =
c3 (times c2) c1) =
(\s.\z.s (s (s z))) (times c2) c1 =
(times c2) ((times c2) ((times c2) c1)) =
(times c2) ((times c2) c2) =
(times c2) c4 =
c8
```
Mapping between Church numerals and Church booleans with `iszro`.
```
iszro=\n.n (\_ fls) tru # c0 does not execute s, only returns z, z=tru here.
# Trying out iszro with c0 and c3
iszro c0 = (\n.n (\_ fls) tru) c0 = c0 (\_ fls) tru = (\s.\z.z) (\_ fls) tru = tru
iszro c3 = (\n.n (\_ fls) tru) c3 = c3 (\_ fls) tru = (\s.\z.s (s (s z))) (\_ fls) true = (\_ fls) ((\_ fls) ((\_ fls) true)) = fls
```

Predecessor
This is more complicated, it involves building a list of (cn-1, cn) church numerals, up until cn, then returning cn-1.
```
zz=pair c0 c0
ss=\p.pair (snd p) (plus (snd p) c1)
prd=\m.fst (m ss zz)
# Trying out prd
prd c2 =
(\m.fst (m ss zz)) c2 =
fst (c2 ss zz) =
fst ((\s.\z s (s z)) ss zz) =
fst (ss (ss zz)) =
fst (ss (\p.pair (snd p) (plus (snd p) c1) (pair c0 c0))) =
fst (ss (pair c0 c1)) =
fst (\p.pair (snd p) (plus (snd p) c1) (pair c0 c1)) =
fst (pair c1 c2) =
c1
# Trying out prd for c0
prd c0 =
(\m.fst (m ss zz)) c0 =
fst (c0 ss zz) =
fst zz =
fst (pair c0 c0) =
c0 # predecessor of c0 is c0
```
Subtraction
```
sub=\n.\m.m prd n # EX.5.2.5 subtraction using prd, n - m applies prd on n, m times
# Trying out sub, without expanding prd.
sub c4 c2 =
(\n.\m.m prd n) c4 c2 =
c2 prd c4 =
(\x.\z.s (s z)) prd c4 =
prd (prd c4) = c2
# Trying out sub in case of a negative result.
sub c2 c4 =
(\n.\m.m prd n) c4 c2 =
c4 prd c2 =
(\x.\z.s (s (s (s z)))) prd c2 =
prd (prd (prd (prd c2))) =
prd (prd c0) =
c0 # instead of a negative result we get c0
```
EX.5.2.6. sub will do pred (pred (pred ... (pred n))), m times.
Each pred does n steps, so (n-m) + (n-m+1) + .. + n = n - m/2 total calculations.

Equality (EX.5.2.7) Q: Can I do a better zero?!
```
equal=\n.\m.iszro (sub n m) # Does not work when m > n
equal=\n.\m.and (iszero (sub m n)) (iszro (sub n m) # will work but is complicated!
# Trying equal without evaluating iszro and sub
equal c3 c2 =
and (iszro (sub c2 c3)) (iszro (sub c3 c2)) =
and (iszro c0) (iszro c1) =
and tru fls =
fls
```

## Lists
EX.5.2.8 [source](https://en.wikipedia.org/wiki/Church_encoding#Represent_the_list_using_right_fold)
Construct a list from a value h - the new list's head - and another list t - tail.
The empty list is nil whic is a function that returns its second argument.
```
nil=\c.\n.n # nil is always the second argument of a list abstraction
cons=\h.\t.\c.\n.c h (t c n)
# Trying out cons
l1 = cons x nil = # list with one value x
(\h.\t.\c.\n.c h (t c n)) x nil =
\c.\n.c x (nil c n) =
\c.\n.c x (\c'.\n'.n' c n) =
\c.\n.c x n

l2 = cons y (cons x nil) = # list with two values x, y
cons y ((\h.\t.\c.\n.c h (t c n)) x nil) =
cons y (\c.\n.c x (nil c n)) =
cons y (\c.\n.c x ((\c'.\n'.n') c n)) =
cons y (\c.\n.c x n) =
(\h.\t.\c.\n.c h (t c n)) y (\c'.\n'.c' x n') =
\c.\n.c y ((\c'.\n'.c' x n') c n)) =
\c.\n.c y (c x n)
```
A mapping from a list to a Church boolean.
```
isnil=\l.l (\h.\t.fls) tru # this looks similar to pattern matching
isnil nil =
(\l.l (\h.\t.fls) tru) nil =
nil (\h.\t.fls) tru =
(\c.\n.n) (\h.\t.fls) tru =
tru
# isnil on the list with one element.
isnil (cons x nil) =
(\l.l (\h.\t.fls) tru) (cons x nil) =
(cons x nil) (\h.\t.fls) tru =
(\c.\n.c x n) (\h.\t.fls) tru =
(\h.\t.fls) x tru =
fls
```
Extract the first element of the list
```
head=\l.l (\h.\t.h) nil
# Trying out head
head (cons x nil) =
(\l.l (\h.\t.h) nil) (cons x nil) =
(cons x nil) (\h.\t.h) nil =
(\c.\n.c x n) (\h.\t.h) nil =
(\h.\t.h) x nil =
x
```
Tail of a list
```
tail=\l.l (\h.\t.t) nil # Q: will this work ok?!
tail (cons x (cons y nil)) =
tail (\c.\n.c x (c y n)) =
(\l.l (\h.\t.t) nil) (\c.\n.c x (c y n)) =
(\c.\n.c x (c y n)) (\h.\t.t) nil =
(\h.\t.t) x ((\h.\t.t) y nil) =
(\h.\t.t) x nil =
nil # DOES NOT WORK!!!
```

## Lambda NB
```
realbool=\b.b true false # convert Church bool to a primitive bool
churchbool=\b.if b then tru else fls # converts a primitive bool to a Church bool
realeq=\m.\n. (equal m n) true false # checks if two Church bools are equal
realnat=\m.m (\x.succ x) 0 # converts a Church numeral into a primitive number
```

## Recursion
```
omega=(\x.x x) (\x.x x) # the omega combinator is a divergent operator
fix=\f.(\x.f (\y.x x y)) (\x.f (\y.x x y)) # the fix-point combinator or the call-by-value Y-combinator
fix'=\f.(\x.f (x x)) (\x.f (x x)) # call-by-name version of the Y-combinator

fix g =
(\f.(\x.f (\y.x x y)) (\x.f (\y.x x y))) g =
(\x.g (\y.x x y)) (\x.g (\y.x x y)) =
g (\y.(\x.g (\y.x x y)) (\x.g (\y.x x y)) y) =
g (\y.(fix g) y) =
g (fix g) # Q: is this true!?
```
Note that `fix g = g (fix g)` so fix is self-replicating.

Factorial
```
factorial=fix (\f.\n.if realeq n c0 then c1 else times n (f (pred n)))k
factorial'=fix (\f.\n.test (realeq n c0) c1 (times n (f pred n))) # Ex.5.2.9 Q: Why do we use if and not test; it's the same thing!?
# Trying the first factorial
factorial c3 =
fix g c3 = # where g = \f.\n.if realeq n c0 then c1 else times n (f (pred n))
\f.(\x.f (\y.x x y)) (\x.f (\y.x x y)) g c3 =
(\x.g (\y.x x y)) (\x.g (\y.x x y)) c3 =
(\x.g (\y.x x y)) (\x.g (\y.x x y)) c3 = # h h c3, where h = \x.g (\y.x x y)
g (\y.(\x.g (\y.x x y)) (\x.g (\y.x x y)) y) c3 = # g fct c3, where fct = \y.h h y
g fct c3 =
(\f.\n.if realeq n c0 then c1 else times n (f (pred n))) fct c3 =
if realeq c3 c0 then c1 else times c3 (fct (pred c3)) =
times c3 (fct c2') = # where c2' behaves like c2
times c3 ((\y.h h y) c2') =
times c3 (h h c2') = # this is the result of h h c3, so we can extrapolate that h h c2' is..
times c3 (times c2' (h h c1')) = # where c1' behaves like c1'
times c3 (times c2' (times c1' (h h c0'))) = (h h c0' = c1)
times c3 (times c2' (times c1' c1)) =
c6' # c6' is behaviorally equivalent to c6
```
Convert a primitive number into a Church numeral - Ex.5.2.10
```
churchnat=fix (\f.\n.\s.\z.if eq n 0 then z else s (f (pred n)))
# Trying it out
churchnat 3 =
fix g 3 =  # where g = \f.\n.\s.\z.if eq n 0 then z else s (f (pred n))
(\f.(\x.f (\y.x x y)) (\x.f (\y.x x y))) g 3 =
(\x.g (\y.x x y)) (\x.g (\y.x x y)) 3 =
(g (\y.(\x.g (\y.x x y)) (\x.g (\y.x x y)) y)) 3 =
g (fix g) 3 = # Q: is this correct?
(\f.\n.\s.\z.if (eq n 0) then z else s (f (pred n))) (fix g) 3 =
\s.\z.if (eq 3 0) then z else s ((fix g) (pred 3))) =
\s.\z.s (fix g) 2 = # recursion!
\s.\z.s (\s'.\z'.s' (fix g) 1) =
\s.\z.s (\s'.\z'.s' (\s".\z".s" (fix g) 0)) =
\s.\z.s (\s'.\z'.s' (\s".\z".s" (\s'".\z'".z"))) =
c3' # equivalent to c3
```
Sum a list of church numerals - Ex.5.2.11
Q: Can you apply sum to a list?
```
sum=fix (\f.\l.if (isnil l) then c0 else plus (head l) (f (tail l))) #
# Tryig it out
sum l3 = # where l3 = (\c.\n.c x (c y (c z n))) and x,y,z are Church numerals.
fix g l3 =
(\f.(\x.f (\y.x x y)) (\x.f (\y.x x y))) g l3 =
(\x.g (\y.x x y)) (\x.g (\y.x x y)) l3 =
g (\y.(\x.g (\y.x x y)) (\x.g (\y.x x y)) y) l3 =
g (fix g) l3 =
(\f.\l.if isnil l then c0 else plus (head l) (f (tail l))) (fix g) l3 =
plus (head l3) ((fix g) (tail l3)) =
plus x ((fix g) l2) = # where l2 = \c.\n.c y (c z n)
plus x (plus y ((fix g) l1)) = # where l1 = \c.\n.c z n
plus x (plus y (plus z ((fix g) l0)) = # Where l0 = \c.\n.n - empty list
plus x (plus y (plus z c0)) =
```
Tried a reduce (or fold) function. Q: how do you implement this?
```
reduce=\l.\l.fix ()
```

### Formalism

* Substitution:
```
[x-s]x       = s
[x-s]y       = y, x != y
[x->s](\y.t1) = \y.[x-s]t1, y != x & y not in FV(s) # x is not the bound variable y AND y should not be part of the free variables of s
[x->s](t1 t2) = [x-s]t1 [x-s]t2
```
This works if we assume that bound varialbe y is always different than x. Renaming is also an option.

- names of bound variables do not matter. eg. \x.x == \y.y == identity
- you can see non-canonical representations of Church numerals
- size of a term: the number of nodes in its abstract syntax tree
- the set of free variables in a term:
```
FV(x) = {x}
FV(\x.t) = FV(t) - {x}
FV(t1 t2) = FV(t1) U FV(t2)
```
EX.5.3.3.|FV(t)| <= size(t) because t can have bound variables which appear in the AST Q: Is this correct?!

* operational semantics
```
Syntax:
t ::= x - variable
      \x.t - abstraction
      t t - application

Values:
v ::= \x.t - abstraction value

Evaluation:
    t1 -> t1'
----------------- (E-App1)
 t1 t2 -> t1' t2

    t2 -> t2'
--------------- (E-App2)
t1 t2 -> t1 t2'

(\x.t12) v2 -> [x->v2]t12 (E-AppAbs)
```

EX.5.3.6. HOW!?!?

## Questions for Ch5.
* Should I implement a lambda calculus interpretor?
* Do all the types of evaluation yield the same result all the time?
* Can I do a better `equal`?
* I don't know how to implement `tail` and I don't understand the one on Wikipedia.
* call-by-name vs call-by-value. What is the difference? Eg. fix and fix'
* Review exercises in the recursion section work.
* How do you implement a reduce method?
* Should we do the exercises in the formalism section?
* How do you get to the fix combinator? Is there any process to reach it?
* Is it true that fix f = f (fix f) ?
* How would you make a fold function over a list?

