(*
Get average of all elements in binary search tree which are in range [low, high] inclusive.
Eg:
              7
            /   \
           4     8
          / \     \
         3   5     9
        /
       2

Node (7, (Node (4, (Node (3, (Node (2, Empty, Empty)), Empty)), Node (5, Empty, Empty))), (Node (8, Empty, Node (9, Empty, Empty))))

Input: [4, 6] => 4.5
*)

type 'a bst = Empty | Node of 'a * 'a bst * 'a bst

(* val avg : int -> int -> int bst -> int * int *)
let avg low high t =
  let rec avg_aux low high t =
    match t with
    | Empty -> (0, 0)
    | Node (v, left, right) ->
        if v >= low && v <= high then
          let ls, lc = avg_aux low high left in
          let rs, rc = avg_aux low high right in
          (v + ls + rs, 1 + lc + rc)
        else if v < low then
          avg_aux low high right
        else (* if v > high *)
          avg_aux low high left
  in let sum, count = avg_aux low high t
  in
    if count = 0 then 0.
    else (float_of_int sum) /. (float_of_int count)
