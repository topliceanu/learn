(* Binary Trees *)

type 'a binary_tree =
  | Empty
  | Node of 'a * 'a binary_tree * 'a binary_tree

(* 55. Construct completely balanced binary trees. (medium)
 * Write a function cbal_tree to construct completely balanced binary trees for
 * a given number of nodes. The function should generate all solutions via backtracking.
 * Put the letter 'x' as information into all nodes of the tree.
 *
 * val cbal_tree : int -> char binary_tree
 **)

(* val cartesian_prod : 'a list -> 'b list -> ('a * 'b) list *)
let cartesian_prod xs ys =
  List.concat (List.map (fun x -> List.map (fun y -> (x, y)) ys) xs)

(* val cbal_tree : int -> 'a binary_tree list *)
let rec cbal_tree n =
  if n = 0 then []
  else if n = 1 then [ Node ('x', Empty, Empty) ]
  else if n = 2 then [
    Node ('x', Node ('x', Empty, Empty), Empty);
    Node ('x', Empty, Node ('x', Empty, Empty))
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

let cbal_tree_theirs n =
  let add_trees_with left right all =
    let add_right_tree all l =
      List.fold_left (fun acc r -> Node ('x', l, r) :: acc) all right
    in List.fold_left add_right_tree all left

  in let rec cbal_tree_aux n =
    if n = 0 then [ Empty ]
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
 * Write a function is_symmetric to check whether a given binary tree is symmetric.
 *
 * is_symmetric : 'a binary_tree -> bool
 **)
let is_symmetric tr =
  let rec is_symmetric_aux t1 t2 =
    match (t1, t2) with
    | (Empty, Empty) -> true
    | (Empty, Node _) | (Node _, Empty) -> false
    | (Node (_, ll, lr), Node (_, rl, rr)) ->
        let lsym = is_symmetric_aux ll rr in
        let rsym = is_symmetric_aux lr rl in
        lsym && rsym
  in match tr with
  | Empty -> true
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
    | Empty -> Node (x, Empty, Empty)
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

  in aux Empty xs

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
  (* val combine : 'a binary_tree list -> 'a binary_tree list -> 'a binary_tree list *)
  let combine lefts rights =
    List.flatten (List.map (fun l -> List.map (fun r -> Node ('x', l, r)) rights) lefts)

  (* val hbal_tree_aux : int -> 'a binary_tree list *)
  in let rec hbal_tree_aux n =
    if n = 0 then [ Empty ]
    else if n = 1 then [ Node ('x', Empty, Empty) ]
    else
      let n1 = hbal_tree_aux (n - 1) in
      let n2 = hbal_tree_aux (n - 2) in
      List.concat [
        (combine n1 n1);
        (combine n1 n2);
        (combine n2 n1)
      ]

  in hbal_tree_aux n

(* 60. Construct height-balanced binary trees with a given number of nodes. (medium) *)
(* 60.a. What is the minimum number min_nodes? This question is more difficult.
 * Try to find a recursive statement and turn it into a function min_nodes defined
 * as follows: min_nodes h returns the minimum number of nodes in a height-balanced
 * binary tree of height h.
 **)
let max_nodes h =
  1 lsl h - 1

let min_nodes h =
  if h = 0 then 0
  else if h = 1 then 1
  else min_nodes (h-1) + min_nodes (h-2) + 1

(* 60.b. What are the minimum (resp. maximum) height H a height-balanced binary
 * tree with N nodes can have?
 **)
let min_height n =

let max_height n =
