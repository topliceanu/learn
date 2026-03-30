use std::cell::RefCell;
use std::collections::HashSet;
use std::rc::Rc;

pub enum List {
    Nil,
    Cons(i32, Box<List>),
}

// CCI-book, ed6, ch2. pr 2.1 Remove dups: remove duplicates from an unsorted linked list.
// What if you're not allowed a temporary buf?

pub fn remove_dups(list: &List) -> List {
    let mut seen: HashSet<i32> = HashSet::new();
    let mut values: Vec<i32> = Vec::new();

    let mut current = list;
    while let List::Cons(value, rest) = current {
        if !seen.contains(value) {
            seen.insert(*value);
            values.push(*value);
        }
        current = rest.as_ref();
    }
    let mut output = List::Nil;
    for value in values.into_iter().rev() {
        output = List::Cons(value, Box::new(output));
    }
    return output;
}

pub fn remove_dups_v2(list: &List) -> List {
    match list {
        List::Nil => List::Nil,
        List::Cons(value, rest) => {
            let new_list = remove_dups_of(*value, rest);
            let new_list = remove_dups_v2(&new_list);
            List::Cons(*value, Box::new(new_list))
        }
    }
}

fn remove_dups_of(value: i32, rest: &List) -> List {
    match rest {
        List::Nil => List::Nil,
        List::Cons(another_value, another_rest) => {
            let clean = remove_dups_of(value, another_rest);
            if *another_value == value {
                clean
            } else {
                List::Cons(*another_value, Box::new(clean))
            }
        }
    }
}

pub enum List2 {
    Nil,
    Cons(i32, Rc<RefCell<List>>), // I need Rc in order to share ownership of the tail of the list between the old list and the clean list. Q: Can't I just do it with RefCell. So I can pass it to a subroutine to cleanup.
                                  // I need RefCell in order to mutate the tail List.
}

pub fn remove_dups_v3(list: &mut List2) {
    // TODO Removes duplicates in place with constant extra memory.
}

// Test helpers

fn to_list(values: &Vec<i32>) -> List {
    values
        .into_iter()
        .rev()
        .fold(List::Nil, |acc, val| List::Cons(*val, Box::new(acc)))
}

fn to_values(list: &List) -> Vec<i32> {
    let mut output: Vec<i32> = Vec::new();
    let mut current = list;
    while let List::Cons(value, rest) = current {
        output.push(*value);
        current = rest.as_ref();
    }
    output
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn smoke_test() {
        let tests: Vec<(Vec<i32>, Vec<i32>)> = vec![
            (vec![], vec![]),
            (vec![1], vec![1]),
            (vec![1, 1], vec![1]),
            (vec![1, 2, 1], vec![1, 2]),
            (vec![1, 1, 1], vec![1]),
            (vec![2, 1, 1, 1], vec![2, 1]),
            (vec![3, 2, 1, 1, 2, 3], vec![3, 2, 1]), // Keep initial order.
        ];
        for (raw, expected) in tests {
            let subject = to_list(&raw);
            let actual1 = remove_dups(&subject);
            assert_eq!(
                expected,
                to_values(&actual1),
                "v1 input={:?} expected={:?}",
                raw,
                expected
            );
            let actual2 = remove_dups_v2(&subject);
            assert_eq!(
                expected,
                to_values(&actual2),
                "v2 input={:?} expected={:?}",
                raw,
                expected
            );
        }
    }
}
