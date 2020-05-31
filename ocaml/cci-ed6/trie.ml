(* A Trie is a tree with large branching order.
 * 'a is the value stored behind that key
 * Inspirations:
 * - https://gist.github.com/owainlewis/4066049
 * - https://gist.github.com/komamitsu/6474266
 **)

(* Trie structure where keys are strings and values can be any type 'a
 * Invariants:
 * - the Root has no key and no value but has children.
 * - nodes in the tree all have a key, some don't have a value attacked - NoValueNode - some do - ValueNode.
 * *)

module M = Map.Make(String)

type 'a trie =
  | Empty
  | Node of 'a trie M.t
  | ValueNode of string * 'a trie M.t

(* val find_or_create : string -> 'a trie M.t -> 'a option *)
let find_or_create c children value =
  match ((M.find_opt c children), value) with
  | (None, None) -> raise Not_found (* this is an impossible state *)
  | (None, Some value') -> ValueNode (value', M.empty)
  | (Some Empty, _) -> raise Not_found (* this should not be possible *)
  | (Some (Node children'), None) -> Node children'
  | (Some (Node children'), (Some value')) -> ValueNode (value', children')
  | (Some (ValueNode (value', children')), None) -> ValueNode (value', children')
  | (Some (ValueNode (value', children')), (Some value'')) -> ValueNode (value'', children')

type key_parts =
| Blank
| Last of string
| More of string * string

(* val split_key : string -> key_parts *)
let split_key s =
  let n = String.length s
  in if n = 0 then Blank
  else if n = 1 then Last s
  else
    let hd = String.sub s 0 1
    in let tl = String.sub s 1 (n - 1)
    in More (hd, tl)

(* val upsert : string -> 'a -> 'a trie -> 'a trie *)
let rec upsert key value tr =
  let parts = split_key key in
  match (tr, parts) with
  | (_, Blank) -> raise Not_found
  | (Empty, Last c) ->
      let node = ValueNode (value, M.empty) in
      let children = M.add c node M.empty in
      Node children (* root node *)
  | (Node children, Last c) ->
      let node = find_or_create c children (Some value) in
      let children = M.add c node children in
      Node children
  | (ValueNode (value', children), Last c) ->
      let node = find_or_create c children (Some value) in
      let children' = M.add c node children in
      ValueNode (value', children')
  | (Empty, More (c, rest)) ->
      let node = upsert rest value (Node M.empty) in
      let children = M.add c node M.empty
      in Node children
  | (Node children, More (c, rest)) ->
      let node = find_or_create c children None in
      let node' = upsert rest value node in
      let children' = M.add c node' children in
      Node children'
  | (ValueNode (value', children), More (c, rest)) ->
      let node = find_or_create c children None in
      let node' = upsert rest value node in
      let children' = M.add c node' children in
      ValueNode (value', children')
