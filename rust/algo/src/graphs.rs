use std::{collections::{BinaryHeap, HashMap, HashSet, VecDeque}};
use std::cmp::{Reverse};

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
            // THINK ABOUT IT: maybe throwing a panic is better than inserting previously unknown vertices!
            if !vertices.contains(&start) { vertices.insert(*start); }
            if !vertices.contains(&end) { vertices.insert(*end); }
            edges.push((*start, *end));
        }
        Graph { vertices, edges }
    }
    pub fn transpose(g: &Graph) -> Self {
        Graph {
            edges: g.edges.iter().map(|(a, b)| (*b, *a)).collect(),
            vertices: g.vertices.clone(),
        }
    }
    pub fn adjacents(&self, vertex: &u32) -> Vec<u32> {
        let mut out: Vec<u32> = vec![];
        for (start, end) in self.edges.iter() {
            if start == vertex { out.push(*end); }
        }
        out.sort_unstable();
        return out
    }
    pub fn bfs(&self, start: &u32) -> Vec<u32> {
        if !self.vertices.contains(&start) {
            return vec![]
        }

        let mut queue: VecDeque<u32> = VecDeque::new();
        let mut visited: HashSet<u32> = HashSet::new();
        let mut output: Vec<u32> = vec![];

        queue.push_back(*start);
        while let Some(current) = queue.pop_front() {
            if visited.contains(&current) {
                continue
            }
            visited.insert(current);
            output.push(current);
            for adj in self.adjacents(&current) {
                queue.push_back(adj);
            }
        }
        return output
    }
    pub fn dfs(&self, start: &u32) -> Vec<u32> {
        if !self.vertices.contains(&start) {
            return vec![];
        }

        let mut stack: Vec<u32> = vec![];
        let mut visited: HashSet<u32> = HashSet::new();
        let mut output: Vec<u32> = vec![];

        stack.push(*start);
        while let Some(current) = stack.pop() {
            if visited.contains(&current) {
                continue
            }
            visited.insert(current);
            output.push(current);
            for adj in self.adjacents(&current) {
                stack.push(adj);
            }
        }
        return output
    }

    pub fn has_cycles(&self) -> bool {
        enum Action {
            Enter(u32),
            Exit(u32),
        }
        let mut global_visited: HashSet<u32> = HashSet::new();
        let mut path: HashSet<u32> = HashSet::new();
        let mut stack = Vec::new();

        for vertex in &self.vertices {
            let start = *vertex;
            if global_visited.contains(&start) || path.contains(&start) {
                continue;
            }
            stack.push(Action::Enter(start));
            while let Some(action) = stack.pop() {
                match action {
                    Action::Enter(current) => {
                        // If the node is currently on our active path, we found a cycle!
                        if path.contains(&current) {
                            return true;
                        }
                        // If it's already fully processed from another branch, skip it
                        if global_visited.contains(&current) {
                            continue;
                        }
                        // Mark as active in the current path and schedule its exit
                        path.insert(current);
                        stack.push(Action::Exit(current));

                        // Push all neighbors to be explored
                        for adj in self.adjacents(&current) {
                            stack.push(Action::Enter(adj));
                        }
                    }
                    Action::Exit(current) => {
                        // Backtracking: remove from active path and mark fully visited
                        path.remove(&current);
                        global_visited.insert(current);
                    }
                }
            }
        }
        return false;
    }
 
    // This method uses Khan's algorithm to recursively remove sink vertices from the graph.
    // See https://en.wikipedia.org/wiki/Topological_sorting
    pub fn topological_sort(&self) -> Option<Vec<u32>> {
        // The return type captures the fact that the graph may have cycles in it so it won't have a topological ordering.
        let mut in_degree: HashMap<u32, usize> = HashMap::new();
        for v in self.vertices.iter() {
            in_degree.entry(*v).or_insert(0);
        }
        for (_, b) in self.edges.iter() {
            *in_degree.entry(*b).or_insert(0) += 1;
        }
        let mut queue: VecDeque<u32> = VecDeque::new();
        for (&v, &in_deg) in in_degree.iter() {
            if in_deg == 0 {
                queue.push_back(v);
            }
        }
        let mut output: Vec<u32> = vec![];
        while let Some(vertex) = queue.pop_front() {
            output.push(vertex);
            // Simulate removing the vertex from the graph by decreasing the in-degree of all adjacent nodes.
            for adj in self.adjacents(&vertex) {
                let deg = in_degree.get_mut(&adj).unwrap();
                *deg -= 1;
                if *deg == 0 {
                    queue.push_back(adj);
                }
            }
        }
        if output.len() != self.vertices.len() {
            return None
        }
        return Some(output)
    }

    fn dfs_helper(g: &Graph, vertex: u32, visited: &mut HashSet<u32>, order: &mut Vec<u32>) {
        let mut stack: Vec<u32> = vec![vertex];
        while let Some(vertex) = stack.pop() {
            if visited.contains(&vertex) {
                continue
            }
            visited.insert(vertex);
            for adj in g.adjacents(&vertex) {
                stack.push(adj);
            }
            order.push(vertex);
        }
    }

    // See Kosaraju's algorithm: https://cp-algorithms.com/graph/strongly-connected-components.html
    // Step 1. Run a sequence of depth first searches, which will yield some list (e.g. order) of vertices, sorted on increasing exit time.
    // Step 2. Build the transpose graph, and run a series of depth first searches on the vertices in reverse order (i.e., in decreasing order of exit times). 
    // Each depth first search will yield one strongly connected component.
    pub fn strongly_connected_components_kosaraju(&self) -> Vec<Vec<u32>> {
        let mut visited: HashSet<u32> = HashSet::new();
        let mut components:Vec<Vec<u32>> = vec![];
        let mut order:Vec<u32> = vec![]; // sorted list of vertices by exit time.
        // Step 1. 
        for vertex in self.vertices.iter() {
            if !visited.contains(vertex) {
                Self::dfs_helper(self, *vertex, &mut visited, &mut order);
            }
        }
        // Step 2.
        visited.clear();
        let transpose = Graph::transpose(self);
        for vertex in order.iter().rev() {
            if !visited.contains(vertex) {
                let mut component:Vec<u32> = vec![];
                Self::dfs_helper(&transpose, *vertex, &mut visited, &mut component);
                components.push(component);
            }
        }
        return components;
    }
}

pub struct WeightedGraph {
    vertices: HashSet<u32>,
    edges: Vec<(u32, u32, i64)>,
}

impl WeightedGraph {
    pub fn single_source_shortest_path_dijkstra(&self, source: u32) -> HashMap<u32, Vec<u32>> {
        let mut distances: HashMap<u32, u32> = HashMap::new();
        let mut predecessors: HashMap<u32, u32> = HashMap::new();
        
        // BinaryHeap is a max-heap by default. Wrapping tuples in Reverse 
        // gives us a min-heap ordered by cost (the first element of the tuple).
        let mut heap: BinaryHeap<Reverse<(u32, u32)>> = BinaryHeap::new();

        // Initialize source node
        distances.insert(source, 0);
        heap.push(Reverse((0, source)));

        while let Some(Reverse((current_cost, u))) = heap.pop() {
            // Skip processing if a shorter path to `u` has already been processed
            if let Some(&min_cost) = distances.get(&u) {
                if current_cost > min_cost {
                    continue;
                }
            }

            // Explore outgoing neighbors (assuming adjacents returns &[(u32, u32)] of (neighbor, weight))
            for v in self.adjacents(&u) {
                let next_cost = current_cost + weight;

                // Relax the edge if a strictly shorter path is found
                if next_cost < *distances.get(&v).unwrap_or(&u32::MAX) {
                    distances.insert(v, next_cost);
                    predecessors.insert(v, u);
                    heap.push(Reverse((next_cost, v)));
                }
            }
        }
        // Reconstruct full paths from source to each reachable destination
        let mut paths = HashMap::new();
        for &target in distances.keys() {
            let mut path = Vec::new();
            let mut curr = target;
            
            while let Some(&prev) = predecessors.get(&curr) {
                path.push(curr);
                curr = prev;
            }
            path.push(source);
            path.reverse();
            
            paths.insert(target, path);
        }
        paths
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_adjacents() {
        let g1 = Graph::new(&vec![1,2,3,4], &vec![(1,2), (1,3), (2,3), (2,4)]);
        let cases: Vec<(&Graph, u32, Vec<u32>)> = vec![
            (&g1, 1, vec![2, 3]),
            (&g1, 2, vec![3, 4]),
            (&g1, 3, vec![]),
            (&g1, 4, vec![]),
        ];
        for (graph, start, expected) in cases {
            let actual = graph.adjacents(&start);
            assert_eq!(expected, actual);
        }
    }
    #[test]
    fn test_bfs() {
        let g1 = Graph::new(&vec![1,2,3,4,5], &vec![(1,2), (1,3), (2,3), (2,4)]);
        let cases: Vec<(&Graph, u32, Vec<u32>)> = vec![
            (&g1, 1, vec![1, 2, 3, 4]),
            (&g1, 2, vec![2, 3, 4]),
            (&g1, 3, vec![3]),
            (&g1, 4, vec![4]),
        ];
        for (graph, start, expected) in cases {
            let actual = graph.bfs(&start);
            assert_eq!(expected, actual, "start={:}", start);
        }
    }
    #[test]
    fn test_dfs() {
        let g1 = Graph::new(&vec![1,2,3,4,5], &vec![(1,2), (1,3), (2,3), (2,4), (3,4)]);
        let cases: Vec<(&Graph, u32, Vec<u32>)> = vec![
            (&g1, 1, vec![1, 3, 4, 2]),
            (&g1, 2, vec![2, 4, 3]),
            (&g1, 3, vec![3, 4]),
            (&g1, 4, vec![4]),
        ];
        for (graph, start, expected) in cases {
            let actual = graph.dfs(&start);
            assert_eq!(expected, actual, "start={:}", start);
        }
    }
    #[test]
    fn test_topological_sort() {
        let cases: Vec<(Graph, Option<Vec<u32>>)> = vec![
            (Graph::new(&vec![0,1,2], &vec![(0,1), (1,2), (2,0)]), None),
            (Graph::new(&vec![0,1,2], &vec![(0,1), (0,2), (1,2)]), Some(vec![0, 1, 2])),
        ];
        for (graph, expected) in cases {
            let actual = graph.topological_sort();
            assert_eq!(expected, actual);
        }
    }
    #[ignore]
    #[test]
    fn test_strongly_connected_components() {
        let cases: Vec<(Graph, Vec<Vec<u32>>)> = vec![
            (Graph::new(&vec![0,1,2], &vec![(0,1), (1,2), (2,0)]), vec![vec![2,1,0]]), // Graph with cycle.
            (Graph::new(&vec![0,1,2], &vec![(0,1), (0,2), (1,2)]), vec![vec![0, 1], vec![2]]), // Graph with no cycles and no connected compoments.
            (Graph::new(&vec![0,1,2,3,4,5,6,7,8,9], &vec![(0,1), (0,7), (1,1), (1,2), (2,1), (2,5), (3,2), (3,4), (4, 9), (5,3), (5,6), (5,9), (6,2), (7,0), (7,6), (7,8), (8,6), (8,9), (9,4)]), vec![vec![0,7], vec![8], vec![4, 9], vec![1,2,3,5,6]]),
        ];
        for (graph, mut expected) in cases {
            let mut actual = graph.strongly_connected_components_kosaraju();
            assert_eq!(expected.len(), actual.len());
            expected.sort_unstable();
            actual.sort_unstable();
            for i in 0..actual.len() {
                expected[i].sort_unstable();
                actual[i].sort_unstable();
                assert_eq!(expected[i], actual[i]);
            }
        }
    }
}
