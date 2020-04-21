# -*- coding: utf-8 -*-

class LinkedListNode(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None

def from_list(lst):
    """ helper method builds a single linked list from a list """
    if len(lst) == 0:
        return None
    node = LinkedListNode(lst[0])
    node.next = from_list(lst[1:])
    return node

def to_list(head):
    """ helper method to turn a linked list into a list for easier printing """
    if head == None:
        return []
    out = [head.value]
    out.extend(to_list(head.next))
    return out

def value(head):
    if head == None:
        return None
    return head.value

def goto(head, val):
    if head == None:
        return None
    if head.value == val:
        return head
    return goto(head.next, val)

def remove_dups(head):
    """ 2.1 Remove Dups! Write code to remove duplicates from an unsorted
    linked list.
    FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?
    """
    def chase(node, val):
        while node != None and node.value == val:
            node = node.next
        return node

    node = head
    while node != None:
        first_distinct_node = chase(node, node.value)
        node.next = first_distinct_node
        node = first_distinct_node
    return head

def kth_to_last(head, k):
    """ 2.2 Return Kth to Last: Implement an algorithm to find the kth to last
    element of a singly linked list.
    """
    def advance(node, n):
        if node == None or n == 0:
            return (node, n)
        else:
            return advance(node.next, n - 1)

    (runner, index) = advance(head, k)
    if index != 0 or runner == None:
        return None
    node = head
    runner = runner.next
    while runner != None:
        runner = runner.next
        node = node.next
    return node

def delete_middle(middle):
    """ 2.3 Delete Middle Node: Implement an algorithm to delete a node in the
    middle (i.e., any node but the first and last node, not necessarily the exact
    middle) of a singly linked list, given only access to that node.
    EXAMPLE
    Input: the node c from the linked list a->b->c->d->e->f
    Result: nothing is returned, but the new linked list looks like a->b->d->e->f
    """
    middle.value = middle.next.value
    middle.next = middle.next.next

