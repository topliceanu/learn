(* Logic and Codes *)
open Format

type bool_expr =
  Var of string
| Not of bool_expr
| And of bool_expr * bool_expr
| Or of bool_expr * bool_expr

(* 46 & 47. Truth tables for logical expressions (2 variables). (medium)
 * Define a function, table2 which returns the truth table of a given logical
 * expression in two variables (specified as arguments).
 * The return value must be a list of triples containing
 * (value_of_a, value_of_b, value_of_expr).
 *
 * - generate all combinations [true, false] for (a, b)
 * - evaluate expression with bool inputs
 * var table2 : string -> string -> bool_expr -> (bool * bool * bool) list
 **)
let table2 a b expr =
  (* val eval_aux : string -> bool -> string -> bool -> bool_expr -> bool *)
  let rec eval_aux a a_val b b_val = function
    | Var x ->
        if x = a then a_val
        else if x = b then b_val
        else failwith "invalid variable in expression"
    | Not expr ->
        let expr_val = eval_aux a a_val b b_val expr in not expr_val
    | And (left, right) ->
        let left_val = eval_aux a a_val b b_val left
        in let right_val = eval_aux a a_val b b_val right
        in left_val && right_val
    | Or (left, right) ->
        let left_val = eval_aux a a_val b b_val left
        in let right_val = eval_aux a a_val b b_val right
        in left_val || right_val
  (* val vals : bool * bool list *)
  in let vals = [(true, true); (true, false); (false, true); (false, false)]
  (* val apply_aux : bool_expr -> bool * bool list -> (bool * bool * bool) list *)
  in let rec apply_aux expr = function
    | [] -> []
    | (a_val, b_val) :: xs -> (a_val, b_val, (eval_aux a a_val b b_val expr)) :: apply_aux expr xs
  in apply_aux expr vals

(* 48. Truth tables for logical expressions. (medium)
 * Generalize the previous problem in such a way that the logical expression may
 * contain any number of logical variables. Define table in a way that table
 * variables expr returns the truth table for the expression expr, which contains
 * the logical variables enumerated in variables.
 *
 * val table : string list -> bool_expr -> ((string * bool list) * bool) list
 **)
let table symbols expr =
  (* val combinations : int -> bool list list*)
  let combinations n =
    let rec append x = function
      | [] -> []
      | xs :: xss -> (x :: xs) :: append x xss
    in let rec aux n =
      if n = 0 then []
      else if n = 1 then [ [true]; [false] ]
      else
        let xs = aux (n-1)
        in List.append (append true xs) (append false xs)
    in aux n
  (* val lookup : string -> (string * bool) list -> bool *)
  in let rec lookup symbol table =
    match table with
    | [] -> failwith "symbol not found"
    | (s, v) :: tl ->
        if s = symbol then v
        else lookup symbol tl
  (* val evaluate : bool_expr -> (string * bool) list -> bool *)
  in let rec evaluate expr table =
    match expr with
      | Var symbol -> lookup symbol table
      | Not e1 -> not (evaluate e1 table)
      | And (e1, e2) -> (evaluate e1 table) && (evaluate e2 table)
      | Or (e1, e2) -> (evaluate e1 table) || (evaluate e2 table)
  in let comb = combinations (List.length symbols)
  in let tables = List.map (fun c -> List.combine symbols c) comb
  in List.map (fun t -> (t, evaluate expr t)) tables

(* 49. Gray code. (medium). An n-bit Gray code is a sequence of n-bit strings
 * constructed according to certain rules:
 * n = 1: C(1) = ['0','1']
 * n = 2: C(2) = ['00','01','11','10'] - 0 1 3 2
 * n = 3: C(3) = ['000','001','011','010',´110´,´111´,´101´,´100´] - 0 1 3 2 6 7 5 4
 * Find out the construction rules and write a function with the following
 * specification: gray n returns the n-bit Gray code.
 *
 * val gray : int -> string list
 **)
let gray n =
  (* val append : int -> string list -> string list *)
  let rec append i = function
    | [] -> []
    | x :: xs ->
        if i mod 2 = 0 then (x^"0") :: (x^"1") :: append (i+1) xs
        else (x^"1") :: (x^"0") :: append (i+1) xs
  (* val iter : int -> string list *)
  in let rec iter n =
    if n == 1 then ["0"; "1"]
    else append 0 (iter (n-1))
  in iter n

(* 50 Huffman code (hard)
 **)

type tree = Empty | Node of tree * string * int * tree

(* val huffman : string * int list -> string * string list *)
let huffman probabilities =
  let build_min_heap pairs =
    let sorted = List.sort (fun (s1, p1) (s2, p2) -> compare p1 p2) pairs in
    List.map (fun (x, p) -> Node (Empty, x, p, Empty)) sorted

  in let get_prob = function
    | Empty -> raise Not_found
    | Node (_, _, prob, _) -> prob

  in let rec insert_min_heap tree heap =
    let cmp t1 t2 =
      let p1, p2 = (get_prob t1), (get_prob t2) in compare p1 p2
    in List.sort cmp (tree :: heap)

  in let merge left right =
    match (left, right) with
      | (Empty, Empty) -> Empty
      | (Empty, (Node _ as node)) -> node
      | ((Node _ as node), Empty) -> node
      | (Node (_, lstr, lprob, _), Node (_, rstr, rprob, _)) ->
          if lprob >= rprob then
            Node(left, lstr ^ rstr, lprob + rprob, right)
          else
            Node(right, rstr ^ lstr, rprob + lprob, left)

  in let rec build_tree = function
    | [] -> []
    | hd :: [] -> hd :: []
    | hd1 :: hd2 :: rest ->
        let merged = merge hd1 hd2 in
        let new_heap = insert_min_heap merged rest in
        build_tree new_heap

  in let rec encoding prefix output = function
    | Empty -> output
    | Node (Empty, str, prob, Empty) ->
        (str, prefix) :: output
    | Node (left, str, prob, right) ->
        let left_enc = encoding (prefix^"1") output left in
        let right_enc = encoding (prefix^"0") output right in
        left_enc @ right_enc

  in let heap = build_min_heap probabilities
  in let result = build_tree heap
  in let encodings = encoding "" [] (List.hd result)
  in encodings

(* TODO val huffman_encode : string * string list -> string -> string *)
