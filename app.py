from flask import Flask, request, jsonify
from tictactoe import TicTacToe
from gamestatus import GameStatus
from flask_cors import CORS
app = Flask(__name__)

CORS(app)

@app.route('/new_game', methods=['GET'])
def new_game():
    game = TicTacToe()
    return jsonify({'board': game.board, 'status': GameStatus.PLAYING.value})

@app.route('/make_move', methods=['POST'])
def make_move():
    data = request.get_json()
    print(data)
    board = data['board']
    turn = data['turn']
    game = TicTacToe(board, turn)
    best_move = game.generate_move()
    board = game.make_move(best_move[0], best_move[1])
    status = game.check_game_over()
    return jsonify({'board': board, 'best_move': best_move, 'status': status.value})

@app.route('/check_status', methods=['POST'])
def check_status():
    data = request.get_json()
    board = data['board']
    game = TicTacToe(board)
    status = game.check_game_over()
    return jsonify({'status': status.name})

if __name__ == '__main__':
    app.run(debug=True)
