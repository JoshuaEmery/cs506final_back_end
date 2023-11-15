from enum import Enum

class GameStatus(Enum):
    X_WINS = "X wins"
    O_WINS = "O wins"
    DRAW = "Draw"
    X_TURN = "X Turn"
    O_TURN = "O Turn"