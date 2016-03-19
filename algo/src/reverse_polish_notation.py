#-*- coding:utf-8 -*-

LEFT = 0x001
RIGHT = 0x002
COMA = ','
LEFT_PARANTHESES = '('
RIGHT_PARANTHESES = ')'

def reverse_polish_notation(tokens):
    """ Implements Dijkstra's Shunting Yard algorithm for converting an infix
    expression into a postfix expression.

    Handles functions and paranthesis.

    Obs: operator precendence from infix notation translates into operator
    order into postfix notation.

    Args:
        tokens: list, of strings with input tokens in infix notation.
        operators: list, format [[operator, precedence, associativity]].
            operator: character
            precedence: number, 1 to 10, conveys the order in which operators are evaluated.
            associativity: number, either LEFT or RIGHT
    Returns:
        output: list of string token in postfix notation.
    """
    output_queue = []
    operator_stack = []

    for token in tokens:
        if is_operand(token):
            output_queue.append(token)
        elif is_function(token):
            operator_stack.append(token)
        elif token == ',':
            while len(operator_stack) > 0 and operator_stack[-1] != LEFT_PARANTHESES:
                output_queue.append(operator_stack.pop())
            if len(operator_stack) == 0:
                raise Error('Misplaced separator or missmatch parantheses')
        elif is_operator(token):
            while len(operator_stack) > 0 and \
              is_operator(operator_stack[-1]) and \
              ((associativity(token) == LEFT and precedence(token) <= precedence(operator_stack[-1])) or \
               (associativity(token) == RIGHT and precedence(token) < precedence(operator_stack[-1]))):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == LEFT_PARANTHESES:
            operator_stack.append(token)
        elif token == RIGHT_PARANTHESES:
            while (len(operator_stack) > 0 and operator_stack[-1] != LEFT_PARANTHESES):
                output_queue.append(operator_stack.pop())
            if len(operator_stack) == 0:
                raise Error('Mismatch parantheses')
            left_parantheses = operator_stack.pop()
            if len(operator_stack) > 0 and is_function(operator_stack[-1]):
                output_queue.append(operator_stack.pop())

    while len(operator_stack) != 0:
        if operator_stack[-1] in [LEFT_PARANTHESES, RIGHT_PARANTHESES]:
            raise Error('Missmatch parantheses')
        output_queue.append(operator_stack.pop())

    return output_queue

# Utils

def is_operand(token):
    return token in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def is_function(token):
    return token in ['sin', 'cos', 'max', 'min']

def is_operator(token):
    return token in ['+', '-', '*', '/', '^']

def associativity(operator):
    if operator in ['+', '-', '/', '*']:
        return LEFT
    return RIGHT

def precedence(operator):
    levels = {
        '+': 2,
        '-': 2,
        '*': 3,
        '/': 3,
        '^': 4
    }
    return levels[operator]
