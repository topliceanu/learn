(* Logic and Codes *)

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

let table symbols expr =
  let comb = combinations (List.length symbols)
  let groups = List.map (fun c -> List.zip symbols c) comb
