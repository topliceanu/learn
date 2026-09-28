(* CCI-book, ed.6, ch.1, pr. 1: is unique:
 * Implement an algorithm to determine if a string has all unique characters. 
 * What if you cannot use additional data structures? 
 *)
(* val is_unique: string -> bool *)
let is_unique str = 
  let rec count_c c = function 
    | [] -> (0, [])
    | x :: xs as xss -> 
      if c == x then 
        let cnt, rest = count_c c xs 
        in (1 + cnt, rest)
      else (0, xss)
  (* val is_unique : char list -> bool *)
  in let rec is_unique_aux len_is_odd = function
    | [] -> true
    | c :: cs -> 
      let (nc, rest) = count_c c cs in
      let is_even = (nc+1) mod 2 == 0 in
      if is_even || (len_is_odd && not is_even) then is_unique_aux false rest
      else false
  in let cs = List.init (String.length str) (String.get str) 
  in let cs = List.sort (fun c1 c2 -> if c1 > c2 then 1 else if c1 < c2 then -1 else 0) cs 
  in is_unique_aux ((List.length cs) mod 2 == 1) cs


(* CCI-book, ed.6, ch.1, pr.2: check permutation 
 * Given two strings, write a method to decide if one is a permutation of the other.
 *)
(* val is_perm : String -> String -> bool *)
let is_perm s1 s2 =
  let as_list s = List.init (String.length s) (String.get s) in
  let sort_c c1 c2 = if c1 > c2 then 1 else if c2 > c1 then -1 else 0 in
  let sl1 = List.sort sort_c (as_list s1) in
  let sl2 = List.sort sort_c (as_list s2) in
  List.fold_left2 (fun acc c1 c2 -> acc && c1 == c2) true sl1 sl2 

(* CCI-book, ed. 6, ch. 1, pr.5: One Away
* There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. 
* Given two strings, write a function to check if they are one edit (or zero edits) away.*)
let one_away s1 s2 =
  let min a b c = 
    let m = if a < b then a else b
    in if m < c then m else c
  in let rec min_steps = function 
  | [], [] -> 0
  | [], _::_ -> List.length s2 (* Insert all the characters from s2 into s1. *)
  | _::_, [] -> List.length s1 (* Remove all the characters from s1 to equal s2. *)
  | (x::xs, y::ys) ->
    if x == y then min_steps (xs, ys)
    else min
      (1 + min_steps (xs, ys)) (* Replace x with y in s1. *)
      (1 + min_steps (xs, s2)) (* Remove x from s1 *)
      (1 + min_steps (s1, ys)) (* Insert y from s2 in s1 at the head.*)
  in min_steps (s1, s2) == 1

(* Prev impl is more elegant but doesn't use the fact that we only need 2 operations to return false. *)
let rec one_away' s1 s2 =
  match (s1, s2) with 
  | [], [] -> true (* Same length. *)
  | _::[], [] | [], _::[] -> true (* Difference of one. *)
  | _::_, [] | [], _::_ -> false (* Difference of more than one *) 
  | x::xs, y::ys ->
    if x == y then one_away' xs ys
    else (xs == ys) || (xs == s2) || (s1 == ys)

(* CCI-book, ed. 6, ch. 1, pr. 6: String compression 
 * Implement a method to perform basic string compression using the counts of repeated characters. 
 * For example, the string aabcccccaaa would become a2blc5a3, 
 * If the "compressed" string would not become smaller than the original string, your method should return the original string. 
 * You can assume the string has only uppercase and lowercase letters (a - z).
 *) 
let rec str_compress = function
  | [] -> []
  | x::xs as l -> 
    let (count, rest) = consume x xs 
    in (x, count+1) :: str_compress rest
and consume x = function 
  | [] -> (0, [])
  | y::ys as l -> 
      if x != y then (0, l)
      else let (count, rest) = consume x ys
      in (count+1, rest)

(* CCI-book, ed. 6, ch. 1. pr. 7: Rotate matrix 
* Given an image represented by an NxN matrix, where each pixel in the image is 4
* bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
*)
let rotate matrix = true

(* CCI-book, ed.6, ch.1 pr.8: Zero Matrix
 * Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
 *)
let zero_matrix mat =

  (* 'a list list -> ('a list * 'a list list) *)
  let rec heads = function 
  | [] -> ([], [])
  | row :: rows ->  
    match row with 
    | [] ->  ([], [])
    | x :: xs -> 
      let (hds, tls) = heads rows
      in (x :: hds, xs :: tls)

  (* 'a list list -> 'a list list *)
  in let rec transpose mat =
    let (heads, tails) = heads mat in heads :: (transpose tails)

  (* 'a list -> bool *)
  in let rec has_zeros = function
  | [] -> false
  | x :: xs -> if x == 0 then true else has_zeros xs

  (* 'a list list -> bool list *)
  in let rec has_rows_with_zeros = function 
  | [] -> []
  | row :: rows -> (has_zeros row) :: has_rows_with_zeros rows

  (* 'a list -> bool list -> 'a list *)
  in let rec update_row row flags = 
    match row, flags with
    | [], [] | [], _ | _, [] -> [] 
    | x::xs, flag::rest ->
      (if flag == true then 0 else x) :: (update_row row rest)

  (* bool list -> 'a list list -> 'a list list*)
  in let rec update_matrix flags = function
  | [] -> []
  | row :: rows -> (update_row row flags) :: (update_matrix flags rows)

  in let zero_rows = has_rows_with_zeros mat in
  let zero_cols = has_rows_with_zeros (transpose mat) in
  transpose (update_matrix zero_cols (transpose (update_matrix zero_rows mat)))


