import numpy as np

class MineSweeper(object):
	def __init__(self, player_name, size, n_mines):
		self._board = Board(size, n_mines)
		self._player = Player(name)

	def start(self):
		# game loop
		survive = True
		while self._board.is_available():

			self._board.show()

			print('please select one cell (row,col): ')
			pos = self._player.move()

			# check availability of input
			while not self._board.check_status(pos):
				print('place has been already taken, please re-select one cell (row,col): ')
				pos = self._player.move()

			# check mine
			survive = self._board.click(pos)

			if not survive:
				self._end_game(win=False)
				break

		if survive:
			self._end_game(win=True)


	def _end_game(self, win=False):
		print('====== Game End ======')
		self._board.show(reveal=True)

		if win:
			print(self._player.name + ' wins !!!!')

		else:
			print(self._player.name + ' lost ....')

class Board(object):
	def __init__(self, size, n_mines):
		self._size = size
		self._n_mines = n_mines
		self._mine_symbol = 'x'
		self._remain = size * size - n_mines
		self._board = self._creat_board(size, n_mines)
		self._status = [[False for _ in range(size)] for _ in range(size)] # has been clicked or not

	def _creat_board(self, size, n_mines):
		board = [[0 for _ in range(size)] for _ in range(size)]
		mines = self._random_mines( size, n_mines)

		# set mines as -1 in board
		for x, y in mines:
			board[x][y] = self._mine_symbol

		# calculate the number of each cell
		search_range = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
		for i in range(size):
			for j in range(size):
				if (i,j) in mines:
					continue
				# search neighbor
				neighbor_mines = 0
				for di, dj in search_range:
					if (i+di, j+dj) in mines:
						neighbor_mines += 1

				board[i][j] = neighbor_mines

		return board

	def _random_mines(self, size, n_mines):
		mines_pos = set() # position of mines

		cnt = 0
		while cnt < n_mines:
			# random choose
			x = np.random.choice(range(size))
			y = np.random.choice(range(size))

			if (x,y) not in mines_pos:
				mines_pos.add((x,y))
				cnt += 1

		return mines_pos

	def check_status(self, pos):
		# check cell is already taken

		x, y = pos

		if self._status[x][y]:
			return False

		else:
			return True

	def click(self, pos):
		x, y = pos

		# is mine
		if self._board[x][y] == self._mine_symbol:
			self._status[x][y] = True
			return False

		elif self._board[x][y] == 0:
			self._expand(x,y)
			return True
		else:
			self._status[x][y] = True
			self._remain -= 1
			return True

	def _expand(self, x, y):
		# dfs find zeros
		if self._status[x][y]:
			return

		else:
			self._remain -= 1
			self._status[x][y] = True
			neighbor_range = [(-1,0),(1,0),(0,-1),(0,1)]

			for dx, dy in neighbor_range:
				if 0 <= x+dx < self._size and 0 <= y+dy < self._size:
					if self._board[x+dx][y+dy] == 0:
						self._expand(x+dx, y+dy)

	def is_available(self):
		# check if there is any place that can be selected
		if self._remain >= 0:
			return True

		else:
			return False

	def show(self, reveal=False):
		for i in range(self._size):
			row_str = ''
			for j in range(self._size):
				if self._status[i][j] or reveal:
					row_str += str(self._board[i][j]) + ' '
				else:
					row_str += 'Ｏ'
			print(row_str)

class Player(object):
	def __init__(self, name):
		self.name = name

	def move(self):
		pos = tuple(map(int, input().split(',')))
		return pos

if __name__ == '__main__':
	print('Please input your name: ')
	name = input()

	print('Please input board size: ')
	size = int(input())

	print('Please input mines number: ')
	n_mines = int(input())

	game = MineSweeper(name, size, n_mines)
	game.start()
