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
let sym_cbal_trees n =
  List.filter is_symmetric t (cbal_tree n)

(* 59.
