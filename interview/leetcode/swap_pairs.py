# -*- coding: utf-8 -*-

# Source https://leetcode.com/problems/swap-nodes-in-pairs/

def swap_pairs(head):
    if head == None:
        return None
    if head.next == None:
        return head
    first = head.next
    second = first.next

    first.next = head
    head.next = swap_pairs(second)
    return first
