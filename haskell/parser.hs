-- alias for the type of all parser functions.
-- Note! If a parser fails, it will return the empty list.
type Parser a = String -> [(a, String)]

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
