from adversarial_game import AdversarialGame
from minmax import ScorePair


node_count = 0

class AlphaBeta:
    def __init__(self, game: AdversarialGame, max_depth=32, verbose=None):        
        self.game = game
        self.verbose = verbose
        self._max_depth = max_depth

    def move_for_player_1(self):
        global node_count
        node_count = 0

        best_move = None
        best_score = ScorePair(self.game.min_evaluation_value(), 0, max_depth=self._max_depth)
        for move in self.game.next_move():
            self.game.play(move)
            score = self.min()
            if self.verbose:
                print(self.game)
                print(f"with {score=}")
            self.game.unplay(move)
            if score > best_score:
                best_score = score
                best_move = move

        if self.verbose:
            print(f"{node_count=}")

        return best_move

    def move_for_player_2(self):
        global node_count
        node_count = 0

        best_move = None
        best_score = ScorePair(self.game.max_evaluation_value(), 0, max_depth=self._max_depth)
        for move in self.game.next_move():
            self.game.play(move)
            score = self.max()
            if self.verbose:
                print(self.game)
                print(f"with {score=}")
            self.game.unplay(move)
            if score < best_score:
                best_score = score
                best_move = move

        if self.verbose:
            print(f"{node_count=}")

        return best_move

    def max(self, depth=0, alpha=None, beta=None):
        global node_count
        node_count += 1
        if alpha is None:
            alpha = ScorePair(-1, 0, max_depth=self._max_depth)
            beta = ScorePair(1, 0, max_depth=self._max_depth)
        if self.game.game_over:
            return ScorePair(self.game.evaluate(), depth, max_depth=self._max_depth)
        best_score = ScorePair(self.game.min_evaluation_value(), depth, max_depth=self._max_depth)
        for move in self.game.next_move():
            self.game.play(move)
            score = self.min(depth=depth + 1, alpha=alpha, beta=beta)
            self.game.unplay(move)
            if score > best_score:
                best_score = score
            if best_score > beta:
                return best_score
            if best_score > alpha:
                alpha = best_score

        return best_score

    def min(self, depth=0, alpha=None, beta=None):
        global node_count
        node_count += 1
        if alpha is None:
            alpha = ScorePair(-1, 0, max_depth=self._max_depth)
            beta = ScorePair(1, 0, max_depth=self._max_depth)
        if self.game.game_over:
            return ScorePair(self.game.evaluate(), depth, max_depth=self._max_depth)
        best_score = ScorePair( self.game.max_evaluation_value(), depth, max_depth=self._max_depth)
        for move in self.game.next_move():
            self.game.play(move)
            score = self.max(depth=depth + 1, alpha=alpha, beta=beta)
            self.game.unplay(move)
            if score < best_score:
                best_score = score
            if best_score < alpha:
                return best_score
            if best_score < beta:
                beta = best_score

        return best_score
