import numpy as np

'''
Start with those first:
aggregate height, 
complete lines, 
holes,  
bumpiness,
'''








# for each hole, count how many blocks are above it and add it to the total that you will return from the function.
def count_hole_effect(board):
    pass


# For each column, if there is a hole *segment*, count how many block needs to be cleared for the entire segment to be free (have nothing above it)
def count_hole_segements_effect(board):
    pass



# How many rows are cleared in the move
# give some n*X points in case of n row cleared (choose X, but don't choose is negative nor too big)
# def rows_cleared_effect(current_board, previous_board):
#     pass


# 
# max(Max height - 8, 0) so simple, right?
def height_effect(board):
    pass



# empty columns - 1, even more simple!
def columns_effect(board):
    pass

# 
# NOTE: MAKE SURE TO INCREASE THE REWARD FOR MORE CONSECUTIVE ROWS

# Reward for each *1* consecutive row with 1 column (the same column) only empty.


def one_rows_effect(board):
    pass


# Reward for each *2* consecutive row with 2 column (the same column) only empty.
def two_rows_effect(board):
    pass


# Reward for each *3* consecutive row with 3 column (the same column) only empty.
def three_rows_effect(board):
    pass


# Reward for each *4* consecutive row with 4 column (the same column) only empty.
def four_rows_effect(board):
    pass
