module Counter exposing (view, Msg, Model, update, init)

import Html exposing (Html, div, h3, button, text)
import Html.Attributes exposing (..)
import Html.Events exposing (onClick, onInput)

type alias Model = {
  counter: Int
}

init : (Model, Cmd Msg)
init = ({
    counter = 0
  }, Cmd.none)

type Msg
  = Increment
  | Decrement
  | Reset

view : Model -> Html Msg
view model =
  div [] [
    h3 [] [ text "Counter" ],
    button [ onClick Decrement ] [ text "-" ],
    div [] [ text (toString model.counter) ],
    button [ onClick Increment ] [ text "+" ],
    button [ onClick Reset ] [ text "0" ]
  ]

update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
  case msg of
    Increment ->
      ({ model | counter = model.counter + 1 }, Cmd.none)
    Decrement ->
      ({ model | counter = model.counter - 1 }, Cmd.none)
    Reset ->
      ({ model | counter = 0 }, Cmd.none)
