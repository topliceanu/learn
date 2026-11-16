import unittest

from src.leetcode.leetcode import ListNode, reverse_k_group, merge_k_lists

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