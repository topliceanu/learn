Welcome to Facebook!

This is just a simple shared plaintext pad, with no execution capabilities.

When you know what language you would like to use for your interview,
simply choose it from the dropdown in the top bar.

Enjoy your interview!

Get average of all elements in binary search tree which are in range [low, high] inclusive.
              7
            /   \
           4     8
          / \     \
         3   5     9
        /
       2



Input: [4, 6] => 4.5


class Node(object):
    __initiaze__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traverse2(node, low, high):
    if node == None:
        return 0, 0
    if node.value > high:
        return traverse2(node.left, low, high)
    if node.value < low:
        return traverse2(node.right, low, high)
    s, c = node.value, 1
    s_l, c_l = traverse2(node.left, low, high)
    s_r, c_r = traverse2(node.right, low, high)
    return s + s_l + s_r, c + c_l + c_r

# return (sum, count)
def traverse(node, low, high):
    s, c = 0, 0
    if low <= node.value and node.value <= high:
        s += node.value
        c += 1
    if node.left != None and low <= node.left.value and node.left.value <= high:
        l_sum, l_count = traverse(node.left, low, high)
        s += l_sum
        c += l_count
    if node.right != None and low <= node.right.value and node.right.value <= high:
        r_sum, r_count = traverse(node.right, low, high)
        s += r_sum
        c += r_count
    return s, c

def avg(root, low, high):
    s, count = traverse(root, low, high)
    if count == 0:
        return 0
    return s / count # float division

---------------------------------------------------------------------------------------------------

Write a function that returns whether a list of strings is sorted given a specific alphabet.
A list of N words with max length M and a K-sized alphabet are given.

input:  words =    ["ca", "cat", "bat", "tab"]
        alphabet = ['c', 'b', 'a', 't'] # {"c": 0, ...
output: True

def le(w1, w2, alphabet): # boolean
    i = 0
    while i < len(w1) and i < len(w2): # M * K , i = 0, 1, 2
        c1, c2 = w1[i], w2[i] # b t, a a, t b
        idx1 = alphabet.indexOf(c1) # 1, 2, 3
        idx2 = alphabet.indexOf(c2) # 3, 2, 1
        if idx1 < idx2:
            return True
        if idx1 > idx2:
            return False # return False
        i += 1
    if len(s1) > len(s2): # cat ca 3 2
        return False
    return True

def is_sorted(words, alphabet):
    # O(N * M * K) time, O(1) space -> O(N*M) time, O(K) space
    for i in range(len(words)-1):
        w1 = words[i]
        w2 = words[i+1]
        if not le(w1, w2, alphabet):
            return False
    return True
