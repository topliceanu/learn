open Opium.Std

let print_param =
  put "/hello/:name" (fun ({Request.body; _} as req) ->
    let body = Opium_kernel.Body.of_string ("Hello " ^ param req "name")
    in Response.make ~body ())

