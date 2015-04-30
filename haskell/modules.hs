import Data.Char (ord, chr, digitToInt)
import Data.List (words, nub, sort, group, tails, isPrefixOf)


-- counts the number of unique elements in a list.
numUniques :: (Eq a) => [a] -> Int
numUniques = length . nub

-- count the number of times each word appears in the input
wordCounts :: [Char] -> [([Char], Int)]
-- wordCounts = map (\ws -> (head ws, length ws)) . group . sort . words
wordCounts s = map (\ws -> (head ws, length ws)) $ (group . sort . words) s

-- checks whether needle string exists inside the haystack string
contains' :: (Eq a) => [a] -> [a] -> Bool
contains' needle = any (isPrefixOf needle) . tails

-- encode/decode using the Caesar coding scheme
caesarEncode :: Int -> [Char] -> [Char]
caesarEncode offset = map (\c -> chr $ ord c + offset)

caesarDecode :: Int -> [Char] -> [Char]
caesarDecode offset = map (\c -> chr $ ord c - offset)

-- fetch the data in the repo
