(*
Write a function that returns whether a list of strings is sorted given a specific alphabet.
A list of N words with max length M and a K-sized alphabet are given.

input:  words =    ["ca", "cat", "bat", "tab"]
        alphabet = ['c', 'b', 'a', 't']
output: True
*)

(* val is_sorted : string list -> char list -> bool *)
let is_sorted words alphabet =
  (* val list_of_string : string -> char list *)
  let rec list_of_string s =
    List.init (String.length s) (String.get s)

  (* val pos : char -> list char -> int option *)
  in let pos x alphabeth =
    let rec aux x n = function
      | [] -> None
      | y :: ys ->
          if x = y then Some n
          else aux x (n+1) ys
    in aux x 0 alphabeth

  (* val is_lte : char list -> char list -> char list -> bool *)
  in let rec is_lte w1 w2 alphabet =
    match (w1, w2) with
    | [], [] -> true
    | _ :: _, [] -> false
    | [], _ :: _ -> true
    | x :: xs, y :: ys ->
        (match (pos x alphabet), (pos y alphabet) with
        | None, None | None, _ | _, None -> failwith "chars not in the alphabet"
        | (Some pos_x), (Some pos_y) ->
          if pos_x <= pos_y then is_lte xs ys alphabet
          else false)

  (* val is_sorted_aux -> char list list -> char list -> bool *)
  in let rec is_sorted_aux words alphabet =
    match words with
    | [] | _ :: [] -> true
    | w1 :: (w2 :: _) as rest ->
        if is_lte w1 w2 alphabet = false then false
        else is_sorted_aux rest alphabet

  in is_sorted_aux (List.map list_of_string words) alphabet
