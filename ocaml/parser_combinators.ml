let ( ||| ) p1 p2 s =
  try p1 s with Not_found -> p2 s

let ( ++ ) p1 p2 s =
  let e1, s = p1 s in
  let e2, s = p2 s in
  (e1, e2), s

let rec many p s =
  try
    let e, s = p s in
    let es, s = many p s in
    e::es, s
  with Not_found ->
    [], s

let ( >| ) p k i =
  let e, s = p i in
  k e, s
