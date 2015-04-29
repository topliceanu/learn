import Data.Char


-- computes xor of two boolean values.
xor :: Bool -> Bool -> Bool
xor a b = not (a == b)

-- returns the lowercase version of the input string.
toLowerCase :: [Char] -> [Char]
toLowerCase s = [if ('A' <= c) && (c <= 'Z') then chr ((ord c) + 32) else c | c <- s]

-- return the uppercase version of the input string.
toUpperCase :: [Char] -> [Char]
toUpperCase s = [if ('a' <= c) && (c <= 'z') then chr ((ord c) - 32) else c | c <- s]

-- extracting data from triples:
first :: (a, b, c) -> a
first (x, _, _) = x

second :: (a, b, c) -> b
second (_, y, _) = y

third :: (a, b, c) -> c
third (_, _, z) = z

-- capitalizes the first letter of a given word
capitalize :: [Char] -> [Char]
capitalize [] = []
capitalize (x:xs) = (toUpperCase [x]) ++ xs

-- computes factorial of a number.
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n-1)

-- computes the body mass index
bmi :: Float -> Float -> [Char]
bmi weight height
    | index <= skinny = "underweight"
    | index <= normal = "normal"
    | index <= fat    = "overweight"
    | otherwise       = "obese"
    where index = weight / height ^ 2
          skinny = 18.5
          normal = 25.0
          fat = 30.0
