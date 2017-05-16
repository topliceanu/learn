import String

type Visibility = All | Active | Completed

type Task  = {
    task: String,
    complete: Bool
  }

buy : Task
buy = { task = "Buy liquids", complete = True }

drink : Task
drink = { task = "Drink liquids", complete = False }

keep : Visibility -> List Task -> List Task
keep visibility tasks =
  case visibility of
    All ->
      tasks
    Active ->
      List.filter (\t -> not task.complete) tasks
    Completed ->
      List.filter (\t -> task.complete) tasks

-- generic linked list type
type LinkedList a = Empty | Node a (List a)

-- generic binary search tree.
type Tree a
  = Empty
  | Node a (Tree a) (Tree a)

-- creates a leaft node, ie. has no children.
leaf : a -> Tree a
leaf v = Node v Empty Empty

-- inserts a new value in an existing tree, removing duplicates!
insert : a -> Tree a -> Tree a
insert x tree =
  case tree of
    Empty -> leaf a
    Node y left right ->
      if x > y then
        Node y left (insert x right)
      else if x < y then
        Node y (insert x left) right
      else
        tree

-- traverses a list and creates a binary search tree.
fromList : List a -> Tree a
fromList xs = List.foldl insert Empty xs

-- calculates the depth of a tree
depth : Tree a -> Int
depth tree =
  case tree of
    Empty -> 0
    Node x left right ->
      1 + max (depth left) (depth right)

map : (a -> b) -> Tree a -> Tree b
map pred tree =
  case tree of
    Empty -> Empty
    Node x left right ->
      Node (pred x) (map pred left) (map pred right)

sum : Tree a -> a
sum tree =
  case tree of
    Empty -> 0
    Node x left right ->
      x + (sum left) + (sum right)
-- sum tree = fold (+) 0 tree


-- flatten does inorder traversal of the tree to produce a sorted list of it's values.
flatten : Tree a -> List a
flatten tree =
  case tree of
    Empty -> []
    Node x left right ->
      List.concat [(flatten left), [x], (flatten right)]
-- flatten tree = fold (::) [] tree

-- isElement performs binary search.
isElement : comparable -> Tree comparable -> Bool
isElement x tree =
  case tree of
    Empty -> False
    Node y left right ->
      if x == y then
        True
      else if x < y then
        isElement x left
      else
        isElement x right
-- isElement x tree = fold (\y c -> c || x == y) False tree

-- general function to traverse and compress trees.
fold : (a -> b -> b) -> b -> Tree a -> b
fold pred collect tree =
  case tree of
    Empty -> collect
    Node x left right ->
      let
        newCollect = pred x collect
        leftCollect = fold pred newCollect left
        rightCollect = fold pred leftCollect right
      in
        rightCollect
