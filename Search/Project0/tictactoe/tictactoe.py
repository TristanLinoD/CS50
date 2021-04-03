"""
Tic Tac Toe Player
"""
import random
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
    cp_board = copy.deepcopy(board)
    board[i][j] = player(board)
    return board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if (board[i][0] == board[i][1]) and (board[i][0]  == board[i][2]):
            return board[i][0]
    for j in range(3):
        if (board[0][j] == board[1][j]) and (board[0][j]  == board[2][j]):
            return board[0][j]
    if (board[0][0] == board[1][1]) and (board[0][0] == board[2][2]):
        return board[0][0]
    elif (board[0][2] == board[1][1]) and (board[0][2] == board[2][0]):
        return board[0][2]
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if len(actions(board)) == 0:
        return True
    elif winner(board) != None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return -1
    elif w == O:
        return 1
    else:
        return 0

def moveAI(board):
    bestScore = -math.inf
    available_movesO = actions(board)
    for _ in range(len(available_movesO)):
            (i,j) = available_movesO.pop()
            board[i][j] = O
            score = minimax(board)
            board[i][j] = EMPTY
            if score > bestScore:
                bestScore = score
                bestMove = (i,j)  # (-1|(1,0), 1|(2,0), -1|(2,2))
    return bestMove

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board)

    if player(board) == O:  # Maximizer player
        bestScore = -math.inf
        available_movesO = actions(board)
        for _ in range(len(available_movesO)):
            (i,j) = available_movesO.pop()
            board[i][j] = O
            score = minimax(board)
            board[i][j] = EMPTY
            bestScore = max(score, bestScore)
        return bestScore
    else:
        worstScore = math.inf
        available_movesX = actions(board)
        for _ in range(len(available_movesX)):
            (i,j) = available_movesX.pop()
            board[i][j] = X
            score = minimax(board)
            board[i][j] = EMPTY
            worstScore = min(score, worstScore)
        return worstScore
