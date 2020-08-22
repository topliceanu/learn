# Rust's borrow checker

- simple values are copied. Eg. integers, what else?
  - simple values are allocated on the stack
- complex values are allocated on the heap. Eg. strings
- when a variable goes out of scope, it's allocated memory is freed.
- the _double free error_ when two variable reference the same memory address.
