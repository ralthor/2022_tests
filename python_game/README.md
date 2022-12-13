# Decoupled AlphaBeta Solver

This project is a study of decoupling the solver engine from the game. The game inherites from an abstract that the solver uses: `AdversarialGame`.

```
    +--------+               +-------------+
    |GameMove|<--------------|TicTacToeMove|
    +--------+               +-------------+
        ^                           ^
        |                           |
        |                           |
+---------------+              +---------+
|AdversarialGame|<-------------|TicTacToe|
+---------------+              +---------+
        ^
        |
        |
   +---------+
   |AlphaBeta|
   +---------+
```

## GameMove

## Tic Tac Toe Example

This class inherites `AdversarialGame`

The way the TicTacToe `__str__` method works:

```
O| |
-+-+-
 |X|
-+-+-
 | |
```

### Tic Tac Toe Move

A pair of integers, starting from `0 0` to `2 2`.
