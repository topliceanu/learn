(* Binary Trees *)

type 'a bst =
  | Leaf
  | Node of 'a * 'a bst * 'a bst

(* 55. Construct completely balanced binary trees. (medium)
 * Write a function cbal_tree to construct completely balanced binary trees for
 * a given number of nodes. The function should generate all solutions via backtracking.
 * Put the letter 'x' as information into all nodes of the tree.
 *
 * val cbal_tree : int -> char binary_tree
 **)


(* val cbal_tree : int -> 'a binary_tree list *)
let rec cbal_tree n =
  if n = 0 then []
  else if n = 1 then [ Node ('x', Leaf, Leaf) ]
  else if n = 2 then [
    Node ('x', Node ('x', Leaf, Leaf), Leaf);
    Node ('x', Leaf, Node ('x', Leaf, Leaf))
  ]
  else if n mod 2 = 1 then
    let n1, n2 = (n-1) / 2, (n-1) / 2
    in combine_aux n1 n2
  else
    let n1, n2, n3, n4 = (n-1) / 2, n / 2, n / 2, (n-1) / 2
    in List.append (combine_aux n1 n2) (combine_aux n3 n4)

(* val combine_aux : int -> int -> 'a binary_tree list *)
and combine_aux n1 n2 =
  let left = cbal_tree n1
  in let right = cbal_tree n2
  in let prod = cartesian_prod left right
  in List.map (fun (l, r) -> Node ('x', l, r)) prod

(* val cartesian_prod : 'a list -> 'b list -> ('a * 'b) list *)
and cartesian_prod xs ys =
  List.concat (List.map (fun x -> List.map (fun y -> (x, y)) ys) xs)

let cbal_tree_theirs n =
  let add_trees_with left right all =
    let add_right_tree all l =
      List.fold_left (fun acc r -> Node ('x', l, r) :: acc) all right
    in List.fold_left add_right_tree all left

  in let rec cbal_tree_aux n =
    if n = 0 then [ Leaf ]
    else if n mod 2 = 1 then
      let l = cbal_tree_aux (n / 2)
      in add_trees_with l l []
    else (* n mod 2 = 0 *)
      let l1 = cbal_tree_aux (n / 2 - 1)
      in let l2 = cbal_tree_aux (n / 2)
      in let reverse = add_trees_with l2 l1 []
      in add_trees_with l1 l2 reverse

  in cbal_tree_aux n

(* 56. Symmetric binary trees. (medium)
 * Let us call a binary tree symmetric if you can draw a vertical line through the root node and then the right subtree is the mirror image of the left subtree. 
 * Write a function is_symmetric to check whether a given binary tree is symmetric.
 *
 * val is_symmetric : 'a binary_tree -> bool = <fun>
 **)
let is_symmetric tr =
  let rec is_symmetric_aux t1 t2 =
    match (t1, t2) with
    | (Leaf, Leaf) -> true
    | (Leaf, Node _) | (Node _, Leaf) -> false
    | (Node (_, ll, lr), Node (_, rl, rr)) ->
        let lsym = is_symmetric_aux ll rr in
        let rsym = is_symmetric_aux lr rl in
        lsym && rsym
  in match tr with
  | Leaf -> true
  | Node (_, l, r) -> is_symmetric_aux l r


(* 57. Binary search trees (dictionaries). (medium)
 * Construct a binary search tree from a list of integer numbers.
 *
 * val construct : 'a list -> 'a binary_tree
 **)
let construct xs =
  (* val add : 'a binary_tree -> 'a -> 'a binary_tree *)
  let rec add tr x =
    match tr with
    | Leaf -> Node (x, Leaf, Leaf)
    | Node (y, left, right) ->
        if x > y then
          let new_right = add right x
          in Node (y, left, new_right)
        else
          let new_left = add left x
          in Node (y, new_left, right)

  in let rec aux tr = function
    | [] -> tr
    | x :: xs -> aux (add tr x) xs

  in aux Leaf xs

(* the solution from the website: https://ocaml.org/exercises#63 *)  
let construct' xs =
  let rec insert x = function
    | Leaf -> Node (x, Leaf, Leaf)
    | Node (y, left, right) as node -> 
        if x > y then Node (y, insert x left, right)
        else if x < y then Node (y, left, insert x right)
        else node
  in let rec insert_all tree = function 
    | [] -> tree
    | x :: xs -> insert_all (insert x tree) xs
  in insert_all Leaf xs

(* 58. Generate-and-test paradigm. (medium)
 * Apply the generate-and-test paradigm to construct all symmetric, completely balanced binary trees with a given number of nodes.
 **)
(* val syn_cbal_trees : int -> 'a binary_tree list *)
let sym_cbal_trees n =
  List.filter is_symmetric (cbal_tree n)

(* 59. Construct height-balanced binary trees. (medium)
 * In a height-balanced binary tree, the following property holds for every node:
 * The height of its left subtree and the height of its right subtree are almost
 * equal, which means their difference is not greater than one.
 * Write a function hbal_tree to construct height-balanced binary trees for a
 * given height. The function should generate all solutions via backtracking.
 * Put the letter 'x' as information into all nodes of the tree.
 **)
(* val hbal_tree : int -> 'a binary_tree list *)
let hbal_tree n =

  (* val add_trees_with : 'a binary_tree list -> 'a binary_tree list -> 'a binary_tree list -> 'a binary_tree list *)
  let add_trees_with left right all =
    let add_right_tree all l =
      List.fold_left (fun a r -> Node ('x', l, r) :: a) all right in
    List.fold_left add_right_tree all left

  (* val hbal_tree_aux : int -> 'a binary_tree list *)
  in let rec hbal_tree_aux n =
    if n = 0 then [ Leaf ]
    else if n = 1 then [ Node ('x', Leaf, Leaf) ]
    else
      let t1 = hbal_tree_aux (n - 1) in
      let t2 = hbal_tree_aux (n - 2) in
      add_trees_with t1 t2 (add_trees_with t2 t1 [])

  in hbal_tree_aux n

(* 60. Construct height-balanced binary trees with a given number of nodes. (medium) *)
(* 60.a. What is the minimum number min_nodes? This question is more difficult.
 * Try to find a recursive statement and turn it into a function min_nodes defined
 * as follows: min_nodes h returns the minimum number of nodes in a height-balanced
 * binary tree of height h.
 *
 * Pick up from https://ocaml.org/exercises#60
 **)

