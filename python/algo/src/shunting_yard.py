# -*- coding:utf-8 -*-

from collections import deque

op_prec = {
    '+': 2,
    '-': 2,
    '*': 3,
    '/': 3,
    '^': 4,
}

def prec(op):
    if op in op_prec:
        return op_prec[op]
    return -1

def assoc(op):
    if op == '^':
        return 'right'
    return 'left'

def shunting_yard(tokens):
    output_queue = deque([])
    operator_stack = []
    for token in tokens:
        if str.isdigit(token):
            output_queue.appendleft(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                output_queue.appendleft(operator_stack.pop())
            operator_stack.pop() # ditch the '('
        elif token in ['+', '-', '*', '/', '^']:
            while len(operator_stack) > 0 and \
                    operator_stack[-1] != '(' and \
                    (prec(operator_stack[-1]) > prec(token) or \
                    (prec(operator_stack[-1]) == prec(token) and assoc(token) == 'left')):
                output_queue.appendleft(operator_stack.pop())
            operator_stack.append(token)
        else: # is function
            operator_stack.append(token)
    while len(operator_stack) > 0:
        output_queue.appendleft(operator_stack.pop())
    return list(output_queue)

class ASTNode(object):
    def __init__(self, token, left=None, right=None):
        self.token = token
        self.left = left
        self.right = right

def parse(tokens):
    stack = []
    rpn = shunting_yard(tokens)
    for token in reversed(rpn):
        if str.isdigit(token):
            stack.append(ASTNode(token))
        else:
            op = ASTNode(token, stack.pop(), stack.pop())
            stack.append(op)
    return stack.pop()
