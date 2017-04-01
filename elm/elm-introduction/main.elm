import Html exposing (Html, button, div, text, ul, li, input, h3, button, span, img, p, select, option)
import Html.Attributes exposing (..)
import Html.Events exposing (onClick, onInput)
import Http
import Random
import Json.Decode as Decode
import Svg
import Svg.Attributes as SAttr

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
  dieFaces: (Int, Int),
  topic: String,
  gifUrl: String,
  disableMoreButton: Bool,
  error: String
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
    dieFaces = (1, 1),
    topic = "cats",
    gifUrl = "waiting.gif",
    disableMoreButton = False,
    error = ""
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
  -- fetch cat gifs with http api
  | More
  | NewGif (Result Http.Error String)
  | ChangeTopic String

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

-- rolls the two dices and return a message with a function that returns two random number
rollDices : Cmd Msg
rollDices = Random.generate NewFace (Random.pair (Random.int 1 6) (Random.int 1 6))

decodeResponse : Decode.Decoder String
decodeResponse = Decode.at ["data", "image_url"] Decode.string

-- retrieves a random topic gif
getRandomGif : String -> Cmd Msg
getRandomGif topic =
  let
    url = "https://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=" ++ topic
    request = Http.get url decodeResponse
  in
    Http.send NewGif request

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
      (model, rollDices)
    NewFace newFaces ->
      ({ model | dieFaces = newFaces, history = addToHistory "dices rolled" model.history }, Cmd.none)
    More ->
      ({ model | disableMoreButton = True , history = addToHistory "ask for another image" model.history }, getRandomGif model.topic)
    NewGif (Ok newUrl) ->
      ({ model | gifUrl = newUrl, error = "", disableMoreButton = False }, Cmd.none)
    NewGif (Err e) ->
      ({ model | error = (toString e), disableMoreButton = False, history = addToHistory "error fetching image" model.history }, Cmd.none)
    ChangeTopic newTopic ->
      ({ model | topic = newTopic, history = addToHistory "change topic" model.history }, Cmd.none)

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

isError : String -> Bool
isError err =
  case err of
    "" -> False
    _ -> True

-- displays an ul with topic options.
topicSelect : Model -> List String -> Html Msg
topicSelect model options =
  let htmlOpts =
    List.map (\o -> option [ selected (model.topic == o), value o ] [ text o ]) options
  in
    select [ onInput ChangeTopic ] htmlOpts

-- display an svg dice face
dot : Int -> List Int -> String -> String -> Svg.Svg Msg
dot n valid x y =
  if (List.member n valid) then
      Svg.circle [SAttr.cx x, SAttr.cy y, SAttr.r "5", SAttr.fill "white"] []
  else
      Svg.circle [SAttr.cx x, SAttr.cy y, SAttr.r "5", SAttr.fill "black"] []

displayDiceFace : Int -> Html Msg
displayDiceFace face =
  Svg.svg [ SAttr.version "1.1", SAttr.width "100", SAttr.height "100", SAttr.viewBox "0 0 100 100" ] [
    Svg.rect [ SAttr.x "0", SAttr.y "0", SAttr.width "100", SAttr.height "100", SAttr.rx "15", SAttr.ry "15", SAttr.color "black" ] [],
    dot face [4, 5, 6] "40" "40",
    dot face [6] "60" "40",
    dot face [4, 5, 6] "80" "40",

    dot face [2, 3] "40" "60",
    dot face [1, 3, 5] "60" "60",
    dot face [2, 3] "80" "60",

    dot face [4, 5, 6] "40" "80",
    dot face [6] "60" "80",
    dot face [4, 5, 6] "80" "80"
  ]

renderClock Int -> Html Msg
rencerClock curTime =
  let
    angle = turns (Time.inMinutes curTime)
    handX = toString (50 + 40 * cos angle)
    handY = toString (50 + 40 * sin angle)
  in
    Svg.svg [ SAttr.viewBox "0 0 100 100", SAttr.width "300px" ] [
      Svg.circle [ SAttr.cx "50", SAttr.cy "50", SAttr.r "45", SAttr.fill "#0B79CE" ] [],
      Svg.line [ SAttr.x1 "50", SAttr.y1 "50", SAttr.x2 handX, y2 SAttr.handY, SAttr.stroke "#023963" ] []
    ]

-- view
view : Model -> Html Msg
view model =
  div [] [
    p [ hidden (not (isError model.error))] [ text model.error ],

    h3 [] [ text "Cat pics" ],
    img [ src model.gifUrl ] [],
    button [ onClick More, disabled model.disableMoreButton ] [ text "More Pictures!" ],
    topicSelect model [ "cats", "dogs", "unicorns" ],

    h3 [] [ text "Roll the dice" ],
    displayDiceFace (Tuple.first model.dieFaces),
    displayDiceFace (Tuple.second model.dieFaces),
    --span [] [ text (toString (Tuple.first model.dieFaces)) ],
    --span [] [ text (toString (Tuple.second model.dieFaces)) ],
    button [ onClick Roll ] [ text "Roll" ],

    h3 [] [ text "Signup Form" ],
    input [ type_ "text", placeholder "Name", onInput Name ] [],
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
