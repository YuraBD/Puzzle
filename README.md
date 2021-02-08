Module **puzzle.py** checks if the game board of
 puzzle game is correct.
Return False is there are same numbers in row, colum or color.

It has 5 functions:

1) **horizontal_check**
Check if rows have similar numbers
Return False if have, True otherwise

2) **hor_to_ver**
Reverse board. Rows become columns and columns
become rows

3) **vertical_check**
Check if columns have similar numbers
Return False if have, True otherwise

4) **color_check**
Check if colors have similar numbers
Return False if have, True otherwise

5) **validate_board**
Check whether board status is compliant with rules.
Return True if the board status is compliant with the rules,
False otherwise.