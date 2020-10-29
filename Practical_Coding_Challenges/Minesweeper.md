"""
Objective: Coding Minesweeper from scratch
Dependcies: Python 3.6, numpy, re, time, ascii_lowercase
**Coding Minesweeper from scratch**

Step 0: Play a [Minesweeper](http://minesweeperonline.com/) game and/or check out the example below.

Step 1: Take any board length (the board is square) and number of mines
* Default is 9x9 board with 10 mines
* Now silently thank Amber for gifting you this beautiful board

Step 2: Take user input as x, y coordinates
* Easiest to make the rows numbers and columns letters (eg. a5).

Step 3: End the game if they click a mine

Step 4: Reveal the numbers if they click somewhere else.

Step 5: If they click on a square with “zero”, the board propagates the reveal all consecutive 0's (and surrounding numbers) as a convenience method. **This is the hardest part!**

Step 6: Check edge cases
* Tips:
* import re
* from string import ascii_lowercase

Step 7: Have the player be able to mark the mines
* To place or remove a flag, add 'f' to the cell (eg. a5f).
* You can also toggle flag (flag: a5)

Step 8: Bonus
Add time played
*  import time
*  Minutes, seconds = divmod(int(time.time() - starttime), 60)
* Or use a @decorator
* Or timeit
* time.time or time.clock, see timeit.default_timer

Add animate to the propagation

**Example:**

![Ex 2](https://codesignal.s3.amazonaws.com/uploads/1593570610131/Screen_Shot_2020-06-30_at_6.31.23_PM.png)
![ ](https://codesignal.s3.amazonaws.com/uploads/1593570776392/Screen_Shot_2020-06-30_at_7.32.26_PM.png)
![ ](https://codesignal.s3.amazonaws.com/uploads/1593573679741/Screen_Shot_2020-06-30_at_7.43.04_PM.png)
![](https://codesignal.s3.amazonaws.com/uploads/1593573698324/Screen_Shot_2020-06-30_at_7.43.40_PM.png)

"""
