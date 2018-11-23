from tkinter import *
import tkinter.messagebox
import ttt


class GameBoard:

    def __init__(self, master):

        Grid.rowconfigure(master, 0, weight=1)
        Grid.columnconfigure(master, 0, weight=1)

        self.frame = Frame(master)
        self.frame.grid(row=0, column=0, sticky=N + S + E + W)

        for row_index in range(3):
            Grid.rowconfigure(self.frame, row_index, weight=1)
            for col_index in range(3):
                Grid.columnconfigure(self.frame, col_index, weight=1)
        Grid.rowconfigure(self.frame, 3, weight=1,)

        self.var = IntVar()
        if not board.twoplayer:
            self.var.trace('w', self.turn)
        elif board.twoplayer:
            self.var.trace('w', self.double)

        self.btn1 = Button(self.frame, command=lambda: self.var.set(0))
        self.btn1.grid(row=0, column=0, sticky=N + S + E + W)

        self.btn2 = Button(self.frame, command=lambda: self.var.set(1))
        self.btn2.grid(row=0, column=1, sticky=N + S + E + W)

        self.btn3 = Button(self.frame, command=lambda: self.var.set(2))
        self.btn3.grid(row=0, column=2, sticky=N + S + E + W)

        self.btn4 = Button(self.frame, command=lambda: self.var.set(3))
        self.btn4.grid(row=1, column=0, sticky=N + S + E + W)

        self.btn5 = Button(self.frame, command=lambda: self.var.set(4))
        self.btn5.grid(row=1, column=1, sticky=N + S + E + W)

        self.btn6 = Button(self.frame, command=lambda: self.var.set(5))
        self.btn6.grid(row=1, column=2, sticky=N + S + E + W)

        self.btn7 = Button(self.frame, command=lambda: self.var.set(6))
        self.btn7.grid(row=2, column=0, sticky=N + S + E + W)

        self.btn8 = Button(self.frame, command=lambda: self.var.set(7))
        self.btn8.grid(row=2, column=1, sticky=N + S + E + W)

        self.btn9 = Button(self.frame, command=lambda: self.var.set(8))
        self.btn9.grid(row=2, column=2, sticky=N + S + E + W)

        self.reset = Button(self.frame, text="Reset")
        self.reset.bind("<Button-1>", self.restart)
        self.reset.grid(row=3, columnspan=3, sticky=N + S + E + W)

        self.toggle = Button(self.frame, text="Switch to Two Player Mode")
        self.toggle.bind("<Button-1>", self.toggleb)
        self.toggle.grid(row=4, columnspan=3, sticky=N + S + E + W)


        self.btnlist = \
            [
                   self.btn1,
                   self.btn2,
                   self.btn3,
                   self.btn4,
                   self.btn5,
                   self.btn6,
                   self.btn7,
                   self.btn8,
                   self.btn9,
            ]

    def disable(self):
        for index, i in enumerate(board.board_literal):
            if i != '-':
                self.btnlist[index].config(state=DISABLED)
                if i == 'X':
                    self.btnlist[index].config(text='X')
                elif i == 'O':
                    self.btnlist[index].config(text='O')
        if board.gameover:
            for index, i in enumerate(self.btnlist):
                self.btnlist[index].config(state=DISABLED)

    def turn(self, *args):
            if not board.twoplayer:
                board.playermove(self.var.get())
                board.checkboard()
                self.disable()
                if not board.gameover:
                    board.opponentmove()
                    board.checkboard()
                    self.disable()
                self.winner()

            if board.twoplayer:
                if board.player == 1:
                    board.playermove(self.var.get())
                    board.checkboard()
                    board.player = 2
                    self.disable()
                elif board.player == 2:
                    board.player2move(self.var.get())
                    board.checkboard()
                    board.player = 1
                    self.disable()
                self.winner()


    def _drawtest(self, *args):
            board.board_literal = ['O', 'X', 'O', 'O', 'X', 'X', 'X', 'O', 'X', ]
            board.checkboard()
            self.disable()
            if not board.gameover:
                board.opponentmove()
                board.checkboard()
                self.disable()
            self.winner()

    def restart(self, *args):
            board.newgame()
            for index, i in enumerate(self.btnlist):
                    self.btnlist[index].config(state=ACTIVE)
                    self.btnlist[index].config(text=" ")

    def winner(self):
        if board.winner == 'X':
            tkinter.messagebox.showinfo('Winner', 'The winner is X!')
        elif board.winner == 'O':
            tkinter.messagebox.showinfo('Winner', 'The winner is O!')
        elif board.winner == 'Draw':
            tkinter.messagebox.showinfo('Draw', 'It was a draw!')

    def toggleb(self, *args):
        if board.twoplayer:
            board.twoplayer = False
            self.toggle.config(text='Switch to Two Player Mode')
            print(1)
        elif not board.twoplayer:
            board.twoplayer = True
            self.toggle.config(text='Switch to Single Player Mode')
            print(2)



board = ttt.Board()
root = Tk()
root.geometry("500x550")
root.winfo_toplevel().title("Tic-Tac-Toe")
boardg = GameBoard(root)
root.mainloop()






