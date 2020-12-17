import pygame

pygame.init()

winHeiht = 400
winWight = 400

win = pygame.display.set_mode((winWight, winHeiht))
TicTacToe = True
Menu = True

turn = 0

theBoard = [None for _ in range(9)]

x = pygame.image.load('TicTacToe/Imgs/x.png')
o = pygame.image.load('TicTacToe/Imgs/o.png')

font = pygame.font.Font("TicTacToe/Font/FreeSansBold.ttf", 24)
font2 = pygame.font.Font("TicTacToe/Font/FreeSansBold.ttf", 32)

pos = [0, 0]
slot = 0

won_time_x = 0
won_time_o = 0

gameIsEnd = False

restartON = False
