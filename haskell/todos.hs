-- program to list / add / remove todos from a text file.
-- usage:
--  $ runghc todo.hs <action> <path> <args>, where <action> = add|view|remove
--                                         <path> - path to the todos list

import Data.List (delete)
import System.Directory (removeFile, renameFile)
import System.Environment (getArgs, getProgName)
import System.IO (FilePath, openFile, readFile, readFile, appendFile,
                  IOMode(..), hGetContents, hClose, hPutStr, openTempFile)


todosFilePath :: FilePath
todosFilePath = "/tmp/todos.txt"

append' :: String -> [String] -> [String]
append' new existing = existing ++ [new]

remove' :: Int -> [String] -> [String]
remove' _ [] = []
remove' 0 (x:xs) = xs
remove' index (x:xs)
    | index < size = error $ "cannot remove index "++(show index)++" from list of "++(show size)
    | otherwise = remove' (index-1) xs
        where size = 1 + length xs

add :: [String] -> IO ()
add [filePath, todo] = appendFile filePath $ todo ++ ("\n")

view :: [String] -> IO ()
view [filePath] = do
    contents <- readFile filePath
    let todos = lines contents
        indexedTodos = zipWith (\num line -> (show num)++" - "++line ) [1..] todos
    putStr $ unlines indexedTodos

-- removes an item from a list by creating a temporary file, copying over all
-- items that should not be removed to it, then deleting the original file,
-- then renaming the temp file to the original file.
remove :: [String] -> IO ()
remove [filePath, indexString] = do
    fileHandle <- openFile filePath ReadMode
    (tempPath, tempHandle) <- openTempFile "." "temp"
    fileContents <-hGetContents tempHandle
    let index = read indexString :: Int
        todos = lines fileContents
        leftTodos = delete (todos !! index) todos
    hPutStr tempHandle $ unlines leftTodos
    hClose fileHandle
    hClose tempHandle
    removeFile filePath
    renameFile tempPath filePath

dispatch :: [(String, [String] -> IO ())]
dispatch = [ ("add", add)
           , ("view", view)
           , ("remove", remove)
           ]

main = do
    (command:args) <- getArgs
    putStrLn command
    let (Just action) = lookup command dispatch
    action args
