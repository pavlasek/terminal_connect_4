import os
import platform
import time
import random

class Connect4Game:
    game_grid = []
    cursor_position = 0

    def __init__(self):
        self.game_grid = [
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "]]


    def playGame(self):
        self.showStartingInfo()        

    def showStartingInfo(self):
        """Prints information at the start of the game. Prints instruction
        and how to play the game."""

        print("--------------------------------------------------------------------------------------------")     
        print("Welcome to the Connect 4 Game!")
        print("--------------------------------------------------------------------------------------------\n")
        print("How to play: ")
        print(" + Players takes turns to inserts stones into grid using.")
        print(" + Switch between columns using LEFT and RIGHT arrow and put the stone using the DOWN arrow.")
        print(" + Blinking # symbol shows in which column the stone will be placed.")
        print(" + Second player uses A, D and S keys.")
        print(" + Player who connects 4 in row, column or diagonally wins.")
        print("\n--------------------------------------------------------------------------------------------\n")

    def checkWinner(self):
        pass

    def showFinalInfo(self):
        pass

    def showStartingGrid(self):
        """Shows the starting grid and the cursor in the default position."""
        
        pass

    def clearTerminal(self):
        """Clears terminal based on which operating system the game is running."""
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def animateCursor(self):
        pass

    def switchCursorLeft(self):
        pass

    def switchCursorRight(self):
        pass

    def placeStone(self):
        pass

    def showGrid(self):
        pass
    


game = Connect4Game()
game.playGame()