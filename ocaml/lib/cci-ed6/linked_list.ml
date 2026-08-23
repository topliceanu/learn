type 'a linked_list =
  Empty
| Cons of 'a * 'a linked_list

(* val make : 'a list -> 'a linked_list *)
let rec from_list = function
  | [] -> Empty
  | x :: xs -> Cons (x, from_list xs)

(* val to_list : 'a linked_list -> 'a list *)
let rec to_list = function
  | Empty -> []
  | Cons (x, xs) -> x :: (to_list xs)

(* CCI-book, ed.6, ch.2, problem 1: remove dups
 * Write code to remove duplicates from an unsorted linked list. How would you solve this problem if a temporary buffer is not allowed?
 *)
(* val remove_dups : 'a linked_list -> 'a linked_list *)
let rec remove_dups ls =
  let rec chase x = function
    | Empty -> Empty
    | Cons (y, ys) as l ->
        if x == y then chase x ys
        else l
  in match ls with
  | Empty -> Empty
  | Cons (y, ys) ->
      match chase y ys with
      | Empty -> Cons (y, Empty)
      | Cons (_, _) as l ->  Cons (y, remove_dups l)
    
(* Shorter version, it iterates over the list, filter out duplicate values. 
 * Complexity: time O(n^2) space O(1) *)      
let rec remove_dups' = function 
  | [] -> []
  | x :: xs -> 
    let ys = List.filter (fun y -> y != x) xs
    in remove_dups' ys

(* Optimised version, it iterates over the sorted version of the list, eliminating duplicate sequences.
 * Compexity: time O(nlogn) space O(1) *)      
let rec remove_dups'' ls = 
  let sortl = List.sort (fun l1 l2 -> if l1 > l2 then 1 else if l1 < l2 then -1 else 0) in
  let rec eat pred = function 
    | [] -> []
    | x :: xs as l -> if pred x then eat pred xs else l
  in let rec remove_dups_aux = function
    | [] -> []
    | x :: xs -> 
      let ys = eat (fun y -> x == y) xs 
      in x :: (remove_dups_aux ys)
  in remove_dups_aux (sortl ls)

(* CCI-book, ed.6, ch.2, problem 2: return k-th to last
 *  Implement an algorithm to find the kth to last element of a singly linked list.
 *)
(* val kth_to_last : int -> 'a linked_list -> 'a option *)
let kth_to_last k ls =
  (* val advance : int -> 'a linked_list -> 'a linked_list *)
  let rec advance k = function
    | Empty -> Empty
    | Cons (x, xs) as l ->
        if k = 0 then l
        else advance (k - 1) xs

  (* val advance : 'a linked_list -> 'a linked_list -> 'a option *)
  in let rec advance_to_end follower leader =
    match (follower, leader) with
    | (Empty, Empty) -> None
    | (Empty, Cons (y, ys)) -> None (* this case cannot be possible *)
    | (Cons (x, _), Empty) -> Some x
    | (Cons (x, xs), Cons (y, ys)) -> advance_to_end xs ys

  in match advance k ls with
  | Empty -> None
  | Cons (_, _) as leader -> advance_to_end ls leader
