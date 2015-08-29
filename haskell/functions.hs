import Data.Char


-- our own version of and, this is more efficient because it only evaluates
-- the first argument of the function.
and' :: Bool -> Bool -> Bool
and' True b = b
and' False _ = False

-- computes xor of two boolean values.
xor :: Bool -> Bool -> Bool
xor a b = not (a == b)

-- returns the lowercase version of the input string.
toLowerCase :: [Char] -> [Char]
toLowerCase s = [if elem c ['A'..'Z'] then chr ((ord c) + 32) else c | c <- s]

-- return the uppercase version of the input string.
toUpperCase :: [Char] -> [Char]
toUpperCase s = [if elem c ['a'..'z'] then chr ((ord c) - 32) else c | c <- s]

-- mimics the length function
length' :: [a] -> Int
length' [] = 0
length' (x:xs) = 1 + length' xs

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

-- takes all words in a string and capitalizes them.
titleize :: [Char] -> [Char]
titleize [] = []
titleize s = unwords . map capitalize $ words s

-- computes factorial of a number.
factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n-1)

-- computes fibonacci numbers.
fibonacci :: Int -> Int
fibonacci 0 = 1
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)

-- computes the body mass index and tells you how you look.
bmi :: Float -> Float -> [Char]
bmi weight height
    | index <= skinny = "underweight"
    | index <= normal = "normal"
    | index <= fat    = "overweight"
    | otherwise       = "obese" -- default fallback using keyword `otherwise`
    where index = weight / height ^ 2 -- guards using where syntax
          (skinny, normal, fat) = (18.5, 25.0, 30.0) -- where using pattern matching

-- my own version of maximum
maximum' :: (Ord a) => [a] -> a
maximum' ([]) = error "No maximum in empty list"
maximum' (x:[]) = x
maximum' (x:xs) = max x (maximum' xs)

-- my own version of replicate, ie. produces a list by repeating the input int.
replicate' :: Int -> a -> [a]
replicate' n x
    | n <= 0 = []
    | otherwise = x:replicate' (n-1) x

-- my own version of take
take' :: Int -> [a] -> [a]
take' n _
    | n <= 0 = []
take' n [] = []
take' n (x:xs) = x:take' (n-1) xs

-- my own reverse version, takes an array and reverses it.
reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:[]) = [x]
reverse' (x:xs) = (reverse' xs) ++ [x]

reverse'' :: [a] -> [a]
reverse'' = foldl (\acc x -> x:acc) []

-- my own version of zip
zip' :: [a] -> [b] -> [(a, b)]
zip' [] _ = []
zip' _ [] = []
zip' (x:xs) (y:ys) = (x, y):zip' xs ys

-- my own version of elem, checks if an element is in a list of elements.
elem' :: (Eq a) => a -> [a] -> Bool
elem' _ [] = False
elem' x (y:ys)
    | x == y = True
    | otherwise = elem' x ys

-- naive implementation of quick sort, ie:
-- it's not performed inplace, no side effects, remember !?!
-- it does two passes through the input array to position the pivot
quickSort :: (Ord a) => [a] -> [a]
quickSort [] = []
quickSort (x:xs) = quickSort smaller ++ [x] ++ quickSort larger
    where smaller = filter (<= x) xs -- [y | y <- xs, y <= x]
          larger = filter (> x) xs -- [y | y <- xs, y > x]

-- my own version of zipWith
zipWith' :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith' _ [] _ = []
zipWith' _ _ [] = []
zipWith' f (x:xs) (y:ys) = (f x y) : zipWith' f xs ys

-- my own version of flip: takes a function with two arguments and returns the
-- same function with the arguments flipped.
flip' :: (a -> b -> c) -> (b -> a -> c)
flip' f x y = f y x  -- this works because it returns a curried version of f where parameters are applied in reverse.

-- functions operating on lists
map' :: (a -> b) -> [a] -> [b]
map' _ [] = []
map' f (x:xs) = f x : map' f xs

filter' :: (a -> Bool) -> [a] -> [a]
filter' _ [] = []
filter' f (x:xs)
    | f x == True = x : filter' f xs
    | otherwise = filter' f xs

-- build a Collatz sequence or chain
-- the ideea is that people have proven that this sequence always ends in a 1.
collatz :: Int -> [Int]
collatz 1 = [1]
collatz n
    | odd n = n : collatz (n * 3 + 1)
    | even n = n : collatz (div n 2)

-- returns the sign of the input number.
signum' :: Int -> Int
signum' 0 = 0
signum' n
    | n < 0 = (-1)
    | otherwise = 1

-- example of an infix operator (non-alphanumeric function name)
(|>) :: Int -> Int -> Int
x |> y = x + y

-- safer version of tail which doesn't throw error when applied to an empty list.
safeTail :: [a] -> [a]
safeTail [] = []
safeTail (x:xs) = xs

safeTail' :: [a] -> [a]
safeTail' l = if null l then [] else let (x:xs) = l in xs

safeTail'' :: [a] -> [a]
safeTail'' l
    | null l = []
    | otherwise = xs
        where x:xs = l

-- my own versions of foldr, foldl, foldr1 and foldl1
foldr' :: (a -> b -> b) -> b -> [a] -> b
foldr' _ acc [] = acc
foldr' f acc (x:xs) = f x rightAcc
    where rightAcc = foldr' f acc xs

foldl' :: (a -> b -> a) -> a -> [b] -> a
foldl' _ acc [] = acc
foldl' f acc (x:xs) = foldl' f leftAcc xs
    where leftAcc = f acc x

foldr1' :: (a -> a -> a) -> [a] -> a
foldr1' _ [] = error "Input list must have at least one element"
foldr1' f (x:xs) = foldr' f x xs

foldl1' :: (a -> a -> a) -> [a] -> a
foldl1' _ [] = error "Input list must have at least one element"
foldl1' f (x:xs) = foldl' f x xs

-- given a list of lists concatenate these lists.
flatten :: [[a]] -> [a]
flatten xss = [x | xs <- xss, x <- xs]

-- extracts the factors of a given number.
factors :: Int -> [Int]
factors n = [x | x <- [1..n], n `mod` x == 0]

-- figure out if the input is prime.
prime :: Int -> Bool
prime 1 = True
prime n = (factors n) == [1, n]

-- given an input number return a list with all prime numbers up to the input.
primes :: Int -> [Int]
primes n = [x | x <- [2..n], prime x]

-- compute pairs of adjacent elements from a list
pairs :: [Int] -> [(Int, Int)]
pairs xs = zip (init xs) (tail xs)

-- check if a list is sorted
isSorted :: [Int] -> Bool
isSorted xs = and [x <= y | (x, y) <- pairs xs]

-- prints a list of all numbers which are pythagoriec when coupled with the input.
pyths :: Int -> [(Int, Int, Int)]
pyths n = [(x, y, n) | x <- [1..n], y <- [1..n], x^2 + y^2 == n^2]

-- prints the list of first n pythagoreic integers.
pyths' :: Int -> [(Int, Int, Int)]
pyths' n = [(x, y, i) | i <- [1..n], x <- [1..i], y <- [1..i], x^2 + y^2 == i^2]

-- return a list of perfect numbers less than the input, ie. numbers whose
-- sum of factors equal the number itself.
perfects :: Int -> [Int]
perfects n = [x | x <- [1..n], x == (sum $ init $ factors x)]

newton-raphson method for computing a square root of a number.
sqrt' :: Float -> Int -> Float
sqrt' n eps = next n eps
    where next n x = (x + n / x) / 2

-- merge two sorted arrays
merge' :: (Ord a) => [a] -> [a] -> [a]
merge' [] [] = []
merge' xs [] = xs
merge' [] ys = ys
merge' (x:xs) (y:ys)
    | x < y = x:(merge' xs (y:ys))
    | otherwise = y:(merge' (x:xs) ys)
