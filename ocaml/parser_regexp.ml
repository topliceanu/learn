(* A lexer transforms a string into a list of tokens.
 *    string -> char list -> ... -> token list
 *
 * Each transformation in the chain consumes as much chars as needed to
 * produce a token, then returns the token and the rest of the char list.
 *    char list -> token * char list
 *
 * A parser takes a list of tokens and transforms it into an AST.
 *    token list -> 'a
 *)

type token =
  | Ident of string (* includes all the event characters *)
  | Kwd of string (* includes all the supported special character: *, +, ?, ., <> *)

let string_to_char_list str =
  let l = ref [] in
  String.iter (fun c -> l := c :: !l) str;
  List.rev !l

(* is_alpha : char -> bool
 * Matches an alphabetical character.
 * *)
let is_aplha = function
  | 'a'..'z' | 'A'..'Z' -> true
  | _ -> false

(* val build_ident : char -> token *)
let build_ident c =
  Ident c

(* val char list -> list token * char list *)


(* var lexer: string -> Token list *)
let lexer str =
  (string_to_char_list str)
