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

    # return [[EMPTY, X, O],
    #         [O, X, X],
    #         [X, EMPTY, O]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #raise NotImplementedError
    Xcount = 0
    Ocount = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                Xcount += 1
            if board[i][j] == O:
                Ocount += 1
    if Xcount > Ocount:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #raise NotImplementedError
    action = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action += [(i, j)]
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #raise NotImplementedError
    Xcount = 0
    Ocount = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                Xcount += 1
            if board[i][j] == O:
                Ocount += 1
    i, j = action
    if Xcount > Ocount:
        #print("Set O")
        board[i][j] = O
    else:
        #print("Set X")
        board[i][j] = X

    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #raise NotImplementedError
    win = utility(board)
    if win == 1:
        return X
    elif win == -1:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #raise NotImplementedError
    if winner(board) is not None:
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #raise NotImplementedError
    # diagonal
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return -1
    elif board[2][0] == O and board[1][1] == O and board[0][2] == O:
        return -1
    elif board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return 1
    elif board[2][0] == X and board[1][1] == X and board[0][2] == X:
        return 1
    else:
        for k in range(3):
            # horizontal
            if board[k][0] == O and board[k][1] == O and board[k][2] == O:
                return -1
            elif board[0][k] == O and board[1][k] == O and board[2][k] == O:
                return -1
            # vertical
            elif board[k][0] == X and board[k][1] == X and board[k][2] == X:
                return 1
            elif board[0][k] == X and board[1][k] == X and board[2][k] == X:
                return 1
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #raise NotImplementedError
    def max_value(board):
        if terminal(board):
            #print("max return %d" % utility(board))
            return utility(board)
        v = -2
        #print(actions(board))
        for (i, j) in actions(board):
            #print(board)
            v = max(v, min_value(result(board, (i, j))))
            #print(board)
            board[i][j] = EMPTY
            #print("max = %d, move_to (%d, %d)" % (v, i, j))
        return v
        
    def min_value(board):
        if terminal(board):
            #print("min return %d" % utility(board))
            return utility(board)
        v = 2
        #print(actions(board))
        for (i, j) in actions(board):
            v = min(v, max_value(result(board, (i, j))))
            board[i][j] = EMPTY
            #print("min = %d, move_to (%d, %d)" % (v, i, j))
        return v
    
            
    opt_act = None
    if player(board) == X:
        #print("X")
        v = -2
        for (i, j) in actions(board):
            board[i][j] = X
            s = min_value(board)
            board[i][j] = EMPTY
            if s > v:
                v = s
                opt_act = (i, j)
    else:
        #print("O")
        v = 2
        for (i, j) in actions(board):
            board[i][j] = O
            s = max_value(board)
            board[i][j] = EMPTY
            if s < v:
                v = s
                opt_act = (i, j)
    return opt_act

    # for i in range(3):
    #     for j in range(3):
    #         if board[i][j] == EMPTY:
    #             return (i, j)
