import numpy as np

class Board:
	def __init__(self, grid_size=(6, 7)):
		self.grid_size = grid_size
		self.empty = "_"
		self.state = np.tile(self.empty, grid_size)

	def display_board(self):
		print()
		for row in self.state:
				print(*row)
		print()

	def place_token(self, token, col):
		if self.state[0, col] != self.empty:
			print('This column is full!')
			return False
		else:
			for i in range(0, self.grid_size[0])[::-1]:
				if self.state[i, col] == self.empty:
					self.state[i, col] = token
					return True

	def available_plays(self):
		return [i for i in range(self.grid_size[1]) if self.state[0, i] == self.empty]

	def is_full(self):
		return not self.empty in self.state


class Player:
	def __init__(self, token, human=True):
		self.token = token
		self.human = human

	def play_move(self, board):
		played_move = False
		while not played_move:
			if self.human:
				col = int(input('Choose column: '))
			else:
				col = np.random.choice(board.available_plays())
			played_move = board.place_token(self.token, col)


class Game:
	def __init__(self):
		self.board = Board()
		self.players = [Player('X'), Player('O', False)]

	def reset(self):
		self.board = Board()
		self.players = [Player('X'), Player('O', False)]

	def game_is_won(self):
		done = False

		for i in range(self.board.grid_size[0]):
			done |= self._check_line(self.board.state[i, :])

		for i in range(self.board.grid_size[1]):
			done |= self._check_line(self.board.state[:, i])

		for i in range(sum(self.board.grid_size)):
			j = i-self.board.grid_size[0]+1
			k = i-self.board.grid_size[1]+1
			done |= self._check_line(np.diag(self.board.state, j))
			done |= self._check_line(np.diag(np.rot90(self.board.state), k))

		if not done and self.board.is_full():
			done = True
			print('DRAW! Board is full!')
		return done

	def _check_line(self, line):
		current_token = None
		count = 0
		for token in line:
			if token != current_token or token == self.board.empty:
				current_token = token
				count = 1 if token != self.board.empty else 0
			else:
				count += 1
			if count == 4:
				print('{} has won!'.format(current_token))
				return True
		return False

	def run(self):
		self.reset()
		self.board.display_board()
		current_player = 0
		while not self.game_is_won():
			self.players[current_player].play_move(self.board)
			self.board.display_board()
			current_player ^= 1

	def play(self):
		play_again = True
		while play_again:
			self.run()
			play_again = input('Play Again? (yes/no) ')
			play_again = True if play_again=='yes' else False


if __name__=='__main__':
	game = Game()
	game.play()
