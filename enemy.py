import pygame


class Akva():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_spd = 0
        self.y_vel = 0
        self.blit_Akva = pygame.image.load("art_assets/Akva.png")
        self.rect = pygame.Rect([self.x, self.y, 8, 16])

    def draw_akva(self, gameDisplay):
        self.rect = pygame.Rect([self.x, self.y, 8, 16])

        self.blit_Akva = pygame.image.load("art_assets/Akva.png")
        gameDisplay.blit(self.blit_Akva, self.rect)

        #pass

# tilesize=11;20
# akvasize=8;16

##movement


"""def akva_move():
    if (playerself.x - self.x) < 0:
        self.x -= 1
        print("cyka")
    elif (playerself.x - self.x) > 0:
        self.x += 1"""


"""xya
xyb=
def kaugus():
    if (xya - xyb) <= 100:
        jooks()
    elif (xya - xyb) >= 100:
        rip()

    if rip() == True:
        gameExit = True"""