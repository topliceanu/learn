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
