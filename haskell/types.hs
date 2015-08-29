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
vectPlus :: (Num t) => Vector t -> Vector t -> Vector t
(Vector i j k) `vectPlus` (Vector l m n) = Vector (i+l) (j+m) (k+n)

-- multiply two vectors.
vectMult :: (Num t) => Vector t -> Vector t -> Vector t
(Vector i j k) `vectMult` (Vector l m n) = Vector (i*l) (j*m) (k*n)

-- scalar multiplication of two vectors.
vectScalarMult :: (Num t) => Vector t -> Vector t -> t
(Vector i j k) `vectScalarMult` (Vector l m n) = i*l + j*m + k*n


-- days of the week
data Day = Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday
    deriving (Show, Read, Eq, Ord, Bounded, Enum)

