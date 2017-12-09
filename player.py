import pygame

<<<<<<< HEAD

pygame.init()

class Jooksja():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rectangle = pygame.Rect([self.x, self.y, 100, 100])

        self.blit_Jooksja = pygame.image.load("art_assets/Jooksja.png")

    def draw_player(self, gameDisplay):
        gameDisplay.blit(self.blit_Jooksja, self.rectangle)
=======
#class Player:
#    def __init__(self):
>>>>>>> 86b14bc08b21fb1a993db6a0416f8b9b4b9d26d9
