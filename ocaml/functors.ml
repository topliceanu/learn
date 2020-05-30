module Int_set = Set.Make (
  struct
    type t = int
    let compare = compare
  end
)

module String_set = Set.Make (String)
