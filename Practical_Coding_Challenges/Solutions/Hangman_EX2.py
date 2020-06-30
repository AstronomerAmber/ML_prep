"""
Code hangman from scratch
3 class solution
"""
from collections import Counter
print('Downloading word dictionary ...')
import urllib.request as request
import numpy as np
target_url = "https://www.norvig.com/ngrams/sowpods.txt"
data = request.urlopen(target_url)
words = list()
for word in data:
    words.append(word.decode("utf-8").strip())
print('Downloading word dictionary. Done!')

class board:
    def __init__(self):
        self.word = np.random.choice(words)
        self.n = len(self.word)
        self.s_current = ['_' for _ in range(self.n)]
        self.s_true = list(self.word.lower())

    def __repr__(self):
        return ' '.join(self.s_current)


class player:
    def guess(self):
        """check if alpha"""
        inp = input("Make your guess for letters in the word: ")
        if inp.isalpha():
            s = inp.lower()
            return s
        else:
            print("Invalid input, please choose a letter for your guess")
            return self.guess()

class game(board, player):
    def __init__(self):
        self.guesses = 6
        self.board = board()
        self.player = player()
        self.wrong_guess = set()
        self.left_count = Counter(self.board.s_true)

    def rematch(self):
        """
        ask if play again
        """
        re = input('Want to play again? [y/n]')
        if re == 'y':
            return True
        elif re == 'n':
            return False
        else:
            print('Please input "y" or "n" as your choice!')
            return self.rematch()


    def validate_guess(self, guess):
        # print(self.board.s_true)
        if self.left_count.get(guess, 0) > 0:
            print('The letter you guess ({}) is in word!'.format(guess))
            for i in range(self.board.n):
                if self.board.s_true[i] == guess and self.board.s_current[i] == '_':
                    self.board.s_current[i] = guess
                    self.left_count[guess] -= 1
                    break
            # idx = self.board.s_true.index(guess)
            print(self.board)
        else:
            print('The letter you guess ({}) is not in word!'.format(guess))
            if guess not in self.wrong_guess:
                self.wrong_guess.add(guess)
                self.guesses -= 1
            print(self.board)
        print('You have {} guesses left.'.format(self.guesses))
        print('\n')

    def check_win(self):
        for l in self.board.s_current:
            if l == '_':
                return False
        return True

    def check_stop(self):
        if self.guesses == 0:
            return True
        else:
            return False

    def play(self):
        print('='*30)
        print('Starting the hangman game. You have {} guesses in total!'.format(self.guesses))
        print('='*30)
        print(self.board)
        while not self.check_stop():
            self.validate_guess(self.player.guess())
            if self.check_win():
                print('=' * 30)
                print('Congratulations! You win.')
                print('=' * 30)
                break
        print('='*30)
        print('You lose the game for running out of guesses!')
        print('='*30)

        if self.rematch():
            self.__init__()
            self.play()
        else:
            return

if __name__ == "__main__":
    g = game()
    g.play()
