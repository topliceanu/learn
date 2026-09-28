use std::cell::RefCell;
use std::collections::HashSet;
use std::rc::Rc;

pub enum List {
    Nil,
    Cons(i32, Box<List>),
}

impl List {
    pub fn new(values: &Vec<i32>) -> Self {
        values
            .into_iter()
            .rev()
            .fold(List::Nil, |acc, val| List::Cons(*val, Box::new(acc)))
    }

    pub fn to_values(&self) -> Vec<i32> {
        let mut output: Vec<i32> = Vec::new();
        let mut current = self;
        while let List::Cons(value, rest) = current {
            output.push(*value);
            current = rest.as_ref();
        }
        output
    }
}

// Problem 2.1 Remove dups:
// Remove duplicates from an unsorted linked list. What if you're not allowed a temporary buf?

// This is the recomended way to solve this, with no unsafe code and no raw pointers. Time and space complexity is O(n).
pub fn remove_dups(list: &mut List) {
    if let List::Nil = list {
        return
    } 
    let mut seen: HashSet<i32> = HashSet::new();
    let mut values: Vec<i32> = Vec::new();

    let mut current = &*list; // Traverse an immutable reference to list.
    while let List::Cons(value, rest) = current {
        if !seen.contains(value) {
            seen.insert(*value);
            values.push(*value);
        }
        current = rest;
    }
    let new_list = values
        .into_iter()
        .rev()
        .fold(List::Nil, |rest, value| { 
            List::Cons(value, Box::new(rest))
        });
    // current now holds the input list
    *list = new_list;
}

// Problem 2.2 Return Kth to Last: 
// Implement an algorithm to find the kth to last element of a singly linked list.

pub fn kth_to_last(list: &List, k: usize) -> Option<i32> {
    let mut current = list;
    let mut tracker = &List::Nil;
    let mut i = 0;
    while let List::Cons (_, next) = current {
        if i >= k {
            match tracker {
                List::Nil => tracker = list,
                List::Cons(_, next) => tracker = next,
            }
        }
        current = next;
        i += 1;
    }
    match tracker {
        List::Nil => Option::None,
        List::Cons(value, _) => Some(*value),
    }
}

pub fn kth(list: &List, k: usize) -> Option<i32> {
    let mut ahead = list;
    let mut i: usize = 0;
    while let List::Cons (value, next) = ahead && i <= k {
        if i == k {
            return Some(*value);
        }
        ahead = next;
        i += 1;
    }
    return None 
}

// Problem 2.3 Delete Middle Node: 
// Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) 
// of a singly linked list, given only access to that node.
pub fn delete_middle_node(list: &mut List, to_delete: i32) {
    let mut values:Vec<i32> = vec![];
    let mut current = &*list;
    while let List::Cons(value, next) = current {
        if *value != to_delete {
            values.push(*value)
        }
        current = next.as_ref();
    }
    let new_list = values.into_iter().rev().fold(List::Nil, |acc, value| {List::Cons(value, Box::new(acc))});
    *list = new_list;
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_remove_dups() {
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
            let mut subject = List::new(&raw);
            remove_dups(&mut subject);
            assert_eq!(
                expected,
                subject.to_values(),
                "input={:?}",
                raw,
            );
        }
    }

    #[test]
    fn test_kth_to_last() {
        let tests: Vec<(Vec<i32>, usize, Option<i32>)> = vec![
            (vec![], 0, None),
            (vec![1], 2, None),
            (vec![1], 0, Some(1)),
            (vec![1,2,3,4,5], 2, Some(3)),
        ];
        for (input, k, expected) in tests {
            let list = List::new(&input);
            let actual = kth_to_last(&list, k);
            assert_eq!(expected, actual, "input={:?} k={:}", input, k)
        }
    }

    #[test]
    fn test_delete_middle_node() {
        let tests: Vec<(Vec<i32>, i32, Vec<i32>)> = vec![
            (vec![], -2, vec![]),
            (vec![1,2,3,4], 5, vec![1,2,3,4]),
            (vec![1,2,3,4], 2, vec![1,3,4]),
            (vec![1,2,3], 3, vec![1,2]),
        ];
        for (input, to_delete, expected) in tests {
            let mut list = List::new(&input);
            delete_middle_node(&mut list, to_delete);
            assert_eq!(expected, list.to_values(), "input={:?} k={:}", input, to_delete)
        }
    }
 
}
