import qualified Data.Map as Map

-- Data structure for a person.
data Person = Person {
        firstName :: String,
        lastName :: String,
        age :: Int
        -- age :: Int,
        -- height :: Float,
        -- phoneNumber :: String,
        -- flavor :: String
    } deriving (Show, Read, Eq)

-- Data structure for a car.
data Car = Car {
        company :: String,
        model :: String,
        year :: Int
    } deriving (Show)

-- a 3d vector data structure.
data Vector a = Vector a a a deriving (Show)

-- adds two numeric vector together.
vPlus :: (Num t) => Vector t -> Vector t -> Vector t
(Vector i j k) `vPlus` (Vector l m n) = Vector (i+l) (j+m) (k+n)

-- multiply two vectors.
vMult :: (Num t) => Vector t -> Vector t -> Vector t
(Vector i j k) `vMult` (Vector l m n) = Vector (i*l) (j*m) (k*n)

-- scalar multiplication of two vectors.
scalarMult :: (Num t) => Vector t -> Vector t -> t
(Vector i j k) `scalarMult` (Vector l m n) = i*l + j*m + k*n


-- days of the week
data Day = Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday
    deriving (Show, Read, Eq, Ord, Bounded, Enum)

-- Lockers.
-- A locker is identified by and Int id. It can have two states: taken and free.
-- If taken, a locker also has an assigned code.
data LockerState = Taken | Free deriving (Show, Eq)
type Code = String
type LockerMap = Map.Map Int (LockerState, Code)

-- TODO not working!
lockerLookup :: Int -> LockerMap -> Either String Code
lockerLookup lockerNumber map =
    case Map.lookup lockerNumber map of
      Nothing -> Left $ "Locker number " ++ show lockerNumber ++ " doesn't exist!"
      Just (state, code) -> if state /= Taken
                            then Right code
                            else Left $ "Locker " ++ show lockerNumber ++ " is already taken!"

-- My own implementation of the list data type.
data List a = Empty | Cons a (List a) deriving (Show, Read, Eq, Ord)

(.++) :: List a -> List a -> List a
Empty .++ ys = ys
(Cons x xs) .++ ys = Cons x (xs .++ ys)

{- -- duplicate instance of Functor for Data.Map.Map type.
instance Functor (Map.Map k) where
    fmap = Map.fromList . (map (\(k,v) -> (k, fmap v))) $ Map.toList
-}
