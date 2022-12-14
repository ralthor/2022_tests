from connect4 import Connect4Game, Connect4Move
from minmax import MinMax
from alphabeta import AlphaBeta
from tictactoe import TicTacToe, TicTacToeMove
from adversarial_game import InvalidMoveException


def next_move_ai(game, solver_class=AlphaBeta):
    if game.player == 1:
        move = solver_class(game, max_depth=9, verbose=True).move_for_player_1()
    else:
        move = solver_class(game, max_depth=9, verbose=True).move_for_player_2()
    return move


def next_tictactoe_move_player(game):
    invalid_move = True
    while invalid_move:
        try:
            print(game)
            x, y = map(int, input("Enter coordinates: ").split())
            move = TicTacToeMove(x, y)
            game.play(move)
            game.unplay(move)
            invalid_move = False
        except (InvalidMoveException, IndexError):
            print("Invalid move, try again")
            invalid_move = True
    return move


def next_connect4_move_player(game):
    invalid_move = True
    while invalid_move:
        try:
            print(game)
            c = int(input("Enter column: "))
            move = Connect4Move(c)
            game.play(move)
            game.unplay(move)
            invalid_move = False
        except (InvalidMoveException, IndexError):
            print("Invalid move, try again")
            invalid_move = True
    return move


def play_with_friend(game_class=TicTacToe, game_move_callable=next_tictactoe_move_player):
    game = game_class()
    while not game.game_over:
        move = game_move_callable(game)
        game.play(move)
    print(game)
    if game.winner is None:
        print("Draw")
    else:
        print("Player {} wins".format(game.winner))


def play_with_ai(player=1, solver_class=AlphaBeta):
    game = TicTacToe()
    while not game.game_over:
        print(game)
        if game.player == player:
            move = next_tictactoe_move_player(game)
        else:
            move = next_move_ai(game, solver_class=solver_class)
        game.play(move)
    print(game)
    if game.winner is None:
        print("Draw")
    else:
        print("Player {} wins".format(game.winner))


def test_ai():
    game = TicTacToe()
    game.board = [
        [None, None, None],
        [2, None, None],
        [1, None, None]]
    game.player = 1
    game.moves = 2
    move = AlphaBeta(game, verbose=True).move_for_player_1()
    game.play(move)
    print(game)


def test_connect4_ai():
    game = Connect4Game()
    game.board = [
        [None, None, None],
        [2, 2, None],
        [1, 1, None],
        [1, 2, None],
    ]
    game.columns = len(game.board)
    game.rows = len(game.board[0])
    game.player = 1
    game.moves = 6
    move = AlphaBeta(game, verbose=True).move_for_player_1()
    game.play(move)
    print(game)


if __name__ == "__main__":
    # play_with_ai(player=1, solver_class=AlphaBeta)
    play_with_friend(game_class=Connect4Game, game_move_callable=next_connect4_move_player)