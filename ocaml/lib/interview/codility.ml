(* Problem: You are given n binary values x0, x1, . . . , xn−1, such that xi in {0, 1}.
 * This array represents holes in a roof (1 is a hole). You are also given k boards
 * of the same size.
 * The goalis to choose the optimal (minimal) size of the boards that allows
 * all the holes to be coveredby boards.
 * Source: https://codility.com/media/train/12-BinarySearch.pdf
 *
 * val minimal_size : int list -> int -> int
 **)
(* val advance : int -> 'a list -> 'a list *)
let rec advance count = function
  | [] -> []
  | _ :: tl as l ->
      if count == 0 then l
      else advance (count - 1) tl

(* val count_num_boards : int list -> int -> int *)
let rec count_num_boards holes board_size =
  match holes with
  | [] -> 0
  | hole :: rest ->
      if hole = 0 then count_num_boards rest board_size
      else 1 + count_num_boards (advance board_size holes) board_size

(* val min_size_rec : int list -> int -> int -> int *)
let rec min_size_rec holes available_boards size_so_far count_so_far =
  let half_size = size_so_far / 2 in
  let count_half = count_num_boards holes half_size in
  if count_half > available_boards then count_so_far
  else min_size_rec holes available_boards half_size count_half

let minimal_size holes available_boards =
  min_size_rec holes available_boards (List.length holes) 1
