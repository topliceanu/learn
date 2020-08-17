(* CCI Book, ed.6, ch.4, problem 10: check subtree *)
type 'a binary_tree = Empty | Node of ('a * 'a binary_tree * 'a binary_tree)

(* val is_equal : 'a binary_tree -> 'a binary_tree -> bool *)
let rec is_equal t1 t2 =
  match t1, t2 with
  | Empty, Empty -> true
  | Empty, Node _ | Node _, Empty -> false
  | (Node (v1, l1, r1)), (Node (v2, l2, r2)) ->
      if v1 <> v2 then false
      else (is_equal l1 l2) && (is_equal r1 r2)

let rec check_subtree haystack needle =
  match haystack, needle with
  | Empty, Empty -> true
  | Empty, Node _ | Node _, Empty -> false
  | (Node (v1, l1, r1)), (Node (v2, l2, r2)) ->
      if v1 = v2 && is_equal haystack needle = true then true
      else (check_subtree l1 l2) || (check_subtree r1 r2)

(* CCI Book, ed.6, ch.4, problem 11: random node in tree *)
let random_node root =
  (* val size : 'a binary_tree -> int *)
  let rec size node =
    match node with
    | Empty -> 0
    | Node(_, l, r) -> 1 + size l + size r

  (* val find : 'a binary_tree -> int -> 'a binary_tree option *)
  in let rec find node idx =
    match node with
    | Empty -> None
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

(* CCI Book, ed.6, ch.4, problem 14: random node in tree *)
let paths_with_sums root sum =
  let rec sums_from node sum =
    match node with
    | Empty -> if sum = 0 then 1 else 0
    | Node (v, l, r) -> sums_from l (sum-v) + sums_from r (sum-v)

  in let rec aux sum = function
    | Empty -> 0
    | Node (v, l, r) as n ->
        (sums_from n sum) + (aux sum l) + (aux sum r)

  in aux sum root

(* faster version to the above *)
let paths_with_sums2 root sum =

  (* build a separate tree where each node is annotated with the sum of all elements in the path to the root *)
  let add_path_sums node total =
    match node with
    | Empty -> Empty
    | Node (v, l, r) ->
        let new_total = total + v
        in Node (new_total, (add_path_sums l new_total), (add_path_sums r new_total))

  in let sum_root = add_path_sums root 0

