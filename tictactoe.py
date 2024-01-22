import math, copy, random

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    count_X = sum(row.count(X) for row in board)
    count_O = sum(row.count(O) for row in board)

    return X if count_X == count_O else O

def actions(board):
    possible_actions = set()

    if terminal(board):
        return possible_actions

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions

def result(board, action):
    if action is None:
        raise ValueError("Invalid action: None")

    i, j = action

    # Print indices for debugging
    print("i:", i, "j:", j)

    # Check if i and j are within the valid range
    if 0 <= i < 3 and 0 <= j < 3:
        if board[i][j] == EMPTY:
            new_board = copy.deepcopy(board)
            new_board[i][j] = player(new_board)
            return new_board
        else:
            raise ValueError("Invalid action: Cell is not empty")
    else:
        raise ValueError("Invalid action: Indices out of range")


def winner(board):
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O

    for col in range(3):
        if all(board[row][col] == X for row in range(3)):
            return X
        elif all(board[row][col] == O for row in range(3)):
            return O

    if all(board[i][i] == X for i in range(3)) or all(board[i][2 - i] == X for i in range(3)):
        return X
    elif all(board[i][i] == O for i in range(3)) or all(board[i][2 - i] == O for i in range(3)):
        return O

    return None

def terminal(board):
    return not any(EMPTY in row for row in board) or winner(board) is not None

def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board, maximizing_player=True):
    positive_infinity = math.inf
    negative_infinity = -math.inf

    if terminal(board):
        return None, None

    best_move = None
    best_score = -math.inf if maximizing_player else math.inf

    for move in actions(board):
        result_board = result(board, move)
        score, _ = minimax(result_board, not maximizing_player)

        if score is None:
            continue

        if maximizing_player:
            if score > best_score:
                best_score = score
                best_move = move
        else:
            if score < best_score:
                best_score = score
                best_move = move

    return best_score, best_move


