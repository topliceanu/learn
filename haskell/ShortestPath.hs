-- Solves the single source shortest path problem.

import Data.List(groupBy)

-- each node holds reference to the next node on the same main node or a node
-- on the other main road.
data Node = Node Road Road | EndNode Road
-- length of the road and which node it points to.
data Road = Road Int Node

-- a road section is represented as a triplet of road lengths.
data Section = Section {getA :: Int, getB :: Int, getC :: Int} deriving (Show)
-- the roadsystem is a list of all road section.
type RoadSystem = [Section]


heathrowToLondon :: RoadSystem
heathrowToLondon = [Section 50 10 30, Section 5 90 20, Section 40 2 25, Section 10 8 0]

-- labels for the roads connecting nodes.
data Label = A | B | C deriving (Show)
-- a path is a set of labels indicating which road to take from the previous
-- node to the next and the length of that road.
type Path = [(Label, Int)]

-- builds new optimal paths given a pair of optimal paths and the next section in the road.
roadStep :: (Path, Path) -> Section -> (Path, Path)
roadStep (pathA, pathB) (Section a b c) = let
        priceA = sum $ map snd pathA
        priceB = sum $ map snd pathB
        forwardPriceToA = priceA + a
        crossPriceToA = priceA + c + b
        forwardPriceToB = priceB + b
        crossPriceToB = priceB + c + a
        pathA' = if forwardPriceToA < crossPriceToA then (A, a):pathA else (C, c):(B, b):pathB
        pathB' = if forwardPriceToB < crossPriceToB then (B, b):pathB else (C, c):(A, a):pathA
    in (pathA', pathB')

-- computes the optimal path through the road system.
optimalPath :: RoadSystem -> Path
optimalPath roadSystem =
    let (pathA, pathB) = foldl roadStep ([], []) roadSystem
        sumPathA = sum $ map snd pathA
        sumPathB = sum $ map snd pathB
        minimumPath = if sumPathA > sumPathB then pathB else pathA
    in reverse minimumPath

-- splits a list into lists of size 3.
groupsOf :: Int -> [a] -> [[a]]
groupsOf 0 _ = []
groupsOf _ [] = []
groupsOf n xs = takeN : groupsOf n dropN
    where takeN = take n xs
          dropN = drop n xs

main = do
    contents <- getContents
    let distances = map read $ lines contents :: [Int]
        threes = groupsOf 3 distances
        roadSystem = map (\[a,b,c] -> Section a b c) threes
        path = optimalPath roadSystem
    putStrLn $ "Optimal path is " ++ show path
