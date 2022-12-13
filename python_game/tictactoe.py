import random

from adversarial_game import AdversarialGame, GameMove, GameOverException, InvalidMoveException


class TicTacToeMove(GameMove):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __call__(self) -> tuple:
        return self.x, self.y


class TicTacToe(AdversarialGame):
    def __init__(self, game: "TicTacToe" = None):
        if game is None:
            self.board = [[None for i in range(3)] for j in range(3)]
            self.player = 1
            self.moves = 0
            self.winner = None
            self.game_over = False
        else:
            self.board = [row[:] for row in game.board]
            self.player = game.player
            self.moves = game.moves
            self.winner = game.winner
            self.game_over = game.game_over

    def change_player(self):
        self.player = 2 if self.player == 1 else 1

    def play(self, m: TicTacToeMove):
        x, y = m()
        if self.game_over:
            raise GameOverException("Game over")
        if self.board[x][y] is not None:
            raise InvalidMoveException("Invalid move")
        self.board[x][y] = self.player
        self.moves += 1
        self.change_player()
        self.check()

    def check(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                self.winner = self.board[i][0]
                self.game_over = True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                self.winner = self.board[0][i]
                self.game_over = True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            self.winner = self.board[0][0]
            self.game_over = True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            self.winner = self.board[0][2]
            self.game_over = True
        if self.moves == 9:
            self.game_over = True

    def unplay(self, m: TicTacToeMove):
        x, y = m()
        self.board[x][y] = None
        if self.moves == 0:
            raise InvalidMoveException("Invalid move")
        self.moves -= 1
        self.change_player()
        self.winner = None
        self.game_over = False

    def next_game(self):
        if self.game_over:
            raise GameOverException("Game over")
        game = TicTacToe(self)
        for move in self.next_move():
            game.play(move)
            yield game
            game.unplay(move)

    def next_move(self):
        """Returns a generator of all possible moves in random order"""
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    moves.append(TicTacToeMove(i, j))
        random.shuffle(moves)
        for move in moves:
            yield move

    def evaluate(self):
        if self.winner == 1:
            return 1
        elif self.winner == 2:
            return -1
        else:
            return 0
    
    def min_evaluation_value(self):
        return -1

    def max_evaluation_value(self):
        return 1

    def __str__(self):
        s = "\n"
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    s += " "
                elif self.board[i][j] == 1:
                    s += "X"
                else:
                    s += "O"
                if j != 2:
                    s += "|"
            if i != 2:
                s += "\n-+-+-\n"
        return s

    def copy(self):
        return TicTacToe(self.game)
