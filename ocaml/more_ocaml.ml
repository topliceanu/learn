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
