use std::ops::Deref;

pub enum List<T> {
    Nil,
    Cons(T, Box<List<T>>),
}

pub struct MyBox<T>(T);

impl<T> MyBox<T> {
    pub fn new(x: T) -> MyBox<T> {
        MyBox(x)
    }
}

impl<T> Deref for MyBox<T> {
    type Target = T;

    fn deref(self: &Self) -> &Self::Target {
        &self.0
    }
}