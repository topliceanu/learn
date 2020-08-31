# Exceptions

- a way to return errors from functions is to return option types (like Option or Result).
However, as a convenience for the client of the function, for _truly exceptional_ situations,
we can throw an exception.

```
Syntax:
t ::= ...
      error        - run-time error

Evaluation:
error t2 -> error (E-AppErr1)

v1 error -> error (E-AppErr2)

Typing:
Γ|-error:T (T-Error) - the term error is allowed to have any type T
```

- note that `error` is not a value, but a term. Also, `error` is a non-value normal
- E-AppErr2 suggests that the left-hand side of an application needs to be evaluated down to a value, before the execution is aborted. Eg:
```
(\x:Nat.0) error - yields error not 0
(fix (\x:Nat.x)) error - diverges before aborting with error
```
- error can have any type (as per T-Error) which breaks the rule that every typable term has a unique type.
You can get around this by having error be of type _Bottom_ which can be promoted to any other type or giving error a polymorphic type.

EX14.1.1. Wouldn’t it be simpler just to require the programmer to annotate error with its intended type in each context where it is used?
```
In terms of programmer convenience, it wouldn't be "simpler", because the programmer would have to calculate the type or error himself.
This can be difficult even for simple expressions. Eg: (λx:Bool.x) (error true) - the type of error is Bool->Bool.

In terms of correctness, you may have in the same context error with different types, which will fail the type checker
Eg: if t1 then (error true) else error - this expression does not type check because error is simultaneously Bool->Bool and Bool.
```

- new progress theorem: if t is a closed, well-typed normal form, then t is either a value or is `error`.

```
Syntax:
t ::= ...
      try t with t     - trap errors

Evaluation:
try v1 with t2 -> v1 (E-TryV)   - we can throw away the try because we have a value.

try error with t2 -> t2 (E-TryError)   - replace try with t2 when t1 evaluates to error

            t1 -> t1'
---------------------------------- (E-Try)  - keep evaluating t1 as long as it doesn't evaluate to error
try t1 with t2 -> try t1' with t2

Typing:
 Γ|-t1:T     Γ|-t2:T
--------------------- (T-Try) - even if you install an exception handler t2, it has to have the same type as t1.
 Γ|-try t1 with t2:T
```
- the exeption works as non-local transfer of control, whose target is the most recently installed exception handler.
- try t1 with t2 - return the result of t1 unless it aborts in which case return the result of t2.

## Exceptions carrying data

```
Syntax:
t ::= ...
      raise t             - raise exception
      try t with t        - handle exceptions

Evaluation:
(raise v11) t2 -> raise v11 (E-AppRaise1)
v1 (raise v21) -> raise v21 (E-AppRaise2)

      t1 -> t1'
--------------------- (E-Raise)
raise t1 -> raise t1'

raise (raise v11) -> raise v1 (E-RaiseRaise)

try v1 with t2 -> v1 (E-TryV)
try raise v11 with t2 -> t2 v11 (E-TryRaise)

            t1 -> t1'
--------------------------------- (E-Try)
try t1 with t2 -> try t1' with t2

Typing:

  Γ|-t1:Texn
--------------- (T-Exn)
 Γ|-raise t1:T

Γ|-t1:T  Γ|-t2:Texn->T
----------------------- (T-Try)
 Γ|-try t1 with t2:T
```
