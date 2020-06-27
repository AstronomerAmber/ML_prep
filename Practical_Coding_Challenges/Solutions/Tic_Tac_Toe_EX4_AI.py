"""
Code up the game tic tac toe
4 class solution
AI player
"""
import random
import numpy as np

#Dictionary to change from number to board notation and vice versa
PLAYER_TO_NUM = {'X':1, 'O':-1, '_':0}
NUM_TO_PLAYR = {1:'X', -1:'O', 0:'_'}

class Game:
    '''
    The class to play the game. Player 2 can be either human or computer.
    If player 2 is a computer, a random move will be chosen from available spots.
    Player 1 moves first. Player 1 is 'X' and Player 2 is 'O'.
    '''
    def __init__(self):
        '''
        Keywords:
            player2: str. Player 2 type. Either 'human' or 'computer'
        '''
        self.board = Board()
        self.board_play = self.board.current_board
        #The dictionary to keep the two players
        self.player = {}
        self.player['X'] = self.choose_player_type(player='X')
        self.player['O'] = self.choose_player_type(player='O')
        print("Game initialization done. Player X starts first.")
        #Print the initialized board.
        print("Current board:")
        for i in range(3):
            print(' '.join([NUM_TO_PLAYR[self.board_play[i][x]] for x in range(3)]))
        print('\n')

    def choose_player_type(self, player='X'):
        '''
        Keywords:
            player: str. Either 'X' or 'O'
        Return:
            Class HumanPlayer or Class Agent, depending on the keyboard input.
        '''
        #The flag to check if the player type is corretly chosen.
        player_chosen = False

        #Keeps asking for player type until a correct one is given.
        while player_chosen == False:
            player_type = input("Choose player {} type, human or computer: ".format(player))

            #If choose HumanPlayer
            if player_type == 'human':
                player_chosen = True
                return HumanPlayer(player=player)
            #If choose Agent(computer)
            elif player_type == 'computer':
                player_chosen = True
                return Agent(player=player)
            #Invalid input.
            else:
                print("Player {} can only be \'human\' or \'computer\'. Please choose again.".format(player))

    def play(self, player='X', spots_left=9):
        '''
        Keywords:
            player: str. Either 'X' or 'O'.
            spots_left: int. Number of empty spots on the board. 0-9.
        '''
        #The flag to check if the move is valid.
        is_move_valid = False

        #Keeps asking until a valid move is given.
        while is_move_valid == False:

            #If player X's turn
            if player == 'X':
                row, column = self.player['X'].move(self.board_play)
                next_player = 'O'
            #If player O's turn
            elif player == 'O':
                row, column = self.player['O'].move(self.board_play)
                next_player = 'X'
            #Invalid player
            else:
                print("Invalid player. Either 'X' or 'O'.")
                exit(1)

            #Check if move is valid, and make a move on board if it is.
            is_move_valid = self.board.make_move(player, row, column)

        #Check if the game is finished or not.
        win_or_draw = self.check_win(spots_left-1)

        #Not finished yet
        if win_or_draw == 0:
            self.play(next_player, spots_left-1)
        #Game finished
        else:
            print("Game finished.")
            print("\n")

    def check_win(self,spots_left):
        '''
        Inputs:
            spots_left: int. Number of empty spots on the board. 0-9.
        Returns:
            int. Game state. 0: Keeps playing. 1: A player wins. 2: Draw.
        '''
        #Check row, column, diagnal sum.
        row_sum = np.sum(self.board_play, axis=1)
        col_sum = np.sum(self.board_play, axis=0)
        diag_sum = np.sum(np.diag(self.board_play))
        anti_diag_sum = np.sum(np.diag(np.rot90(self.board_play)))
        #If any number==3, Player X wins.
        if diag_sum==3 or anti_diag_sum==3 or 3 in row_sum or 3 in col_sum:
            print("Player X wins.")
            return 1
        #If any number == -3, Player O wins.
        elif diag_sum==-3 or anti_diag_sum==-3 or -3 in row_sum or -3 in col_sum:
            print("Player O wins.")
            return 1

        #If no spots available, it's a draw.
        if spots_left == 0:
            print("It's a draw.")
            return 2
        #Keeps playing otherwise.
        else:
            return 0


class Board:
    '''
    The class for the board.
    0 for an empty spot, 1 if Player X placed on the grid. -1 if Player O placed on the grid.
    '''
    def __init__(self):
        #Initialize the board with 0.
        self.current_board = np.zeros((3,3),dtype=int)

    def make_move(self, player, row, column):
        '''
        Inputs:
            player: str. Either 'X' or 'O'.
            row: int. 1-3.
            column: int. 1-3
        Returns:
            move_made: bool. If a valid move is made or not.
        '''
        #Make sure if player is correct. Really shouldn't reach the line here.
        assert player == 'X' or player == 'O', "Invalid player name. Should be either X or O"

        #Flag to check if a valid move is made.
        move_made  = False

        #Invalid move if the spot is already taken.
        if self.current_board[row-1][column-1] != 0:
            print("Spot ({},{}) is taken. Pick another one.".format(row, column))
        else:
            self.current_board[row-1][column-1] = PLAYER_TO_NUM[player]
            print('player {} made a move at ({},{}).'.format(player, row, column))
            for i in range(3):
                print(' '.join([NUM_TO_PLAYR[self.current_board[i][x]] for x in range(3)]))
            print('\n')
            move_made = True

        return move_made


class HumanPlayer:
    '''
    The class for a human player.
    '''
    def __init__(self, player='X'):
        '''
        Keywords;
            player: str. Either 'X' or 'O'.
        '''
        assert player == 'X' or player == 'O', "Invalid player name. Should be either X or O"
        self.player = player

    def move(self, board):
        '''
        Inputs:
            board: numpy.ndarray. Should be a (3,3) numpy array.
        Returns:
            r: int. Row number.
            c: int. Column number.
        '''
        #To do: Check if it's a valid number.
        r = input("Player {} pick a row (1-3): ".format(self.player))
        c = input("Player {} pick a column (1-3): ".format(self.player))
        return int(r), int(c)


class Agent:
    '''
    The class for a computer player.
    The computer player will choose a random move from available spots.
    It follows these 3 rules in order:
        1 If it can win in the next turn, it does
        2 If it can stop the enemy from winning, it does
        3 It tries to line up 2 tokens so that it can win the next round
    '''
    def __init__(self,player='O'):
        '''
        Keywords:
            player: str. Either 'X' or 'O'.
        '''
        self.player = player

    def _get_available_spots(self, board):
        '''
        Inputs:
            board: numpy.ndarray. Should be a (3,3) numpy array.
        Returns:
            spot_list: list. A list of all available spots. Each element is a tuple (row, column)
        '''
        spot_list = []

        #Find all available spots.
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    spot_list.append((i+1,j+1))

        return spot_list

    def move(self, board):
        '''
        Inputs:
            board: numpy.ndarray. Should be a (3,3) numpy array.
        Returns:
            tuple. The spot to place. (row, column)
        '''
        spots_available = self._get_available_spots(board)
        player_num = 1 if self.player=='X' else -1

        row_sum = np.sum(board, axis=1)*player_num
        col_sum = np.sum(board, axis=0)*player_num
        diag_sum = np.sum(np.diag(board))*player_num
        anti_diag_sum = np.sum(np.diag(np.rot90(board)))*player_num
        row_prod = np.prod(board, axis=1)
        col_prod = np.prod(board, axis=0)
        diag_prod = np.prod(np.diag(board))
        anti_diag_prod = np.prod(np.diag(np.rot90(board)))

        #Rule 1
        if diag_sum==2 and diag_prod==0:
            for i in range(3):
                if (i+1,i+1) in spots_available:
                    return i+1, i+1
        if anti_diag_sum==2 and anti_diag_prod==0:
            for i in range(3):
                if (i+1,3-i) in spots_available:
                    return i+1, 3-i

        for i in range(3):
            if row_sum[i]==2 and row_prod[i]==0:
                for j in range(3):
                    if (i+1,j+1) in spots_available:
                        return i+1, j+1
            if col_sum[i]==2 and col_prod[i]==0:
                for j in range(3):
                    if (j+1,i+1) in spots_available:
                        return j+1, i+1

        #Rule 2
        if diag_sum==-2 and diag_prod==0:
            for i in range(3):
                if (i+1,i+1) in spots_available:
                    return i+1, i+1
        if anti_diag_sum==-2 and anti_diag_prod==0:
            for i in range(3):
                if (i+1,3-i) in spots_available:
                    return i+1, 3-i

        for i in range(3):
            if row_sum[i]==-2 and row_prod[i]==0:
                for j in range(3):
                    if (i+1,j+1) in spots_available:
                        return i+1, j+1
            if col_sum[i]==-2 and col_prod[i]==0:
                for j in range(3):
                    if (j+1,i+1) in spots_available:
                        return j+1, i+1

        #Rule 3
        cand = []
        if diag_sum==1 and diag_prod==0:
            if (2,2) in spots_available:
                cand.append((2,2))
            else:
                cand.extend([(1,1),(3,3)])
        if anti_diag_sum==1 and anti_diag_prod==0:
            if (2,2) in spots_available:
                cand.append((2,2))
            else:
                cand.extend([(1,3),(3,1)])

        for i in range(3):
            if row_sum[i]==1 and row_prod[i]==0:
                if (i+1,2) in spots_available:
                    cand.append((i+1,2))
                else:
                    cand.extend([(i,1),(i,3)])
            if col_sum[i]==1 and col_prod[i]==0:
                if (2,i+1) in spots_available:
                    cand.append((2,i+1))
                else:
                    cand.extend([(1,i+1),(3,i+1)])

        return random.choice(list(set(cand))) if len(cand) else random.choice(spots_available)



if __name__ == '__main__':

    current_game = Game()
    current_game.play()

    play = True
    while play:
        play_again = input("Do you want to play again? Answer yes or no:")
        if play_again == 'yes':
            current_game = Game()
            current_game.play()
        elif play_again == 'no':
            print("You chose not to play. Exit.")
            play = False
        else:
            print("Wrong input either yes or no. Exit.")
            play = False
