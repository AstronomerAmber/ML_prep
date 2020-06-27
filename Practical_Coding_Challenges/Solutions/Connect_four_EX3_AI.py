"""
Code up the game connect four
3 class solution
AI player
"""

import numpy as np
import pdb

class Game():
    def __init__(self, player1_human=True, player2_human=False,
                    rows=4, columns=4, win=4):
        self.player1 = Player('X', 1, ishuman=player1_human)
        self.player2 = Player('O', 2, ishuman=player2_human)
        token_dict = {0:'_', 1:'X', 2:'O'}
        self.game_board = Board(token_dict, rows=rows, columns=columns,
                                    win=win)

    def play_game(self):
        print('Welcome to tic tac toe')
        move_number = 0
        while not self.game_board.is_full():
            #pdb.set_trace()
            print(self.game_board.board_to_string())
            self.make_move(move_number)

            score = self.game_board.check_wins()

            if score:
                break

            move_number += 1

        if score:
            print(self.game_board.board_to_string())
            print(f'Player {score} has won Connect Four!')
        else:
            print('No moves left!')

        next_game = input('\nWould you like to play again? [y/n]: ')
        if next_game[0].upper() == 'Y':
            print('Starting new game\n')
            self.reset_board()
            self.play_game()
        else:
            print('Thank you for playing')


    def reset_board(self):
        token_dict = self.game_board.token_dict
        rows = self.game_board.rows
        cols = self.game_board.columns
        win = self.game_board.win
        self.game_board = Board(token_dict, rows=rows, columns=cols,
                                    win=win)


    def make_move(self, move_number):
        if move_number % 2 == 0:
            player_to_go = self.player1
        else:
            player_to_go = self.player2

        move = player_to_go.make_move(self.game_board)

        if self.game_board.validate_move(move):
            self.game_board.make_move(move, player_to_go.player_int)
        else:
            print('Invalid Move! Choose another location\n')
            self.make_move(move_number)


class Board():
    def __init__(self, token_dict, rows=4, columns=4, win=4):
        self.token_dict = token_dict
        self.rows = rows
        self.columns = columns
        self.create_board(rows, columns)
        self.win = win

    def create_board(self, rows, columns):
        self.board = np.zeros((rows, columns)).astype(int)

    def make_move(self, column, token_int):
        if self.validate_move(column):
            board_col = self.board[:, column]
            empty_rows = []
            for i, value in enumerate(board_col):
                if value == 0:
                    empty_rows.append(i)

            bottom_row = empty_rows[-1]
            self.board[bottom_row, column] = token_int

        else:
            print(f'Invalid move, column {column} is full')

    def board_to_string(self):
        board = np.vectorize(self.token_dict.get)(self.board).tolist()
        board_str = ''
        for i in range(len(board[0])):
            board_str += f' {i}'
        board_str += '\n'
        for row in board:
            board_str += '|' + '|'.join(row) + '|' + '\n'

        return board_str

    def get_valid_moves(self):
        valid_moves = []
        top_row = self.board[0,:]
        for i, row_val in enumerate(top_row):
            if row_val == 0:
                valid_moves.append(i)

        return valid_moves

    def validate_move(self, move):
        if move in self.get_valid_moves():
            return True
        else:
            return False

    def check_wins(self):
        board_sections = self.get_board_sections()

        for section in board_sections:
            if len(section) > self.win:
                section_chunks = self.chunk_section(section, self.win)
            else:
                section_chunks = [section]

            for chunk in section_chunks:
                if self.validate_section(chunk):
                    return self.validate_section(chunk)

        return False

    def is_full(self):
        if (self.board == 0).sum() == 0:
            return True
        else:
            return False

    def chunk_section(self, section, chunksize):
        chunks = [section[i:i+chunksize] for i in range(0, len(section)-chunksize+1)]
        return chunks

    def get_board_sections(self):
        sections = []
        for row in range(self.rows):
            sections.append(self.board[row,:])


        for col in range(self.columns):
            sections.append(self.board[:,col])

        sections += self.grab_diagonals(self.board)
        sections += self.grab_diagonals(np.rot90(self.board))

        return sections

    def grab_diagonals(self, board):
        rows, cols = board.shape
        diags = [np.diag(board)]
        for i in range(1, cols):
            diag = np.diag(board, i)
            if len(diag) >= self.win:
                diags.append(diag)

        for i in range(1, rows):
            diag = np.diag(board, -1*i)
            if len(diag) >= self.win:
                diags.append(diag)

        return diags

    def validate_section(self, section):
        tokens = list(set(section))
        if len(tokens) == 1 and not tokens[0] == 0:
            return tokens[0]
        else:
            return False

    def reverse_move(self, column):
        col = self.board[:, column]
        for i, value in enumerate(col):
            if not value == 0:
                self.board[i, column] = 0
                break

    def __repr__(self):
        return self.board_to_string()

class Player():
    def __init__(self, player_token, player_int, ishuman=True):
        self.player_token = player_token
        self.player_int = player_int
        self.ishuman = ishuman

    def make_move(self, board):
        if self.ishuman:
            return self.human_move()
        else:
            return self.ai_move(board)

    def human_move(self):
        col = int(input('Input column to play: '))
        return col

    def ai_move(self, board):
        move = self.ai_play(board)
        print(f'AI plays column {move}')
        return move

    def ai_play(self, board):
        synthetic_board = Board(board.token_dict, rows=board.rows,
                                columns=board.columns, win=board.win)
        synthetic_board.board = np.copy(board.board)

        self_win = self.find_winning_move(synthetic_board, self.player_int)
        if self_win:
            print('AI goes for the win')
            return self_win

        opponent_token = 2 if self.player_int == 1 else 1
        opponent_win = self.find_winning_move(synthetic_board, opponent_token)
        if opponent_win:
            print('AI moves to block')
            return opponent_win

        possible_moves = synthetic_board.get_valid_moves()
        print('AI makes a random move')
        return np.random.choice(possible_moves)


    def find_winning_move(self, board, token):
        moves = board.get_valid_moves()
        for move in moves:
            board.make_move(move, token)
            if board.check_wins():
                return move
            else:
                board.reverse_move(move)
        return False
