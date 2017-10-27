(* 1. Write a function last : 'a list -> 'a option that returns the last element of a list. (easy) *)
let rec last xs =
  match xs with
  | [] -> None
  | [x] -> Some x
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
    (List.times x n) :: acc
  in List.fold_left pred [] xs
