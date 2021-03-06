# -*- coding: utf-8 -*-

# Source: https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def to_list(self):
        if self.next == None:
            return [self.val]
        else:
            return [self.val] + self.next.to_list()

def copy_node(l, carry=0):
    if l == None:
        if carry != 0:
            return ListNode(val=carry)
        return None
    val = l.val + carry
    carry = val / 10
    val = val % 10
    new_node = ListNode(val=val)
    new_node.next = copy_node(l.next, carry)
    return new_node

def add_lists(l1, l2, carry):
    if l1 == None and l2 == None:
        return copy_node(None, carry)

    if l1 != None and l2 == None:
        return copy_node(l1, carry)

    if l1 == None and l2 != None:
        return copy_node(l2, carry)

    val = l1.val + l2.val + carry
    carry = val / 10
    val = val % 10
    new_node = ListNode(val=val)
    new_node.next = add_lists(l1.next, l2.next, carry)
    return new_node

class Solution:
    def addTwoNumber(self, l1, l2):
        return add_lists(l1, l2, 0)
