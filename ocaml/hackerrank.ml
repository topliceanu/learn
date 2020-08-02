(* read from stdin *)
(*
let rec read_lines () =
  try let line = read_line () in
    int_of_string (line) :: read_lines()
  with
    End_of_file -> []
*)

(* write to stdout *)
(*
let () =
  let n::arr = read_lines() in
  let ans = f n arr in
  List.iter (fun x -> print_int x; print_newline ()) ans;;
*)

(* Simple *)

(* 1. https://www.hackerrank.com/challenges/fp-list-replication/problem *)
let replicate_list n l =
  let rec times x n acc =
    if n = 0 then acc
    else x :: times x (n-1) acc
  in let rec aux n = function
    | [] -> []
    | x :: xs -> times x n (aux n xs)
  in aux n l

let replicate_list_2 n l =
  let rec repeat n acc x =
    if n = 0 then acc
    else repeat (n-1) (x :: acc) x
  in List.rev (List.fold_left (repeat n) [] l)

(* 2. https://www.hackerrank.com/challenges/fp-filter-array/problem
 * let filter : int list -> int -> int list
 **)
let rec filter n = function
  | [] ->  []
  | x :: xs -> if x < n then x :: filter n xs else filter n xs

(* 3. https://www.hackerrank.com/challenges/fp-filter-positions-in-a-list/problem *)
let filter_odd_poss l =
  let rec aux idx = function
    | [] -> []
    | x :: xs ->
        if idx mod 2 = 1 then aux (idx+1) xs
        else x :: aux (idx+1) xs
  in aux 0 l

(* 4. https://www.hackerrank.com/challenges/fp-array-of-n-elements/problem *)
let rec make_array n =
  if n = 0 then []
  else n :: make_array (n-1)

(* 5. https://www.hackerrank.com/challenges/fp-reverse-a-list/problem *)
let reverse l =
  let rec aux acc = function
    | [] -> acc
    | x :: xs -> aux (x :: acc) xs
  in aux [] l

(* 6. https://www.hackerrank.com/challenges/fp-sum-of-odd-elements/problem *)
let rec sum_of_odd = function
  | [] -> 0
  | x :: xs ->
      if x mod 2 = 1 || x mod 2 = -1 then x + sum_of_odd xs
      else sum_of_odd xs

(* 7. https://www.hackerrank.com/challenges/fp-list-length/problem *)
let rec length = function
  | [] -> 0
  | _ :: xs -> 1 + length xs

(* 8. https://www.hackerrank.com/challenges/fp-update-list/problem *)
let rec abs_list = function
  | [] -> []
  | x :: xs ->
      if x < 0 then (-x) :: abs_list xs
      else x :: abs_list xs

(* 9. https://www.hackerrank.com/challenges/eval-ex/problem *)
let e_pow_x x =
  let rec aux x n sum prev =
    if n = 10 then sum
    else aux x (n+1) (sum +. prev) (prev *. x /. float_of_int(n+1))
  in aux x 0 0. 1.

(* 10. https://www.hackerrank.com/challenges/area-under-curves-and-volume-of-revolving-a-curv/problem TODO *)

(* 11. https://www.hackerrank.com/challenges/functions-or-not/problem *)
let func_or_not pairs =
  let values = List.map (fun p -> snd p) pairs in
  let unique_sorted = List.sort_uniq compare values in
  (List.length values) = (List.length unique_sorted)
