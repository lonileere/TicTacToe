import random

class Board:
    def __init__(self):
        self.board_literal = ['-', '-', '-', '-', '-', '-', '-', '-', '-', ]
        self.gameover = False
        self.winner = " "
        self.player = 1
        self.twoplayer = False

    def newgame(self):
        self.board_literal = ['-', '-', '-', '-', '-', '-', '-', '-', '-', ]
        self.gameover = False
        self.winner = ' '

    def _printboard(self):
        self.board = f'''
          {self.board_literal[0:3]} {map_1}
          {self.board_literal[3:6]} {map_2}
          {self.board_literal[6:9]} {map_3}                                                                            
        '''
        print(self.board)

    def playermove(self, space):
        self.board_literal[space] = 'X'

    def player2move(self, space):
        self.board_literal[space] = 'O'

    def opponentmove(self):
        move = random.randint(0, 8)
        if '-' in self.board_literal:
            if self.board_literal[move] != '-':
                self.opponentmove()
            elif self.board_literal[move] == '-':
                self.board_literal[move] = 'O'
        else:
            self.checkboard()

    def checkboard(self):
        i = self.board_literal

        # board win conditions
        x = ('X', 'X', 'X')
        o = ('O', 'O', 'O')

        if (i[0], i[1], i[2]) == x or (i[0], i[1], i[2]) == o:  # check for first row
            self.winner = i[0]
            self.gameover = True
        elif (i[3], i[4], i[5]) == x or (i[3], i[4], i[5]) == o:  # check for second row
            self.winner = i[3]
            self.gameover = True
        elif (i[6], i[7], i[8]) == x or (i[6], i[7], i[8]) == o:  # check for third row
            self.winner = i[6]
            self.gameover = True
        elif (i[0], i[3], i[6]) == x or (i[0], i[3], i[6]) == o:  # check for first column
            self.winner = i[0]
            self.gameover = True
        elif (i[1], i[4], i[7]) == x or (i[1], i[4], i[7]) == o:  # check for second column
            self.winner = i[1]
            self.gameover = True
        elif (i[2], i[5], i[8]) == x or (i[2], i[5], i[8]) == o:  # check for third column
            self.winner = i[2]
            self.gameover = True
        elif (i[0], i[4], i[8]) == x or (i[0], i[4], i[8]) == o:  # check for l to r diagonal
            self.winner = i[0]
            self.gameover = True
        elif (i[2], i[4], i[6]) == x or (i[2], i[4], i[6]) == o:  # check for r to l diagonal
            self.winner = i[2]
            self.gameover = True
        elif '-' not in i:  # check for draw
            self.winner = 'Draw'
            self.gameover = True


