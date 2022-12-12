class GameMove:
    def __init__(self):
        raise NotImplementedError


class AdversarialGame:
    """
    An abstract class for adversarial games
    There are two players, 1 and 2
    Player 1 is the maximizer
    Player 2 is the minimizer
    Evaluation function returns positive if player 1 wins, negative if player 2 wins, 0 if draw
    """
    def change_player(self):
        raise NotImplementedError
    
    def play(self, m: GameMove):
        raise NotImplementedError
    
    def unplay(self, m: GameMove):
        raise NotImplementedError

    def next_game(self):
        raise NotImplementedError
    
    def next_move(self):
        raise NotImplementedError
    
    def evaluate(self):
        raise NotImplementedError
    
    def min_evaluation_value(self):
        raise NotImplementedError

    def max_evaluation_value(self):
        raise NotImplementedError


class GameOverException(Exception):
    pass


class InvalidMoveException(Exception):
    pass
