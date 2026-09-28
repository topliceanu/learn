use std::collections::{HashSet, VecDeque};

pub struct Graph {
    pub vertices: HashSet<u32>,
    pub edges: Vec<(u32, u32)>, // (source vertex, destination vertex)
}

impl Graph {
    pub fn new(_vertices: &[u32], _edges: &[(u32, u32)]) -> Self {
        let mut vertices: HashSet<u32> = HashSet::new();
        let mut edges: Vec<(u32, u32)> = vec![];
        for vertex in _vertices.iter() {
            vertices.insert(*vertex);
        }
        for (start, end) in _edges {
            // OPTIONAL: maybe throwing a panic is better than inserting previously unknown vertices!
            if !vertices.contains(&start) { vertices.insert(*start); }
            if !vertices.contains(&end) { vertices.insert(*end); }
            edges.push((*start, *end));
        }
        Graph { vertices, edges }
    }
    pub fn adjacents(&self, vertex: u32) -> Vec<u32> {
        let mut out: Vec<u32> = vec![];
        for &(start, end) in self.edges.iter() {
            if start == vertex { out.push(end); }
        }
        return out
    }
}

// Problem 4.1: Route between nodes
// Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
pub fn route_between_nodes(g: &Graph, start: u32, finish: u32) -> bool {
    if !(g.vertices.contains(&start) && g.vertices.contains(&finish)) {
        return false
    }
    // Breath-first search.
    let mut queue: VecDeque<u32> = VecDeque::new();
    let mut visited: HashSet<u32> = HashSet::new();
    queue.push_back(start);
    while let Some(next) = queue.pop_front() {
        if visited.contains(&next) {
            continue
        }
        visited.insert(next);
        let adjs = g.adjacents(next);
        for &adj in adjs.iter() {
            queue.push_back(adj);
        }
    }
    return visited.contains(&finish);
}

// Same as above but using Depth-first search.
// The difference between DFS and BFS is that DFS uses a queue and BFS uses a stack.
pub fn route_between_nodes2(g: &Graph, start: u32, finish: u32) -> bool {
    if !(g.vertices.contains(&start) && g.vertices.contains(&finish)) {
        return false
    }
    let mut visited: HashSet<u32> = HashSet::new();
    let mut stack: VecDeque<u32> = VecDeque::new();
    stack.push_back(start);
    while let Some(next) = stack.pop_back() {
        if visited.contains(&next) {
            continue
        }
        visited.insert(next);
        let adjs = g.adjacents(next); 
        for &adj in adjs.iter() {
            stack.push_back(adj);
        }
    }
    return visited.contains(&finish);
}

// Problem 4.2 Minimal Tree:
// Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.

pub enum BTN<T> {
    Leaf,
    Node (T, Box<BTN<T>>, Box<BTN<T>>),
}

impl<T> BTN<T> {
    pub fn insert(&mut self, x: T) {
        
    }
}

pub fn minimal_tree(input: &[i32]) -> BTN<i32> {
    let mut start = 0;
    let mut end = input.len() - 1 ;
    let output = BTN::Leaf; 
    while start <= end {
        todo!()
    }
    return output;
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_route_between_nodes() {
        let tests: Vec<(Vec<u32>, Vec<(u32, u32)>, u32, u32, bool)> = vec![
            (vec![1,2,3], vec![(1,2), (2,3)], 1, 3, true),
            (vec![1,2,3,4], vec![(1,2), (3,4)], 1, 4, false),
        ];
        for (vertices, edges, start, finish, expected) in tests {
            let g = Graph::new(&vertices, &edges);
            let actual = route_between_nodes(&g, start, finish);
            assert_eq!(expected, actual)
        }
    }
}