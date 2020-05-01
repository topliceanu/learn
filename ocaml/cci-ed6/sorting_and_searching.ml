(* val merge : 'a list -> 'a list -> 'a list
 * CCI book, 5th edition, problem 11.1:
 * You are given two sorted arrays, A and B, where A has a large enough buffer
 * at the end to hold B. Write a method to merge B and A in sorted order.
 **)
let rec merge l1 l2 =
  match (l1, l2) with
  | ([], []) -> []
  | ([], ys) -> ys
  | (xs, []) -> xs
  | (x :: xs, y :: ys) ->
      if x < y then x :: (merge xs (y :: ys))
      else y :: (merge (x :: xs) ys)
