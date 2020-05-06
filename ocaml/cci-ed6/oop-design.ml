(* 7.1 Deck of cards. Design the data structures for a generic deck of cards.
 * Explain how you would subclass the data structures to implement blackjack.
 **)

type suit =
  Club
| Diamond
| Heart
| Spade
type card =
  One
| Two
| Three
| Four
| Five
| Six
| Seven
| Eight
| Nine
| Ten
| Ace
| Jack
| Queen
| King

type deck = card list

type hand = card list

(* for some games, some cards are not available *)
exception Not_available

(* blackjack *)

(* val value : card -> int *)
let value = function
  | One -> raise Not_available
  | Two -> 2
  | Three -> 3
  | Four -> 4
  | Five -> 5
  | Six -> 6
  | Seven -> 7
  | Eight -> 8
  | Nine -> 9
  | Ten -> 10
  | Ace -> 1
  | Jack -> 11
  | Queen -> 12
  | King -> 13

(* val score : card list -> int *)
let score = function
  | [] -> 0
  | hd :: tl -> hd + score(tl)

let is_blackjack cs =
  score cs == 21
