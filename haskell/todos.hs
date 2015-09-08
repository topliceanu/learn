-- program to add / remove todos from a text file
module Todos (
    addTodo,
    removeTodo
) where

import System.IO (FilePath, writeFile, readFile, appendFile)


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

addTodo :: String -> IO ()
addTodo newTodo = do
    appendFile todosFilePath newTodo

removeTodo :: Int -> IO ()
removeTodo pos = do
    contents <- readFile todosFilePath
    let newContents = unlines $ remove' pos $ lines contents
    writeFile todosFilePath newContents
