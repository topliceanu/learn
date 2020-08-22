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
| Cons of 'a * 'a linked_list

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
        else Cons (carry, Empty)
    | (Empty, Cons (x, xs)) | (Cons (x, xs), Empty) ->
        let carry, new_x = add_10 [x; carry]
        in Cons (new_x, (add_lists Empty xs carry))
    | (Cons (x, xs), Cons (y, ys)) ->
      let carry, z = add_10 [x; y; carry]
      in Cons (z, (add_lists xs ys carry))

  in add_lists l1 l2 0

(* Source: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
 * var letter_combinations : char list -> string list
 **)
let letter_combinations digits =
  let mapping = [
     ('1', []);
     ('2', ['a'; 'b'; 'c']);
     ('3', ['d'; 'e'; 'f']);
     ('4', ['g'; 'h'; 'i']);
     ('5', ['j'; 'k'; 'l']);
     ('6', ['m'; 'n'; 'o']);
     ('7', ['p'; 'q'; 'r'; 's']);
     ('8', ['t'; 'u'; 'v']);
     ('9', ['w'; 'x'; 'y'; 'z']);
  ]

  (* val find : char -> (char * char list) list -> char list *)
  in let rec find ch = function
    | [] -> raise Not_found
    | (c, ls) :: rest ->
        if c = ch then ls
        else find ch rest

  (* val rec_let_comb : char list -> string list *)
  in let rec rec_let_comb = function
    | [] -> [ ]
    | d :: digits ->
        let combs = rec_let_comb digits in
        let mappings = find d mapping in
        if List.length mappings = 0 then combs
        else if List.length combs = 0 then List.map Char.escaped mappings
        else
          List.flatten (List.map (fun m -> List.map (fun c -> (Char.escaped m) ^ c) combs) mappings)

  in rec_let_comb digits

(* Source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
 * Given a linked list, remove the n-th node from the end of list and return its head.
 * *)

(* val remove_nth_from_end : 'a linked_list -> int -> 'a linked_list *)
let remove_nth_from_end ls n =
  (* val length : 'a linked_list -> int *)
  let rec length = function
    | Empty -> 0
    | Cons (_, tl) -> 1 + length tl

  (* val remove : int -> 'a linked_list -> 'a linked_list *)
  in let rec remove n = function
    | Empty -> Empty
    | Cons (hd, tl) ->
        if n = 0 then tl
        else Cons (hd, (remove (n-1) tl))

  in let len = length ls
  in
    if len - n < 0 then ls
    else remove (len - n) ls

(* Source: https://leetcode.com/problems/swap-nodes-in-pairs/ *)
(* let swap_pairs : 'a linked_list -> 'a linked_list *)

let rec swap_pairs node =
  match node with
  | Empty -> Empty
  | Cons (_, Empty) -> node
  | Cons (x, Cons(y, rest)) -> Cons (y, Cons (x, (swap_pairs rest)))


(* Source: https://leetcode.com/problems/median-of-two-sorted-arrays/ *)
