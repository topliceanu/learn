import Html exposing (Html, button, div, text, ul, li, input, h3)
import Html.Attributes exposing (..)
import Html.Events exposing (onClick, onInput)

-- model
type alias Model = {
  counter: Int,
  history: List String,
  content: String,
  name: String,
  pass: String,
  passAgain: String
}

model : Model
model = {
    counter = 0,
    history = [ "initial" ],
    content = "",
    name = "",
    pass = "",
    passAgain = ""
  }

-- update
type Msg
  -- counter
  = Increment
  | Decrement
  | Reset
  | Change String
  -- register form, the inputs will be changed separately
  | Name String
  | Pass String
  | PassAgain String

-- limits the number of items in a list
addToHistory : String -> List String -> List String
addToHistory update history =
  List.take 20 (update :: history)

update : Msg -> Model -> Model
update msg model =
  case msg of
    Increment ->
      { model | counter = model.counter + 1, history = addToHistory "inc" model.history }
    Decrement ->
      { model | counter = model.counter - 1, history = addToHistory "dec" model.history }
    Reset ->
      { model | counter = 0, history = addToHistory "reset" model.history }
    Change newContent ->
      { model | content = newContent, history = addToHistory "content changed" model.history }
    Name newName ->
      { model | name = newName, history = addToHistory "name changed" model.history }
    Pass newPass ->
      { model | pass = newPass, history = addToHistory "password changed" model.history }
    PassAgain newPassAgain ->
      { model | passAgain = newPassAgain, history = addToHistory "re-entered password changed" model.history }

-- renders the history as a UL of LIs
showHist : List String -> Html Msg
showHist history =
  ul [] (List.map (\h -> li [] [text h]) history)

viewValidation : Model -> Html msg
viewValidation model =
  let (color, message) =
    if model.pass == model.passAgain then
      ("green", "All OK!")
    else
      ("red", "Passwords do not match")
  in
    div [ style [ ("color", color) ] ] [ text message ]

-- view
view : Model -> Html Msg
view model =
  div [] [
    h3 [] [ text "Signup Form" ],
    input [ type_ "test", placeholder "Name", onInput Name ] [],
    input [ type_ "password", placeholder "Password", onInput Pass ] [],
    input [ type_ "password", placeholder "Re-enter password", onInput PassAgain ] [],
    viewValidation model,

    h3 [] [ text "Reversing Text" ],
    input [ placeholder "Text to reverse", onInput Change ] [],
    div [] [ text (String.reverse model.content) ],

    h3 [] [ text "Counter" ],
    button [ onClick Decrement ] [ text "-" ],
    div [] [ text (toString model.counter) ],
    button [ onClick Increment ] [ text "+" ],
    button [ onClick Reset ] [ text "0" ],

    h3 [] [ text "history" ],
    showHist(model.history)
  ]

-- application
main =
  Html.beginnerProgram {
    model = model,
    view = view,
    update = update
  }

