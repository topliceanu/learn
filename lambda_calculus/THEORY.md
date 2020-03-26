# Lambda calculus

## Concepts
* term:
  - either a variable (x)
  - an abstraction (\x.t, or function definition, t is the body of the abstraction)
  - or an application (t t, t applied to t)
* concrete syntax (or surface syntax): the source text
* abstract syntax: simpler internal representation of the program as ASTs
* application associates to the left: eg. s t u == (s t) u
* bodies of abstractions are extended as far to the right as possible (they are as long as possible)
  Eg. \x.\y.x y x == \x.(\y.((x y) x))
* metavariables,
  Eg. in \x.\y.x y == \z.s, where z = x, x = \y.x y are metavariables
* \x.t - the variable x is bound by the abstraction t; \x is the binder whose scope is term t.
* \y.x y - the variable x is free. (\x.x) x - the first x is bound, the second is free.
* a term with no free variable is closed, also called combinator
  Eg. simplest combinator is the identity function id=\x.x
* an evaluation: (\x.t1) t2 -> [x:=t2]t1 - substituting the right-hand components (t2) for the bound variable (x) in t1.
  [x:=t2]t1is a term obtained by replacing all bound occurances of x in t1 with t2
* redex - reducible expression, eg. (\x.t1) t2 = [x:=t2] t1
* beta-reduction - the operation of reducing a redex to simpler form
* types of evaluation
- full beta-reduction: pick any redex to evaluate first.
- normal strategy: leftmost, outermost redex is always reduced first
- call by name strategy: no reduction inside abstractions is allowed
  - call by need: instead of re-evaluating a term every time it's used, overwrite all occurrences with its value the first time it is evaluated. Lazy!
- call by value strategy: outermost redexes are reduced first; a redex is reduced only when it's right-hand side has already been reduced to a value. Strict.
* value - a term that is finished computing and cannot be reduced anymore.

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

## Pairs
```
pair=\f.\s.\b.b f s # encoded as a func which takes a boolean.
fst=\p.p tru
snd=\p.p fls
```

## Church numerals
A numeral cn is encoded as functions which take a function s and a value z and
applies s to z n times
```
c0=\s.\z.z
c1=\s.\z.s z
c2=\s.\z.s (s z)
# ...
scc=\n.\s.\z.s (n s z)
scc=\n.\s.\z.n s (s z) # alternative impl. # EX.5.2.2
scc=\n.\s.s (n s) # EX.5.2.2 Works!
plus=\n.\m.\s.\z.n s (m s z)
times=\n.\m.m (plus n) c0 # adds n to 0, m times!
times'=\n.\m.\s.\z.n (m s) z # EX.5.2.3 Works!

times'c2 c3 =
(\n.\m.\s.\z.n (m s) z) c2 c3 =
(\n.\m.\s.\z.n (m s) z) (\s'.\z'.s' (s' z')) (\s".\z".s" (s" (s" z"))) =
\m.\s.\z.(\s'.\z'.s' (s' z')) (m s) z =
\m.\s.\z.(m s) ((m s) z)) =
\s.\z.((\s".\z".s" (s" (s" z")) s) (((\s".\z".s" (s" (s" z"))) s) z)) =
\s.\z.(\z".s (s (s z")) (s (s (s z)) =
\s.\z.s (s (s (s (s (s z))))) = c6

pow=\n.\m.m (times n) n # n^m=n*n*..*n, m times. EX.5.2.4. Q: does this work?
iszro=\n.n (\x fls) true # c0 is the only Church numeral which does not apply s to z, so it will return true. For all other number, s is apply and it will discard the parameter and return fls.

# predecessor is more complicated, it involves building a list of (cn-1, cn) church numerals, up until cn, then returning cn-1.
zz=pair c0 c0
ss=\p.pair (snd p) (plus (snd p) c1)
prd=\m.fst (m ss zz)
sub=\n.\m.m pred n # n - m so it applies pred on n, m times EX.5.2.5 subtraction using pred
```
EX.5.2.6. sub will do pred (pred (pred ... (pred n))), m times. Each pred does n steps, so (n-m) + (n-m+1) + .. + n = n - m/2
```
equal=\n.\m.iszro (sub n m) # EX.5.2.7 DOES NOT WORK
```

## Lists EX.5.2.8 [source](https://en.wikipedia.org/wiki/Church_encoding#Represent_the_list_using_right_fold)
```
fold=\x.\c.\n.c x n # for one value
fold=\x.\y.\c.\n.c x (c y n) # for two values
fold=\x.\y.\z.\c.\n.c x (c y (c z n)) # for three values
nil=\c.\n.n # nil is always the second argument of a list abstraction
cons=\h.\t.\c.\n.c h (t c n)
isnil=\l.l (\h.\t.fls) tru # this looks similar to pattern matching
head=\l.l (\h.\t.h) nil
tail=\l.l (\h.\t.t) nil # Q: will this work ok?!
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
factorial=fix (\f.\n.if realeq n c0 then c1 else times n (f pred n))
factorial'=fix (\f.\n.test (realeq n c0) c1 (times n (f pred n))) # Ex.5.2.9 Q: Why do we use if and not test; it's the same thing!?
churchnat=fix (\f.\n.\s.\z.if (realeq n 0) then z else s (f (n - 1))) # Ex.5.2.10 converts a primitive natural number to a Church numeral
sum=fix (\f.\l.if (isnil l) then c0 else plus (head l) (f (tail l))) # Ex.5.2.11 sum the church numerals in a list. How do you apply sum to a list?!
reduce=\l.\l.fix () # Ex.5.2.11 tried my hand at a fold-like function
```

## Formalism
- size of a term: the number of nodes in its abstract syntax tree
- the set of free variables in a term:
  FV(x) = {x}
  FV(\x.t) = FV(t) - {x}
  FV(t1 t2) = FV(t1) U FV(t2)

EX.5.3.3.|FV(t)| <= size(t) because t can have bound variables which appear in the AST Q: Is this correct?!

# Questions:
1. Should I implement a lambda calculus interpretor?
2. I'm having trouble with this application to the left! Is it common? Isn't it to the right in other languages?
3. We're encoding a pair in terms of the exhaustive set of operations we know it supports (fst, snd). Is it ok?
4. Do all the types of evaluation yield the same result all the time?
5. I need help with the application! Eg. (times c2 c2)
6. call-by-name vs call-by-value. What is the difference? Eg. fix and fix'
7. I don't understand recursion with the fix function! What it the practical use of learning/understanding this construct? Where can I use it?

# Resources
1. Church encodings used in TaPL [wiki](https://en.wikipedia.org/wiki/Church_encoding#List_encodings)
2. System F, a typed lambda calculus [wiki](https://en.wikipedia.org/wiki/System_F)
3. Impl of lambda calculus in Racket [link](http://matt.might.net/articles/compiling-up-to-lambda-calculus/)
4. Computerfile videos on this:
  - [Lambda calculus](https://www.youtube.com/watch?v=eis11j_iGMs)
  - [Y combinator](https://www.youtube.com/watch?v=9T8A89jgeTI) - good intuition on recursion in lambda calculus
  - [What is a monad](https://www.youtube.com/watch?v=t1e8gqXLbsU)
  - [Functional parsing](https://www.youtube.com/watch?v=dDtZLm7HIJs)
  - [What is Functional Programming](https://www.youtube.com/watch?v=LnX3B9oaKzw)
