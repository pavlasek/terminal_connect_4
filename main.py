import os
import platform
import random
import sys
import tty
import termios
import time
import select


class Connect4Game:
    game_grid = []
    cursor_position = 5
    cursor_symbol = "$"
    first_player = "X"
    second_player = "O"

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
        self.showGrid(self.cursor_symbol)
        while end_of_the_game == False:
            key = self.waitForInput()
            #self.game_move(key)
            winning_player = self.checkWinner()
            if winning_player == None:
                continue
            else:
                end_of_the_game = True
                self.showFinalInfo(winning_player)

    def waitForInput(self):
        key_pressed = False
        while key_pressed == False:
            key = self.get_key()
            
            if key == None:
                continue

            print(f"You pressed: {key}")
            if key == 'q':
                exit()



    def get_key(self):
        """Reads the key from the terminal."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key_start = sys.stdin.read(1)

            if key_start == '\x1b':  
                key_end = key_start + sys.stdin.read(2)

                if key_end == '\x1b[B':
                    return 'DOWN'
                elif key_end == '\x1b[C':  
                    return 'RIGHT'
                elif key_end == '\x1b[D':
                    return 'LEFT'

            else:
                if key_start in {'q', 'a', 's', 'd'}:
                    return key_start

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) 


    def showStartingInfo(self):
        """Prints information at the start of the game. Prints instruction
        and how to play the game."""

        print("--------------------------------------------------------------------------------------------")     
        print("Welcome to the Connect 4 Game!")
        print("--------------------------------------------------------------------------------------------\n")
        print("How to play: ")
        print(" + Players takes turns to inserts stones into grid using.")
        print(" + Switch between columns using LEFT and RIGHT arrow and put the stone using the DOWN arrow.")
        print(" + # symbol shows in which column the stone will be placed.")
        print(" + Second player uses A, D and S keys.")
        print(" + Player who connects 4 in row, column or diagonally wins.")
        print("\n--------------------------------------------------------------------------------------------\n")

    def checkWinner(self):
        pass

    def showFinalInfo(self, winning_player):
        """Prints information at the end of the game."""
        if winning_player == 0:
            print("--------------------------------------------------------------------------------------------")
            print("IT IS A DRAW!")
        elif winning_player == 1:
            print("--------------------------------------------------------------------------------------------")
            print("PLAYER1 WINS!")
        elif(winning_player == 2):
            print("--------------------------------------------------------------------------------------------")
            print("PLAYER2 WINS!")
        

    def clearTerminal(self):
        """Clears terminal based on which operating system the game is running."""
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def switchCursorLeft(self):
        pass

    def switchCursorRight(self):
        pass

    def placeStone(self):
        pass

    def showGrid(self, cursor_symbol):
        horizontal_size = len(self.game_grid[1]) * 2 + 1
        vertical_size = len(self.game_grid) + 2            

        for i in range(vertical_size):
            if i == 0:
                self.printFirstLine(horizontal_size, cursor_symbol)
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
    
    def printFirstLine(self, horizontal_size, cursor_symbol):
        cursor_i = 2 * self.cursor_position + 1
        for i in range(horizontal_size):
            if i == 0:
                print("@", end="")
            elif i == horizontal_size - 1:
                print("@", end="\n")
            elif i == cursor_i:
                print(cursor_symbol, end="")
            else:
                print(" ", end="")
        
        

game = Connect4Game()
game.playGame()