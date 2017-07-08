type regexp =
  | Empty
  | Char of char
  | Concat of regexp * regexp
  | Choice of regexp * regexp (* | *)
  | AtLeastOnce of regexp (* + *)
  | AtMostOnce of regexp (* ? *)
  | ZeroOrMore of regexp (* * *)
  | Not of regexp (* ^ *)
  | Timeout of int * regexp (* <> *)

let x = "(a|b)c+d?e*^f<30s>g"
