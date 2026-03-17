use std::ops::Deref;
use std::rc::Rc;
use std::cell::RefCell;
use std::rc::Weak;

pub enum List<T> {
    Nil,
    Cons(T, Box<List< T>>),
}

pub enum List1<'a, T> {
    Nil1,
    Cons1(T,  Box<&'a List1<'a, T>>),
}

pub enum List2<T> {
    Nil2,
    Cons2(T,  Rc<List2<T>>),
}

pub enum List3<T> {
    Nil3,
    Cons3(Rc<RefCell<T>>, Rc<List3<T>>)
}

#[derive(Debug)]
pub enum List4<T> {
    Nil4, 
    Cons4(T, RefCell<Rc<List4<T>>>)
}
 
impl<T> List4<T> {
    pub fn tail(&self) -> Option<&RefCell<Rc<List4<T>>>> {
        match self {
            List4::Cons4(_, rest) => Some(rest),
            List4::Nil4 => None,
        }
    }
}

#[derive(Debug)]
pub struct Node<T> {
    pub value: T,
    pub parent: RefCell<Weak<Node<T>>>,
    pub children: RefCell<Vec<Rc<Node<T>>>>,
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

pub trait Messenger {
    fn send(&self, msg: &str);
}

pub struct LimitTracker<'a, T: Messenger> {
    messenger: &'a T,
    value: usize,
    max: usize,
}

impl<'a, T> LimitTracker<'a, T>
where
    T: Messenger,
{
    pub fn new(messenger: &'a T, max: usize) -> LimitTracker<'a, T> {
        LimitTracker {
            messenger,
            value: 0,
            max,
        }
    }

    pub fn set_value(&mut self, value: usize) {
        self.value = value;

        let percentage_of_max = self.value as f64 / self.max as f64;

        if percentage_of_max >= 1.0 {
            self.messenger.send("Error: You are over your quota!");
        } else if percentage_of_max >= 0.9 {
            self.messenger
                .send("Urgent warning: You've used up over 90% of your quota!");
        } else if percentage_of_max >= 0.75 {
            self.messenger
                .send("Warning: You've used up over 75% of your quota!");
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::cell::RefCell;

    struct MockMessenger {
        sent_messages: RefCell<Vec<String>>,
    }

    impl MockMessenger {
        fn new() -> MockMessenger {
            MockMessenger {
                sent_messages: RefCell::new(vec![]),
            }
        }
    }

    impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
            self.sent_messages.borrow_mut().push(String::from(message));
        }
    }

    #[test]
    fn it_sends_an_over_75_percent_warning_message() {
        let mock_messenger = MockMessenger::new();
        let mut limit_tracker = LimitTracker::new(&mock_messenger, 100);

        limit_tracker.set_value(80);

        assert_eq!(mock_messenger.sent_messages.borrow().len(), 1);
    }
}

pub struct DLNode<T> {
    pub value:T, 
    pub prev: Option<Rc<RefCell<DLNode<T>>>>,
    pub next: Option<Rc<RefCell<DLNode<T>>>>,
}

