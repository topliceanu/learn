import System.Random (RandomGen, Random, random, StdGen)


-- generator of a list of random variables
-- usage: take 10 $ randoms' (mkStdGet 123) :: [Int]
randoms' :: (RandomGen g, Random a) => g -> [a]
randoms' gen = let (value, newGen) = random gen
               in value:randoms' newGen

-- simulates three coin flips
threeCoins :: StdGen -> (Bool, Bool, Bool)
threeCoins gen =
    let (first, gen') = random gen
        (second, gen'') = random gen'
        (third, _) = random gen''
    in (first, second, third)

-- generates a finite list of numbers and a generator
finiteRandoms :: (RandomGen g, Random a) => Int -> g -> ([a], g)
finiteRandoms 0 gen = ([], gen)
finiteRandoms n gen =
    let (r, gen') = random gen
        (rs, gen'') = finiteRandoms (n-1) gen'
    in (r:rs, gen'')
