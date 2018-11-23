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

    def printboard(self):
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
            if self.board_literal[0] == self.board_literal[1] == self.board_literal[2]:
                if self.board_literal[0] != '-':
                    self.winner = self.board_literal[0]
                    self.gameover = True
            elif self.board_literal[0] == self.board_literal[3] == self.board_literal[6]:
                if self.board_literal[0] != '-':
                    self.winner = self.board_literal[0]
                    self.gameover = True
            elif self.board_literal[0] == self.board_literal[4] == self.board_literal[8]:
                if self.board_literal[0] != '-':
                    self.winner = self.board_literal[0]
                    self.gameover = True
            elif self.board_literal[3] == self.board_literal[4] == self.board_literal[5]:
                if self.board_literal[3] != '-':
                    self.winner = self.board_literal[3]
                    self.gameover = True
            elif self.board_literal[6] == self.board_literal[7] == self.board_literal[8]:
                if self.board_literal[6] != '-':
                    self.winner = self.board_literal[6]
                    self.gameover = True
            elif self.board_literal[1] == self.board_literal[4] == self.board_literal[7]:
                if self.board_literal[1] != '-':
                    self.winner = self.board_literal[1]
                    self.gameover = True
            elif self.board_literal[2] == self.board_literal[5] == self.board_literal[8]:
                if self.board_literal[2] != '-':
                    self.winner = self.board_literal[2]
                    self.gameover = True
            elif self.board_literal[2] == self.board_literal[4] == self.board_literal[6]:
                if self.board_literal[2] != '-':
                    self.winner = self.board_literal[2]
                    self.gameover = True
            elif '-' not in self.board_literal:
                print('Draw!')
                self.winner = 'Draw'
                self.gameover = True

