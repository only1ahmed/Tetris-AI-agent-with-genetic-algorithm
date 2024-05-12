import numpy as np
import tetris_base as tb


HEURISTIC_NAMES = [
    'aggregate_height',
    'complete_lines', 
    'holes', 
    'bumpiness',
    'hole_segments',
    'max_height',
    'empty_columns',
    'one_rows',
    'two_rows',
    'three_rows',
    'four_rows'
]


BLANK = '.'

def cal_board_heuristics(board, heuristic_to_use = HEURISTIC_NAMES):

    heights = height_each_col(board)
    cal_data = {}

    for heuristic in heuristic_to_use:
        
        if heuristic == 'aggregate_height':
            cal_data['aggregate_height'] = sum(heights)
        elif heuristic == 'complete_lines':
            cal_data['complete_lines'] = complete_lines_effect(board)
        elif heuristic == 'holes':
            cal_data['holes'] = holes_effect(board)
        elif heuristic == 'bumpiness':
            cal_data['bumpiness'] = bumpiness_effect(heights)
        elif heuristic == 'hole_segments':
            cal_data['hole_segments'] = count_hole_segements_effect(board)
        elif heuristic == 'max_height':
            cal_data['max_height'] = height_effect(board)
        elif heuristic == 'empty_columns':
            cal_data['empty_columns'] = columns_effect(board)
        elif heuristic == 'one_rows':
            cal_data['one_rows'] = one_rows_effect(board)
        elif heuristic == 'two_rows':
            cal_data['two_rows'] = two_rows_effect(board)
        elif heuristic == 'three_rows':
            cal_data['three_rows'] = three_rows_effect(board)
        elif heuristic == 'four_rows':
            cal_data['four_rows'] = four_rows_effect(board)

    return cal_data
 
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
    return tb.remove_complete_lines(board) ** 6

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
                # old holes_effect requires this (DON'T DELETE)
                col_holes = 0
            
    return holes**2

def bumpiness_effect(heights):
    '''
    Returns a measure on how bumpy the surface is
    '''
    bumpiness = 0
    for i in range(len(heights)-1):
        bumpiness += abs(heights[i] - heights[i+1])

    return bumpiness


#######################################################################

# For each column, if there is a hole *segment*, count how many block needs to be cleared for the entire segment to be free (have nothing above it)
def count_hole_segements_effect(board):
    sum = 0
    for col in range(tb.BOARDWIDTH):
        col_segs = 0
        for row in range(tb.BOARDHEIGHT-1,-1,-1):
            if board[col][row] == BLANK:
                col_segs += 1
                while row >= 0 and board[col][row] == BLANK:
                    row -= 1
                row += 1
            elif board[col][row] != BLANK:
                sum += col_segs
                
    return sum

 
# max(Max height - 8, 0) so simple, right?
def height_effect(board):
    maxes = height_each_col(board)

    return max(max(maxes) - 8, 0) ** 2
    
# empty columns - 1, even more simple!
def columns_effect(board):
    cnt = 0
    cols = height_each_col(board)
    for i in range(len(cols)):
        if cols[i] == 0:
            cnt+=1
    return max(0, cnt - 1)

# Reward for each *1* consecutive row with 1 column (the same column) only empty.
def one_rows_effect(board):
    sum = 0
    for row in range(tb.BOARDHEIGHT-1,-1,-1):
        full_col = 0
        empty_pos = -1
        for col in range(tb.BOARDWIDTH):
            if board[col][row] != BLANK:
                full_col += 1
            else:
                empty_pos = col
        if full_col == tb.BOARDWIDTH - 1:
            seg_cnt = 0
            while row >= 0 and board[empty_pos][row] == BLANK:
                full_col2 = 0
                for col in range(tb.BOARDWIDTH):
                    if board[col][row] != BLANK:
                        full_col2 += 1
                if full_col2 == tb.BOARDWIDTH - 1:
                    seg_cnt+=1
                else:
                    break;
                row-=1
            row+=1
            if seg_cnt == 1:
                sum+=1
    return sum * 1


# Reward for each *2* consecutive row with 2 column (the same column) only empty.
def two_rows_effect(board):
    sum = 0
    for row in range(tb.BOARDHEIGHT-1,-1,-1):
        full_col = 0
        empty_pos = -1
        for col in range(tb.BOARDWIDTH):
            if board[col][row] != BLANK:
                full_col += 1
            else:
                empty_pos = col
        if full_col == tb.BOARDWIDTH - 1:
            seg_cnt = 0
            while row >= 0 and board[empty_pos][row] == BLANK:
                full_col2 = 0
                for col in range(tb.BOARDWIDTH):
                    if board[col][row] != BLANK:
                        full_col2 += 1
                if full_col2 == tb.BOARDWIDTH - 1:
                    seg_cnt+=1
                else:
                    break;
                row-=1
            row+=1
            if seg_cnt == 2:
                sum+=1
    return sum * 2

# Reward for each *3* consecutive row with 3 column (the same column) only empty.
def three_rows_effect(board):
    sum = 0
    for row in range(tb.BOARDHEIGHT-1,-1,-1):
        full_col = 0
        empty_pos = -1
        for col in range(tb.BOARDWIDTH):
            if board[col][row] != BLANK:
                full_col += 1
            else:
                empty_pos = col
        if full_col == tb.BOARDWIDTH - 1:
            seg_cnt = 0
            while row >= 0 and board[empty_pos][row] == BLANK:
                full_col2 = 0
                for col in range(tb.BOARDWIDTH):
                    if board[col][row] != BLANK:
                        full_col2 += 1
                if full_col2 == tb.BOARDWIDTH - 1:
                    seg_cnt+=1
                else:
                    break;
                row-=1
            row+=1
            if seg_cnt == 3:
                sum+=1
    return sum * 3


# Reward for each *4* consecutive row with 4 column (the same column) only empty.
def four_rows_effect(board):
    sum = 0
    for row in range(tb.BOARDHEIGHT-1,-1,-1):
        full_col = 0
        empty_pos = -1
        for col in range(tb.BOARDWIDTH):
            if board[col][row] != BLANK:
                full_col += 1
            else:
                empty_pos = col
        if full_col == tb.BOARDWIDTH - 1:
            seg_cnt = 0
            while row >= 0 and board[empty_pos][row] == BLANK:
                full_col2 = 0
                for col in range(tb.BOARDWIDTH):
                    if board[col][row] != BLANK:
                        full_col2 += 1
                if full_col2 == tb.BOARDWIDTH - 1:
                    seg_cnt+=1
                else:
                    break;
                row-=1
            row+=1
            if seg_cnt == 4:
                sum+=1
    return sum * 4