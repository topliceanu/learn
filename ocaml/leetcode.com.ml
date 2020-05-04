(* Solutions to problems from leetcode.com *)

(* Medium *)

(* 2. Add Two Numbers
 * You are given two non-empty linked lists representing two non-negative integers.
 * The digits are stored in reverse order and each of their nodes contain a single digit.
 * Add the two numbers and return it as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 * Example:
 *  Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 *  Output: 7 -> 0 -> 8
 *  Explanation: 342 + 465 = 807.
 **)
type 'a linked_list =
  Empty
| Node of 'a * 'a linked_list

(* val add_linked_lists : int linked_list -> int linked_list -> int linked_list *)
let add_linked_lists l1 l2 =

  (* val add_10 : int list -> (int, int) *)
  let add_10 l =
    let sum = List.fold_left (+) 0 l in sum / 10, sum mod 10

  (* val add_lists : int linked_list -> int linked_list -> int -> int linked_list *)
  in let rec add_lists l1 l2 carry =
    match (l1, l2) with
    | (Empty, Empty) ->
        if carry = 0 then Empty
        else Node (carry, Empty)
    | (Empty, Node (x, xs)) | (Node (x, xs), Empty) ->
        let carry, new_x = add_10 [x; carry]
        in Node (new_x, (add_lists Empty xs carry))
    | (Node (x, xs), Node (y, ys)) ->
      let carry, z = add_10 [x; y; carry]
      in Node (z, (add_lists xs ys carry))

  in add_lists l1 l2 0
