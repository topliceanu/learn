(* See: https://exercism.org/tracks/rust/exercises/series *)

(* take builds a list of the first n elements from xs. If there aren't enough elements it returns false. *)
(* val take: int -> 'a list -> ('a list * bool) *)
let rec take n l = match (n, l) with
| 0, _ -> ([], true)
| _, [] -> ([], false)
| _, hd :: tl -> 
  let (so_far, success) = take (n-1) tl in
  if success then (hd :: so_far, true)
  else ([], false)

let rec series n = function
| [] -> let (res, _) = take n [] in res
| x :: xs as l -> 
  let (res, success) = (take n l) in
  if success then res :: (series n xs)
  else []

(* See: https://exercism.org/tracks/rust/exercises/sublist *) 

let sublist first second = 
  let rec is_equal xs ys = 
    match (xs, ys) with
    | [], [] -> true
    | _::_, [] | [], _::_ -> false
    | x::xs, y::ys -> x == y && is_equal xs ys
  in let rec is_prefix xs ys =
    match (xs, ys) with 
    | [], [] | _::_, [] -> true
    | [], _::_ -> false
    | x::xs, y::ys -> x == y && is_prefix xs ys
  in let rec is_sublist xs ys = 
    match xs with 
    | [] -> false
    | _::rest -> (is_prefix xs ys) || (is_sublist rest ys)
  in (is_equal first second) || (is_sublist first second) || (is_sublist second first)
