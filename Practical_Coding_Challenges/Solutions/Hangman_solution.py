"""
Author: @Amber

Read the text file from the internet.

Tips:

1/
import urllib.request as request
data = request.urlopen(self.target_url)
self.target_url = "https://www.norvig.com/ngrams/sowpods.txt"
words = list()
for word in data:
    words.append(word.decode("utf-8").strip())

2/
You may use the isalpha() function.
"""


import urllib.request as request
import random

class Game:
    def __init__(self):
        self.target_url = "https://www.norvig.com/ngrams/sowpods.txt"
        self.word = self.choose_random_word()
        self.guessed = ['_'] * len(self.word)
        self.figure = list()
        for _ in range(3):
            self.figure.append([' '] * 3)
        self.num_misses = 0
        self.guessed_letters = set()

    def guess(self, letter):
        if len(letter) != 1:
            raise ValueError("Too many characters.")
        elif not letter.isalpha():
            raise ValueError("Must enter a letter.")
        elif letter in self.guessed_letters:
            raise ValueError("You've already guessed the letter {:s}".format(
                letter))
        self.guessed_letters.add(letter)
        good_guess = False
        for i in range(len(self.word)):
            if self.guessed[i] == '_' and self.word[i] == letter:
                good_guess = True
                self.guessed[i] = letter
        return good_guess

    def choose_random_word(self):
        data = request.urlopen(self.target_url)
        words = list()
        for word in data:
            words.append(word.decode("utf-8").strip())
        num_words = len(words)
        i = random.randint(0, num_words - 1)
        return words[i]

    def update_figure(self):
        if not (0 <= self.num_misses < 7):
            raise ValueError("Invalid number of guesses: {:d}".format(
                self.num_misses))
        if self.num_misses == 1:
            self.figure[0][1] = 'o'
        elif self.num_misses == 2:
            self.figure[1][0] = '-'
        elif self.num_misses == 3:
            self.figure[1][1] = '|'
        elif self.num_misses == 4:
            self.figure[1][2] = '-'
        elif self.num_misses == 5:
            self.figure[2][0] = '/'
        else: # num_misses == 6
            self.figure[2][2] = '\\'

    def display(self):
        print("Word:", ' '.join(self.guessed))
        for row in self.figure:
            print(''.join(row))
        print("You have {:d} miss(es) remaining.".format(
            6 - self.num_misses))

    def play(self):
        while True:
            self.display()
            if '_' not in self.guessed:
                print("You win! The word is {:s}.".format(
                    self.word))
                break
            elif self.num_misses >= 6:
                print("You lose! The word is {:s}.".format(
                    self.word))
                break
            else:
                guess = input("Make a guess.\n")
                try:
                    guess = guess.upper()
                    good_guess = self.guess(guess)
                    if good_guess:
                        print("The secret word contains the letter {:s}!".format(
                            guess))
                    else:
                        print("The secret word does not contain the letter {:s}.".format(
                            guess))
                        self.num_misses += 1
                        self.update_figure()
                except ValueError as err:
                    print(err)


def wants_to_play_again():
    ans = ''
    while ans not in ['y', 'n', "yes", "no"]:
        try:
            ans = input("Want to play again? [y/n]\n")
            ans = ans.lower()
        except:
            print("Sorry, didn't get that.")
    if ans in ['y', "yes"]:
        return True
    else:
        return False


def main():
    wants_to_play = True
    while wants_to_play:
        game = Game()
        game.play()
        wants_to_play = wants_to_play_again()


if __name__ == "__main__":
    main()
