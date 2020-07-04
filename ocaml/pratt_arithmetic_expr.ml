(* This file contains a parser and evaluator for a simple arithmetic expression:
  * - all the numbers are positive integers - no floating point or negative numbers.
  * - allowed operators are + - * / ^
  * - support for parantheses
  **)

(***************** TOKENIZE ****************)

type token =
  Number of int
| LeftParan
| RightParan
| Add
| Subtract
| Multiply
| Divide
| Pow

(* let tokenize : string -> token list *)
let tokenize s =

  (* let string_to_chars : string -> char list *)
  let string_to_chars s =
    List.init (String.length s) (String.get s)

  (* let consume_digit : char list -> char list * char list *)
  in let consume_digit = function
    | [] -> ([], [])
    | hd :: tl as l ->
        match hd with
          |'0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9' -> ([hd], tl)
          | _ -> ([], l)

  (* consume_multiple : char list -> char list * char list *)
  in let consume_multiple parser_func input =
    let rec aux acc fn xs =
      match fn xs with
        | ([], rest) -> (acc, rest)
        | (matched, rest) -> aux (acc @ matched) fn rest
    in aux [] parser_func input

  (* consume_int : char list -> char list * char list
   * Parses zero, one or more digits from the input
   **)
  in let rec consume_int = consume_multiple consume_digit

  (* let to_int : char list -> int *)
  in let to_int chars =
    let buf = Buffer.create 16
    in List.iter (Buffer.add_char buf) chars;
    let str = Buffer.contents buf
    in int_of_string str

  (* let consume : list char -> list token *)
  in let rec consume l =
    match l with
      | [] -> []
      | hd :: tl ->
          match hd with
            |'0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9' ->
                let num_chars, rest = consume_int l
                in (Number (to_int num_chars)) :: (consume rest)
            | '(' -> LeftParan :: (consume tl)
            | ')' -> RightParan :: (consume tl)
            | '+' -> Add :: (consume tl)
            | '-' -> Subtract :: (consume tl)
            | '*' -> Multiply :: (consume tl)
            | '/' -> Divide :: (consume tl)
            | '^' -> Pow :: (consume tl)
            | _ -> raise Not_found

  in consume (string_to_chars s)

(**************** PARSE ***************)

type expr =
  Value of int
| Addition of expr * expr
| Subtraction of expr * expr
| Multiplication of expr * expr
| Division of expr * expr
| Power of expr * expr

(* val precedence : token -> int *)
let precedence op =
  match op with
  | Add -> 2
  | Subtract -> 2
  | Multiply -> 3
  | Divide -> 3
  | Pow -> 4
  | _ -> -1

type associativity = Left | Right

(* val assoc : token -> associativity *)
let assoc op =
  match op with
  | Pow -> Right
  | _ -> Left

(* val split_while : ('a -> bool) -> 'a list -> 'a list * 'a list
 * Utility to split a list in two: the first list contains all successive elements that
 * match the predicate, stops at the first that doesn't pass the predicate anymore.
 * The second contains everything else in the list.
 * *)
let split_while pred xs =
  let rec aux left right =
    match right with
    | [] -> left, right
    | x :: xs ->
        if pred x then aux (x :: left) xs
        else left, right
  in aux [] xs

(* let shunting_yard : token list -> token list
 * Transforms an infix list of tokens into a postfix list of tokens.
 * See https://rosettacode.org/wiki/Parsing/Shunting-yard_algorithm#OCaml
 * *)
let shunting_yard tokens =
  (* let pusher : token list -> token list -> token list -> token list *)
  let rec pusher stack queue = function
    | [] -> (List.rev queue) @ stack (* append stack at the end of the queue *)
    | LeftParan :: tokens' -> pusher (LeftParan :: stack) queue tokens'
    | RightParan :: tokens' ->
        (* push everything inside the parans onto the queue *)
        let inside_parans, stack' = split_while (fun x -> x <> LeftParan) stack
        in pusher (List.tl stack') (inside_parans @ queue) tokens'
    | number :: tokens' when precedence number < 0 ->
        pusher stack (number :: queue) tokens'
    | op:: tokens' ->
        (* val should_move_to_queue : token -> bool *)
        let should_move_to_queue op' =
          (match assoc op' with
            | Left -> precedence op <= precedence op'
            | Right -> precedence op < precedence op')
        in let to_move, stack' = split_while should_move_to_queue stack
        in pusher (op :: stack') (to_move @ queue) tokens'
  in pusher [] [] tokens

(* val build_ast : token list -> expr list
 * Builds an AST from a postfix list of tokens.
 * *)
let build_ast tokens =
  (* val pop_twice : 'a list -> ('a * 'a) *)
  let pop_twice = function
    | x :: x' :: xs -> (x, x', xs)
    | _ -> raise Not_found
  (* val aux : expr list -> token list -> expr list *)
  in let rec aux stack = function
    | [] -> stack
    | Number x :: toks -> aux((Value x) :: stack) toks
    | Add :: toks ->
        let h, h', stack' = pop_twice stack
        in aux (Addition (h', h) :: stack') toks
    | Subtract :: toks ->
        let h, h', stack' = pop_twice stack
        in aux (Subtraction (h', h) :: stack') toks
    | Multiply :: toks ->
        let h, h', stack' = pop_twice stack
        in aux (Multiplication (h', h) :: stack') toks
    | Divide :: toks ->
        let h, h', stack' = pop_twice stack
        in aux (Division (h', h) :: stack') toks
    | Pow :: toks ->
        let h, h', stack' = pop_twice stack
        in aux (Power (h', h) :: stack') toks
    | LeftParan :: _ | RightParan :: _ -> raise Not_found
  in let exprs = aux [] tokens
  in List.hd exprs

(* let parse : token list -> expr *)
let parse tokens =
  let postfix = shunting_yard tokens
  in build_ast postfix

(****************** EVALUATE *****************)

(* let evaluate : expr -> int *)
let rec evaluate = function
  | Value a -> a
  | Addition (e1, e2) -> (evaluate e1) + (evaluate e2)
  | Subtraction (e1, e2) -> (evaluate e1) - (evaluate e2)
  | Multiplication (e1, e2) -> (evaluate e1) * (evaluate e2)
  | Division (e1, e2) -> (evaluate e1) / (evaluate e2)
  | Power (e1, e2) -> int_of_float ((float_of_int (evaluate e1)) ** (float_of_int (evaluate e2)))
