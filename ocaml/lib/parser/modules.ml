(* source: https://ocaml.org/learn/tutorials/modules.html *)

(* submodule implementation *)
module Hello1 = struct
  let message = "hello1"
  let hello () = print_endline message
end

(* submodule interface *)
module Hello2 : sig
  val hello = unit -> unit
end =
  struct
    let message = "hello2"
    let hello () = print_endline message
  end

(* module type definition *)
module type Hello_type = sig
  val hello : unit -> unit
end

(* module defintion implements Hello_type module type *)
module Hello3 : Hello_type = struct
  let message = "Hello"
  let hello () = print_endline message
end

let goodbye () = print_endline "Goodbye!"

let hello_goodbye =
  Hello3.hello () ;
  goodbye ()
