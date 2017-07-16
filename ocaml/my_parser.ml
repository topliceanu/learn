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

(* chr matches a character *)
let is_char c =
  match c with
  | 'A'..'Z' -> true
  | _ -> false


