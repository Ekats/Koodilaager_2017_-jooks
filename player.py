import pygame



pygame.init()

class Jooksja():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rectangle = pygame.Rect([self.x, self.y, 25, 25])

        self.blit_Jooksja = pygame.image.load("art_assets/Jooksja.png")

    def draw_player(self, gameDisplay):
        self.rectangle = pygame.Rect([self.x, self.y, 25, 25])

        self.blit_Jooksja = pygame.image.load("art_assets/Jooksja.png")
        gameDisplay.blit(self.blit_Jooksja, self.rectangle)

    def move(self, direction):
        if direction == 'up':
            self.y -= 1
        elif direction == 'down':
            self.y += 1
        elif direction == 'left':
            self.x -= 1
        elif direction == 'right':
            self.x += 1
#class Player:
#    def __init__(playerself):

