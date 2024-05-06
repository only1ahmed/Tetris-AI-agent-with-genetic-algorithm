import numpy as np
import tetris_base as tb
'''
Start with those first:
aggregate height, 
complete lines, 
holes,  
bumpiness,
'''
BLANK = '.'

def cal_board_heuristics(board):

    heights = height_each_col(board)
    # print('Heights: ',heights)
    aggregate_height = sum(heights)
    complete_lines = complete_lines_effect(board)
    holes = holes_effect(board)
    bumpiness = bumpiness_effect(heights)

    return {'aggregate_height': aggregate_height, 'complete_lines': complete_lines, 'holes': holes, 'bumpiness': bumpiness} 

def height_each_col(board):
    '''
    Returns a list of the height of each column in the board
    '''
    col_heights = []
    for col in range(tb.BOARDWIDTH):
        temp_col_h = 0
        for i, cell in enumerate(board[col]):
            if cell != BLANK:
                temp_col_h = tb.BOARDHEIGHT - i
                break
        col_heights.append(temp_col_h)

    return col_heights

def complete_lines_effect(board):
    '''
    Removes the completed lines and 
    Returns the number of removed lines
    '''
    return tb.remove_complete_lines(board)

def holes_effect(board):
    '''
    Returns the number of holes
    '''
    holes = 0
    for col in range(tb.BOARDWIDTH):
        col_holes = 0
        for row in range(tb.BOARDHEIGHT-1,-1,-1):
            if board[col][row] == BLANK:
                col_holes += 1
            elif board[col][row] != BLANK:
                holes += col_holes
                col_holes = 0
            
    return holes

def bumpiness_effect(heights):
    '''
    Returns a measure on how bumpy the surface is
    '''
    bumpiness = 0
    for i in range(len(heights)-1):
        bumpiness += abs(heights[i] - heights[i+1])

    return bumpiness


#######################################################################

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
