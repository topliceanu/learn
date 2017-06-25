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
  | [x, y] -> Some (x, y)
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
  let rec aux n lst =
    match l with
    | [] -> n
    | _ :: t -> aux (n+1) t
  in aux 0 lst

(* 5. Reverse a list. (easy) *)
let rec rev l =
  match l with
  | [] -> []
  | x :: t -> concat (rev t) x
