# IMPORTANT NOTES:
# The board contains two type of characters (.) and (O) "without brackets"
# (.) means that the cell is BLANK "it is declared as BLANK globaly, so use it"
# (O) means that the cell is occupied
# Each cell has its own color


# KHALED
# Main function for making the computer play
def computer_plays(board, piece, chromosom):
    pass


# OMAR
# Refer to the function (calc_move_info)
# It should return the optimal rotation and column for the piece
def test_all_moves(board, piece, chromosom):
    pass


# FAWZY
# Play the move after finding the optimal one
# Refer to the function (run_game)
def play_move(board, rotation, column):
    pass

# MOHSEN
# for each hole, count how many blocks are above it and add it to the total that you will return from the function.


def count_hole_effect(board):
    pass


# MOHSEN
# For each column, if there is a hole *segment*, count how many block needs to be cleared for the entire segment to be free (have nothing above it)
def count_hole_segements_effect(board):
    pass


# KHALED
# How many rows are cleared in the move
# give some n*X points in case of n row cleared (choose X, but don't choose is negative nor too big)
def rows_cleared_effect(current_board, previous_board):
    pass


# FAWZY
# max(Max height - 8, 0) so simple, right?
def height_effect(board):
    pass


# KHALED
# empty columns - 1, even more simple!
def columns_effect(board):
    pass

# OMAR
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