type input = char list
(** Parser input is a list of characters. *)

module Parser : sig
  (** This interface implements a basic monadic parser. *)

  (* Questions:
    * - where is result defined? stdlib, it's like Either
    * - the type has changed to accomodate errors!
    * - why do you need to duplicate it in the implementation?
    * *)
  type 'a t = input -> ('a * input, string) result
  (** Parser is a function from input to an intermediate value and the leftover
     of input, or an error if parsing fails. *)

  val run : 'a t -> input -> 'a
  (** [run p input] is the result of running the parser [p] with [input].
      @raises an exception with an error message if the parsing fails. *)

  val empty : 'a t
  (** [empty] is a parser that always fails regardless of the input. *)

  val unit : 'a -> 'a t
  (* [unit x] puts [x] into the parser structure. Also known as `return` or
     `pure` in the Monad interface. *)

  val and_then : ('a -> 'b t) -> 'a t -> 'b t
  (** [and_then handler p] runs the parser [p] and feeds its result into the
      [handler] producing a new parser. *)
end

