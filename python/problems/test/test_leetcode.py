import unittest

from src.leetcode.leetcode import ListNode, reverse_k_group, merge_k_lists, is_valid_sudoku, four_sum2

class TestLeetCode(unittest.TestCase):
    # FIXME
    def _test_reverse_k_group(self):
        tests = [
            ([1,2,3,4,5], 2, [2,1,4,3,5]),
            #([1,2,3,4,5,6], 2, [2,1,4,3,6,5]),
        ]
        for (raw, k, expected) in tests:
            lst = make_linked_list(raw)
            actual = reverse_k_group(lst, k)
            actual = make_list(actual)
            self.assertEquals(expected, actual)

    def test_merge_k_sorted_lists(self):
        tests = [
            ([[], []], []),
            ([[1,2], []], [1,2]),
            ([[], [1,2]], [1,2]),
            ([[1,2], [3,4], []], [1,2,3,4]),
            ([[1,2,3], [1,2,3]], [1,1,2,2,3,3]),
            ([[1,2], [1,2,3,4]], [1,1,2,2,3,4]),
            ([[1,2,3,4], [1,2]], [1,1,2,2,3,4]),
            ([[1,2,3], [1,2,3], [1,2,3]], [1,1,1,2,2,2,3,3,3]),
        ]
        for (lists, expected) in tests:
            lists = [make_linked_list(l) for l in lists]
            actual = merge_k_lists(lists)
            self.assertEquals(expected, make_list(actual))
        
    def test_is_valid_sudoku(self):
        tests = [
            ([["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]], True),
            ([["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]], False),
        ]
        for (board, expected) in tests:
            actual = is_valid_sudoku(board)
            self.assertEqual(expected, actual)

    def test_four_sum(self):
        tests = [
            ([1,0,-1,0,-2,2], 0, [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]),
            ([2,2,2,2,2], 8, [[2,2,2,2]]),
            ([0,0,0,0], 0, [[0,0,0,0]]),
            ([0,0,0,0], 1, []),
        ]
        for (nums, target, expected) in tests:
            actual = four_sum2(nums, target)
            print(actual)
            self.assertEqual(len(expected), len(actual), actual)
            expected.sort()
            actual.sort()
            for i in range(len(expected)):
                self.assertEqual(expected[i], actual[i]) 

# Test helpers

def make_linked_list(xs: list[int]) -> ListNode:
    if len(xs) == 0:
        return None
    nxt = None
    xs.reverse()
    for x in xs: 
        nxt = ListNode(x, nxt)
    return nxt

def make_list(head: ListNode) -> list[int]:
    out = []
    while head != None:
        out.append(head.val)
        head = head.next
    return out