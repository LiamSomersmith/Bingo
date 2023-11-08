from tkinter import *
from PIL import Image, ImageTk
import random 

class App(Tk):
    def __init__(self):
        super().__init__()

# Handles the GUI and Game Logic
class Board():
    def __init__(self):
        self.filename = "Phrases.txt"
        self.phraseGrid = [[],[],[],[],[]] # a 2d list with 5 "rows" (like a bingo board!)

    # Gets the text from the file and populates the grip at random
    def getDataFromFile(self):
        with open(self.filename, "r") as cPhrases:
           phrases = cPhrases.readlines()
           for i in range(5):
               for j in range(5):
                   randomNumber = random.randint(0,len(phrases)-1)
                   self.phraseGrid[i].append(phrases[randomNumber])
                   del phrases[randomNumber]

    def clearSquare(x,y,buttonsGrid, scoreGrid):
        buttonsGrid[x][y].configure(fg="white", bg="green")
        scoreGrid[x][y] = 0
        
    def causeWin(grid, buttonGrid,text):
        if Board.winCondition(sGrid=grid) == True:
            for i in range(5):
                for button in buttonGrid[i]:
                    button.destroy()
            text.place(x=723, y=400)
        else:
            pass
          
    def winCondition(sGrid):
        win = False
        #Rows
        for i in range(5):
            if sum(sGrid[i]) == 0:
                win = True
                break
        #Columns
        for i in range(5):
            if sGrid[0][i] == sGrid[1][i] == sGrid[2][i] == sGrid[3][i] == sGrid[4][i] == 0:
                 win = True
                 break
        #Diagonals
        if sGrid[0][0] == sGrid[1][1] == sGrid[2][2] == sGrid[3][3] == sGrid[4][4] == 0:
            win = True
            
        elif sGrid[0][4] == sGrid[1][3] == sGrid[2][2] == sGrid[3][1] == sGrid[4][0] == 0:
            win = True
              
        return win

    def createBoard(self):
        self.app = App()

        # Window Setup
        self.app.geometry=("1446x801")
        self.app.resizable(False,False)
        self.app.title("David Bingo")
        ico = Image.open("icon.png")
        photo = ImageTk.PhotoImage(ico)
        self.app.wm_iconphoto(False, photo)
        t = Label(self.app, text="YOU WIN!")

        #Placing buttons in a 5x5 grid
        buttons = [[],[],[],[],[]]
        binaryGrid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
        for i in range(5):
            for j in range(5):
                b = Button(self.app, text= self.phraseGrid[i][j].strip("\n"), width=40, height=10, command=lambda i=i, j=j: [Board.clearSquare(x=i,y=j, buttonsGrid=buttons, scoreGrid=binaryGrid), Board.causeWin(grid=binaryGrid, buttonGrid=buttons, text=t)])
                b.grid(row=i+1, column=j+1)
                buttons[i].append(b)

        self.app.mainloop()

def main():
    game = Board()
    game.getDataFromFile()
    game.createBoard()

if __name__ == "__main__":
    main()
