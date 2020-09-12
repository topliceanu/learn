# -*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_linked_list(ls):
    if len(ls) == 0:
        return None
    hd, tl = ls[0], ls[1:]
    return ListNode(hd, make_linked_list(tl))

def from_linked_list(ll):
    if ll == None:
        return []
    rest = from_linked_list(ll.next)
    rest.insert(0, ll.val)
    return rest

