'''
Github: https://github.com/YuraBD/Puzzle

This module checks if game board is correct.

It has 5 functions:

1) horizontal_check

Check if rows have similar numbers
Return False if have, True otherwise

>>> horizontal_check(["**** ****","***1 ****","**  3****",\
                      "* 4 1****","     9 5 "," 6  83  *",\
                      "3   1  **","  8  2***","  2  ****"])
True
>>> horizontal_check(["**** ****","***11****","**  3****",\
                      "* 4 1****","     9 5 "," 6  83  *",\
                      "3   1  **","  8  2***","  2  ****"])
False

2) hor_to_ver

Reverse board. Rows become columns and columns
become rows

>>> hor_to_ver(["**** ****","***1 ****","**  3****",\
                "* 4 1****","     9 5 "," 6  83  *",\
                "3   1  **","  8  2***","  2  ****"])
['****  3  ', '***  6   ', '** 4   82', '*1       ', \
'  31 81  ', '****93 2*', '****   **', '****5 ***', '**** ****']

3) vertical_check

Check if columns have similar numbers
Return False if have, True otherwise

>>> vertical_check(["**** ****","***1 ****","**  3****",\
                    "* 4 1****","     9 5 "," 6  83  *",\
                    "3   1  **","  8  2***","  2  ****"])
False
>>> vertical_check(["**** ****","***1 ****","**  3****",\
                    "* 4 1****","     9 5 "," 6  83  *",\
                    "3   5  **","  8  2***","  2  ****"])
True

4) color_check

Check if colors have similar numbers
Return False if have, True otherwise

>>> color_check(["**** ****","***1 ****","**  3****",\
                 "* 4 1****","     9 5 "," 6  83  *",\
                 "3   1  **","  8  2***","  2  ****"])
True
>>> color_check(["**** ****","***1 ****","**  3****",\
                 "* 4 1****"," 2   9 5 "," 6  83  *",\
                 "3   1  **","  8  2***","  2  ****"])
False

5) validate_board

Check whether board status is compliant with rules.
Return True if the board status is compliant with the rules,
False otherwise.

>>> validate_board(["**** ****","***1 ****","**  3****",\
                    "* 4 1****","     9 5 "," 6  83  *",\
                    "3   5  **","  8  2***","  2  ****"])
True
>>> validate_board(["**** ****","***1 ****","**  3****",\
                    "* 4 1****"," 2   9 5 "," 6  83  *",\
                    "3   1  **","  8  2***","  2  ****"])
False
'''


def horizontal_check(board: list) -> bool:
    '''
    Check if rows have similar numbers
    Return False if have, True otherwise

    >>> horizontal_check(["**** ****","***1 ****","**  3****",\
                          "* 4 1****","     9 5 "," 6  83  *",\
                          "3   1  **","  8  2***","  2  ****"])
    True
    >>> horizontal_check(["**** ****","***11****","**  3****",\
                          "* 4 1****","     9 5 "," 6  83  *",\
                          "3   1  **","  8  2***","  2  ****"])
    False
    '''
    c_board = board.copy()
    for row in c_board:
        row = row.replace('*', '')
        row = row.replace(' ', '')
        while row:
            if row.count(row[0]) != 1:
                return False
            row = row.replace(row[0], '')
    return True


def hor_to_ver(board: list) -> list:
    '''
    Reverse board. Rows become columns and columns
     become rows

    >>> hor_to_ver(["**** ****","***1 ****","**  3****",\
                     "* 4 1****","     9 5 "," 6  83  *",\
                     "3   1  **","  8  2***","  2  ****"])
    ['****  3  ', '***  6   ', '** 4   82', '*1       ', \
'  31 81  ', '****93 2*', '****   **', '****5 ***', '**** ****']
    '''
    r_board = []
    for i in range(len(board)):
        row = []
        for j in range(len(board[i])):
            row.append(board[j][i])
        r_board.append(row)
    r_board = list(map(lambda row: ''.join(row), r_board))
    return r_board


def vertical_check(board: list) -> bool:
    '''
    Check if columns have similar numbers
    Return False if have, True otherwise

    >>> vertical_check(["**** ****","***1 ****","**  3****",\
                        "* 4 1****","     9 5 "," 6  83  *",\
                        "3   1  **","  8  2***","  2  ****"])
    False
    >>> vertical_check(["**** ****","***1 ****","**  3****",\
                        "* 4 1****","     9 5 "," 6  83  *",\
                        "3   5  **","  8  2***","  2  ****"])
    True
    '''
    r_board = hor_to_ver(board)
    return horizontal_check(r_board)


def color_check(board: list) -> bool:
    '''
    Check if colors have similar numbers
    Return False if have, True otherwise

    >>> color_check(["**** ****","***1 ****","**  3****",\
                     "* 4 1****","     9 5 "," 6  83  *",\
                     "3   1  **","  8  2***","  2  ****"])
    True
    >>> color_check(["**** ****","***1 ****","**  3****",\
                     "* 4 1****"," 2   9 5 "," 6  83  *",\
                     "3   1  **","  8  2***","  2  ****"])
    False
    '''
    r_board = hor_to_ver(board)
    colors = []
    for i in range(5):
        row = board[8-i][i:]
        r_row = r_board[i][::-1][i+1:]
        colors.append(row+r_row)
    return horizontal_check(colors)


def validate_board(board: list) -> bool:
    '''
    Check whether board status is compliant with rules.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> validate_board(["**** ****","***1 ****","**  3****",\
                        "* 4 1****","     9 5 "," 6  83  *",\
                        "3   5  **","  8  2***","  2  ****"])
    True
    >>> validate_board(["**** ****","***1 ****","**  3****",\
                        "* 4 1****"," 2   9 5 "," 6  83  *",\
                        "3   1  **","  8  2***","  2  ****"])
    False
    '''
    return horizontal_check(board) and\
           vertical_check(board) and\
           color_check(board)


if __name__ == '__main__':
    game_board = [
             "**** ****",
             "***1 ****",
             "**  3****",
             "* 4 1****",
             "     9 5 ",
             " 6  83  *",
             "3   1  **",
             "  8  2***",
             "  2  ****"
            ]
    print(validate_board(game_board))
