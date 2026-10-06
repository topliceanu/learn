use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap, HashSet, VecDeque};

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
            if !vertices.contains(&start) {
                vertices.insert(*start);
            }
            if !vertices.contains(&end) {
                vertices.insert(*end);
            }
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
            if start == vertex {
                out.push(*end);
            }
        }
        out.sort_unstable();
        return out;
    }
    pub fn bfs(&self, start: &u32) -> Vec<u32> {
        if !self.vertices.contains(&start) {
            return vec![];
        }

        let mut queue: VecDeque<u32> = VecDeque::new();
        let mut visited: HashSet<u32> = HashSet::new();
        let mut output: Vec<u32> = vec![];

        queue.push_back(*start);
        while let Some(current) = queue.pop_front() {
            if visited.contains(&current) {
                continue;
            }
            visited.insert(current);
            output.push(current);
            for adj in self.adjacents(&current) {
                queue.push_back(adj);
            }
        }
        return output;
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
                continue;
            }
            visited.insert(current);
            output.push(current);
            for adj in self.adjacents(&current) {
                stack.push(adj);
            }
        }
        return output;
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
            return None;
        }
        return Some(output);
    }

    fn dfs_helper(g: &Graph, vertex: u32, visited: &mut HashSet<u32>, order: &mut Vec<u32>) {
        let mut stack: Vec<u32> = vec![vertex];
        while let Some(vertex) = stack.pop() {
            if visited.contains(&vertex) {
                continue;
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
        let mut components: Vec<Vec<u32>> = vec![];
        let mut order: Vec<u32> = vec![]; // sorted list of vertices by exit time.
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
                let mut component: Vec<u32> = vec![];
                Self::dfs_helper(&transpose, *vertex, &mut visited, &mut component);
                components.push(component);
            }
        }
        return components;
    }
}

pub struct WeightedGraph {
    vertices: HashSet<u32>,
    adjacency: HashMap<u32, HashMap<u32, i64>>,
}

struct FrontierMinHeap {
    heap: Vec<(u32, i64)>,
    indices: HashMap<u32, usize>, // Maintains the position of each vertex u32 in the heap.
}

impl FrontierMinHeap {
    fn heapify(input: &[(u32, i64)]) -> Self {
        let mut heap: Vec<(u32, i64)> = input.iter().map(|(v, c)| (*v, *c)).collect();
        let mut indices: HashMap<u32, usize> = heap.iter().enumerate().fold(HashMap::new(), |mut indices, (idx, (v, _))| {
            indices.insert(*v, idx);
            indices
        });
        let n = heap.len();
        let mut frontier = FrontierMinHeap{ heap, indices };
        for i in (0..n).rev() {
            frontier.bubble_up(i);
        }
        frontier
    }
    fn bubble_up(&mut self, idx: usize) {
        let mut idx = idx;
        if idx == 0 {
            return;
        }
        loop {
            let parent_idx = (idx-1)/2;
            if parent_idx > 0 && self.heap[parent_idx] > self.heap[idx] {
                self.heap.swap(parent_idx, idx);
                idx = parent_idx;
            } else {
                break
            }
        }
    }
    fn pop(&mut self) -> Option<(u32, i64)> {
        let n = self.heap.len();
        if n == 0 {
            return None
        }
        self.heap.swap(0, n-1);
        let first = self.heap.pop();
        let last = self.heap[0];
        *self.indices.entry(last.0).or_insert(0) = 0;
        if let Some((vertex, _)) = first {
            self.indices.remove(&vertex);
        }
        self.bubble_down(0);
        return first
    }
    fn bubble_down(&mut self, idx: usize) {
        todo!()
    }
    fn remove(&mut self, vertex: u32) -> Option<(u32, i64)> {
        let &idx = self.indices.get(&vertex)?;
        let n = self.heap.len();
        if n == 0 {
            return None
        }
        self.heap.swap(idx, n-1);
        let removed = self.heap.pop();
        if let Some((vertex, _)) = removed {
            self.indices.remove(&vertex);
        }
        *self.indices.entry(self.heap[idx].0).or_insert(0) = idx;
        return removed
    }
    fn push(&mut self, vertex: u32, cost: i64) {
        let n = self.heap.len();
        self.heap.push((vertex, cost));
        *self.indices.entry(vertex).or_insert(0) = n;
        self.bubble_up(n);
    }
}

impl WeightedGraph {
    pub fn new(_vertices: &[u32], _edges: &[(u32, u32, i64)]) -> Self {
        let mut vertices: HashSet<u32> = HashSet::new();
        let mut adjacency: HashMap<u32, HashMap<u32, i64>> = HashMap::new();
        for vertex in _vertices.iter() {
            vertices.insert(*vertex);
        }
        for (start, end, weight) in _edges {
            if !vertices.contains(&start) {
                vertices.insert(*start);
            }
            if !vertices.contains(&end) {
                vertices.insert(*end);
            }
            *adjacency.entry(*start).or_default().entry(*end).or_insert(0) = *weight;
        }
        WeightedGraph { vertices, adjacency }
    }
 
    pub fn single_source_shortest_path_dijkstra(&self, source: u32) -> HashMap<u32, Vec<u32>> {
        let n = self.vertices.len();

        let mut processed: HashSet<u32> = HashSet::with_capacity(n);
        processed.insert(source);

        let mut distances: HashMap<u32, i64> = HashMap::with_capacity(n);
        let mut frontier = FrontierMinHeap::heapify(&self.vertices.iter().map(|v| (*v, i64::MIN)).collect::<Vec<(u32, i64)>>());
        //let mut frontier: BinaryHeap<Reverse<(i64, u32)>> = BinaryHeap::from_iter(
        //    self.vertices.iter().map(|v| Reverse((i64::MAX, *v)))
        //);

        let mut predecessors: HashMap<u32, u32> = HashMap::with_capacity(n);

        let mut pair = (source, 0);
        loop {
            let (vertex, distance_so_far) = pair;
            processed.insert(vertex); // mark as processed.
            distances.insert(vertex, distance_so_far);
            if processed.len() == n {
                break;
            }
            let Some(neighbours) = self.adjacency.get(&vertex) else {
                continue
            };
            for (to, distance) in neighbours.iter() {
                if processed.contains(to) {
                    continue;
                }
                // TODO: frontier.pop() needs to be replaced with frontier.remove(to) ie. remove the smallest distance to the "to" vertex.
                //let Reverse((mut min_distance, _)) = frontier.pop().unwrap();
                let (_, mut min_distance) = frontier.remove(*to).unwrap();
                if min_distance > distance + distance_so_far {
                    min_distance = distance + distance_so_far;
                    predecessors.insert(*to, vertex);
                }
                //frontier.push(Reverse((min_distance, *to)));
                frontier.push(*to, min_distance);
            }
            //let Reverse((distance, to)) = frontier.pop().unwrap();
            let (to, distance) = frontier.pop().unwrap();
            pair = (to, distance);
        }
        // Recover the paths.
        let mut paths:HashMap<u32, Vec<u32>> = HashMap::with_capacity(n);
        for vertex in self.vertices.iter() {
            let mut v: u32 = *vertex;
            let mut path: Vec<u32> = vec![];
            while let Some(pred) = predecessors.get(&v) && *pred != source {
                path.push(*pred);
                v = *pred;
            }
            path.reverse();
            paths.insert(*vertex, path);
        }
        paths
    }

    pub fn minimum_spanning_tree_prim_jarnik(&self, start: u32) -> Vec<(u32, u32, i64)> {
        todo!()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_adjacents() {
        let g1 = Graph::new(&vec![1, 2, 3, 4], &vec![(1, 2), (1, 3), (2, 3), (2, 4)]);
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
        let g1 = Graph::new(&vec![1, 2, 3, 4, 5], &vec![(1, 2), (1, 3), (2, 3), (2, 4)]);
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
        let g1 = Graph::new(
            &vec![1, 2, 3, 4, 5],
            &vec![(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)],
        );
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
            (
                Graph::new(&vec![0, 1, 2], &vec![(0, 1), (1, 2), (2, 0)]),
                None,
            ),
            (
                Graph::new(&vec![0, 1, 2], &vec![(0, 1), (0, 2), (1, 2)]),
                Some(vec![0, 1, 2]),
            ),
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
            (
                Graph::new(&vec![0, 1, 2], &vec![(0, 1), (1, 2), (2, 0)]),
                vec![vec![2, 1, 0]],
            ), // Graph with cycle.
            (
                Graph::new(&vec![0, 1, 2], &vec![(0, 1), (0, 2), (1, 2)]),
                vec![vec![0, 1], vec![2]],
            ), // Graph with no cycles and no connected compoments.
            (
                Graph::new(
                    &vec![0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                    &vec![
                        (0, 1),
                        (0, 7),
                        (1, 1),
                        (1, 2),
                        (2, 1),
                        (2, 5),
                        (3, 2),
                        (3, 4),
                        (4, 9),
                        (5, 3),
                        (5, 6),
                        (5, 9),
                        (6, 2),
                        (7, 0),
                        (7, 6),
                        (7, 8),
                        (8, 6),
                        (8, 9),
                        (9, 4),
                    ],
                ),
                vec![vec![0, 7], vec![8], vec![4, 9], vec![1, 2, 3, 5, 6]],
            ),
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

    #[test]
    #[ignore]
    fn test_dijkstra() {
        let cases: Vec<(WeightedGraph, u32, HashMap<u32, Vec<u32>>)> = vec![
            (
                WeightedGraph::new(&vec![1,2,3,4], &vec![(1,2,1), (1,3,4), (2,4,6), (3,4,3), (2,3,2)]), 
                1, 
                HashMap::from([(2, vec![]), (3, vec![2]), (4, vec![2, 3])]),
            ),
        ];
        for (graph, source, expected) in cases {
            let actual = graph.single_source_shortest_path_dijkstra(source);
            assert_eq!(expected, actual)
        }
    }
}
