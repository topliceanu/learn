(* The "More Ocaml" book, chapter 2: Being Lazy *)

type 'a lazylist = Cons of 'a * (unit -> 'a lazylist)

(* lseq : int -> int lazylist
 * builds a lazy list starting with n*)
let rec lseq n =
  Cons (n, fun () -> lseq (n + 1))

(* lhead : 'a lazylist -> 'a *)
let lhead ls =
  let Cons (hd, _) = ls in hd

(* ltail : 'a lazylist -> 'a lazylist *)
let ltail ls =
  let Cons (_, tl) = ls in tl ()

(* ltake : 'a lazylist -> int -> 'a list *)
let rec ltake ls n =
  match n with
  | 0 -> []
  | _ ->
      let Cons (hd, tl) = ls in
      hd :: ltake (tl ()) (n-1)

(* ldrop : 'a lazylist -> n -> 'a lazylist *)
let rec ldrop ls n =
  match n with
  | 0 -> ls
  | _ ->
      ldrop (ltail ls) (n - 1)

(* lmap : ('a -> 'b) -> 'a lazylist -> 'b lazylist *)
let rec lmap p ls =
  let Cons (hd, tl) = ls in
  Cons ((p hd), fun () -> lmap p (tl ()))

(* lfilter : ('a -> bool) -> 'a lazylifter -> 'a lazyfilter *)
let rec lfilter p (Cons (hd, lt)) =
  let rest = fun () ->
    lfilter p (lt ())
  in
    if p hd = true
    then Cons (hd, rest)
    else (rest ())

(* cubes divisible by 5 *)
(* val cubes : int lazylist -> int lazylist *)
let cubes =
  lseq 1 |>
  lmap (fun x -> x * x * x) |>
  lfilter (fun x -> x mod 5 = 0)
  (*
  let src = lseq 1 in
  let cbs = lmap (fun x -> x * x * x) src in
  lfilter (fun x -> x mod 5 = 0) cbs
  *)

(* filters the input seed list to return all primes *)
(* mkprimes : 'a lazylist -> 'a lazylist *)
let rec mkprimes (Cons (hd, tl)) =
  Cons (hd, fun () ->
    mkprimes (lfilter (fun x -> x mod hd <> 0) (tl ())))

(* interleaves elements from two lazy lists between each-other. *)
let rec interleave (Cons (hd1, lt1)) l2 =
  Cons (hd1, fun () -> interleave l2 (lt1 ()))

(* lconst produces an infinite list with the same value *)
let rec lconst n =
  Cons (n, fun () -> lconst n)

(* all combinations and permutations of 0 and 1 *)
let rec allfrom l =
  Cons (l, fun () ->
    interleave (allfrom (0 :: l)) (allfrom (1 :: l)))

let allones = allfrom []

(* ex.1 write a lazy list with elements 1, 2, 4, 8, 16,... *)
(* val squares : int lazylist -> float lazylist *)
let squares =
  lseq 1 |>
  lmap (fun x -> (float_of_int x) ** 2.)

(* ex.2 write a function which returns the nth element of a lazy list *)
let rec nth n (Cons (hd, tl)) =
  match n with
  | 0 -> hd
  | _ -> nth (n - 1) (tl ())

(* ex.3 given a list, return the lazy list formed by repeating the input list. The input list cannot be empty *)
(* NOTE Lazy lists cannot be empty! *)
(* val repeat : 'a list -> 'a lazylist *)
let repeat l =
  (* val rep : 'a list -> 'a list -> 'a lazylist *)
  let rec rep it orig =
    match it with
    | [] ->
      let out = match orig with
        | [] -> raise Not_found
        | hd :: tl -> Cons (hd, fun () -> (rep tl orig))
      in out
    | hd :: tl -> Cons (hd, fun () -> (rep tl orig))
  in rep l l

(* ex.4 write a fibonaccy numbers generator *)
let rec fibonacci x y =
  Cons (x + y, fun () -> fibonacci y (x + y))

let fib = Cons (0, fun () -> Cons (1, fun () -> (fibonacci 0 1)))

(* ex.5 given a list produces two lazy lists, one on even positions, one on odd positions *)
(* val unleave : 'a lazylist -> 'a lazylist * 'a lazylist *)
let rec unleave (Cons (hd, tl)) =
  let Cons (hd', tl') = tl () in
  let t = tl' () in
  (Cons (hd, fun () -> fst (unleave t)),
   Cons (hd', fun () -> snd (unleave t)))

(* not an exercise per-se, I wanted to create an infinite list of primes using the Sieve of Erathostene
 * FIXME why is this not working correctly?!
 * val lprimes : int lazylist
 **)
let rec lprimes =
  (* val not_divisible_by : int -> int lazylist -> int lazylist *)
  let rec not_divisible_by k l =
    lfilter (fun x -> x mod k <> 0) l

  (* val sieve: int lazylist -> int lazylist *)
  in let rec sieve src =
    let Cons (hd, tl) = src in
    Cons (hd, fun () -> sieve (not_divisible_by hd (tl ())))

  in sieve (lseq 2)

(* ex.6 write a lazy list which produces A, B, C .. X, Y, Z, AA, AB, AC .. AX, AY, AZ, BA, BB, ... BX, BY, BZ, ...
 * val labels : string lazylist
 **)

(* generates charaters starting with 'A'
 * val uppercase : char lazylist
 * *)
let uppercase =
  let rec next c =
    Cons (c, fun () -> next (Char.chr (Char.code c + 1)))
  in next 'A'

(* generates strings from "A" to "Z" then starts over.
 * Note that it returns strings instead of characters!
 * val uppercase_circular : string lazylist
 **)
let uppercase_circular =
  let next_str c =
    Char.escaped (Char.chr ((Char.code (String.get c 0)) + 1))
  in let rec next c =
    if c = "Z" then Cons ("Z", fun () -> next "A")
    else Cons (c, fun () -> next (next_str c))
  in next "A"

(* merges two uppercase_circular lazy lists by going through
 * the second one for each element of the first one
 * val merge : string lazylist -> string lazylist -> string lazylist
 **)
let rec merge xs ys =
  match (xs, ys) with
  | ((Cons (x, xss)), (Cons (y, yss))) ->
    if y = "Z" then Cons (x ^ y, fun () -> merge (xss ()) (yss ()))
    else Cons (x ^ y, fun () -> merge xs (yss ()))

(* lfill is a lazy list that produces the same thing parameter all the time
 * val lfill : 'a -> 'a lazylist
 **)
let rec lfill x = Cons (x, fun () -> lfill x)

(* FIXME *)
(* let labels = *)
