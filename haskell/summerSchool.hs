-- algebraic data type for a user event.
data Event = Error | Key Char | Click Int Int

-- checks the validity of an event.
isOk :: Event -> Bool
isOk event = case event of
    Error -> False
    Key k -> k /= 'q'
    Click x y -> x > 0 && y > 0

-- translates the age into a noun.
describe :: Int -> String
describe age =
    case age of
        n | n > 20 -> "Adult"
        n | n > 13 -> "Teenager"
        n | n > 2 -> "Child"
        _ -> "Infant"

-- slower and faster versions of the factorial function, using tail recursion.
factorial :: Int -> Int
factorial 0 = 1
factorial n = n * (factorial (n - 1)) -- no tail recursion because the compiler has to evaluate n.

factorial' :: Int -> Int
factorial' n = loop 1 n
    where loop acc 0 = acc
          loop acc n = loop (acc * n) (n - 1) -- tail recursion!

-- Lab #1, min 38
