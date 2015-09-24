import Control.Monad (forM, when, forever)
import Data.Char (toUpper)
import System.IO (openFile, IOMode, hGetContents, hClose, IOMode(ReadMode),
                  readFile,  writeFile, FilePath, Handle)


titleize :: String -> String
titleize [] = []
titleize (x:xs) = (toUpper x) : xs

reverseWords :: String -> String
reverseWords = unwords . (map reverse) . words

isPalindrome :: String -> Bool
isPalindrome xs = (reverse xs) == xs


-- my own version of putStr
putStr' :: String -> IO ()
putStr' [] = return ()
putStr' (x:xs) = do
    putChar x
    putStr' xs

helloUser :: IO ()
helloUser = do
    putStrLn "hello, what is your first name?"
    firstName <- getLine
    putStrLn "what is your second name?"
    lastName <- getLine
    let titleizedFirstName = titleize firstName
        titleizedlastName = titleize lastName
    putStrLn $ "Hey "++titleizedFirstName++" "++titleizedlastName++", how are you?"

reverseCli :: IO ()
reverseCli = do
    line <- getLine
    if null line
        then return () -- return an empty IO action when the user hits enter twice.
        else do -- interestingly that we need to use `do` again because of putStrLn.
            putStrLn $ reverseWords line -- :: IO ()
            reverseCli

-- print each char received from the input twice. Stops on white space.
loopMain :: IO ()
loopMain = do
    c <- getChar
    when (c /= ' ') $ do
        putChar c
        loopMain

loopColors :: IO ()
loopColors = do
    colors <- forM [1,2,3,4] (\a -> do
        putStrLn $ "Which color do you associate with the number " ++ show a
        color <- getLine
        return color)
    putStrLn "The colors that you associate with 1,2,3 and 4 are "
    mapM_ putStrLn colors

-- Passes the input through CAPS LOCK.
capsLocker :: IO ()
capsLocker = forever $ do
    contents <- getContents
    putStrLn $ map toUpper contents

-- splits the input string into lines and keeps only the lines smaller than the input.
shortLinesOnly :: Int -> String -> String
shortLinesOnly n input = unlines $ filter removeLargeLines $ lines input
    -- where removeLargeLines = \line -> length line < n
    where removeLargeLines = (<n) . length

pipeShortLines :: IO ()
pipeShortLines = interact $ shortLinesOnly 20

linesArePalindrome :: IO ()
linesArePalindrome = interact $ unlines . map (show . isPalindrome) . lines

-- reads a file line by line.
readTmpFile = do
    handle <- openFile "/tmp/girlfriend.txt" ReadMode
    contents <- hGetContents handle
    putStr contents
    hClose handle

fileToCaps = do
    contents <- readFile "/tmp/girlfriend.txt"
    writeFile "/tmp/capsGirlfriend.txt" $ map toUpper contents

-- my own version of withFile, opens a file with an access mode, applies a
-- transformation on the handle then closes the file.
withFile' :: FilePath -> IOMode -> (Handle -> IO a) -> IO a
withFile' path mode op = do
    handle <- openFile path mode
    result <- op handle
    hClose handle
    return result


-- main function to be executed.
main :: IO ()
main = fileToCaps
