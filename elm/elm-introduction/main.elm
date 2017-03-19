import Html exposing (Html, button, div, text, ul, li, input)
import Html.Attributes exposing (..)
import Html.Events exposing (onClick, onInput)

-- model
type alias Model = {
  counter: Int,
  history: List String,
  content: String
}

model : Model
model = {
    counter = 0,
    history = [ "initial" ],
    content = ""
  }

-- update
type Msg = Increment
  | Decrement
  | Reset
  | Change String

update : Msg -> Model -> Model
update msg model =
  case msg of
    Increment ->
      { model | counter = model.counter + 1, history = "inc" :: model.history }
    Decrement ->
      { model | counter = model.counter - 1, history = "dec" :: model.history }
    Reset ->
      { model | counter = 0, history = "reset" :: model.history }
    Change newContent ->
      { model | history = "content changed" :: model.history, content = newContent }

-- view
showHist : List String -> Html Msg
showHist history =
  ul [] (List.map (\h -> li [] [text h]) history)

view : Model -> Html Msg
view model =
  div [] [
    input [ placeholder "Text to reverse", onInput Change ] [],
    div [] [ text (String.reverse model.content) ],
    button [ onClick Decrement ] [ text "-" ],
    div [] [ text (toString model.counter) ],
    button [ onClick Increment ] [ text "+" ],
    button [ onClick Reset ] [ text "0" ],
    showHist(model.history)
  ]

-- application
main =
  Html.beginnerProgram {
    model = model,
    view = view,
    update = update
  }

