'''
Fully working with flags and arbitrary board sizes. Total time ~2.5 hours
Now includes option to animate the propogation of 0's :D
'''
import numpy as np
import time

class Minesweeper() :
    def __init__(self, rows=5, cols=5, numbombs=5, animate_propogate=True) :
        self.rows = rows
        self.cols = min(26, cols)
        self.board = self.Board(rows,cols, numbombs, self)
        self.alphabet, self.alphadict, self.reverseAlphaDict = self.getAlphabet()
        self.num_bombs = numbombs
        self.animate_propogate = animate_propogate

    def playGame(self) :
        while True :
            self.showGame()
            flag, space = self.getInput()
            selected_space = self.board.getSpace(space)

            if flag :
                selected_space.flagged = not selected_space.flagged
                continue
            if selected_space.isbomb:
                print('BOOM! BOOM! BOOM!\n\nFinal Game Board:')
                self.showGame(mode=1)
                break
            else :
                selected_space.propogate()
            if self.checkWin() :
                print('\n\nAll bombs found! Mines swept up. Final Game Board:')
                self.showGame(mode=1)
                break

    def playGames(self) :
        while True:
            self.playGame()
            self.resetGame()
            restart = input('Would you like to play again? [y/n]: ')
            if not restart.lower().strip() == 'y' :
                print('\nHave a good day!\n')
                break

    def resetGame(self) :
        self.board = self.Board(self.rows,self.cols, self.num_bombs, self)

    def getInput(self) :
        while True :
            try :
                space = input('Input guess location [toggle flag like flag:b2]: ')
                flag = False
                if 'flag:' in space.lower() :
                    space = space.split(':')[1]
                    flag = True
                if len(space) <= 1 :
                    print('Invalid input, too short.')
                    continue
                col = int(self.reverseAlphaDict[space[0]])
                row = int(space[1:])

                if (col<0 or row<0 or col>=self.cols or row>=self.rows) :
                    print('Out of range.')
                    continue
                return flag, (row,col)

            except(KeyboardInterrupt) :
                break
            except :
                print('Invalid input, try again.')
                continue

    def showGame(self, mode=0) :
        print('    ' + self.alphabet[:self.cols].upper())
        for r in range(self.rows) :
            print(' {:2} '.format(r), end='')
            for c in range(self.cols) :
                end = '' if c<self.cols-1 else '\n'
                extra = ''
                if self.cols > 5 and c == self.cols-1:
                        extra = ' {:2} '.format(r)

                if mode == 0 :
                    print(str(self.board.board[r][c]) + extra, end=end)
                elif mode == 1 :
                    to_show = self.board.board[r][c]
                    output = 'B' if to_show.isbomb else str(to_show.bombsnearby)
                    print(output + extra, end=end)
        if self.rows > 5 : print('    ' + self.alphabet[:self.cols].upper())

    def showDebug(self, mode) :
        for r in range(self.rows) :
            for c in range(self.cols) :
                print(self.board.board[r][c].debugShow(mode), end= ('' if c<self.cols-1 else '\n'))

    def checkWin(self) :
        num_found = self.board.getNumRevealed()
        if (self.rows*self.cols - num_found) <= self.num_bombs :
            return True
        else :
            return False

    def getAlphabet(self) :
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphadict = { k:v for k,v in enumerate(alphabet)}
        reverseAlphaDict = { v:k for k,v in enumerate(alphabet)}
        return alphabet, alphadict, reverseAlphaDict

    class Board() :
        def __init__(self, rows, cols, num_bombs, game) :
            self.rows = rows
            self.cols = cols
            self.numbombs = num_bombs
            self.board = [ ([0] * cols) for row in range(rows)]
            for r in range(rows) :
                for c in range(cols) :
                    self.board[r][c] = self.Space(r, c, game)

            self.placeBombs(num_bombs)
            self.getAllNeigbors()
            self.updateBombDists()

        def getNumRevealed(self):
            num_revealed = 0
            for r in range(self.rows) :
                for c in range(self.cols) :
                    if (self.getSpace((r,c)).revealed) : num_revealed += 1
            return num_revealed

        def placeBombs(self, num_bombs) :
            placed_bombs = 0
            while placed_bombs < num_bombs :
                spot = np.random.randint((self.rows, self.cols))
                test_space = self.getSpace(spot)

                if (not test_space.isbomb) :
                    test_space.isbomb = True
                    test_space.bombsnearby = -1
                    placed_bombs += 1

        def getSpace(self, spot) :
            return self.board[spot[0]][spot[1]]

        def updateBombDists(self) :
            for r in range(self.rows) :
                for c in range(self.cols) :
                    self.getSpace((r,c)).neighborBombs()
        '''
        Return a list with neighbor space links (null if doesn't exist):
        0  1  2
        3     4
        5  6  7
        '''
        def getAllNeigbors(self) :
            for r in range(self.rows) :
                for c in range(self.cols) :
                    neighbors = []
                    for relrow in [-1, 0, 1] :
                        for relcol in [-1, 0, 1] :
                            if (relrow==0 and relcol==0) :
                                continue
                            row = r + relrow
                            col = c + relcol
                            if (row >= self.rows or row < 0) or (col >= self.cols or col < 0):
                                neighbors.append(None)
                            else:
                                neighbors.append(self.getSpace((row,col)))
                    self.getSpace((r,c)).neighbors = neighbors


        class Space() :
            def __init__(self, row, col, game) :
                self.isbomb = False
                self.revealed = False
                self.flagged = False
                self.bombsnearby = 0
                self.row = row
                self.col = col
                self.neighbors = []
                self.game = game

            def __repr__(self) :
                if not self.revealed and self.flagged :
                    return 'F'
                elif not self.revealed :
                    return '*'
                else :
                    return str(self.bombsnearby)

            def debugShow(self, mode) :
                if mode==0 : return '{}:{} '.format(self.row,self.col)
                if mode==1 : return 'B' if self.isbomb else str(self.revealed)[0]

            def neighborBombs(self) :
                nbombs = 0
                for neighbor in self.neighbors :
                    if neighbor == None :
                        continue
                    if neighbor.isbomb :
                        nbombs += 1
                self.bombsnearby = nbombs

            def propogate(self) :
                self.revealed = True
                if self.bombsnearby > 0 :
                    return
                for nb in self.neighbors :
                    if not nb == None and not nb.revealed :
                        if (self.game.animate_propogate) :
                            print('\n')
                            self.game.showGame()
                            time.sleep(0.05)
                            print('\n')
                        nb.propogate()

            def printNeighbors(self) :
                print('{} {} {}'.format(self.neighbors[0], self.neighbors[1], self.neighbors[2]))
                print('{} {} {}'.format(self.neighbors[3], '    ', self.neighbors[4]))
                print('{} {} {}'.format(self.neighbors[5], self.neighbors[6], self.neighbors[7]))

#%% Testing
game = Minesweeper(10,10,10,animate_propogate=True)
game.playGames()
