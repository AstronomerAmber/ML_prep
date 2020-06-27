"""
Save file as: FIRSTNAME_LASTINITIAL_Mineswepper.py
Timestamp: 02042020
Objective: Coding Minesweeper from scratch
Dependcies: Python 3.6, numpy, re, time, ascii_lowercase

@author: Amber
///////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\


Step 0: Code a Minesweeper game
Step 1: Take any board length (the board is square) and number of mines
        - Standard is 9x9 board with 10 mines
Step 2: Take user input as x, y coordinates
        - Easiest to make the rows numbers and columns letters (eg. a5).
Step 3: End the game if they click a mine
Step 4: Reveal the numbers if they click somewhere else.
Step 5: If they click on a square with “zero”, the board propagates the reveal all
consecutive 0's (and surrounding numbers) as a convenience method.
Step 6: Check edge cases
        - import re
        - from string import ascii_lowercase
Step 6: Bonus: Have the player be able to mark the mines
        - To place or remove a flag, add 'f' to the cell (eg. a5f).
Step 7: Bonus: Add time played
        -  import time
        -  Minutes, seconds = divmod(int(time.time() - starttime), 60)

"""
