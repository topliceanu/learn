def match_parantheses(data):
    """ Makes sure the parantheses in data are correctly closed.

    Returns:
        True if the parantheses are correctly closed.
    """
    parantheses = ['[', ']', '(', ')']
    matches = {
        '[': ']',
        '(': ')'
    }
    stack = []

    for char in data:
        if char in parantheses:
            isOpening = char in matches.keys()
            isClosing = char in matches.values()
            if isOpening:
                stack.append(char)
            if isClosing:
                opened = stack.pop()
                if matches[opened] != char:
                    return False

    if len(stack) != 0:
        return False

    return True
