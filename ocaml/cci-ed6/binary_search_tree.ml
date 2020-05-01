open Printf

(* binary search tree*)
type 'a tree =
  | Leaf
  | Node of 'a tree * 'a * 'a tree

(* val insert : 'a -> 'a tree *)
let rec insert a = function
  | Leaf -> Node (Leaf, a, Leaf)
  | Node (left, b, right) ->
      if a > b then Node (left, b, (insert a right))
      else Node ((insert a left), b, right)

(* val print_tree : int tree -> unit *)
let print_tree t =
  (* val print_tree_prefix : string -> int tree -> unit *)
  let rec print_tree_prefix prefix = function
    | Leaf -> Printf.printf "%s├──X\n" prefix
    | Node (left, x, right) ->
        Printf.printf "%s├──%d\n" prefix x;
        print_tree_prefix (prefix ^ "├──") left;
        print_tree_prefix (prefix ^ "├──") right
  in print_tree_prefix "" t

(* val print_node: 'a tree option -> 'a option *)
let print_node = function
  | None -> None
  | Some t ->
      match t with
      | Leaf -> None
      | Node (_, x, _) -> Some x

(* val rec : 'a list -> 'a tree *)
let make l =
  (* val aux : 'a tree -> 'a list -> 'a tree *)
  let rec aux t = function
    | [] -> t
    | x :: xs -> aux (insert x t) xs
  in aux Leaf l

(* val lookup : 'a -> 'a tree -> bool *)
let rec lookup a = function
  | Leaf -> false
  | Node (left, b, right) ->
      if a = b then true
      else if a < b then lookup a left
      else lookup a right

(* val get_min : 'a tree -> 'a option *)
let rec get_min = function
  | Leaf -> None
  | Node (left, a, _) ->
      match left with
      | Leaf -> Some a
      | Node (_, _, _) -> get_min left

(* val get_max : 'a tree -> 'a option *)
let rec get_max = function
  | Leaf -> None
  | Node (_, a, right) ->
      match right with
      | Leaf -> Some a
      | Node (_, _, _) -> get_max right

(* val size : `a tree -> int
 * Returns the number of nodes in the given tree, including the root.
 **)
let rec size = function
  | Leaf -> 0
  | Node (left, _, right) -> 1 + (size left) + (size right)

(* val rank : 'a -> 'a tree -> int option
 * What is the rank of a value in a given tree.
 * Time complexity: O(n)
 * *)
let rank a t =
  let rec count_smaller a = function
    | Leaf -> 0
    | Node (left, x, right) ->
        (if x < a then 1 else 0) +
        (count_smaller a left) +
        (count_smaller a right)
  in let num_smaller = count_smaller a t
  in let size_t = size t
  in
    if num_smaller < size_t then Some (num_smaller + 1)
    else None

(* val select : int -> 'a tree -> 'a option
 * What is the node corresponding to the given rank.
 * *)
let rec select n = function
  | Leaf -> None
  | Node (left, a, right) as current->
    let left_size = size(left) in
      if left_size = n then Some current
      else if left_size > n then select n left
      else select (n - left_size - 1) right

(* val path : 'a -> 'a tree -> 'a list option
 * TODO: What if the node does not exist in the tree?
 * *)
let rec path x = function
  | Leaf -> None
  | Node (left, y, right) ->
      if x = y then Some [x]
      else if x < y then
        match path x left with
        | None -> None
        | Some l -> Some (y :: l)
      else
        match path x right with
        | None -> None
        | Some l -> Some (y :: l)

(* val depth : 'a tree -> int *)
let rec depth = function
  | Leaf -> 0
  | Node (left, _, right) -> 1 + max (depth left) (depth right)

(* val height : 'a tree -> int
 * Returns the lenght of the longest path to a Leaf from the current node.
 **)
let rec height = function
  | Leaf -> 0
  | Node (left, _, right) ->
      let left_height = height left in
      let right_height = height right in
      1 + max left_height right_height

(* val diameter: 'a tree -> int
 * The diameter of a tree is the lenght of the longest path between any two nodes.
 **)
let rec diameter = function
  | Leaf -> 0
  | Node (left, _, right) ->
      let left_diameter = diameter left in
      let right_diameter = diameter right in
      let left_height = height left in
      let right_height = height right in
        max (max left_diameter right_diameter) (left_height + right_height + 1)

(* val merge: 'a tree -> 'a tree -> 'a tree *)
let rec merge t1 t2 =
  match t1 with
  | Leaf -> t2
  | Node (left, x, right) ->
      let left_and_t2 = merge left t2 in
      let right_and_left_and_t2 = merge right left_and_t2 in
        insert x right_and_left_and_t2

(* val is_ballanced : 'a tree -> bool
 * CCI book, 5th edition, problem 4.1
 **)
let is_ballanced t =
  let rec get_min_max_height = function
    | Leaf -> (0, 0)
    | Node (left, x, right) ->
        let (min_left, max_left) = get_min_max_height left in
        let (min_right, max_right) = get_min_max_height right in
        (1 + (min min_left min_right), 1 + (max max_left max_right))
  in
    let (min_height, max_height) = get_min_max_height t
    in
      if max_height <= (min_height + 1) then true
      else false
