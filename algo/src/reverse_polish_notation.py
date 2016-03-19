#-*- coding:utf-8 -*-

LEFT = 0x001
RIGHT = 0x002
COMA = ','
LEFT_PARANTHESES = '('
RIGHT_PARANTHESES = ')'

def reverse_polish_notation(tokens, operators, functions=[]):
    """ Implements Dijkstra's Shunting Yard algorithm for converting an infix
    expression into a postfix expression.

    Handles functions and paranthesis.

    Obs: operator precedence from infix notation translates into operator
    order into postfix notation.

    Args:
        tokens: list, of strings with input tokens in infix notation.
        operators: dict, format {operator: {operator, precedence, associativity}}
            operator: character
            precedence: number, 1 to 10, conveys the order in which operators are evaluated.
            associativity: number, either LEFT or RIGHT
        functions: list, of name strings.
    Returns:
        output: list of string token in postfix notation.
    """
    output_queue = []
    operator_stack = []

    for token in tokens:
        if is_operand(token, operators, functions):
            output_queue.append(token)
        elif is_function(token, functions):
            operator_stack.append(token)
        elif token == ',':
            while len(operator_stack) > 0 and operator_stack[-1] != LEFT_PARANTHESES:
                output_queue.append(operator_stack.pop())
            if len(operator_stack) == 0:
                raise Error('Misplaced separator or missmatch parantheses')
        elif is_operator(token, operators):
            while len(operator_stack) > 0 and \
              is_operator(operator_stack[-1], operators) and \
              ((associativity(token, operators) == LEFT and precedence(token, operators) <= precedence(operator_stack[-1], operators)) or \
               (associativity(token, operators) == RIGHT and precedence(token, operators) < precedence(operator_stack[-1], operators))):
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
            if len(operator_stack) > 0 and is_function(operator_stack[-1], functions):
                output_queue.append(operator_stack.pop())

    while len(operator_stack) != 0:
        if operator_stack[-1] in [LEFT_PARANTHESES, RIGHT_PARANTHESES]:
            raise Error('Missmatch parantheses')
        output_queue.append(operator_stack.pop())

    return output_queue

# Utils

def is_operand(token, operators, functions):
    return (not is_function(token, functions)) and \
           (not is_operator(token, operators)) and \
           (token not in [',', LEFT_PARANTHESES, RIGHT_PARANTHESES])


def is_function(token, functions):
    return token in functions

def is_operator(token, operators):
    return token in operators.keys()

def associativity(operator, operators):
    return operators[operator]['associativity']

def precedence(operator, operators):
    return operators[operator]['precedence']
