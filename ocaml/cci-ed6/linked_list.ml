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
