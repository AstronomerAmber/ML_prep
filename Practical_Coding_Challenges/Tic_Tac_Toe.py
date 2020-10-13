[Play Tic Tac Toe (also known as knots and crosses)](https://playtictactoe.org/)

**Step 0: Create a game class**

- Input a move through the command line (have clear instructions for them)
- Write make_move function that will take in a location [r,c] and a mark type ('X' or 'O')
- Validate it (and give clarification if the user input is wrong)
- Keep going until the board is full!
- Detect if a player has won!
- Provide the option for the players to play again after the game has ended.

**Step 1: Create board class**
- Display current board status in the terminal and ask for the next move

**Step 2: Create human player class**
- Write a second player or agent that takes the board and plays a random move
- Use input() from a command line

**Step 2: Create an agent class**
- Use either input() from a command line or a random number generated directly from your script

**Step 3: Add in conditional breaks**
- Spot is taken
- Board is full
- Valid inputs

**Step 4 (optional): Create an AI that is better.**
It follows these 3 rules in order:
- If it can win in the next turn, it does
- If it can stop the enemy from winning, it does
- It tries to line up 2 tokens so that it can win the next round
