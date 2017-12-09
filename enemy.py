import pygame


class Akva():
    def __init__(self, x, y, akva_pilt):
        self.x = x
        self.y = y
        self.x_spd = 0
        self.y_vel = 0
        self.icon = akva_pilt
        self.dead = false
        self.rect = pygame.Rect([self.x, self.y, (cellx - 3), (celly - 4)])
        self.dead = false

    def draw(self):
        pass

# tilesize=11;20
# akvasize=8;16



##movement




"""xya
xyb=
def kaugus():
    if (xya - xyb) <= 100:
        jooks()
    elif (xya - xyb) >= 100:
        rip()

    if rip() == True:
        gameExit = True"""