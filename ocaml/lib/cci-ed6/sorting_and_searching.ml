(* CCI book, 6th edition, problem 10.1:
 * Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer
 * at the end to hold B. Write a method to merge B and A in sorted order.
 * val sorted_merge : 'a list -> 'a list -> 'a list
 **)
let rec sorted_merge l1 l2 =
  match (l1, l2) with
  | ([], []) -> []
  | ([], ys) -> ys
  | (xs, []) -> xs
  | (x :: xs, y :: ys) ->
      if x < y then x :: (sorted_merge xs (y :: ys))
      else y :: (sorted_merge (x :: xs) ys)

(* CCI book, 6th edition, problem 10.2
 * Group Anagrams: Write a method to sort an array of strings so that all the
 * anagrams are next to each other.
 * val group_anagrams : string list -> string list
 **)
let group_anagrams words =
  (* val to_list : string -> char list *)
  let rec to_list = function
    | "" -> []
    | s -> (String.get s 0) :: to_list (String.sub s 1 ((String.length s) - 1))

  (* val anagrams_cmp : char list -> char list -> bool *)
  in let rec anagrams_cmp a b =
    match (a, b) with
    | ([], []) -> 0
    | ([], _ :: _ ) -> -1
    | (_ :: _, []) -> 1
    | (x :: xs, y :: ys) ->
        if compare x y <> 0 then compare x y
        else anagrams_cmp xs ys

  in let words_with_sorted = List.map (fun w -> (w, (List.sort compare (to_list w)))) words
  in let sorted = List.sort (fun (_, xa) (_, ya) -> anagrams_cmp xa ya) words_with_sorted
  in List.map (fun s -> fst s) sorted
