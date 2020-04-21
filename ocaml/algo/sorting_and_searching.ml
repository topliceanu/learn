(* val merge : 'a list -> 'a list -> 'a list
 * CCI book, 5th edition, problem 9.1
 **)
let rec merge l1 l2 =
  match (l1, l2) with
  | ([], []) -> []
  | ([], ys) -> ys
  | (xs, []) -> xs
  | (x :: xs, y :: ys) ->
      if x < y then x :: (merge xs (y :: ys))
      else y :: (merge (x :: xs) ys)

