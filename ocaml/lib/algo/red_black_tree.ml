(* See https://cs3110.github.io/textbook/chapters/ds/rb.html *)

type color = Red | Black

type 'a rbtree =
    | Leaf
    | Node of (color * 'a * 'a rbtree * 'a rbtree) (* color X value X left subtree X right subtree *)

(* mem returns true is the input value is present in the input tree *)
(* val mem : 'a -> 'a rbtree -> bool *)
let rec mem x = function 
    | Leaf -> false
    | Node (_, y, left, right) -> 
        if x < y then mem x left
        else if x > y then mem x right
        else true
 
(* The four cases violating the local invariant (no two consecutive red nodes)

           1             2             3             4                          

           Bz            Bz            Bx            Bx                              Ry
          / \           / \           / \           / \                             / \
         Ry  d         Rx  d         a   Rz        a   Ry            =>           Bx   Bz
        /  \          / \               /  \          /  \                       / \   / \
     [Rx]  c         a  [Ry]          [Ry]  d        b   [Rz]                   a   b c   d
     /  \               /  \          / \                /  \
    a    b             b    c        b   c              c    d

Labels are selected suc that a < x < b < y < c < z < d which makes the pattern matching more elegant.
*)
(* val balance : color * 'a * 'a rbtree * 'a rbtree *)
let balance = function 
    | Black, z, Node (Red, y, Node (Red, x, a, b), c), d
    | Black, z, Node (Red, x, a, Node(Red, y, b, c)), d
    | Black, x, a, Node (Red, z, Node (Red, y, b, c), d)
    | Black, x, a, Node (Red, y, b, Node (Red, z, c, d)) ->
        Node (Red, y, Node (Black, x, a, b), Node(Black, z, c, d))
    | color, value, left, right -> Node (color, value, left, right)
    
let insert x subtree = 
    let rec insert_aux x = function 
        | Leaf -> Node (Red, x, Leaf, Leaf)
        | Node (color, y, left, right) as node -> 
            if x < y then balance (color, y, insert_aux y left, right)
            else if x > y then balance (color, y, left, insert_aux y right)
            else node
    in match insert_aux x subtree with 
        | Node (_, value, left, right) -> Node (Black, value, left, right)
        | Leaf -> failwith "Cannot insert in leaf. Guaranteed not to happen"
