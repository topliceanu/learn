-- https://github.com/dserban/lambda2015summer

import Data.List
import Data.List.Split


initialGameState = [0,0,2,4,0,4,4,8,0,0,2,0,2,0,2,0,2,0,8,8,8,0,0,0,8,8,0,0,8,8]

swipeRowLeft :: (Num a, Eq a) => [a] -> [a]
swipeRowLeft input =
  let
    tmp = map sum $ concat $ map (chunksOf 2) $ group $ filter (/=0) input
    lenInput = length input
  in
    take lenInput $ tmp ++ (replicate lenInput 0)

swipeBoardLeft :: (Num a, Eq a) => [[a]] -> [[a]]
swipeBoardLeft = map swipeRowLeft -- point free style

swipeRowRight :: (Num a, Eq a) => [a] -> [a]
swipeRowRight = reverse . swipeRowLeft . reverse

swipeBoardRight :: (Num a, Eq a) => [[a]] -> [[a]]
swipeBoardRight = map swipeRowRight
