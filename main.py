import os
import platform
import time
import random

class Connect4Game:
    game_grid = []
    cursor_position = 5

    def __init__(self):
        self.game_grid = [
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "]]


    def playGame(self):
        end_of_the_game = False
        self.showStartingInfo()
        self.showGrid()
        while end_of_the_game == False:
            continue

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
        horizontal_size = len(self.game_grid[1]) * 2 + 1
        vertical_size = len(self.game_grid) + 2            

        for i in range(vertical_size):
            if i == 0:
                self.printFirstLine(horizontal_size)
            elif i == vertical_size - 1:
                print("@" * (horizontal_size))
            else:
                grid_row = i - 1
                print("@", end="")
                for j in range(len(self.game_grid[grid_row])):
                    if j == len(self.game_grid[grid_row]) - 1:
                        print(self.game_grid[grid_row][j] + "@", end="\n")
                    else:
                        print(self.game_grid[grid_row][j] + "|", end="")
    
    def printFirstLine(self, horizontal_size):
        cursor_i = 2 * self.cursor_position + 1
        for i in range(horizontal_size):
            if i == 0:
                print("@", end="")
            elif i == horizontal_size - 1:
                print("@", end="\n")
            elif i == cursor_i:
                print("$", end="")
            else:
                print(" ", end="")
        
        

game = Connect4Game()
game.playGame()