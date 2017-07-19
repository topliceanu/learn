(* lazy lists *)

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
