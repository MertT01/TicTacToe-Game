import pygame
from TicTacToe import button
from TicTacToe import draw
from TicTacToe import variables

pygame.display.set_caption("TicTacToe")

MainButton = button.Button(variables.pos, variables.slot)
MainDraw = draw.Draw((255, 255, 255), variables.x, variables.o)

def the_move():
    if variables.theBoard[variables.slot - 1] != None:
        return False
    else:
        return True

def is_game_over():
    for _ in range(0,9,3):
        if variables.theBoard[_] == variables.theBoard[_ + 1] == variables.theBoard[_ + 2] and variables.theBoard[_] != None:
            variables.gameIsEnd = True
            return True
    for _ in range(0,3,1):
        if variables.theBoard[_] == variables.theBoard[_ + 3] == variables.theBoard[_ + 6] and variables.theBoard[_] != None:
            variables.gameIsEnd = True
            return True
    if (variables.theBoard[0] == variables.theBoard[4] == variables.theBoard[8] and variables.theBoard[0] != None) or (variables.theBoard[2] == variables.theBoard[4] == variables.theBoard[6] and variables.theBoard[2] != None):
        variables.gameIsEnd = True
        return True
    elif variables.turn == 9 and variables.TicTacToe == True:
        variables.gameIsEnd = True
        return False
        
def restart():
    variables.win.fill((0, 0, 0))
    variables.theBoard = [None for _ in range(9)]
    variables.turn = 0
    variables.pos = [0, 0]
    variables.slot = 0
    variables.gameIsEnd = False
    variables.restartON = False

while variables.Menu:
    pygame.time.delay(10)

    MainDraw.menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            variables.Menu = False
            variables.TicTacToe = False
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                variables.pos = pygame.mouse.get_pos()
                MainButton.menu_buttons()

    pygame.display.update()

if variables.TicTacToe:
    variables.winWight = 890
    variables.winHeiht = 890
    variables.win = pygame.display.set_mode((variables.winWight, variables.winHeiht))
    variables.win.fill((0, 0, 0))
    pygame.display.update()


while variables.TicTacToe:
    pygame.time.delay(10)
    if variables.restartON == True:
        restart()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            variables.TicTacToe = False
        if (event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pressed()[0]):
                variables.pos = pygame.mouse.get_pos()
                MainButton.game_buttons()
                if the_move():
                    variables.turn += 1
                    if variables.turn % 2 == 1 and variables.slot > 0 and variables.turn < 10:
                        variables.theBoard[variables.slot - 1] = "x"
                    elif variables.turn % 2 == 0 and variables.slot > 0 and variables.turn < 10:
                        variables.theBoard[variables.slot - 1] = "o"
                    if variables.turn % 2 == 0 and is_game_over():
                        variables.win.fill((0, 0, 0))
                        MainDraw.won_draw("player two won the game!", (189, 67))
                        variables.won_time_o += 1
                    elif variables.turn % 2 == 1 and is_game_over():
                        variables.win.fill((0, 0, 0))
                        MainDraw.won_draw("player one won the game!", (189, 67))
                        variables.won_time_x += 1
                    elif is_game_over() == False and variables.turn == 9:
                        variables.win.fill((0, 0, 0))
                        MainDraw.won_draw("tie!", (319, 67))
                        variables.won_time_o += 0.5
                        variables.won_time_x += 0.5
    
    MainDraw.main_draw()
    MainDraw.characters_draw()
    
pygame.quit()
