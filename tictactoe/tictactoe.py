"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    In the initial game state, X gets the first move. 
    Subsequently, the player alternates with each additional move.
    """
    if board_sum(board)%2 == 0:
        return X
    else:
        return O

def board_sum(board):
    """
    Counts number of tiles played so far
    """
    board_sum = 0
    for row in board:
        for entry in row:
            if entry != EMPTY:
                board_sum += 1
    return board_sum

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    In order fo there to be a winner there must be at least five tiles played
    """
    tiles_played = board_sum(board)
    # Check if enough tiles have been played
    if tiles_played < 5:
        return False

    # Check if all tiles have been played
    if tiles_played > 8:
        return True
    
    # Check if X has winned

    # Check if O has winned

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
