# -*- coding: utf-8 -*-

def find_empty(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                return (i, j)
    return (-1, -1)

def check_row(board, row, col, val):
    for i in range(len(board)):
        if i != col and board[row][i] == val:
            return False
    return True

def check_column(board, row, col, val):
    for j in range(len(board)):
        if j != row and board[j][col] == val:
            return False
    return True

def check_square(board, row, col, val):
    n = len(board)
    row_low, row_high = (row / 3) * 3, (row / 3 + 1) * 3
    col_low, col_high = (col / 3) * 3, (col / 3 + 1) * 3
    for i in range(row_low, row_high):
        for j in range(col_low, col_high):
            if i != row and j != col and board[i][j] == val:
                return False
    return True

def valid(board, row, col, val):
    return \
        check_row(board, row, col, val) and \
        check_column(board, row, col, val) and \
        check_square(board, row, col, val)

def sudoku_solver(board):
    """ Backtracking algorithm to solve a Sudoku board.
    Args:
        board, a 2D 9x9 matrix of integers corresponding to the Sudoku board.
    Returns:
        boolean, True if the board was solved. The board is updated in place with the solution.
    """
    row, col= find_empty(board)
    if row == -1 and col == -1:
        return True
    for i in range(1, 10):
        if valid(board, row, col, i):
            board[row][col] = i
            if sudoku_solver(board):
                return True
            board[row][col] = 0
    return False


"""
$ mail list [<page> <num_items_on_page> --filter=from=alex@gmail.com --filter=to=daniel@metabase.com]
<email_id> <from_email> <email_subject> <100_chars_body> <read?> <starred?>

mail search <keyword>
<email_id> <from_email> <email_subject> <100_chars_body> <read?> <starred?>

mail mark-as-read <email_id>
mail open <email_id>
mail delete <email_id>
cat email.txt | mail send --to=daniel@metabase.com

type email = {
    id int
    subject string
    from string
    body string
}
"""

def format_body(body):
    return body # add ...

def list_emails(emails):
    for email in emails:
        print "({}) {} {}: {}".format(email["id"], email["from"], email["subject"], format_body(email["body"]))

"""
list_emails([
    {
        "id": 123,
        "from": "test@gmail.com",
        "subject": "Hello there",
        "body": "How are you doing?",
    },
    {
        "id": 123,
        "from": "test@gmail.com",
        "subject": "Hello there",
        "body": "How are you doing?",
    },
    {
        "id": 123,
        "from": "test@gmail.com",
        "subject": "Hello there",
        "body": "How are you doing?",
    },
    {
        "id": 123,
        "from": "test@gmail.com",
        "subject": "Hello there",
        "body": "How are you doing?",
    }
])
"""

def levenstein(s, t):
    """ Calculates the Levenstein distance between two strings.

    Below is the types returned by the algorithm if we wanted to
    return the list of operations:
        type operations = [operation]
        type operation =
        | Nothing existing_char
        | Insert new_char
        | Delete orig_char
        | Substitute orig_char, new_char
    """
    if len(s) == 0:
        # t additions
        return len(t)
    if len(t) == 0:
        # s additions
        return len(s)
    if s[-1] == t[-1]:
        return levenstein(s[:-1], t[:-1])

    a = levenstein(s[:-1], t[:-1])
    b = levenstein(s, t[:-1])
    c = levenstein(s[:-1], t)

    return min(a, b, c) + 1
