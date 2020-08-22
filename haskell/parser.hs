-- Source: Monadic Combinator Parsers, Graham Hutton, Erik Meijer

-- alias for the type of all parser functions.
-- Note! If a parser fails, it will return the empty list.
type Parser a = String -> [(a, String)]

-- PRIMITIVE PARSERS

-- result always succeeds, it does not consume any input and returns the single result v
result :: a -> Parser a
result v => \inp -> [(v, inp)]

-- zero always fails (denoted by an empty result list) and does not consume any value
zero :: Parser Char
zero = \inp -> []

-- item consumes the first character of the input as log as the input is not empty.
item :: Parser Char
item = \inp -> case inp of
                [] -> []
                (x:xs) -> [(x, xs)]

-- PARSER COMBINATORS

-- combines two or multiple parsers. The parser p is applied to the input;
-- each of its outputs, it is applied to f which yields a new parser. The results
-- are concatenated
bind :: Parser a -> (a -> Parser b) -> Parser b
p `bind` f = \inp -> concat [f v inp' | (v, inp') <- p inp]

-- combines two parsers.
seq :: Parser a -> Parser b -> Parser (a, b)
p `seq` q = p `bind` \x ->
              q `bind` \y ->
                result (x, y)

-- consumes a character that matches the given predicate
sat :: (Char -> Bool) -> Parser Char
sat p = item `bind` \x -> if p x then result x else zero

-- char matches a specific character from the input
char :: Char -> Parser Char
char x = sat (\y -> x == y)

digit :: Parser Char
digit = sat (\x -> '0' <= x && x <= '9')

lower :: Parser Char
lower = sat (\x -> 'a' <= x && x <= 'z')

upper :: Parser Char
upper = sat (\x -> 'A' <= x && x <= 'Z')

-- plus combines two parsers in an OR fashion: either p or q succeed.
plus :: Parser a -> Parser a -> Parser a
p `plus` q = \inp -> (p inp ++ q inp)

letter :: Parser Char
letter = lower `plus` upper

alphanum :: Parser Char
alphanum = letter `plus` digit

word :: Parser String
word = neWord `plus` result ""
        where neWord = letter `bind` \x ->
                          word `bind` \xs ->
                            result (x:xs)

-- OLDER STUFF

-- the actual function which applies the parser on the input.
-- It's the identity function for parsers.
parse :: Parser a -> String -> [(a, String)] -- (String -> [(a, String)]) -> (String -> [(a, String)])
parse p input = p input

-- the single item parser function.
item :: Parser Char -- String -> [(Char, String)]
item [] = []
item (x:xs) = [(x, xs)]

-- a parser that always fails
failure :: Parser a -- String -> [(a, String)]
failure _ = []

-- a parser which always returns the value v without consuming any input
returns :: a -> Parser a -- a -> (String -> [(a, String)])
returns v = \input -> [(v, input)]

-- a parser which tries the first input parser, if that fails it tries the second input parser.
(+++) :: Parser a -> Parser a -> Parser a
p +++ q = \input -> case p input of
                      [] -> parse q input -- if p fails.
                      [(v, out)] -> [(v, out)] -- if p succeeds.

sat :: (Char -> Bool) -> Parser Char
sat p = do
  x <- item
  if p x then
    returns x
  else
    failure
