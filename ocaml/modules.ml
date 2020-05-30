(* module type definition *)
module type Hello_type = sig
  val hello : unit -> unit
end

(* module defintion implements Hello_type module type *)
module Hello : Hello_type = struct
  let message = "Hello"
  let hello () = print_endline message
end

let goodbye () = print_endline "Goodbye!"

let hello_goodbye =
  Hello.hello () ;
  goodbye ()
