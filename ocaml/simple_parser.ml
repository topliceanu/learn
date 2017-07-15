(*
 * Work-in-progress implementation of a simple parser combinator library.
 *)
type input = char list
(** Parser input is a list of characters. *)

(* Implementation of the Parser interface. *)
module Parser = struct
  type 'a t = input -> ('a * input, string) result

  let run parser input =
    match parser input with
    | Ok (x, _rest) -> x
    | Error msg -> failwith msg

  let unit x =
    fun input -> Ok (x, input)

  let empty =
    fun input -> Error "empty"

  let and_then handler p1 =
    fun input ->
      match p1 input with
      | Ok (x, rest) ->
        let p2 = handler x in
        p2 rest
      | Error msg -> Error msg
end


(* Tests *)

open Parser

(* Regardless of the input this parser will fail and don't run the handler. *)
let test_empty_parser () =
  let parser =
    empty |> and_then (fun x -> print_endline "No!"; unit x) in
  assert (parser ['2'; '+'; '2'] = Error "empty")


(* Regardless of the input this parser will succeed parsing 42. *)
let test_unit_parser () =
  let parser =
    unit 42 |> and_then (fun x -> print_endline "Yes!"; unit x) in
  assert (run parser ['2'; '+'; '2'] = 42)

let () =
  test_empty_parser ();
  test_unit_parser ()

