-- The Countdown Problem
--
-- We're given a list of numbers and a a set of arithmetic operators +, -, *, /
-- Find a way to combine the operators and the given numbers so that the
-- resulting expression returns the largest possible value.
-- Rules: - all numbers used (received and intermediate results) must be positive integers
--        - each of the source numbers can be used at most once
--        - each operator must be used once and only once.
--        - you can use parantheses


-- data type to represent arithmetic operations
data Op = Add | Sub | Mul | Div deriving (Eq, Show)

-- data type to represent arithmethic expressions: either an int or an application.
data Expr = Val Int | App Op Expr Expr deriving (Eq, Show)

-- encapsulates a valid(!) expression and it's result value.
type Result = (Expr, Int)

-- applies an operator on two number.
apply :: Op -> Int -> Int -> Int
apply Add x y = x + y
apply Sub x y = x - y
apply Mul x y = x * y
apply Div x y = x `div` y -- ensure we get a int as the output

-- checks whether or not the operation is valid given the rules of th game.
isValid :: Op -> Int -> Int -> Bool
isValid Add x y = x <= y -- sort the
isValid Sub x y = x > y
isValid Mul x y = x > y && x /= 1 && y /= 1
isValid Div x y = x > y && x `mod` y == 0 && y /= 1

-- evaluates a given expression, if it returns [] it means the evaluation failed.
eval :: Expr -> [Int]
eval (Val n) = [n | n > 0]
eval (App o l r) = [apply o x y | x <- eval l,
                                  y <- eval r,
                                  isValid o x y]

-- computes all subsets of a given set.
choices :: [a] -> [[a]]
choices [] = [[]]
choices (x:xs) = rest ++ (map ([x]++) rest)
    where rest = choices xs

-- extracts all ints out of an expression.
values :: Expr -> [Int]
values (Val n) = [n]
values (App _ l r) = values l ++ values r

-- takes an expression, the packaged up numbers, the target number and returns
-- True or False whether or not that expression solves the problem.
isSolution :: Expr -> [Int] -> Int -> Bool
isSolution e xs x = elem (values e) (choices xs) && -- the expression is in the possible choices list.
                    eval e == [x] -- the expression evaluates to the target value.

-- returns all possible ways of splitting a list into two lists which are non-empty.
-- TODO implement using take() and drop().
split :: [a] -> [([a], [a])]
split [] = []
split (x:[]) = []
split (x:y:[]) = [([x], [y])]
split (x:xs) = [([x], xs)] ++ [(x:l, r) | (l, r) <- split xs]

-- combines two solutions in all possible ways.
combine :: Expr -> Expr -> [Expr]
combine l r = [App o l r | o <- [Add, Sub, Mul, Div]]

combine' :: Result -> Result -> [Result]
combine' (l, x) (r, y) = [(App o l r, apply o x y) | o <- [Add, Sub, Mul, Div],
                                                     isValid o x y]

-- compute all possible expressions given a list of numbers.
exprs :: [Int] -> [Expr]
exprs [] = []
exprs [n] = [Val n]
exprs ns = [e | (ls, rs) <- split ns,
                l <- exprs ls,
                r <- exprs rs,
                e <- combine l r]

-- computes all results coming from valid expressions.
results :: [Int] -> [Result]
results [] = []
results [n] = [(Val n, n) | n > 0]
results ns = [res | (ls, rs) <- split ns,
                    lx <- results ls,
                    rx <- results rs,
                    res <- combine' lx rx]

-- solution finder: given a list of numbers and a target number, this function
-- computes all possible expressions that solve to that problem.
solutions :: [Int] -> Int -> [Expr]
solutions ns n = [e | ns' <- choices ns,
                      e <- exprs ns',
                      eval e == [n]]

solutions' :: [Int] -> Int -> [Expr]
solutions' ns n = [e | ns' <- choices ns,
                       (e, m) <- results ns',
                       n == m]
