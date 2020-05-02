(* binary search tree*)
type 'a bst =
  | Leaf
  | Node of 'a bst * 'a * 'a bst

(* problem 4.5 in CCI book, ed 6
 * val is_bst : 'a bst -> bool *)
let rec is_bst = function
  | Leaf -> true
  | Node (Leaf, root, Leaf) -> true
  | Node ((Node (_, left, _) as left_bst), root, Leaf) ->
      left <= root && is_bst left_bst
  | Node (Leaf, root, (Node (_, right, _) as right_bst)) ->
      root < right && is_bst right_bst
  | Node ((Node (_, left, _) as left_bst), root, (Node (_, right, _) as right_bst)) ->
    left <= root && root < right && (is_bst left_bst) && (is_bst right_bst)

(* undirected or directed graph *)
type 'a graph = {
  vertices: 'a list;
  edges: ('a * 'a) list;
}

(* val dfs : 'a graph -> 'a -> 'a list *)
(* FIXME *)
let dfs { vertices; edges } src =
  (* adjacent : 'a -> ('a * 'a) list -> 'a list *)
  let rec adjacent vertex = function
    | [] -> []
    | (hd, tl) :: rest ->
        if vertex == hd then tl :: adjacent vertex rest
        else if vertex == tl then hd :: adjacent vertex rest
        else adjacent vertex rest

  (* val rdfs : 'a list -> ('a * 'a) list -> 'a -> 'a list *)
  in let rec rdfs visited edges vertex =
    if (List.mem vertex visited) then visited
    else
      List.fold_left
        (fun visited adjacent_vertex -> rdfs visited edges adjacent_vertex )
        (vertex :: visited)
        (adjacent vertex edges)

  in rdfs [] edges src

(* let g = { vertices=[1; 2; 3; 4; 5]; edges=[(1, 2); (1, 3); (2, 3); (4, 5)] } ;; *)
