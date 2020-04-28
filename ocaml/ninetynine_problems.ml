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
let rec range start stop =
  if start = stop then start :: []
  else if start < stop then start :: range (start + 1) stop
  else start :: range (start - 1) stop

(* 23. Extract a given number of randomly selected elements from a list. (medium)
 * The selected items shall be returned in a list. We use the Random module but do
 * not initialize it with Random.self_init for reproducibility.
 **)
(* val rand_select : 'a list -> int -> 'a list *)
let rand_select ls n =
  (* val select : 'a list -> int -> 'a list -> ('a, 'a list)
   * Given a list and an index, it will return the value at that index plus
   * the everything else in the list.
   **)
  let rec select_one acc n = function
    | [] -> raise Not_found
    | x :: xs ->
        if n = 0 then (x, acc @ xs)
        else select_one (x :: acc) (n - 1) xs
  in let rec select_many n ls =
    if n = 0 then []
    else if List.length ls = 0 then []
    else
      let len = List.length ls in
      let k = Random.int len in
      let (selected, rest) = select_one [] k ls in
      selected :: select_many (n - 1) rest

  in select_many n ls

(* My own implementation of the above function
 * FIXME: if the random generator produces the same index multiple times,
 * the output will not contain the corresponding value multiple times.
 **)
let rand_select_mine ls n =
  (* val aux : int list -> int -> 'a list -> 'a list *)
  let rec aux indices current_index ls =
    match (indices, current_index, ls) with
    | ([], _, _) -> []
    | (_, _, []) -> []
    | (i :: is, j, x :: xs) ->
      if i = j then x :: (aux is (j + 1) xs)
      else aux (i :: is) (j + 1) xs
  in
    let len = List.length ls in
    let indices = List.init n (fun _ -> Random.int len)
    in aux indices 0 ls

(* 24. Lotto: Draw N different random numbers from the set 1..M. (easy)
 * The selected numbers shall be returned in a list.
 **)
let rec lotto_select n m =
  let rec exists x = function
    | [] -> false
    | y :: ys ->
        if y = x then true
        else exists x ys
  in let rec select acc max_value count =
    if count = 0 then acc
    else
      let k = Random.int max_value in
      let already_exists = exists k acc in
      if already_exists then select acc max_value count
      else select (k :: acc) max_value (count - 1)
  in select [] m n

(* their solution to this problem *)
let rec lotto_select_theirs n m = rand_select (range 1 m) n

(* 25. Generate a random permutation of the elements of a list. (easy)
 * val permutation : 'a list -> 'a list
 **)
let permutation ls =
  (* val pluck : 'a list -> int -> ('a option, 'a list) *)
  let rec pluck xs k rest =
    match xs with
    | [] -> raise Not_found
    | x :: xss ->
        if k = 0 then (x, rest @ xss)
        else pluck xss (k - 1) (x :: rest)
  (* val build_permutations : 'a list -> int -> 'a list *)
  in let rec build_permutation xs n =
    if n = 0 then []
    else
      let selected, rest = pluck xs (Random.int n) []
      in selected :: (build_permutation rest (n - 1))

  in build_permutation ls (List.length ls)

(* 26. Generate the combinations of K distinct objects chosen from the N elements of a list. (medium)
 * In how many ways can a committee of 3 be chosen from a group of 12 people?
 * We all know that there are C(12,3) = 220 possibilities (C(N,K) denotes the
 * well-known binomial coefficients).
 * For pure mathematicians, this result may be great. But we want to really
 * generate all the possibilities in a list.
 *
 * val extract : int -> 'a list -> 'a list list
 **)
let extract k ls =
  if k = 0 then [[]] (* this is where the recursion ends, k is the number of elements to select from ls *)
  else
    match ls with
    | [] -> []
    | hd :: tl ->
        let with_hd = List.map (fun l -> hd :: l) (extract (k - 1) tl) in
        let without_hd = extract k tl in
        with_hd @ without_hd

(* 27. Group the elements of a set into disjoint subsets. (medium)
 *  * In how many ways can a group of 9 people work in 3 disjoint subgroups of
 *    2, 3 and 4 persons? Write a function that generates all the possibilities
 *    and returns them in a list.
 *  * Generalize the above function in a way that we can specify a list of group
 *    sizes and the function will return a list of groups.
 * val group : 'a list -> int list -> 'a list list list
 *
 * FIXME: does not work
 **)
let group data lengths =
  (* val take : int -> 'a list -> 'a list *)
  let rec take n = function
    | [] -> []
    | x :: xs -> if n = 0 then [] else x :: take (n - 1) xs

  (* val group_by_single : 'a list -> int list -> 'a list list *)
  in let rec group_by_single combination = function
    | [] -> []
    | x :: xs -> (take x combination) :: (group_by_single combination xs)

  (* val group_by : 'a list list -> int list -> 'a list list list *)
  in let rec group_by combinations lengths =
    match combinations with
    | [] -> []
    | cb :: cbs -> (group_by_single cb lengths) :: (group_by cbs lengths)

  in let total_length = List.fold_left (fun acc l -> acc + l) 0 lengths in
  let combinations = extract total_length data in
  group_by combinations lengths

(* 28. Sorting a list of lists according to length of sublists. (medium)
 * 1. We suppose that a list contains elements that are lists themselves.
 *  The objective is to sort the elements of this list according to their length.
 *  E.g. short lists first, longer lists later, or vice versa.
 * 2. Again, we suppose that a list contains elements that are lists themselves.
 *  But this time the objective is to sort the elements of this list according
 *  to their length frequency; i.e., in the default, where sorting is done
 *  ascendingly, lists with rare lengths are placed first, others with a more
 *  frequent length come later.
 **)

