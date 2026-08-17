(* Ocaml implementation of AVL trees. I'm focusing on insert as that's the interesting bit. 
* AVL trees are stricter than Red-black trees, that is they perform more relancings on inserts but search is faster.
* If deletion happens very rarely, you can just mark the node as deleted but not actually remove it!
* Inspiration: https://github.com/stanislav-shchetinin/avl-dict/blob/main/src/avl_dict.ml
*)

type 'a avltree = Leaf | Node of 'a * int * 'a avltree * 'a avltree (* value x height_factor x left x right *)

let height = function
  | Leaf -> 0
  | Node (_, h, _, _) -> h

(* Cases of imbalance after an insert:

      GP(2)           GP(2)         N(0)
      /   \           /  \         /   \
    P(-1)  D  =>    N(1)  D  =>  P(0) GP(0)
   /  \             /   \       / \    / \
  A   N(0)        P(0)   C     A   B  C   D
     /  \        /   \
    B    C      A     B 

  [case 1:       [case 2:
  left-right]    left-left]



      GP(-2)         GP(-2)             N(0)
     /  \             / \              /   \
    A   P(1)   =>    A  N(-1)     =>  GP(0) P(0)
        /  \            /  \         /  \   /  \
      N(0)  D          B   P(0)     A   B  C    D
     /   \                 /  \
    B     C               C    D
    
    [case 3:          [case 4:
    right-left]       right-right]

  In parantheses we have the node's height factor: height of right - height or left.
*)
let rec insert x = function 
  | Leaf -> Node (x, 0, Leaf, Leaf)
  | Node (y, height_factor, left, right) as n ->
    (* when inserting in the right subtree, the heigh factor increases by 1, for left subtree, it decreases by 1*)
    if x > y then balance (y, height_factor+1, left, insert y right)
    else if x < y then balance (y, height_factor-1, insert y left, right)
    else n
and balance = function
  | (gp, 2, Node (p, -1, a, Node (n, 0, b, c)), d) (* case 1 *)
  | (gp, 2, Node (n, 1, Node (p, 0, a, b), c), d) -> (* case 2 *)
     Node (n, 0, Node (p, 0, a, b), Node(gp, 0, c, d))
  | (gp, -2, a, Node (p, 1, Node (n, 0, b, c), d)) (* case 3 *)
  | (gp, -2, a, Node (n, -1, b, Node (p, 0, c, d))) -> (* case 4 *)
    Node (n, 0, Node (gp, 0, a, b), Node (p, 0, c, d))
  | (x, h, l, r) -> Node (x, h, l, r)
  