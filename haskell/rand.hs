import Control.Monad (when)
import System.Random (RandomGen, Random, random, StdGen, randomR, randomRs,
                      newStdGen, getStdGen, mkStdGen)


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

-- function asks the user to guess a random number between 1 and 3.
guess :: IO ()
guess = do
    gen <- getStdGen
    let (value, _) = randomR (1, 3) gen :: (Int, StdGen)
    putStrLn "Which number between 1 and 3 am I thinking of? Press ENTER to exit"
    guessedValueStr <- getLine
    when (not $ null guessedValueStr) $ do
        let guessedValue = read guessedValueStr :: Int
        if guessedValue == value then
            putStrLn "Great! You guessed correctly!"
        else
            putStrLn "Sorry! You guessed wrong!"
        newStdGen
        guess
