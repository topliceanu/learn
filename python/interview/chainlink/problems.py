def solution(prices):
    if len(prices) == 0:
        return 0
    # We are always paying the first price.
    total = prices[0]
    min_price = prices[0]
    for i in range(1, len(prices)):
        if prices[i] > min_price:
            total += prices[i] - min_price
        if prices[i] < min_price:
            min_price = prices[i]
    return total

def num_divisors(number, keys):
    count = 0
    for key in keys:
        if number % key == 0:
            count += 1
    return count

def encryptionValidity(instructionCount, validityPeriod, keys):
    max_num_divisors = float('-inf')
    for key in keys:
        num = num_divisors(key, keys)
        if num > max_num_divisors:
            max_num_divisors = num
    encryption_strength = max_num_divisors * pow(10, 5)
    is_crackable = 1
    if encryption_strength / instructionCount > validityPeriod:
        is_crackable = 0
    return is_crackable, encryption_strength

# Write a function that accepts as an argument a string of addition/subtraction operations.
# The function should return the result of the operations as an integer
# ex: calculate("1 - 2 + 3") => 2

def apply_op(op, a, b):
    if op == 'plus':
        return a + b
    if op == 'minus':
        return a - b

def calculate(expression):
    tokens = expression.split(" ")
    result = 0
    last_op = 'plus'
    for token in tokens:
        if token == "":
            continue
        if str.isdigit(token):
            new_val = int(token)
            result = apply_op(last_op, result, new_val)
        if token == '+':
            last_op = 'plus'
        if token == '-':
            last_op = 'minus'
    return result

# Next, write a function that accepts as an argument a string of addition/subtraction
# operations and also includes parentheses to indicate order of operations. The function
#  should return the result of the operations as an integer
# ex: calculate("1 - (2 + 3)") => -4

def parse_number(expression):
    if len(expression) == 0:
        return '', expression
    hd, tl = expression[0], expression[1:]
    if str.isdigit(hd) == False:
        return '', expression
    more, rest = parse_number(tl)
    return hd + more, rest

def tokenize(expression):
    if len(expression) == 0:
        return []
    hd, tl = expression[0], expression[1:]
    if hd == ' ':
        return tokenize(tl)
    if str.isdigit(hd):
        num, rest = parse_number(expression)
        return [int(num)] + tokenize(rest)
    if hd in ['(', ')', '+', '-']:
        return [hd] + tokenize(tl)

def calculate_two_rec(tokens, result_so_far, last_op):
    if len(tokens) == 0:
        return result_so_far, []
    token, rest = tokens[0], tokens[1:]
    if isinstance(token, int):
        return calculate_two_rec(rest, apply_op(last_op, result_so_far, token), last_op)
    if token == '+':
        return calculate_two_rec(rest, result_so_far, 'plus')
    if token == '-':
        return calculate_two_rec(rest, result_so_far, 'minus')
    if token == '(':
        value_in_paran, rest_after_paran = calculate_two_rec(rest, 0, 'plus')
        return calculate_two_rec(rest_after_paran, apply_op(last_op, result_so_far, value_in_paran), 'plus')
    if token == ')':
        return result_so_far, rest

def calculate_two(expression):
    tokens = tokenize(expression)
    final_result, _ = calculate_two_rec(tokens, 0, 'plus')
    return final_result
