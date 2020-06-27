"""
Code up the game tic tac toe
1 class solution
"""

class TicTacToe():

    def __init__(self):

        self.board = self.create_board()
        self.current = 'X'

    def create_board(self):
        "Create the board for Tic Tac Toe"
        board = [['', '', ''],
                 ['', '', ''],
                 ['', '', '']]
        return board

    def print_board(self):
        """
        Print the board just to check
        """
        for row in self.board:
            print(row)

    def check_rows(self):
        """
        Check all the rows for the current player
        """
        for row in self.board:
            if all([True if cell == self.current else False for cell in row]):
                return True
        return False


    def check_diag(self):
        """
        Check if the current player has completed either of the diagonals
        """
        if self.board[0][0] == self.current and self.board[1][1] == self.current and self.board[2][2] == self.current:
            return True
        elif self.board[0][2] == self.current and self.board[1][1] == self.current and self.board[2][0] == self.current:
            return True
        else:
            return False

    def check_cols(self):
        """
        Check if any of the columns have been completed.
        """
        for i in range(3):
            if all([True if self.board[j][i] == self.current else False for j in range(3)]):
                return True
        return False

    def make_move(self, move):
        curr_player = self.current

        # Make a move
        row, col = move

        if self.board[row][col] == '':
            self.board[row][col] = curr_player
            return True
        else:
            print("Position is already filled with {self.board[row][col]}")
            return False

    def change_player(self):
        """
        Change the player whose turn is
        """
        if self.current == 'X':
            self.current = 'O'
        else:
            self.current = 'X'

    def check_board(self):
        """
        Check if the current player has one the game
        """
        won_game = False

        # Check if any of the rows have been completed
        if self.check_rows() or self.check_cols() or self.check_diag():
            self.print_board()
            won_game = True

        return won_game

    def play_game(self):

        # Print message
        print(f"Player 1 is X and Player2 is O. Player 1 goes first")
        for i in range(9):

            # Current Player makes a move
            while True:
                print(f"Player {self.current} needs to enter a move")
                move = tuple(int(x.strip()) for x in input().split(','))

                # Make the move and check if it is valid
                if self.make_move(move):
                    break

            # Check if the game has been won
            if self.check_board():
                print(f"Player {self.current} has already won.Congratulations")
                return
            # Change the turn of the player
            self.change_player()
            self.print_board()

        print("Nobody won the game. Well played guys")

if __name__ == "__main__":

    t = TicTacToe()
    t.print_board()
    t.play_game()
