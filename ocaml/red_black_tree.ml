(* OCaml implementation of a red-black binary ballanced search tree.
 * The invariants are:
 * - Each node is either Black or Red
 * - The root is always Black
 * - No Red node has a Red parent.
 * - Every path from root to Empty passes through the same number of Black nodes.
 * Reference: https://www.cs.cornell.edu/courses/cs3110/2009sp/lectures/lec11.html
 * *)

type color = Red | Black

type 'a rbtree =
    Empty
  | Node of color * 'a * 'a rbtree * 'a rbtree

let rec lookup x root =
  match root with
      Empty -> false
    | Node (_, y, left, right) ->
        if x = y then true
        else if x < y then lookup x left
        else lookup x right

let balance node =
  match node with
      Black, z, Node (Red, y, Node (Red, x, a, b), c), d
    | Black, z, Node (Red, x, a, Node (Red, y, b, c)), d
    | Black, x, a, Node (Red, z, Node (Red, y, b, c), d)
    | Black, x, a, Node (Red, y, b, Node (Red, z, c, d)) ->
        Node (Red, y, Node (Black, x, a, b), Node (Black, z, c, d))
    | a, b, c, d ->
        Node (a, b, c, d)

let rec insert_red parent x =
  match parent with
    Empty -> Node (Red, x, Empty, Empty)
  | Node (color, y, left, right) ->
      if x < y
      then balance (Node (color, y, (insert_red left x), right))
      else if x > y
      then balance (Node (color, y, left, (insert_red right x)))
      else parent

let insert x root =
  let new_root = insert_red root x in
  match new_root with
      Node (_, y, left, right) ->
        Node(Black, y, left, right)
    | Empty ->
        raise (Failure "Root cannot be empty after an insertion")
