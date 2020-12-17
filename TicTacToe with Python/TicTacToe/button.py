import pygame
from TicTacToe import variables

class Button():
    def __init__(self, pos, slot):
        self.pos = pos
        self.slot = slot

    def game_buttons(self):
        if not variables.gameIsEnd:
            for _ in range(9):
                if ((205*(_%3))+340 > variables.pos[0] > (205*(_%3))+140) and ((205*(_//3))+340 > variables.pos[1] > (205*(_//3))+140):
                    variables.slot = _ + 1
                    break
                elif(_==8):
                    variables.slot = 0
                    variables.turn -= 1
        elif (500 > variables.pos[0] > 385) and (845 > variables.pos[1] > 785):
            variables.restartON = True
        elif (665 > variables.pos[0] > 615) and (840 > variables.pos[1] > 790):
            variables.TicTacToe = False

    def menu_buttons(self):
        if (variables.pos[0] > 163 and variables.pos[0] < 250) and (variables.pos[1] > 140 and variables.pos[1] < 190):
            variables.Menu = False
        elif (variables.pos[0] > 175 and variables.pos[0] < 240) and (variables.pos[1] > 220 and variables.pos[1] < 270):
            variables.Menu = False
            variables.TicTacToe = False
