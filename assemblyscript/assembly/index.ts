// The entry file of your WebAssembly module.

export function add(a: i32, b: i32): i32 {
  return a + b;
}

export function fib(n: i32): i32 {
  let a = 0, b = 1;
  for (let i = 0; i < n; i++) {
    let t = a + b;
    a = b;
    b = t;
  }
  return b
}
