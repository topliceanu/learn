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
  | (None, None) -> Node M.empty
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

(* val print : 'a trie -> unit *)
let print tr =
  (* val print_children : 'a trie M.t -> unit *)
  let rec print_child prefix key value =
    print_trie (prefix ^ key) value
  (* val print_trie : string -> 'a trie -> unit *)
  and print_trie prefix = function
    | Empty -> Printf.printf "%sEmpty\n" prefix
    | Node children -> M.iter (print_child prefix) children
    | ValueNode (value, children) ->
        Printf.printf "%s:%s\n" prefix value;
        M.iter (print_child prefix) children
  in print_trie "" tr

(* val lookup : string -> 'a trie -> 'a trie
 * Returns a node in the trie that matches the key or Empty otherwise
 **)
let rec lookup key tr =
  let parts = split_key key in
  match (tr, parts) with
  | (Empty, _) -> Empty
  | (_, Blank) -> Empty
  | (Node children, Last c) | (ValueNode (_, children), Last c) ->
      (match (M.find_opt c children) with
      | None | Some Empty -> Empty
      | Some node -> node
  | (Node children, More (c, rest)) | (ValueNode (_, children), More (c, rest)) ->
      (match (M.find_opt c children) with
      | None -> None
      | Some node -> lookup rest node)

(* val lookup_value : string -> 'a trie -> string option *)
let lookup_value key tr =
  match lookup key tr with
  | Empty -> None
  | Node _ -> None
  | ValueNode (value, _) -> Some value

(* val traverse : 'a trie -> 'a trie list *)
let traverse tr =
  let rec aux acc tr =
    match tr with
      | Empty -> acc
      | Node children ->
          tr :: (M.fold (fun _ child acc -> aux acc child) tr acc)
      | ValueNode (_, children) ->
          tr :: (M.fold (fun _ child acc -> aux acc child) tr acc)
  in aux [] tr

(* val traverse_values : 'a trie -> string list *)
let traverse_values tr =
  let rec values = function
    | [] -> []
    | Node _ :: nodes -> values nodes
    | ValueNode (value, _) :: nodes -> value :: (values nodes)
  in values (traverse tr)

(* val lookup_prefix : string -> 'a trie -> string list *)
let traverse_prefix prefix tr =
  match lookup prefix tr with
  | Empty -> []
  | _ as node -> traverse_values node

(* val remove : string -> 'a trie -> 'a trie *)
