(* A Trie is a tree with large branching order.
 * 'a is the value stored behind that key
 **)

open Printf

module String_map = Map.Make(String)

type 'a trie =
| Empty
| Node of { key: string option; value: string option; children: 'a trie String_map.t}

(* val upsert : string -> 'a -> 'a trie -> 'a trie *)
let rec upsert key value = function
  | Empty ->
      let root = Node { key=None; value=None; children=String_map.empty }
      in upsert key value root
  | Node {key=nkey; value=nvalue; children=nchildren } ->
      let nchildren = match split_string key with
        | (None, _) -> raise Not_found
        (* we've reached the last character in the key, so write the value*)
        | (Some hd, None) ->
            (match String_map.find_opt hd nchildren with
              (* node with hd does not exist -> create it with value, add it to the children *)
              | None | Some Empty ->
                  let node = Node { key=Some hd; value=Some value; children=String_map.empty }
                  in String_map.add hd node nchildren
              (* node with hd exists -> set/update the value on it *)
              | Some Node { children=fchildren } ->
                  let node = Node { key=Some hd; value=Some value; children=fchildren }
                  in String_map.add hd node nchildren)
        (* we're not done traversing the key characters *)
        | (Some hd, Some rest) ->
            (match String_map.find_opt hd nchildren with
              (* node with hd does not exist -> create it, add it to chilren then upset in it *)
              | None | Some Empty->
                  let node = Node { key=Some hd; value=None; children=String_map.empty }
                  in let node = upsert rest value node
                  in String_map.add hd node nchildren
              (* node with hd exists -> upsert in that node *)
              | Some Node { value=fvalue; children=fchildren } ->
                  let node = Node { key=Some hd; value=fvalue; children=fchildren }
                  in String_map.add hd node nchildren)
      in Node {key=nkey; value=nvalue; children=nchildren }

(* val print : 'a trie -> unit *)
let print t =
  let rec print_rec prefix = function
    | Empty -> Printf.printf "%s  Empty" prefix
    | Node { key; value; children } ->
        (match (key, value) with
        | (None, None) -> Printf.printf "root\n"
        | (None, Some _) -> raise Not_found
        | (Some k, None) -> Printf.printf "%s  %s:x\n" prefix k
        | (Some k, Some v) -> Printf.printf "%s   %s:%s\n" prefix k v);
        List.iter (fun (_, ch) -> print_rec (prefix ^ "  ") ch) (String_map.bindings children);
  in print_rec "" t

(* val lookup : string -> 'a trie -> 'a *)

(* val lookup_prefix: string -> string * 'a trie -> string * 'a list *)

(* val delete : string -> string * 'a trie -> string * 'a trie *)

(* val traverse : string * 'a trie -> string * 'a list *)

(* Utilities *)

(* val split_string : string -> string option * string option *)
let split_string s =
  let n = String.length s
  in if n = 0 then None, None
  else if n = 1 then Some s, None
  else
    let hd = String.sub s 0 1
    in let tl = String.sub s 1 (n - 1)
    in (Some hd, Some tl)
