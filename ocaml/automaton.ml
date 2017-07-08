module Label =
  type t = int
  let compare : t -> t -> int = Pervasives.compare
end
