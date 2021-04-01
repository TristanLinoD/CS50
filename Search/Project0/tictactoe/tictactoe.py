"""
Tic Tac Toe Player
"""
import copy
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

def empty_board(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                return False
    return True

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if empty_board(board):
        return X
    else:
        mov_x = 0
        mov_o = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == X:
                    mov_x += 1
                elif board[i][j] == O:
                    mov_o += 1
        if mov_x == mov_o:
            return X
        else:
            return O
        
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception('Invalid action')
    i,j = action
    cp_board = copy.deepcopy()
    board[i][j] = player(board)
    return board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
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
