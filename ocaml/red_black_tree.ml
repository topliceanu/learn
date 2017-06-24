type node =
    Empty
  | Node of node * int * node ;;

let rec insert root value =
  match root with
    | Empty ->
        Node (Empty, value, Empty) (* value constructors are regular functions which receive a tuple *)
    | Node (left, existing, right) ->
        if existing > value (* how does it know to compare this things *)
        then Node (left, existing, (insert right value))
        else Node ((insert left value), existing, right)

let rec lookup root value =
  match root with
    | Empty -> false
    | Node (left, existing, right) ->
        if existing == value (* how does it know how to compare these things *)
        then true
        else (lookup left value) || (lookup right value)

let root = insert (insert (insert (insert (insert (insert Empty 1) 2) 3) 4) 5) 6
let () =
  let found = lookup root 7 in
  let printable = string_of_bool found in
  print_endline printable
