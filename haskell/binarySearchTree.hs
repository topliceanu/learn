-- immutable data structure which represents a tree
data Tree a = EmptyTree | Node a (Tree a) (Tree a) deriving (Show, Read, Eq)

-- creates a leaf node
treeLeaf :: a -> Tree a
treeLeaf x = Node x EmptyTree EmptyTree

-- produces a new tree by adding a value to the passed in tree.
treeInsert :: (Ord a) => a -> Tree a -> Tree a
treeInsert x EmptyTree = treeLeaf x
treeInsert x (Node y left right)
  | x <= y = Node y (treeInsert x left) right
  | otherwise = Node y left (treeInsert x right)

-- checks if a value is present in the given Tree.
treeElem :: (Ord a) => a -> Tree a -> Bool
treeElem _ EmptyTree = False
treeElem x (Node y left right)
  | x == y = True
  | x < y = treeElem x left
  | otherwise = treeElem x right

-- builds a tree from a list of ordered values.
treeFromList :: (Ord a) => [a] -> Tree a
treeFromList [] = EmptyTree
treeFromList (x:xs) = treeInsert x (treeFromList xs)

treeFromList' :: (Ord a) => [a] -> Tree a
treeFromList' = foldr treeInsert EmptyTree

-- add Tree to the Functor typeclass.
instance Functor Tree where
  fmap f EmptyTree = EmptyTree
  fmap f (Node x left right) = Node (f x) (fmap f left) (fmap f right)
