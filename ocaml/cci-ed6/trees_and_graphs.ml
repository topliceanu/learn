type 'a bst = Leaf | Node of ('a * 'a bst * 'a bst)

(* CCI Book, ed.6, ch.4, problem 2: minimal tree: 
* Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
*)
(* val minimal_tree : 'a list -> 'a bst *)
let minimal_tree xs = 
  let rec minimal_tree_aux xs start stop = 
    if stop - start < 0 then Leaf 
    else
      let mid = (start + stop) / 2 in 
      let x = Array.get xs, mid in 
      Node (x, (minimal_tree_aux xs start (mid-1)), (minimal_tree_aux xs (mid+1) stop))
  in minimal_tree_aux xs 0 ((Array.length xs)-1)

(* CCI Book, ed.6, ch.4, problem 3: list of depths: 
* Given a binary tree, design an algorithm which creates a linked list of all the nodes
* at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
*)
(* val list_of_depths: 'a bst -> 'a list list *)
let rec list_of_depths = function
  | Leaf -> []
  | Node (x, left, right) -> 
    let left_depths = list_of_depths left in
    let right_depths = list_of_depths right in
    [x] :: list_of_depths_merge left_depths right_depths
(* val list_of_depths_aux : 'a list list -> 'a list list -> 'a list list *)
and list_of_depths_merge ls rs = 
  match (ls, rs) with 
  | ([], []) -> []
  | ([], r::_) -> rs
  | (l::_, []) -> ls
  | (l::ls, r::rs) -> (List.append l r) :: list_of_depths_merge ls rs

(* CCI Book, 3d.6, ch.4, problem 5: validate bst *)  
(* Implement a function to check if a binary tree is a binary search tree.*)
(* First solution traverses the tree in-order and checks whether the resulting list is sorted. *)
let validate_bst t = 
  (* val in_order_aux: 'a bst -> 'a list *)
  let rec in_order_aux = function
    | Leaf -> []
    | Node (x, left, right) -> 
      (in_order_aux left) @ [x] @ (in_order_aux right)
  in let rec is_sorted_aux = function 
    | [] | _ :: [] -> true
    | x :: (y :: _) as xs -> x < y && is_sorted_aux xs
  in let xs = in_order_aux t in
  is_sorted_aux xs

(* Second solution checks the BST invariant: every non-root node is between it's parent and grandparent *)
let rec validate_bst' t =
  let rec aux low high = function
    | Leaf -> true
    | Node (x, left, right) -> low <= x && x <= high && (aux low x left) && (aux x high right)
  (* val low : 'a bst -> 'a option *)
  in let rec low = function
    | Leaf -> None
    | Node (x, Leaf, _) -> Some x
    | Node (_, left, _) -> low left
  (* val high : 'a bst -> 'a option *)
  in let rec high = function
    | Leaf -> None
    | Node (x, _, Leaf) -> Some x
    | Node (_, _, right) -> low right
  in match t with
    | Leaf -> true
    | Node _ -> aux (Option.get (low t)) (Option.get (high t)) t

(* CCI Book, ed.6, ch.4, problem 6: successor *)
(* Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
* binary search tree. You may assume that each node has a link to its parent. 
*)
(* val next : 'a -> 'a bstwp -> 'a option *)
let next x t = 
  (* val aux -> 'a option -> 'a bst -> 'a option *)
  let rec next_aux best = function
    | Leaf -> best
    | Node (y, left, right) -> 
      if y <= x then next_aux best right
      else next_aux (Some y) left (* y is larger than x so it's a good candidate. *)
  in next_aux None t  

(* val pred : 'a -> 'a bstwp -> 'a option *)
let pred x t =  
  let rec pred_aux best = function
    | Leaf -> best
    | Node (y, left, right) ->
      if y >= x then pred_aux best left
      else pred_aux (Some y) right
  in pred_aux None t

(* CCI Book, ed.6, ch.4, problem 9: BST sequences *)
(* BST Sequences: A binary search tree was created by traversing through an array from left to right and inserting each element. 
* Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.
*)  
let rec bst_sequences t =
  (* Merge two lists of lists into a single list. If one of the inputs is larger, it simply concatenates as is.*)
  (* val merge: ('a list list, 'a list list) -> 'a list list *)
  let rec merge = function
    | [], [] -> []
    | xs, [] -> xs
    | [], ys -> ys
    | x::xs, y::ys -> [x@y] @ merge (xs, ys)
  (* Traverses a tree, collecting the values of each level in a list *)
  (* val levels : 'a bst -> 'a list list *)
  in let rec levels = function 
    | Leaf -> []
    | Node (v, l, r) -> 
        let ls = levels l in
        let rs = levels r in 
          [v] :: merge (ls, rs)
  (* Builds a set of lists, one for each position where x can be in the input list*)
  (* interleave : 'a -> 'a list -> 'a list list *)
  in let rec interleave x = function  
    | [] -> [[x]]
    | y :: ys as l -> 
      let is = interleave x ys
      in let rest = List.map (fun r -> y :: r) is
      in (x :: l) :: rest
  (* computes permutations of a given array*)
  (* val perms : 'a list -> 'a list list *)
  in let rec perms = function
    | [] -> []
    | x :: xs -> 
      List.concat_map (interleave x) (perms xs)
  in let ls = levels t in
  let pss = List.map (fun l -> perms l) ls in
  List.fold_left (fun acc ps -> 
    List.concat (List.map (fun a -> List.map (fun p -> a @ p) ps) acc)
  ) [[]] pss

(* CCI Book, ed.6, ch.4, problem 10: check subtree *)
(* T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an algorithm to determine if T2 is a subtree of T1.
* A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2, that is, if you cut off the tree at node n, the two trees would be identical. 
*)
let rec check_subtree haystack needle =
  (* Traverse the haystack to identify a node that matches the needle's root. When that's identified, check the haystack subtree and the needle for identity.*)
  match haystack, needle with
  | Leaf, Leaf -> true
  | Leaf, Node _ | Node _, Leaf -> false
  | (Node (x, l, r)), (Node (y, _, _)) ->
      if x = y && is_equal haystack needle = true then true
      else (check_subtree l needle) || (check_subtree r needle)
(* val is_equal : 'a binary_tree -> 'a binary_tree -> bool *)
(* Two trees are equal if their structure and the stored values are equal. *)
 and is_equal t1 t2 =
    match t1, t2 with
    | Leaf, Leaf -> true
    | Leaf, Node _ | Node _, Leaf -> false
    | (Node (v1, l1, r1)), (Node (v2, l2, r2)) ->
        if v1 <> v2 then false
        else (is_equal l1 l2) && (is_equal r1 r2)

(* CCI Book, ed.6, ch.4, problem 11: random node in tree *)
(* Idea: count the total number of nodes in the tree, generate a random number [0, size) and use the "rank" routine to fetch the random node.*)
let random_node root =
  (* val size : 'a binary_tree -> int *)
  let rec size node =
    match node with
    | Leaf -> 0
    | Node(_, l, r) -> 1 + size l + size r

  (* val find : 'a binary_tree -> int -> 'a binary_tree option *)
  in let rec find node idx =
    match node with
    | Leaf -> None
    | Node (_, l, r) ->
        let lsize = size l in
        if lsize = idx then Some node
        else if lsize > idx then find r (idx - lsize - 1)
        else find l idx

  in let num_nodes = size root
  in let idx = Random.int num_nodes
  in
    (match find root idx with
      | None -> raise Not_found
      | Some node -> node)

(* CCI Book, ed.6, ch.4, problem 12: Paths with sum *)
(*  You are given a binary tree in which each node contains an integer value (which might be positive or negative). 
* Design an algorithm to count the number of paths that sum to a given value. 
* The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
*)
let rec paths_with_sums sum = function
(* Traverses the tree and starts a count from each node *)
  | Leaf -> aux sum Leaf
  | Node (v, l, r) as n -> (aux sum n) + (aux sum l) + (aux sum r)
and aux sum = function
(* Counts the number of path down from node that add up to sum. *)
  | Leaf -> if sum == 0 then 1 else 0
  | Node (v, l, r) ->
      if v > sum then 0 
      else if v == sum then 1
      else (aux (sum-v) l) + (aux (sum-v) r)

(* undirected or directed graph *)
type 'a graph = {
  vertices: 'a list;
  edges: ('a * 'a) list;
}

(* val dfs : 'a graph -> 'a -> 'a list *)
(* FIXME *)
let dfs { vertices; edges } src =
  (* adjacent : 'a -> ('a * 'a) list -> 'a list *)
  let rec adjacent vertex = function
    | [] -> []
    | (hd, tl) :: rest ->
        if vertex == hd then tl :: adjacent vertex rest
        else if vertex == tl then hd :: adjacent vertex rest
        else adjacent vertex rest

  (* val rdfs : 'a list -> ('a * 'a) list -> 'a -> 'a list *)
  in let rec rdfs visited edges vertex =
    if (List.mem vertex visited) then visited
    else
      List.fold_left
        (fun visited adjacent_vertex -> rdfs visited edges adjacent_vertex )
        (vertex :: visited)
        (adjacent vertex edges)

  in rdfs [] edges src

(* let g = { vertices=[1; 2; 3; 4; 5]; edges=[(1, 2); (1, 3); (2, 3); (4, 5)] } ;; *)
