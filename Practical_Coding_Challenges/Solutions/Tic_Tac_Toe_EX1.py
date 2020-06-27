"""
Code up the game tic tac toe
2 class solution
"""

import argparse
import random
import numpy as np

class TicTacToe:
    def __init__(self):
        self.player = 'X'
        self.board = Board()
        self.finished = False
        self.move_count = 0
        self.winner = None

    def is_free(self, row, col):
        if row is None or col is None:
            return False
        return self.board.is_free(row, col)

    def place(self, row, col):
        self.board.place(row, col, self.player)
        self.player = 'O' if self.player == 'X' else 'X'
        self.move_count += 1
        self.finished, self.winner = self._finished()

    def _finished(self):
        for row in range(3):
            if all(self.board[row][i] == self.board[row][i + 1]
                    and self.board[row][i] != '_'
                    for i in range(2)):
                return True, self.board[row][0]
        for col in range(3):
            if all(self.board[i][col] == self.board[i + 1][col]
                    and self.board[i][col] != '_'
                    for i in range(2)):
                return True, self.board[0][col]
        if all(self.board[i][i] == self.board[i + 1][i + 1]
                and self.board[i][i] != '_'
                for i in range(2)):
            return True, self.board[0][0]
        if all(self.board[i][2 - i] == self.board[i + 1][2 - i - 1]
                and self.board[i][i] != '_'
                for i in range(2)):
            return True, self.board[0][2]
        if self.move_count >= 9:
            return True, None
        return False, None

    def __str__(self):
        return str(self.board)


class Board:
    def __init__(self):
        self.board = np.tile('_', (3, 3))

    def is_free(self, row, col):
        return self.board[row][col] == '_'

    def place(self, row, col, val):
        if self.board[row][col] != '_':
            raise Exception(
                'Attempted to place a mark where a mark was already place!')
        self.board[row][col] = val

    def __str__(self):
        s = ''
        for row in self.board:
            s += ' '.join(row) + '\n'
        return s

    def __getitem__(self, index):
        return self.board[index]


def input_pos(player, row_col):
    pos = None
    while pos is None:
        try:
            inp = input(f'Player {player} enter a {row_col} to place a mark: ')
            pos = int(inp)
            if pos < 1 or pos > 3:
                pos = None
                raise ValueError
        except ValueError:
            pass
    return pos - 1


def play():
    game = TicTacToe()
    print(game)

    while not game.finished:
        # Input a place to place a mark.
        row, col = None, None
        while not game.is_free(row, col):
            row = input_pos(game.player, 'row')
            col = input_pos(game.player, 'col')

        # Place the mark.
        game.place(row, col)
        print(game)

    if game.winner:
        print(f'Player {game.winner} won!')
    else:
        print('The game was a draw!')


def test():
    game = TicTacToe()
    print(game)

    while not game.finished:
        row, col = None, None
        while not game.is_free(row, col):
            row = random.randint(0, 2)
            col = random.randint(0, 2)
        print(f'Placing {game.player} at ({row}, {col}).')

        game.place(row, col)
        print(game)

    if game.winner:
        print(f'Player {game.winner} won!')
    else:
        print('The game was a draw!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Play games of Tic-Tac-Toe.')
    parser.add_argument(
        '--test',
        action='store_true',
        help='Run a test instead of playing a game.')
    args = parser.parse_args()

    if args.test:
        test()
    else:
        replay = True
        while replay:
            play()
            replay = None
            while replay is None:
                inp = input('Play again (y/n)? ')
                if inp.lower() == 'y':
                    replay = True
                elif inp.lower() == 'n':
                    replay = False
