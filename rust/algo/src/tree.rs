/*
// Red-black tree invariants:
// 1. each node is either red or black.
// 2. root node is always black
// 3. no two reds in a row: the child of a red node cannot be red, it has to be black. Conversely the parent of a red node cannot be red.
// 4. every root-null path has the same number of black nodes. For every node in the tree, any path node-to-null, passes through the same number of black nodes.

use std::cmp::Ordering;

pub enum Color {
    Red,
    Black,
}

pub struct RBTree<T: Ord> {
   pub root: Option<Box<RBNode<T>>>,
}

pub struct RBNode<T> {
    pub value: T, // Note that the node owns the value.
    pub color: Color,
    pub left: Option<Box<RBNode<T>>>,
    pub right: Option<Box<RBNode<T>>>,
}

impl<T: Ord> RBTree<T> {
    pub fn new() -> RBTree<T> {
       return RBTree{ root: None } 
    }
    
    pub fn search(&self, value: &T) -> bool {
        let mut current = &self.root;
        while let Some(node) = current {
            match value.cmp(&node.value) {
                Ordering::Less => current = &node.left,
                Ordering::Greater => current = &node.right,
                Ordering::Equal => return true,
            }
        }
        return false
    }

    pub fn insert(&mut self, value: &T) {
        if let None = self.root {
            self.root = Some(Box::new(RBNode{
                value: value,
                color: Color::Black,
                left: None,
                right: None,
            }));
            return;
        }
        // TODO ...
    }
}
*/