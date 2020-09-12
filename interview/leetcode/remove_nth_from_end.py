# -*- coding: utf-8 -*-

# Source:  https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(ls, n):
    l = length(ls)
    if l < n or n <= 0:
        return ls
    return remove(ls, l - n)

def length(ls):
    if ls == None:
        return 0
    return 1 + length(ls.next)

def remove(ls, n):
    if n == 0:
        return ls.next
    return ListNode(ls.val, remove(ls.next, n-1))
