# Rust's borrow checker

- simple values are copied. Eg. integers, what else?
  - simple values are allocated on the stack
- complex values are allocated on the heap. Eg. strings
- when a variable goes out of scope, it's allocated memory is freed.
- the _double free error_ when two variable reference the same memory address.

Q: What would be the transformation of assignment from Rust in ML?
```
let u = s in t  <=>  [u->s]t; dealloc u
```

- in order to not move, the type (it's size actually) has to be known at compile-time.
Eg: integers, bools, floats, chars, tuples.

- assignment and function application either moves (for references) or copies (for primitives).

Q: Why not make everything a mutable reference? Then you're back to what C does!
- You can only have on mutable reference to a variable

