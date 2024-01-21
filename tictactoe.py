"""
Tic Tac Toe Player
"""

import math, copy

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
    """
    count_X = sum(row.count('X') for row in board)
    count_O = sum(row.count('O') for row in board)

    if terminal(board):
        return None

    return 'X' if count_X == count_O else 'O'

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    if terminal(board):
        return possible_actions

    for i in range(3):
        for j in range(3):
            if board[i][j] == '  ':
                possible_actions.add((i ,j))

    return possible_actions

    # raise NotImplementedError

def valid_action(board, action):

    action = i , j
    return 0 <= i < 3 and 0 <= j < 3 and board[i][j] == ' '


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if not valid_action(board, action):
        raise ValueError("Invalid action: {}".format(action))

    new_board = copy.deepcopy(board)

    i, j = action
    player = player(new_board)

    new_board[i][j] = player

    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return 0

# Check columns
    for col in range(3):
        if all(board[row][col] == X for row in range(3)):
            return X
        elif all(board[row][col] == O for row in range(3)):
            return O

 # Check diagonals
    if all(board[i][i] == X for i in range(3)) or all(board[i][2 - i] == X for i in range(3)):
        return X
    elif all(board[i][i] == O for i in range(3)) or all(board[i][2 - i] == O for i in range(3)):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for row in board:
        if row.count(X) == 3:
            return 1
        elif row.count(O) == 3:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    raise NotImplementedError
