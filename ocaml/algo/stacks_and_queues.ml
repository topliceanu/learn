type 'a stack =
  | Empty
  | Cons of 'a * 'a stack

(* val push : 'a -> 'a stack -> 'a stack *)
let push a = function
  | Empty -> Cons (a, Empty)
  | Cons (_, _) as st -> Cons (a, st)

(* val pop : 'a stack -> 'a option * 'a stack *)
let pop = function
  | Empty -> (None, Empty)
  | Cons (a, rest) -> (Some a, rest)

(* val peek : 'a stack -> 'a option *)
let peek = function
  | Empty -> None
  | Cons (a, _) -> Some a

(* val is_empty : 'a stack -> bool *)
let is_empty = function
  | Empty -> true
  | Cons (_, _) -> false

(* CCI book, 5th ed, problem 3.6
 * Complexity O(n^2) in time, O(1) in space
 **)
(* val bubble_up_min : 'a stack -> 'a stack *)
let rec bubble_up_min = function
  | Empty -> Empty
  | Cons (x, xs) ->
      match bubble_up_min xs with
      | Empty -> Cons (x, Empty)
      | Cons (y, ys) as l ->
          if x > y then Cons (y, Cons (x, ys))
          else Cons (x, l)
(* val sort_stack_asc : 'a stack -> 'a stack *)
let rec sort_stack_asc st =
  match bubble_up_min st with
  | Empty -> Empty
  | Cons (max, rest) -> Cons (max, sort_stack_asc rest)
