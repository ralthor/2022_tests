from minmax import MinMax
from alphabeta import AlphaBeta
from tictactoe_game import TicTacToe, TicTacToeMove
from adversarial_game import InvalidMoveException


def play_with_friend():
    game = TicTacToe()
    while not game.game_over:
        move = next_move_player(game)
        game.play(move)
    print(game)
    if game.winner is None:
        print("Draw")
    else:
        print("Player {} wins".format(game.winner))


def next_move_ai(game, solver_class=AlphaBeta):
    if game.player == 1:
        move = solver_class(game, max_depth=9, verbose=True).move_for_player_1()
    else:
        move = solver_class(game, max_depth=9, verbose=True).move_for_player_2()
    return move


def next_move_player(game):
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


def play_with_ai(player=1, solver_class=AlphaBeta):
    game = TicTacToe()
    while not game.game_over:
        print(game)
        if game.player == player:
            move = next_move_player(game)
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


if __name__ == "__main__":
    play_with_ai(player=1, solver_class=AlphaBeta)
    # play_with_friend()
