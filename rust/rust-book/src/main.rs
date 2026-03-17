
use std::{sync::mpsc, thread};

#[derive(Debug)]
enum Msg {
    Str(String),
    Usize(usize),
}

fn main() {
    let (tx, rx) = mpsc::channel::<Msg>();
    thread::spawn(move || {
        let s = String::from("Hello world");
        tx.send(Msg::Str(s.clone())).unwrap();
        tx.send(Msg::Usize(s.len())).unwrap();
    });
    let s = rx.recv().unwrap();
    let n = rx.recv().unwrap();
    println!("{s:?} {n:?}");
}