import string
import numpy as np
import time
words = string.ascii_lowercase



class board:
    def __init__(self, n_grid=None):
        if n_grid == None:
            n_grid = 9
        self.n_grid = n_grid
        self.cur = [[' ' for _ in range(self.n_grid)] for _ in range(self.n_grid)]



    def __repr__(self):
        # structured print for the board
        res = ''
        for i in range(2*(self.n_grid+1)):
            if i == 0:
                res += ' ' * 6
                res += '   '.join(words[:self.n_grid])
                res += ' ' * 2
                res += '\n'
                continue
            if i % 2 == 1:
                res += ' ' * 4  + '-'* (4*self.n_grid+1) + '\n'
                continue
            res += str(i//2) + ' '*(4-len(str(i//2))) + '| ' + ' | '.join(self.cur[(i-1)//2]) + ' |\n'
        return res


class player:
    def __init__(self, n_grid):
        self.n_grid = n_grid

    def click(self):
        """click on a position on the board"""
        pos = input("Input the position you want to click: \n")
        col, row = pos[0], pos[1:]
        if col.isalpha() and row.isnumeric():
            row, col = int(row)-1, words.index(col.lower())
            if col >= 0 and col < self.n_grid and row >= 0 and row <self.n_grid:
                return col, row
        print("Invalid input! Please choose a position for your click.\n")
        return self.click()


class game(board, player):
    def __init__(self, n_mines=None, n_grid=None):
        if n_mines is None:
            n_mines = 10
        if n_grid is None:
            n_grid = 9
        self.mine_map = board(n_grid) # mine board
        self.dis_map = board(n_grid) # display board
        self.player = player(n_grid)
        self.n_mines = n_mines
        self.n_grid = n_grid
        # randomly initialize the mine positions
        self.pos_mines = list(map(lambda x: divmod(x, self.n_grid), np.random.choice(self.n_grid**2, self.n_mines, replace=False)))

    def rematch(self):
        """
        ask if play again
        """
        re = input('Want a rematch? [y/n]')
        if re == 'y':
            return True
        elif re == 'n':
            return False
        else:
            print('Please input "y" or "n" as your choice!')
            return self.rematch()


    def count_mines(self, row, col):
        ct = 0
        for i in range(row-1, row+2):
            if i < 0 or i >= self.n_grid:
                continue
            for j in range(col-1, col+2):
                if j < 0 or j >= self.n_grid:
                    continue
                if self.mine_map.cur[i][j] == '*': # * stands for mine
                    ct += 1
        return ct


    def get_mine_map(self):
        # place mines

        for r_mine, c_mine in self.pos_mines:
            self.mine_map.cur[r_mine][c_mine] = '*'

        for i in range(self.n_grid):
            for j in range(self.n_grid):
                if self.mine_map.cur[i][j] != '*':
                    self.mine_map.cur[i][j] = str(self.count_mines(i, j))


    def check_click(self, row, col):
        """
        check if the click leads to end of game and update the board
        returns: Boolean, whether or not to end the game
        """
        # if click on mine, boom!
        if self.mine_map.cur[row][col] == '*':
            for r_mine, c_mine in self.pos_mines:
                self.dis_map.cur[r_mine][c_mine] = '\x1b[33m*\x1b[0m'
            self.dis_map.cur[row][col] = '\x1b[31m*\x1b[0m'
            return True
        # if click on 0, get connected component
        elif self.mine_map.cur[row][col] == '0':
            self.propagate_zero(row, col)
            return False
        # o.w. display the click
        else:
            self.dis_map.cur[row][col] = self.mine_map.cur[row][col]
            return False

    def check_win(self):
        """
        Check if the board is full (for winning condition)
        """
        ct = 0
        for i in range(self.n_grid):
            for j in range(self.n_grid):
                if self.dis_map.cur[i][j] == ' ':
                    ct += 1
        return ct == self.n_mines



    def propagate_zero(self, row, col):
        """
        Propagate from a zero and get all adjcent 0's.
        """
        self.dis_map.cur[row][col] = '0'
        positions = [(row, col-1), (row, col+1), (row-1, col), (row+1,col)]
        # recurse, but don't go back to previous node
        for i, j in positions:
            # check for grid boundaries
            if i < 0 or i >= self.n_grid or j < 0 or j >= self.n_grid:
                continue
            # if neighbor is 0, propagate
            if self.mine_map.cur[i][j] == '0':
                # don't go back to previous node
                if self.dis_map.cur[i][j] == ' ':
                   self.propagate_zero(i, j)
            # if neighbor is not 0, reveal the number and stop propagation
            else:
                self.dis_map.cur[i][j] = self.mine_map.cur[i][j]


    def play(self):
        """
        Play the game
        """
        self.get_mine_map()
        print('='*70)
        print("Starting MineSweeper (with {} mines on {}x{} grid.)".format(self.n_mines, self.n_grid, self.n_grid) + '\n')
        print(self.dis_map)
        print('='*70)
        starttime = time.time()
        while True:
            minutes, seconds = divmod(int(time.time() - starttime), 60)
            print('Time played: {} minutes, {} seconds.'.format(minutes, seconds))
            print('='*70)
            col, row = self.player.click() # e.g. a5 as col, row
            end_ = self.check_click(row, col)
            print('=' * 70)
            print(self.dis_map)
            print('=' * 70)
            if end_:
                minutes, seconds = divmod(int(time.time() - starttime), 60)
                print('Time played: {} minutes, {} seconds.'.format(minutes, seconds))
                print('=' * 70)
                print('You clicked on a mine. You lose! :-(\n')
                print('='*70)
                break

            if self.check_win():
                minutes, seconds = divmod(int(time.time() - starttime), 60)
                print('Time played: {} minutes, {} seconds.'.format(minutes, seconds))
                print('=' * 70)
                print('You filled the board. You win! :)\n')
                print('='*70)
                break


        if self.rematch():
            self.__init__(self.n_mines, self.n_grid)
            self.play()
        else:
            return


if __name__ == '__main__':
    g = game(10, 9) # n_mines=15, n_grid=12
    g.play()
