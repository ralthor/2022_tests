import random

from adversarial_game import AdversarialGame, GameMove, GameOverException, InvalidMoveException


class Connect4Move(GameMove):
    def __init__(self, col: int):
        self.col = col


class Connect4Game(AdversarialGame):
    """
    Connect 4 game implementation
    The board is represented as a list of columns, each column is a list of
    rows.
    Each player selects a column to play in. The piece is placed in the lowest
    available row in that column, starting from index 0.
    """	
    def __init__(self, game: "Connect4Game" = None, columns: int = 4, rows: int = 4):
        if game is None:
            self.board = [[None for i in range(rows)] for j in range(columns)]
            self.player = 1
            self.moves = 0
            self.winner = None
            self.game_over = False
            self.columns = columns
            self.rows = rows
        else:
            self.board = [row[:] for row in game.board]
            self.player = game.player
            self.moves = game.moves
            self.winner = game.winner
            self.game_over = game.game_over
            self.columns = game.columns
            self.rows = game.rows

    def change_player(self):
        self.player = 2 if self.player == 1 else 1

    def play(self, move: Connect4Move):
        col = move.col
        if self.game_over:
            raise GameOverException("Game over")
        if self.columns <= col or col < 0:
            raise InvalidMoveException("Invalid move")
        for i in range(self.rows):
            if self.board[col][i] is None:
                self.board[col][i] = self.player
                break
        else:
            raise InvalidMoveException("Invalid move")
        self.moves += 1
        self.change_player()
        self.check()
    
    def check(self):
        for i in range(self.columns):
            for j in range(self.rows):
                if self.board[i][j] is not None:
                    if self._check_line(i, j, 1, 0) or self._check_line(i, j, 0, 1) or self._check_line(i, j, 1, 1) or self._check_line(i, j, 1, -1):
                        self.winner = self.board[i][j]
                        self.game_over = True
        if self.moves == self.columns * self.rows:
            self.game_over = True
        
    def _check_line(self, x: int, y: int, dx: int, dy: int):
        player = self.board[x][y]
        for i in range(1, 4):
            if x + i * dx >= self.columns or y + i * dy >= self.rows or y + i * dy < 0 or self.board[x + i * dx][y + i * dy] != player:
                return False
        return True
    
    def unplay(self, move: Connect4Move):
        col = move.col
        if self.moves == 0:
            raise InvalidMoveException("Invalid move")
        for i in range(self.rows):
            if self.board[col][i] is not None:
                self.board[col][i] = None
                break
        else:
            raise InvalidMoveException("Invalid move")
        self.moves -= 1
        self.change_player()
        self.winner = None
        self.game_over = False
    
    def next_game(self):
        if self.game_over:
            raise GameOverException("Game over")
        game = Connect4Game(self)
        for move in self.next_move():
            game.play(move)
            yield game
            game.unplay(move)
    
    def next_move(self):
        moves = []
        for i in range(self.columns):
            if self.board[i][-1] is None:
                moves.append(Connect4Move(i))
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
        """
        Returns a string representation of the board.
        The rows are shown from bottom to top.
        """
        s = ""
        for i in range(self.rows - 1, -1, -1):
            for j in range(self.columns):
                if self.board[j][i] is None:
                    s += "."
                elif self.board[j][i] == 1:
                    s += "X"
                else:
                    s += "O"
            s += "\n"
        return s
    
    def copy(self):
        return Connect4Game(self)
