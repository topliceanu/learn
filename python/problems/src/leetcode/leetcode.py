#!/bin/python

# Problem 14: Longest Common Prefix
# Source: https://leetcode.com/problems/longest-common-prefix/
def longestCommonPrefix(strs: list[str]) -> str:
    # Naive approach: O(n*m), n = len(strs), m = len(min(strs))
    if len(strs) == 0:
        return ""

    def check(strs: list[str], i: int, prev: str) -> bool:
        for s in strs:
            if i >= len(s): 
                return False
            if s[i] != prev:
                return False
        return True

    i = 0
    while True:
        if i >= len(strs[0]):
            break
        prev = strs[0][i]
        if not self.check(strs, i, prev):
            break
        i += 1
    return strs[0][:i]

# Problem 25: Reverse Nodes in k-Group
# Source: https://leetcode.com/problems/reverse-nodes-in-k-group/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def advance(head: ListNode, k: int) -> ListNode: 
    # Returns the k-th element in the list starting at head or None if the list has less than k elements.
    while head != None and k > 1:
        head = head.next
        k -= 1
    if k == 1 and head != None:
        return head
    return None

def reverse(first: ListNode, last:ListNode) -> (ListNode, ListNode):
    # Reverses a list between first and last 
    # !!! Assumes there is a link between first and last.
    # !!! Assumes first and last are not None.
    # ¡¡¡ Assumes first and last are not identical. 
    # first -> second -> last -> third (might be None)
    # Returns a pointer to the first element and the last one in the reversed list.
    prev = None
    cur = first
    while cur != last:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return (last, first)

def reverse_k_group(head: ListNode, k: int) -> ListNode:
    if head == None:
        return head
    if k <= 1: 
        return head
    last = advance(head, k)
    if last == None:
        return head
    (head, last) = reverse(head, last)
    while last.next != None:
        (first, last) = (last.next, advance(last.next, k))
        if last == None:
            return head
        (new_first, new_last) = reverse(first, last)
        last.next = new_first
        last = new_last
    return head 

def reverse_k_group_2(head: ListNode, k: int) -> ListNode:
    if not head:
        return None

    tail = head

    for _ in range(k):
        if not tail:
            return head
        tail = tail.next

    def reverse(cur, end):
        prev = None

        while cur != end:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev      

    new_head = reverse(head, tail)
    head.next = reverse_k_group(tail, k)

    return new_head 

def merge_k_lists(lists: list[ListNode]) -> ListNode:
    out = None
    for l in lists:
        out = merge_2_lists(out, l)
    return out

def merge_2_lists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None and l2 == None:
        return None
    if l1 == None and l2 != None:
        return l2
    if l1 != None and l2 == None:
        return l1
    new_head = ListNode(-1, None) # Fake first node
    prev = new_head
    while l1 != None and l2 != None:
        if l1.val < l2.val:
            cur = l1
            l1 = l1.next
            cur.next = None
            prev.next = cur
            prev = cur
        elif l1.val > l2.val:
            cur = l2
            l2 = l2.next
            cur.next = None
            prev.next = cur
            prev = cur
        else:
            cur1 = l1 
            cur2 = l2 
            l1 = l1.next
            l2 = l2.next
            prev.next = cur1
            cur1.next = cur2
            cur2.next = None
            prev = cur2
    if l1 != None:
        prev.next = l1
    if l2 != None:
        prev.next = l2
    return new_head.next # Ignore fake first node.

