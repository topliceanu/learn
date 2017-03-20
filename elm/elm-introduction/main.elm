import Html exposing (Html, button, div, text, ul, li, input, h3, button, span)
import Html.Attributes exposing (..)
import Html.Events exposing (onClick, onInput)
import Random

-- model
type alias Model = {
  counter: Int,
  history: List String,
  content: String,
  name: String,
  pass: String,
  passAgain: String,
  age: String,
  isValid: Bool,
  validationErr: String,
  dieFaces: (Int, Int)
}

model : Model
model = {
    counter = 0,
    history = [ "initial" ],
    content = "",
    name = "",
    pass = "",
    passAgain = "",
    age = "20",
    isValid = False,
    validationErr = "",
    dieFaces = (1, 1)
  }

-- init
init : (Model, Cmd Msg)
init =
  (model, Cmd.none)

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
  | Age String
  | Submit
  -- dice roll
  | Roll
  | NewFace (Int, Int)

-- limits the number of items in a list
addToHistory : String -> List String -> List String
addToHistory update history =
  List.take 20 (update :: history)

modelValidation : Model -> (Bool, String)
modelValidation model =
  if model.name == "" then
    (False, "Name is empty")
  else if (String.length model.pass) < 8 then
    (False, "Password should be at least 8 chars long")
  else if model.pass /= model.passAgain then
    (False, "Passwords do not match")
  else
    (True, "")

update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
  case msg of
    Increment ->
      ({ model | counter = model.counter + 1, history = addToHistory "inc" model.history }, Cmd.none)
    Decrement ->
      ({ model | counter = model.counter - 1, history = addToHistory "dec" model.history }, Cmd.none)
    Reset ->
      ({ model | counter = 0, history = addToHistory "reset" model.history }, Cmd.none)
    Change newContent ->
      ({ model | content = newContent, history = addToHistory "content changed" model.history }, Cmd.none)
    Name newName ->
      ({ model | name = newName, history = addToHistory "name changed" model.history }, Cmd.none)
    Pass newPass ->
      ({ model | pass = newPass, history = addToHistory "password changed" model.history }, Cmd.none)
    PassAgain newPassAgain ->
      ({ model | passAgain = newPassAgain, history = addToHistory "re-entered password changed" model.history }, Cmd.none)
    Age newAge ->
      ({ model | age = newAge, history = addToHistory "updated age" model.history }, Cmd.none)
    Submit ->
      let (isValid, err) =
        modelValidation model
      in
        ({ model | isValid = isValid, validationErr = err, history = addToHistory "submit register" model.history }, Cmd.none)
    Roll ->
      (model, Random.generate NewFace (Random.pair (Random.int 1 6) (Random.int 1 6)))
    NewFace newFaces ->
      ({ model | dieFaces = newFaces, history = addToHistory "dices rolled" model.history }, Cmd.none)

-- renders the history as a UL of LIs
showHist : List String -> Html Msg
showHist history =
  ul [] (List.map (\h -> li [] [text h]) history)

viewValidation : Model -> Html msg
viewValidation model =
  let (color, message) =
    if model.isValid == False then
      ("red", model.validationErr)
    else
      ("green", "All OK!")
  in
    div [ style [ ("color", color) ] ] [ text message ]

-- view
view : Model -> Html Msg
view model =
  div [] [
    h3 [] [ text "Roll the dice" ],
    span [] [ text (toString (Tuple.first model.dieFaces)) ],
    span [] [ text (toString (Tuple.second model.dieFaces)) ],
    button [ onClick Roll ] [ text "Roll" ],

    h3 [] [ text "Signup Form" ],
    input [ type_ "test", placeholder "Name", onInput Name ] [],
    input [ type_ "password", placeholder "Password", onInput Pass ] [],
    input [ type_ "password", placeholder "Re-enter password", onInput PassAgain ] [],
    input [ type_ "number", value model.age, onInput Age ] [],
    button [ onClick Submit ] [ text "Submit" ],
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

-- subscriptions
subscriptions : Model -> Sub Msg
subscriptions model =
  Sub.none

-- application
main =
  Html.program {
    init = init,
    view = view,
    update = update,
    subscriptions = subscriptions
  }
