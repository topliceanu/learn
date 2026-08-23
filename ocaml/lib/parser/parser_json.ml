(* Attempt to build a JSON parser using monadic parsing or functional parsing
 * Inspired by Chapter 13 from the book "Programming in Haskell" by Graham Hutton.
 * For an OCaml implementation https://github.com/pyrocat101/opal/blob/master/opal.ml
 * Also https://odis.io/parser-combinators.html
 **)

type 'a parser = char list -> ('a * char list) list

(* val parse : parser -> char list -> ('a * char list) list *)
let parse p inp = p inp

(* item : 'a parser
 * Consumes a single character from the input
 **)
let item = function
  | [] -> []
  | x :: xs -> [ (x, xs) ]

let pure a inp = [ (a, inp) ]



