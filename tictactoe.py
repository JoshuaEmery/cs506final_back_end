from gamestatus import GameStatus
from minimax import Minimax
from copy import deepcopy

class TicTacToe:
    def __init__(self, board = None, turn = None):
        if board == None:
            self.board = self.newgame()
        else:
            self.board = board
        if turn == None:
            self.turn = GameStatus.X_TURN
        elif turn == "x":
            self.turn = GameStatus.X_TURN
        elif turn == "o":
            self.turn = GameStatus.O_TURN
        self.winning_positions = [0b000000111, 0b000111000, 0b111000000, 0b100100100, 0b010010010, 0b001001001, 0b100010001, 0b001010100]
    # method to generate a new board    
    def newgame(self):
         return [[None, None, None], [None, None, None], [None, None, None]]
    # method that switches turns. I dont think we need this but leaving it here just in case
    def switch_turn(self):
        if self.turn == GameStatus.X_TURN:
            self.turn = GameStatus.O_TURN
        else:
            self.turn = GameStatus.X_TURN
        return self.turn
    
    def get_x_binary(self, board):
        # create a 9 bit binary number
        result = 0b000000000
        for i in range(0, 3):
            for j in range(0, 3):
                # short version without the comments
                if board[i][j] == "x":
                    # set the bit at the correct position
                    result = result | (1 << (i * 3 + j))
        return result
    # this method taked a board and returns the current state of the o position
    # as a binary number 000000000
    def get_o_binary(self, board):
            # create a 9 bit binary number
        result = 0b000000000
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == "o":
                    # we found an o
                    # lets calculate the bit position of the o
                    # i is the row and j is the column
                    # for each row we multiply by 3 and add the column
                    bit_position = i * 3 + j
                    # we used the bit position to shift the number 1 that many positions to the left
                    # this gives us a bit mask with a 1 in the correct position
                    bit_mask = 1 << bit_position
                    # the bit mask is the used with bitwise or to flip the bit in the position to 1 of result
                    # because of bitwise or the other bits in result will not be affected
                    result = result | bit_mask
        return result
    # this method compares the binary representation of the x position to the
    # binary representation of the winning positions
    def check_x_win(self, x_binary):
        # get the winning positions
        print(x_binary)
        print(self.winning_positions)
        # iterate over the winning positions
        for winning_position in self.winning_positions:
            # compare the winning position to the x position
            if (x_binary & winning_position) == winning_position:
                return True
        return False
    
    def check_draw(self):
        # check if the board is full
        for row in self.board:
            for cell in row:
                if cell == None:
                    return False
        return True
    
    def check_game_over(self):
        # check if the game is over
        if self.check_x_win(self.get_x_binary(self.board)):
            return GameStatus.X_WINS
        elif self.check_o_win(self.get_o_binary(self.board)):
            return GameStatus.O_WINS
        elif self.check_draw():
            return GameStatus.DRAW
        else:
            return GameStatus.PLAYING
        
    def make_move(self, row, column):
        # make the move
        if self.turn == GameStatus.X_TURN:
            self.board[row][column] = "x"
        else:
            self.board[row][column] = "o"
        # switch the turn
        self.switch_turn()
        return self.board

    # this method compares the binary representation of the o position to the
    # binary representation of the winning positions
    # this method compares the binary representation of the x position to the
    # binary representation of the winning positions
    def check_o_win(self, o_binary):
        # iterate over the winning positions
        for winning_position in self.winning_positions:
            # compare the winning position to the x position
            if (o_binary & winning_position) == winning_position:
                return True
        return False
    # get the best possible next move from minimax and return it
    def generate_move(self):
        # create a minimax object
        # dont send the board, send a copy of the board
        # otherwise minimax will modify the board
        minimax = Minimax(deepcopy(self.board), self.turn)
        # get the best move
        best_move = minimax.find_best_move()
        # make the move
        print(best_move)
        # do not make the move here
        # self.make_move(best_move[0], best_move[1])
        # return the move
        return best_move
    # i cannot take credit for this solution to check for a winner. I did however research the different
    # ways it could be done. Most of them were n^2. This one is constant time. I found it on stack overflow
    # and really enjoyed reading about it. I will explain my understanding below
    # https://stackoverflow.com/a/33456912
    # there are 8 possible winning positions and we can represent them as binary numbers using 9 bits
    # the first 3 bits represent the top row, the middle 3 represent the middle row and the last 3 the bottom row
    # 000000111 - Win on the bottom row
    # 000111000 - Win on the middle row
    # 111000000 - Win on the top row
    # 100100100 - Win on the left column
    # 010010010 - Win on the middle column
    # 001001001 - Win on the right column
    # 100010001 - Win on the top left to bottom right diagonal
    # 001010100 - Win on the top right to bottom left diagonal
    # using the board state of a given player in binary we can compare it to the winning positions
    # with a bitwise and. If the result matches the winning position then we have a winner
    # The board states will be represented internally as a binary number with 9 bits
    # Responses from the API will be in the form of a 2d array

    # i was going to implement minimax here, however minimax needs to modify the board state
    # instead I am going to make minimax a seperate class that takes a board state and returns
    # the best move. I will send a copy of the board to minimax
# testing: