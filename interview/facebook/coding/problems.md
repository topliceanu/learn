# Problems

1. UK Taxes

Given a salary an a set of tax brackets, calculate the required tax that needs to be paid.
Example:
```py
calculate_taxes(55000, [
  [5000, 0],
  [10000, 0.1],
  [15000, 0.2],
  [20000, 0.3],
  [None, 0.4]
])
# For 55000, the result is 5000 * 0 + 10000 * 0.1 + 15000 * 0.2 + 20000 * 0.3 + 5000 * 0.4 = 1000 + 3000 + 6000 + 2000 = 12000
```
If the tax bracket is None, then everything above that threshold is taxed 0.4 * 100 percent and you can ignore the rest of the brackets.
Solution: subtract the tax bracket from the salary. If you get a negative number
the return tax of salary, if you get a positive number, move on to the next bracket,
subtract the bracket from the salary and increase tax by the tax percentage
Complexity: O(n) time, O(1) space

2. Calculate expression

Given an arithmetic expression which contains positive integers, addition and multiplication,
calculate the result of the expression.
You can't have negative numbers, no scientific notation, etc.
Solution: calculate multiplications first, then add the results.
Complexity: O(n) time, O(n) space

3. Given a list of coordinates of n shops [(x, y)] relative to the position of a user (0, 0),
find the nearest k shops to the user.
Solution: calculate distances for each pair from the user; push them into a heap, extract the top k values from the heap.
Complexity: O(n + klogn) time, O(n) space

4. Given an array of integers, calculate for each element, the product of all the numbers to the left of it and all the numbers to the right.
Example:
```py
[1, 2, 3] => [2*3, 1*3, 1*2]
```
Solution: for every element, calculate the multiple all all elements to the left of it
and all elements to the right of it and store them in separate arrays. Finally multiple the results.
Complexity: O(n) time, O(n) space

5. Given a tree (not necessarely binary), find the lowest subtree which contains all the highest depths nodes in the tree.
Example:
```
        a
       / \
      b   c
     /|\   \
    c d e   f
   /|\  |
  g h i j
The correct answer is b.
```
Solution: for every node, we need to know that it has at least 2 children with the highest depth observed.
If that's true, then the current node is a good candidate. If not, the child with the highest depth is a better candidate.
Complexity: O(n) time, O(n) space - because we store the depths.
