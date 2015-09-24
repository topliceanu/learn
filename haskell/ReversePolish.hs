-- Solves the Reverse Polish Notation problem.
--
-- RPN form of the following operation:
--      10 - (4 + 3) * 2
-- is:
--      10 4 3 + 2 * -
-- You traverse the list of symbols from left to right, whever you encounter a
-- number you push it into a stack, when you encounter an operator, pop two
-- numbers from the stack, apply the operator to them, then push the result back
-- to the stack.

module ReversePolish (
    solve
) where

solve :: String -> Float
solve = head . foldl compute [] . words
    where compute (x:x':xs) "*" = (x*x'):xs
          compute (x:x':xs) "+" = (x+x'):xs
          compute (x:x':xs) "-" = (x'-x):xs
          compute (x:x':xs) "/" = (x'/x):xs
          compute (x:x':xs) "^" = (x' ** x):xs
          compute (x:xs) "ln" = (log x):xs
          compute xs "sum" = [sum xs]
          compute xs num = (read num) : xs
