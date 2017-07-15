(* See: http://odis.io/parser-combinators.html *)

open Format

(* val ( ||| ) : ('a -> 'b) -> ('a -> 'b) -> 'a -> 'b
 * It's going to match multiple parsers.
 * *)
let ( ||| ) p1 p2 s =
  try p1 s with Not_found -> p2 s

(* val ( ++ ) : ('a -> 'b * 'c) -> ('a -> 'd * 'e) -> 'a -> ('b * 'd) * 'e
 * Composes two parsers, first part of the string must match the first parser,
 * the rest of the string the second parser.
 * *)
let ( ++ ) p1 p2 s =
  let e1, s = p1 s in
  let e2, s = p2 s in
  (e1, e2), s

(* val many : ('a -> 'b * 'a) -> 'a -> 'b list * 'a
 * Matches multiple successive values against a parser function.
 * *)
let rec many p s =
  try
    let e, s = p s in
    let es, s = many p s in
    e::es, s
  with Not_found ->
    [], s

(* val ( >| ) ('a -> 'b * 'c) -> ('b -> 'd) -> 'a -> 'd * 'c
 * Used to pack a parser response into a value from the grammar!
 * *)
let ( >| ) p k i =
  let e, s = p i in
  k e, s

(* val some : ('a -> bool) -> 'a list -> 'a * 'a list
 * Checks if the head of the input list matches the given predicate.
 * *)
let some p = function
  | h :: t when p h -> h, t
  | _ -> raise Not_found

(* var a : 'a -> 'a list -> 'a * 'a list)
 * Matches a one and only one instance of the following parser.
 *)
let a x = some (( = ) x)

module Abstr : sig
  type t
  val x : t
end = struct
  type t = int
  let x = 0
end

(* val fin : 'a list -> Abstr.t * 'b list
 * Matches the end of the input list, ie when the rest is empty!
 * *)
let fin = function
  | [] as t -> Abstr.x, t
  | _ -> raise Not_found

type token =
  | IDENT of string
  | KWD of string
  | INT of string

(* var several : ('a -> bool) -> 'a list -> 'a list * 'a list
 * Matches as many leading items in the input list, returns a pair, first is a
 * list of matched elements, second is the list of remaining elements.
 * *)
let several p = many (some p)

(* val digit : char -> bool
 * Matches a digit.
 * *)
let digit = function
  | '0'..'9' -> true
  | _ -> false

(* val alpha : char -> bool
 * Matches an ASCII character.
 * *)
let alpha = function
  | 'a'..'z' | 'A'..'Z' -> true
  | _ -> false

(* val alphanum : char -> bool *)
let alphanum c = digit c || alpha c

(* val space : char -> bool *)
let space = function
  | ' ' | '\t' | '\n' -> true
  | _ -> false

(* val collect : char * char list -> string
 * Collects the matches characters in a string.
 * Usefull for building gramar types.
 * *)
let collect (h, t) =
  String.concat "" (List.map (String.make 1) (h :: t))

(* val rawindent : char list -> token * char list
 * Matches an IDENT token
 * *)
let rawindent =
  some alpha ++ several alphanum >| fun x -> IDENT (collect x)

(* val rawnumber: char list -> token * char list
 * Matches an INT token.
 * *)
let rawnumber =
  some digit ++ several digit >| fun x -> INT(collect x)

(* val rawkeyword : char list -> token * char list
 * Matches any non-IDENT|INT keyword and builds a KWD keyword.
 * *)
let rawkeyword =
  let p c = not (space c) && not (digit c) in
  some p ++ several p >| fun x -> KWD(collect x)

(* val token : char list -> token * char list
 * Matches a single token which can either be an indent, a number or a keyword followed by several spaces.
 * *)
let token =
  (rawindent ||| rawnumber ||| rawkeyword) ++ several space >| fst

(* val tokens : char list -> token list * char list
 * Matches as many tokens as possible.
 * *)
let tokens =
  several space ++ many token >| snd

(* val alltokens: char list -> token list * a' list
 * Matches all the tokens until the last end of the input list.
 **)
let alltokens =
  tokens ++ fin >| fst

(* val list_of_strings : string -> char list
 * Splits the input string into an efficient list of characters.
 * *)
let list_of_string str =
  let l = ref [] in
  String.iter (fun c -> l := c :: !l) str;
  List.rev !l

(* val lex : string -> token list
 * Parses the input string into a token stream.
 **)
let lex str =
  fst(alltokens(list_of_string str))

(* Up until this point we have a thing which parses the input string into a list of tokens. This is called a lexer!
 * We need to transform that list of tokens into a tree of tokens.
 * *)

(* Types what will compose the syntax tree *)
type expr =
  | Int of int
  | Var of string
  | Add of expr * expr
  | Mul of expr * expr
  | Pow of expr * expr

(* val ( +: ) expr -> expr -> expr
 * Implements the addition operator. Reduces complexity by replacing two ints added or additions to 0.
 * *)
let rec ( +: ) f g =
  match (f, g) with
  | (Int n, Int m) -> Int (n + m)
  | (Int 0, e) | (e, Int 0) -> e
  | (f, g) -> Add (f, g)

(* val ( *: ) expr -> expr -> expr
 * Implements the multiplication operator. Reduces complexity by replacing multiplication between two ints and multiplication with 0 or 1.
 * *)
let rec ( *: ) f g =
  match (f, g) with
  | (Int n, Int m) -> Int (n * m)
  | (Int 0, e) | (e, Int 0) -> Int 0
  | (Int 1, e) | (e, Int 1) -> e
  | (f, g) -> Mul (f, g)

(* val ( ^: ) expr -> expr -> expr
 * Implements the power operator. Reduces complex expressions in some well known cases.
 * *)
let rec ( ^: ) f g =
  match (f, g) with
  | (Int n, Int m) -> Int (int_of_float ((float_of_int n) ** (float_of_int m)))
  | (Int 0, _) -> Int 0
  | (_, Int 0) | (Int 1, _) -> Int 1
  | (e, Int 1) -> e
  | (f, g) -> Pow (f, g)

(* Helper functions to print the AST *)
let rec print_expr ff = function
  | Int n -> fprintf ff "%d" n
  | Var x -> fprintf ff "%s" x
  | Add (f, g) ->
      fprintf ff "%a + %a" print_expr f print_expr g
  | Mul (f, g) ->
      fprintf ff "%a %a" print_mul f print_mul g
  | Pow (f, g) ->
      fprintf ff "%a ^ %a" print_expr f print_expr g
and print_mul ff = function
  | Add _ as e -> fprintf ff "(%a)" print_expr e
  | e -> fprintf ff "%a" print_expr e

(* val ident : token list -> string * token list *)
let ident = function
  | IDENT x :: t -> x, t
  | _ -> raise Not_found

(* val int : token list -> string * token list *)
let int = function
  | INT n :: t -> n, t
  | _ -> raise Not_found

(* val atom : token list -> expr * token list
 * atom matches either an int, a variable or an expression enclosed in parantheses.
 * *)
let rec atom s =
  ((int >| fun n -> Int (int_of_string n)) |||
   (ident >| fun x -> Var x) |||
   (a (KWD "(") ++ term ++ a (KWD ")") >| fun ((_, e), _) -> e)) s
(* var factor : token list -> expr * token list
 * factor matches one or more atoms without a keyword between them, which
 * implies multiplication.
 *)
 and factor s =
   ((atom ++ factor >| fun (f, g) -> f *: g) ||| atom) s
(* var term : token list -> expr * token list
 * term parses plus and power operations.
 *)
 and term s =
   ((factor ++ a (KWD "+") ++ term >| fun ((f, _), g) -> f +: g) |||
    (factor ++ a (KWD "^") ++ term >| fun ((f, _), g) -> f ^: g) |||
    factor) s

(* val expr : token list -> expr * 'a list *)
let expr =
  term ++ fin >| fst

(* val parse : (token list -> 'a * 'b) -> string -> 'a
 * Parses a string into an AST
 **)
let parse p str =
  fst(p(lex str))

(* parse expr "a x x + b x + c"; *)
