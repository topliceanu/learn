import Html exposing (Html, button, div, text, ul, li)
import Html.Events exposing (onClick)

-- model
type alias Model = {
  counter: Int,
  history: List String
}

model : Model
model = {
    counter = 0,
    history = [ "initial" ]
  }

-- update
type Msg = Increment | Decrement | Reset

update : Msg -> Model -> Model
update msg model =
  case msg of
    Increment ->
      {
        counter = model.counter + 1,
        history = "inc" :: model.history
      }
    Decrement ->
      {
        counter = model.counter - 1,
        history = "dec" :: model.history
      }
    Reset ->
      {
        counter = 0,
        history = "reset" :: model.history
      }

-- view
showHist : List String -> Html Msg
showHist history =
  ul [] (List.map (\h -> li [] [text h]) history)

view : Model -> Html Msg
view model =
  div [] [
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

