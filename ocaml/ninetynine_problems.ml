(* exercises from https://ocaml.org/learn/tutorials/99problems.html *)

(* 1. Write a function last : 'a list -> 'a option that returns the last element of a list. (easy) *)
let rec last xs =
  match xs with
  | [] -> None | [x] -> Some x
  | _ :: t -> last t

(* 2. Find the last but one (last and penultimate) elements of a list. (easy) *)
let rec last_two xs =
  match xs with
  | [] -> None
  | [_] -> None
  | [x; y] -> Some (x, y)
  | _ :: t -> last_two t

(* 3. Find the k'th element of a list. (easy) *)
let rec kth xs k =
  match xs with
  | [] -> None
  | x :: t ->
      if k == 1 then Some x
      else kth t (k - 1)

(* 4. Find the number of elements of a list. (easy) *)
let rec len lst =
  let rec aux n l =
    match l with
    | [] -> n
    | _ :: t -> aux (n+1) t
  in aux 0 lst

(* 5. Reverse a list. (easy) *)
let rec rev l =
  match l with
  | [] -> []
  | x :: t -> List.append (rev t) [x]

(* 6. Find out whether a list is a palindrome. (easy) *)
let is_palindrome l =
  (rev l) = l

(* 7. Flatten a nested list structure. (medium) *)
type 'a node =
  | One of 'a
  | Many of 'a node list

let flatten nodes =
  let rec flat acc nodes =
    match nodes with
    | [] -> acc
    | One x :: tl -> flat (x :: acc) tl
    | Many xs :: tl -> flat (flat acc xs) tl
  in List.rev (flat [] nodes)

(* 8. Eliminate consecutive duplicates of list elements. (medium) *)
let compress xs =
  let rec comp acc xs =
    match xs with
    | x :: (y :: _ as tl) ->
        if x = y then comp acc tl
        else comp (x :: acc) tl
    | x :: [] -> x :: acc
    | [] -> acc
  in List.rev (comp [] xs)

(* 9. Pack consecutive duplicates of list elements into sublists. (medium) *)
(* val pack : 'a list -> 'a list list *)
let pack xs =
  let pred acc x =
    match acc with
    | [] -> []
    | hd :: tl -> begin
      match hd with
      | [] -> [x] :: tl
      | h :: t ->
          if h = x
          then (x :: h :: t) :: tl
          else [x] :: (h :: t) :: tl
    end
  in List.rev (List.fold_left pred [[]] xs)

(* 10. Run-length encoding of a list. (easy) *)
(* val encode : 'a list -> (int * 'a) list *)
let encode xs =
  let count x =
    ((List.length x), (List.nth x 0))
  in match (pack xs) with
  | [] -> []
  | non_empty -> List.map count non_empty

(* 11. Modify the result of the previous problem in such a way that if an
 * element has no duplicates it is simply copied into the result list
 **)
type 'a rle =
  | One of 'a
  | Many of int * 'a

let encode2 xs =
  let count = function
    | [] -> raise (Failure "cannot be empty!")
    | [x] -> One x
    | x :: _ as l -> Many ((List.length l), x)
  in match pack xs with
  | [] -> []
  | non_empty -> List.map count non_empty

(* 12. Decode a run-length encoded list *)
let decode rs =
  let rec rep x = function
    | 0 -> []
    | n -> x :: rep x (n - 1)
  in let expand acc r =
    match r with
    | One x -> acc @ [[x]]
    | Many (count, x) ->
        acc @ [rep x count]
  in List.fold_left expand [] rs

(* 13. Implement the so-called run-length encoding data compression method directly.
 * I.e. don't explicitly create the sublists containing the duplicates, as in problem 9).,
 * but only count them. As in problem 11)., simplify the result list by replacing the singleton lists (1 X) by X.
 * TODO implement this
 **)

(* 14 Duplicate the elements of a list. (easy) TODO test this *)
let duplicate xs =
  let pred acc x =
    x :: ( x :: acc )
  in List.fold_left pred [] xs

(* 15. Replicate the elements of a list a given number of times. (medium) *)
let replicate xs n =
  let pred acc x =
    (List.init n (fun _ -> x)) :: acc
  in List.fold_left pred [] xs

(* 16. Drop every N'th element from a list. (medium)
 * TODO test this!?!
 **)
let rec drop xs n =
  let rec split i ys =
    match ys with
    | [] -> []
    | y :: yss ->
        if i == n then split 1 yss
        else y :: split (i + 1) yss
  in split 1 xs

(* 17. Split a list into two parts; the length of the first part is given. (easy)
 * If the length of the first part is longer than the entire list,
 * then the first part is the list and the second part is empty.
 **)
let split xs n =
  let rec aux ys zs k =
    match zs with
    | [] -> (ys, zs)
    | z :: zss ->
        if k == n+1 then (ys, zs)
        else let (ts, us) = aux ys zss (k + 1)
        in (z :: ts, us)
  in aux [] xs 1

let split' xs n =
  let rec aux i acc = function
    | [] -> (List.rev acc, [])
    | h :: t ->
        if i == n then (List.rev (h :: acc), t)
        else aux (i + 1) (h :: acc) t
  in aux 1 [] xs

(* 18. Extract a slice from a list. (medium)
 * Given two indices, i and k, the slice is the list containing the elements
 * between the i'th and k'th element of the original list (both limits included).
 * Start counting the elements with 0 (this is the way the List module numbers elements).
 **)
let slice xs i j =
  let rec aux k ys =
    match ys with
    | [] -> []
    | y :: yss ->
        if i <= k && k <= j then y :: (aux (k + 1) yss)
        else if k > j then []
        else aux (k + 1) yss
  in aux 0 xs

(* The solution from the ocaml website involves a function fold_until
 * with the signature ('a -> 'b -> 'a) -> 'a -> int -> 'b list -> 'a * list 'b
 * which applies f to each element of the input list until it reaches the n index.
 *
 * This is a cool function!
 **)
let rec fold_until f acc n = function
  | [] -> (acc, [])
  | h :: t as l ->
      if n == 0 then (acc, l)
      else fold_until f (f acc h) (n - 1) t

let slice' xs i j =
  let (_, rest) = fold_until (fun _ x -> []) [] i xs in
  let (pluck, _) = fold_until (fun acc x -> x :: acc) [] (j - i + 1) rest in
  List.rev pluck

(* 19. Rotate a list N places to the left. (medium)
 **)
(* val rotate : 'a list -> int -> 'a list *)
let rotate xs n =
  let m = List.length xs in
  let n = n mod m in
  let (second, first) = fold_until (fun acc x -> x :: acc) [] n xs in
  List.append first (List.rev second)

(* 20. Remove the K'th element from a list. (easy)
 * The first element of the list is numbered 0, the second 1,...
 **)
(* val remove_at : int -> 'a list -> 'a list *)
let rec remove_at n = function
  | [] -> []
  | hd :: tl ->
      if n == 0 then tl
      else hd :: remove_at (n-1) tl

(* 21. Insert an element at a given position into a list. (easy)
 * Start counting list elements with 0. If the position is larger or equal to the
 * length of the list, insert the element at the end.
 * (The behavior is unspecified if the position is negative.)
 **)
(* val insert_at : 'a -> int -> 'a list -> 'a list *)
let rec insert_at x n = function
  | [] -> x :: []
  | hd :: tl ->
      if n == 0 then x :: hd :: tl
      else hd :: insert_at x (n-1) tl

(* 22. Create a list containing all integers within a given range. (easy)
 * If first argument is greater than second, produce a list in decreasing order.
 **)
(* val range int -> int -> int list *)
let range start stop =
  (* val aux : int list -> int -> int -> int list *)
  let rec aux n m =
    if n = m then n :: []
    else if n < m then n :: aux (n + 1) m
    else n :: aux (n - 1) m
  in aux start stop


