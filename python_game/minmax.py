from adversarial_game import AdversarialGame


class ScorePair:
    def __init__(self, score, depth, max_depth):
        self.score = score
        self.depth = depth
        self.max_depth = max_depth

    @property
    def heuristic(self):
        if self.score == 0:
            return 0
        score = self.score
        if abs(score) == 1:
            score = score * self.max_depth

        return (self.max_depth - self.depth) * score

    def __lt__(self, other):
            return self.score < other.score or (self.score == other.score and self.heuristic < other.heuristic)

    def __gt__(self, other):
            return self.score > other.score or (self.score == other.score and self.heuristic > other.heuristic)

    def __repr__(self):
        return f"(score: {self.score}, depth: {self.depth}, heuristic: {self.heuristic})"


node_count = 0


class MinMax:
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

    def max(self, depth=0):
        global node_count
        node_count += 1
        if self.game.game_over:
            return ScorePair(self.game.evaluate(), depth, max_depth=self._max_depth)
        best_score = ScorePair(self.game.min_evaluation_value(), depth, max_depth=self._max_depth)
        for move in self.game.next_move():
            self.game.play(move)
            score = self.min(depth=depth + 1)
            self.game.unplay(move)
            if score > best_score:
                best_score = score

        return best_score

    def min(self, depth=0):
        global node_count
        node_count += 1
        if self.game.game_over:
            return ScorePair(self.game.evaluate(), depth, max_depth=self._max_depth)
        best_score = ScorePair( self.game.max_evaluation_value(), depth, max_depth=self._max_depth)
        for move in self.game.next_move():
            self.game.play(move)
            score = self.max(depth=depth + 1)
            self.game.unplay(move)
            if score < best_score:
                best_score = score
        return best_score
