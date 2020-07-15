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
let rec extract k ls =
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
  let combinations = take total_length data in
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

(* implements bubble sort in O(n^2) time, ie. consecutively look for the smallest element *)
let length_sort ls =
  (* val shortest 'a list list -> 'a list option -> 'a list list -> ('a list, 'a list list) *)
  let rec shortest acc so_far lls =
    match (so_far, lls) with
    | (None, []) -> (None, acc)
    | (Some l, []) -> (Some l, acc)
    | (None, l :: ls) -> shortest acc (Some l) ls
    | (Some ll, l :: ls) ->
        let len_ll = List.length ll in
        let len_l = List.length l in
        if len_l < len_ll then shortest (ll :: acc) (Some l) ls
        else shortest (l :: acc) (Some ll) ls
  in let rec length_sort_rec ls =
    if List.length ls = 0 then []
    else
      let short, rest = shortest [] None ls in
      match short with
      | None -> raise Not_found (* should not get here *)
      | Some l -> l :: length_sort_rec rest
  in length_sort_rec ls

(* their implementation selection sort *)
let length_sort_theirs ls =
  (* val insert : ('a -> 'a -> int) -> 'a -> 'a list -> 'a list
   * Inserts e before the first element in the list that is larger.
   **)
  let rec insert cmp e = function
    | [] -> [e]
    | h :: t as l -> if cmp e h < 0 then e :: l else h :: (insert cmp e t)

  in let rec sort cmp = function
    | [] -> []
    | h :: t -> insert cmp h (sort cmp t)

  in
    let lists_with_lengths = List.map (fun l -> (List.length l, l)) ls in
    let sorted = sort (fun a b -> compare (fst a) (fst b)) lists_with_lengths in
    List.map snd sorted

(* Arithmetic *)

(* 31. Determine whether a given integer number is prime. (medium)
 * val is_prime : int -> bool
 **)
let is_prime n =
  let rec range left right =
    if left = right then [right]
    else left :: range (left + 1) right

  in let rec aux n = function
    | [] -> true
    | x :: xs ->
        if n mod x = 0 then false
        else aux n xs

  in aux n (range 2 (n / 2))

(* this version does not use the extra list *)
let is_prime_theirs n =
  let rec is_not_divisor n m =
    if m * m > n then true
    else
      if n mod m = 0 then false
      else is_not_divisor n (m + 1)
  in
    if n = 1 then true
    else is_not_divisor n 2

(* 32. Determine the greatest common divisor of two positive integer
 * numbers. (medium) Use Euclid's algorithm.
 * val common_denom : int -> int -> bool
 **)
let rec common_denom a b =
  if b = 0 then a
  else common_denom b (a mod b)

(* 33. Determine whether two positive integer numbers are coprime. (easy)
 * Two numbers are coprime if their greatest common divisor equals 1.
 * val coprime : int -> int -> bool
 **)
let coprime a b =
  (common_denom a b) = 1

(* 34. Calculate Euler's totient function φ(m). (medium)
 * Euler's so-called totient function φ(m) is defined as the number of positive
 * integers r (1 ≤ r < m) that are coprime to m. We let φ(1) = 1.
 * Find out what the value of φ(m) is if m is a prime number. Euler's totient
 * function plays an important role in one of the most widely used public key
 * cryptography methods (RSA).
 * In this exercise you should use the most primitive method to calculate this
 * function (there are smarter ways that we shall discuss later).
 *
 * val totient : int -> int
 **)
let totient m =
  let rec totient_rec i m =
    if m = 1 then 1
    else if i = m then 0
    else if coprime i m then 1 + totient_rec (i + 1) m
    else totient_rec (i + 1) m
  in totient_rec 1 m

(* 35. Determine the prime factors of a given positive integer. (medium)
 * Construct a flat list containing the prime factors in ascending order.
 * var factors : int -> int list
 **)
let factors n =
  let rec aux d n =
    if n = 1 then []
    else if n mod d = 0 then d :: aux d (n / d)
    else aux (d + 1) n
  in aux 2 n

(* 36. Determine the prime factors of a given positive integer (2). (medium)
 * Construct a list containing the prime factors and their multiplicity.
 * Hint: The problem is similar to problem Run-length encoding of a list
 * (direct solution).
 * val factors_pow : int -> (int * int) list
 * FIXME does not work all the time, eg factors_pow 12031
 **)
let factors_pow n =
  let rec collect acc = function
    | [] -> []
    | x :: [] -> [(x, acc + 1)]
    | x :: y :: rest ->
      if x <> y then (x, acc + 1) :: collect 0 (y :: rest)
      else collect (acc + 1) (y :: rest)
  in let fact = factors n
  in collect 0 fact

(* 37. Calculate Euler's totient function φ(m) (improved). (medium).
 * See problem "Calculate Euler's totient function φ(m)" for the definition
 * of Euler's totient function. If the list of the prime factors of a number
 * m is known in the form of the previous problem then the function phi(m)
 * can be efficiently calculated as follows
 *
 * Let [(p1, m1); (p2, m2); (p3, m3); ...] be the list of prime factors
 * (and their multiplicities) of a given number m.
 * Then φ(m) can be calculated with the following formula:
 * φ(m) = (p1 - 1) × p1^(m1 - 1) × (p2 - 1) × p2^(m2 - 1) × (p3 - 1) × p3^(m3 - 1) × ...
 *
 * val phi_improved : int -> int
 **)
let phi_improved n =
  let rec pow a b =
    if b = 0 then 1 else a * pow a (b - 1)
  in let rec phi_rec = function
    | [] -> 1
    | (p, m) :: tl -> (p - 1) * (pow p  (m - 1)) * (phi_rec tl)
  in phi_rec (factors_pow n)

(* 38. Compare the two methods of calculating Euler's totient function. (easy)
 * Use the solutions of problems "Calculate Euler's totient function φ(m)" and
 * "Calculate Euler's totient function φ(m) (improved)" to compare the algorithms.
 * Take the number of logical inferences as a measure for efficiency.
 * Try to calculate φ(10090) as an example.
 **)
let timeit f arg =
  let t0 = Unix.gettimeofday() in
  ignore (f arg);
  let t1 = Unix.gettimeofday() in
  t1 -.t0

(* 39. A list of prime numbers. (easy)
 * Given a range of integers by its lower and upper limit, construct a list
 * of all prime numbers in that range.
 *
 * val all_primes : int -> int -> int list
 **)
let all_primes left right =
  let rec is_prime_aux n d =
    if d > n / 2 then true
    else if n mod d == 0 then false
    else is_prime_aux n (d+1)
  in let rec all_primes_aux l r =
    if l > r then []
    else if is_prime_aux l 2 then l :: all_primes_aux (l+1) r
    else all_primes_aux (l+1) r
  in all_primes_aux left right

(* 40. 40. Goldbach's conjecture. (medium)
 * Goldbach's conjecture says that every positive even number greater than 2 is
 * the sum of two prime numbers. Example: 28 = 5 + 23.
 * It is one of the most famous facts in number theory that has not been proved
 * to be correct in the general case. It has been numerically confirmed up to
 * very large numbers. Write a function to find the two prime numbers that
 * sum up to a given even integer.
 * val goldbach : int -> int * int option
 **)
let goldbach n =
  let rec is_prime_aux n d =
    if d > n / 2 then true
    else if n mod d == 0 then false
    else is_prime_aux n (d+1)
  in let rec goldbach_aux p n =
    if (is_prime_aux p 2) && (is_prime_aux (n-p) 2) then Some (p, n-p)
    else goldbach_aux (p+1) n
  in goldbach_aux 2 n

(* 41. A list of Goldbach compositions. (medium)
 * Given a range of integers by its lower and upper limit,
 * print a list of all even numbers and their Goldbach composition.
 * In most cases, if an even number is written as the sum of two prime numbers,
 * one of them is very small. Very rarely, the primes are both bigger than say 50.
 * Try to find out how many such cases there are in the range 2..3000.
 * val goldbach_list : int -> int -> (int * (int * int))
 **)
let goldbach_list low high =
  let rec goldbach_list_aux l h =
    if l > h then []
    else if l mod 2 != 0 then goldbach_list_aux (l+1) h
    else (l, goldbach l) :: goldbach_list_aux (l+2) h
  in goldbach_list_aux low high

(* val goldbach_limit : int -> int -> int -> (int * (int * int)) *)
let goldbach_limit low high thresh =
  let max_aux a b =
    if a >= b then a
    else b
  in let rec goldbach_limit_aux l h =
    if l > h then []
    else if l mod 2 != 0 then goldbach_limit_aux (l+1) h
    else
      (match goldbach l with
        | None -> goldbach_limit_aux (l+2) h
        | Some (p1, p2) ->
          if p1 > thresh && p2 > thresh then (l, (p1, p2)) :: goldbach_limit_aux (l+2) h
          else goldbach_limit_aux (l+2) h)
  in goldbach_limit_aux (max_aux low thresh) (max_aux thresh high)

(* Logic and Codes *)

type bool_expr =
  Var of string
| Not of bool_expr
| And of bool_expr * bool_expr
| Or of bool_expr * bool_expr

(* 46 & 47. Truth tables for logical expressions (2 variables). (medium)
 * Define a function, table2 which returns the truth table of a given logical
 * expression in two variables (specified as arguments).
 * The return value must be a list of triples containing
 * (value_of_a, value_of_b, value_of_expr).
 *
 * - generate all combinations [true, false] for (a, b)
 * - evaluate expression with bool inputs
 * var table2 : string -> string -> bool_expr -> (bool * bool * bool) list
 **)
let table2 a b expr =
  (* val eval_aux : string -> bool -> string -> bool -> bool_expr -> bool *)
  let rec eval_aux a a_val b b_val = function
    | Var x ->
        if x = a then a_val
        else if x = b then b_val
        else raise Not_found
    | Not expr ->
        let expr_val = eval_aux a a_val b b_val expr in not expr_val
    | And (left, right) ->
        let left_val = eval_aux a a_val b b_val left
        in let right_val = eval_aux a a_val b b_val right
        in left_val && right_val
    | Or (left, right) ->
        let left_val = eval_aux a a_val b b_val left
        in let right_val = eval_aux a a_val b b_val right
        in left_val || right_val
  (* val vals : bool * bool list *)
  in let vals = [(true, true); (true, false); (false, true); (false, false)]
  (* val apply_aux : bool_expr -> bool * bool list -> (bool * bool * bool) list *)
  in let rec apply_aux expr = function
    | [] -> []
    | (a_val, b_val) :: xs -> (a_val, b_val, (eval_aux a a_val b b_val expr)) :: apply_aux expr xs
  in apply_aux expr vals




