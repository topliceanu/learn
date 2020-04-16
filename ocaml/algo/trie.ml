(* A Trie is a tree with large branching order.
 * 'a is the type of the key,
 * 'b is the value stored behind that key
 **)
type (string, 'a) trie =
| Empty
| Root of (string, 'a) trie list
| Node of string * 'a option * (string, 'a) trie list

(* val insert : string -> 'a -> (string, 'a) trie -> (string, 'a) trie *)
fun rec insert key a t =
  let (head, tail) = split_key(key) in
  if tail = None then Node head a []
  else
    match t with
    | Empty -> insert tail a (Node head None [])
    | Node (ch, None, children) -> insert
    | Node (ch, Some a, children) ->


(* val lookup : string -> string * 'a trie -> 'a *)

(* val delete : string -> string * 'a trie -> string * 'a trie *)

(* val lookup_prefix: string -> string * 'a trie -> string * 'a list *)

(* val traverse : string * 'a trie -> string * 'a list *)
