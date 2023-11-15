from gamestatus import GameStatus
# I got this from the internet. I did not write this code. I did however research the different
# ways to accomplish this. 
class Minimax:
    def __init__(self, board, player):
        self.board = board
        self.player = player
        if self.player == GameStatus.X_TURN:
            self.player = 'x'
            self.opponent = 'o'
        else:
            self.player = 'o'
            self.opponent = 'x'
    # this i understand
    def is_moves_left(self, board):
        for row in board:
            if None in row:
                return True
        return False
    # this is just a less efficient way of finding a winner, however it does not have to go through
    # and create the binary representation of the board. so maybe it is not less efficient?
    def evaluate(self, b):
        # Check rows for victory
        for row in range(3):
            if b[row][0] == b[row][1] == b[row][2]:
                if b[row][0] == self.player:
                    return 10
                elif b[row][0] == self.opponent:
                    return -10

        # Check columns for victory
        for col in range(3):
            if b[0][col] == b[1][col] == b[2][col]:
                if b[0][col] == self.player:
                    return 10
                elif b[0][col] == self.opponent:
                    return -10

        # Check diagonals for victory
        if b[0][0] == b[1][1] == b[2][2]:
            if b[0][0] == self.player:
                return 10
            elif b[0][0] == self.opponent:
                return -10

        if b[0][2] == b[1][1] == b[2][0]:
            if b[0][2] == self.player:
                return 10
            elif b[0][2] == self.opponent:
                return -10

        # Neither player nor opponent wins
        return 0
    # this method plays out the entire game against itself
    # recursively. It will play out every possible move
    # and return a score for each move. The score is
    # calculated by the evaluate method. The evaluate
    # method returns 10 if the player wins, -10 if the
    # opponent wins, and 0 if the game is a draw.
    def minimax(self, board, depth, is_maximizing_player):
        score = self.evaluate(board)

        if score == 10 or score == -10:
            return score

        if not self.is_moves_left(board):
            return 0
        # Im not gonna pretend I understand this.
        # recursion breaks my mind
        if is_maximizing_player:
            best = -1000
            for i in range(3):
                for j in range(3):
                    if board[i][j] is None:
                        board[i][j] = self.player
                        best = max(best, self.minimax(board, depth + 1, False))
                        board[i][j] = None
            return best
        else:
            best = 1000
            for i in range(3):
                for j in range(3):
                    if board[i][j] is None:
                        board[i][j] = self.opponent
                        best = min(best, self.minimax(board, depth + 1, True))
                        board[i][j] = None
            return best

    def find_best_move(self):
        best_val = -1000 if self.player == 'x' else 1000
        best_move = (-1, -1)

        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    self.board[i][j] = self.player
                    move_val = self.minimax(self.board, 0, self.player == 'o')
                    self.board[i][j] = None

                    if (self.player == 'x' and move_val > best_val) or (self.player == 'o' and move_val < best_val):
                        best_move = (i, j)
                        best_val = move_val

        return best_move

# testing:
# board = [
#     [None, None, None],
#     [None, None, None],
#     [None, None, None]
# ]
# minimax = Minimax(board, 'x')
# best_move = minimax.find_best_move()
# print("Best move for 'x' on an empty board:", best_move)
# board = [
#     ['x', 'x', None],
#     ['o', 'o', None],
#     [None, None, None]
# ]
# minimax = Minimax(board, 'x')
# best_move = minimax.find_best_move()
# print("Best move for 'x' in a near-winning state:", best_move)