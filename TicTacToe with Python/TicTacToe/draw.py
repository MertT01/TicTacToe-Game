import pygame
from TicTacToe import variables

class Draw():
    def __init__(self,color, character1, character2):
        self.color = color
        self.character1 = character1
        self.character2 = character2

    def main_draw(self):
        pygame.draw.rect(variables.win, self.color, (135, 135, 5, 620))
        pygame.draw.rect(variables.win, self.color, (135, 135, 620, 5))
        pygame.draw.rect(variables.win, self.color, (340, 140, 5, 615))   
        pygame.draw.rect(variables.win, self.color, (545, 140, 5, 615))
        pygame.draw.rect(variables.win, self.color, (750, 140, 5, 615))
        pygame.draw.rect(variables.win, self.color, (140, 340, 615, 5))
        pygame.draw.rect(variables.win, self.color, (140, 545, 615, 5))
        pygame.draw.rect(variables.win, self.color, (140, 750, 615, 5))
        
        bar = variables.font2.render("X: {} O: {}".format(str(variables.won_time_x), str(variables.won_time_o)), True, (255, 255, 255))
        variables.win.blit(bar, (30, 800))

        restart = variables.font2.render("Restart", True, (255, 255, 255))
        variables.win.blit(restart, (387, 795))

        exit_b = variables.font2.render("Exit", True, (255, 255, 255))
        variables.win.blit(exit_b, (603, 795))

        pygame.draw.rect(variables.win, self.color, (380, 780, 120, 5))
        pygame.draw.rect(variables.win, self.color, (380, 780, 5, 70))
        pygame.draw.rect(variables.win, self.color, (380, 845, 120, 5))
        pygame.draw.rect(variables.win, self.color, (500, 780, 5, 70))

        pygame.draw.rect(variables.win, self.color, (595, 785, 70, 5))
        pygame.draw.rect(variables.win, self.color, (595, 785, 5, 55))
        pygame.draw.rect(variables.win, self.color, (595, 840, 70, 5))
        pygame.draw.rect(variables.win, self.color, (665, 785, 5, 60))
        pygame.display.update()
    
    def characters_draw(self):
        for _ in range(9):
            if variables.theBoard[_] == "x":
                variables.win.blit(self.character1, ((((_) % 3) * 200) + 135, (((_) // 3)*200) + 135))
            elif variables.theBoard[_] == "o":
                variables.win.blit(self.character2, ((((_) % 3) * 200) + 135, (((_) // 3)*200) + 135))
        pygame.display.update()

    def won_draw(self, won, cor):
        score = variables.font.render("The game resul is {} ".format(won), True, (255, 255, 255))
        variables.win.blit(score, cor)

    def menu(self):
        start = variables.font2.render("Start", True, (255, 255, 255))
        variables.win.blit(start, (170,145))

        exit_a = variables.font2.render("Exit", True, (255, 255, 255))
        variables.win.blit(exit_a, (177, 225))

        pygame.draw.rect(variables.win, self.color, (158, 136, 93, 5))
        pygame.draw.rect(variables.win, self.color, (158, 136, 5, 55))
        pygame.draw.rect(variables.win, self.color, (158, 191, 93, 5))
        pygame.draw.rect(variables.win, self.color, (251, 136, 5, 60))

        pygame.draw.rect(variables.win, self.color, (169, 215, 70, 5))
        pygame.draw.rect(variables.win, self.color, (169, 215, 5, 55))
        pygame.draw.rect(variables.win, self.color, (169, 270, 70, 5))
        pygame.draw.rect(variables.win, self.color, (239, 215, 5, 60))
