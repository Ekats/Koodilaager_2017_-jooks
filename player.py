import pygame



pygame.init()

class Jooksja():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rectangle = pygame.Rect([self.x, self.y, 25, 25])

        self.blit_Jooksja = pygame.image.load("art_assets/Jooksja.png")

    def draw_player(self, gameDisplay):
        gameDisplay.blit(self.blit_Jooksja, self.rectangle)

#class Player:
#    def __init__(self):

