import os
import platform
import sys
import tty
import termios

class Connect4Game:
    game_grid = []
    cursor_position = 0
    first_player = "X"
    second_player = "O"
    cursor_symbol = first_player


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
        current_player = self.first_player

        while end_of_the_game == False:
            
            self.cursor_symbol = current_player

            while True:
                key = self.waitForInput()
                if key in ['a', 'd', 'LEFT', 'RIGHT']:
                    self.gameMove(key)
                elif key in ['s', 'DOWN']:

                    valid_stone_move = self.placeStone(current_player)
                    if valid_stone_move == True:
                        self.showStartingInfo()
                        current_player = self.switchPlayer(current_player)
                        self.cursor_symbol = current_player
                        self.showGrid(self.cursor_symbol)
                        break
                    else:
                        self.showStartingInfo()
                        self.showGrid(self.cursor_symbol)


            winning_player = self.checkWinner()
            if winning_player == None:
                continue
            else:
                end_of_the_game = True
                self.showFinalInfo(winning_player)
                break

            
    def switchPlayer(self, current_player):
        if current_player == "X":
            current_player = "O"
        elif current_player == "O":
            current_player = "X"
        return current_player

    def gameMove(self, key):
        match key:
            case 'a':
                self.switchCursorLeft()
            case 'd':
                self.switchCursorRight()
            case 'LEFT':
                self.switchCursorLeft()
            case 'RIGHT':
                self.switchCursorRight()

    def placeStone(self, current_player):
        self.clearTerminal()
        self.cursor_symbol = current_player

        if self.game_grid[0][self.cursor_position] == ' ':
            self.placeStoneToCol(self.cursor_position, current_player)
            return True
        else:
            return False


        
    
    def placeStoneToCol(self, cursor_position, current_player):
        for i in range(len(self.game_grid)):
            if self.game_grid[len(self.game_grid) - 1 - i][cursor_position] == ' ':
                self.game_grid[len(self.game_grid) - 1 - i][cursor_position] = current_player
                break


    def waitForInput(self):
        key_pressed = False
        while key_pressed == False:
            key = self.get_key()
            
            if key == None:
                continue
            elif key == 'q':
                exit()
            else:
                return key

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
        #check colums
        for i in range(len(self.game_grid[0])):
            winning_symbol = ' '
            counter = 0
            for j in range(len(self.game_grid)):
                if j == 0:
                    if ((self.game_grid[len(self.game_grid) - j - 1][i] == ' ')):
                        break
                    else:
                        winning_symbol = self.game_grid[len(self.game_grid) - j - 1][i]
                        counter = 1
                else:
                    if self.game_grid[len(self.game_grid) - j - 1][i] == winning_symbol:
                        counter += 1
                    else:
                        winning_symbol = self.game_grid[len(self.game_grid) - j - 1][i]
                        if winning_symbol == ' ':
                            counter = 0
                            break
                        else:
                            counter = 1

                if counter == 4:
                    return winning_symbol
        
        #check rows
        for i in range(len(self.game_grid)):
            winning_symbol = ' '
            counter = 0
            for j in range(len(self.game_grid[i])):
                
                if winning_symbol == self.game_grid[i][j]:
                    counter += 1
                else:
                    winning_symbol = self.game_grid[i][j]
                    counter = 1

                if counter == 4 and (winning_symbol == 'X' or winning_symbol == 'O'):
                    return winning_symbol
                
                
                

    def showFinalInfo(self, winning_player):
        """Prints information at the end of the game."""
        if winning_player == 0:
            print("--------------------------------------------------------------------------------------------")
            print("IT IS A DRAW!")
        elif winning_player == 'X':
            print("--------------------------------------------------------------------------------------------")
            print("PLAYER1 WINS!")
        elif(winning_player == 'O'):
            print("--------------------------------------------------------------------------------------------")
            print("PLAYER2 WINS!")
        

    def clearTerminal(self):
        """Clears terminal based on which operating system the game is running."""
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def switchCursorLeft(self):
        self.cursor_position = max(0, self.cursor_position - 1)
        self.clearTerminal()
        self.showStartingInfo()
        self.showGrid(self.cursor_symbol)

    def switchCursorRight(self):
        self.cursor_position = min(self.cursor_position + 1, len(self.game_grid[0]) - 1)
        self.clearTerminal()
        self.showStartingInfo()
        self.showGrid(self.cursor_symbol)

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