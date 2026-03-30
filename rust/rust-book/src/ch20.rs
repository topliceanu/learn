use core::slice;
use std::fmt;

pub trait OutlinePrint: fmt::Display {
    fn outline_print(&self) {
        let output = self.to_string();
        let len = output.len();
        println!("{}", "*".repeat(len + 4));
        println!("*{}*", " ".repeat(len + 2));
        println!("* {output} *");
        println!("*{}*", " ".repeat(len + 2));
        println!("{}", "*".repeat(len + 4));
    }
}

// Splits a mutable slice into two mutable slices.
pub fn split_at_mut(values: &mut [i32], mid: usize) -> (&mut [i32], &mut [i32]) {
    let len = values.len();
    let ptr = values.as_mut_ptr(); // unsafe raw pointer; it's the address of the first value in the array.
    assert!(mid <= len);
    unsafe {
        (
            slice::from_raw_parts_mut(ptr, mid), // a slice is a pointer (an address) and a length in number of bytes.
            slice::from_raw_parts_mut(ptr.add(mid), len - mid),
        )
    }
}

pub struct Counter(i32);

impl Iterator for Counter {
    type Item = i32;

    fn next(&mut self) -> Option<<Self as Iterator>::Item> { 
        None
    }
}
