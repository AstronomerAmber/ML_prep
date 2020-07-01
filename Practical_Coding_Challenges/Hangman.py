'''
Timestamp:
Objective: Coding Hangman from scratch
Dependencies:

@author:
///////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\

1/
Create a game
Start it by picking random word from norvig.com/ngrams/sowpods.txt
Read the text file from the internet (see Tips below)
Create function to display current state

2/
Allow user to guess a letter, and
Validate the input
Display the result (new revealed letters, or write out “not in word!”)

3/
Keep track of the allowed guesses (starts with 6)
Decrement for each new guess (do not penalize for guessing the same letter twice)
Display the remaining allowed guesses at each turn (ie You have 5 guesses remaining)

4/
Have a new game option
Display the hangman to symbolize the number of guesses

5/
Before submitting, you need AT LEAST 2 classes to pass this practical.

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
'''
