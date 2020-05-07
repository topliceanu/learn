module Ref : sig
  type t
  val create : int -> t
  val set : t -> int -> unit
  val get : t -> int
end
=
  struct
    type t = int ref
    let create x = ref x
    let set t x = t := x
    let get t = !t
  end

module RO_ref : sig
  type t
  val create : Ref.t -> t
  val get : t -> int
end
=
  struct
    type t = Ref.t
    let create x = x
    let get = Ref.get
  end

(* Phantom Ref, Q: is prefixing with P a convention? *)
module Pref : sig
  type 'a t
  val create : int -> 'a t
  val set : rw t -> int -> unit
  val get : 'a t -> int
  (* ro and rw are tags, empty data types, uninhabited types, a type without any definition, a type without any value
   * Q: can you just use types that were not defined
   * Q: what is ro or rw?
   **)
  val ro : rw t -> ro t
end
=
struct
  (* 'a is not used in the type *)
  type 'a t = Ref.t
  let create = Ref.create
  let set = Ref.set
  let get = Ref.get
  let ro x = x
end

(* val sum : -> 'a Pref.t list -> int *)
let sum l =
  List.fold_left (fun sum x -> sum + Pref.get x) 0 l

(* val double_list : rw Pref.t list-> ()
 * Q: wasn't 'rw' defined only in Pref? Why not Pref.rw Pref.t list?
 **)
let double_list l =
  List.iter (fun x -> Pref.set x (2 * Pref.get x)) l

type u = {
  a: ro Pref.t list;
  b: rw Pref.t list;
}

let build_u =
  let a = List.map Pref.create [1; 2; 3] in
  let b = List.map Pref.create [4; 5; 6] in
  double_list b; (* you can use ; when the function returns unit *)
  { a = a; b = b }

(* Also: type index values *)
