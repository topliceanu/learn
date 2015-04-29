-- the Op data structure.
data Op = Add | Sub | Mul | Div

-- applies an operator to two integers.
apply           :: Op -> Int -> Int -> Int
apply Add x y   = x + y
apply Sub x y   = x - y
apply Mul x y   = x * y
apply Div x y   = div x y

-- the Expr data type which is either an int or an application.
data Expr = Val Int | App Op Expr Expr

-- checks the validity of an operation and it's parameters.
valid          :: Op -> Int -> Int -> Bool
valid Add _ _   = True
valid Sub x y   = x > y
valid Mul _ _   = True
valid Div x y   = (mod x y) == 0

-- improved solution validity checker.
valid'           :: Op -> Int -> Int -> Bool
valid' Add x y   = x > y -- invalidates the comutated expressions.
valid' Sub x y   = x > y
valid' Mul x y   = (x > y) && (x /= 1 || y /= 1) -- invalidates the comutated expressions and expressions where either memeber is 1.
valid' Div x y   = ((mod x y) == 0) && (y /= 1) -- there is no point in dividing by 1

-- evaluates the application of the application to the two numbers.
eval            :: Expr -> [Int]
eval (Val n)     = [n | n > 0]
eval (App o l r) = [apply o x y | x <- eval l
                                , y <- eval r
                                , valid o x y]

-- returns a list of all combinations of elements in the input
choices :: [a] -> [[a]]
-- TODO

-- extracts all the values from an expression.
values              :: Expr -> [Int]
values (Val n)      = [n]
values (App _ l r)  = values l ++ values r

-- specifies what it means to be a solution of the countdown problem.
solution        :: Expr -> [Int] -> Int -> Bool
solution e ns n = elem (values e) (choices ns) -- checks whether we use each value only once.
                    && eval e == [n] -- checks that the expression solves the problem.

-- splits an input list into all possible combinations of two non-empty lists.
split :: [a] -> [([a], [a])]
-- TODO

-- returns all possible combinations of two expressions using all operators.
combine     :: Expr -> Expr -> [Expr]
combine l r = [App o l r | o <- [Add, Sub, Mul, Div]]

-- returns all possible expressions whose values are the input numbers.
exprs       :: [Int] -> [Expr]
expr []     = []
expr [n]    = [Val n]
expr ns     = [e | (ls, rs) <- split ns
                , l <- exprs ls
                , r <- exprs rs
                , e <- combine l r]

-- solution finder by brute force
solutions       :: [Int] -> Int -> [Expr]
soltuions ns n  = [e | ns' <- choices ns -- generate all possible permutation of numbers.
                    , e <- exprs  ns' -- generate all possible expressions with each permutation.
                    , eval e == [n]] -- evaluate each expression

-- packaging up an valid expression and it's result.
type Result = (Expr, Int)

results     :: [Int] -> [Result]
results []  = []
results [n] = [(Val n,n) | n > 0]
results ns  = [res | (ls, rs) <- split ns
                   , lx       <- results ls
                   , ry       <- results rs
                   , res      <- combine' lx, ry]

-- only combines solutions if their combination is valid.
combine'            :: Result -> Result -> [Result]
combine' (l,x) (r,y) = [(App o l r, apply o x y) | o <- [Add, Sub, Mul, Div]
                                                 , valid o x y]

-- optimized solution finder. It removes the recursion branches on invalid expressions.
solutions'      :: [Int] -> Int -> [Expr]
solutions' ns n = [e | ns' <- choices ns
                     , (e, m) <- results ns'
                     , m == n]
