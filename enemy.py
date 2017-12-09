import pygame
import math

class Akva():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_spd = 0
        self.y_spd = 0
        self.blit_Akva = pygame.image.load("art_assets/Akva.png")
        self.rect = pygame.Rect([self.x, self.y, 8, 16])

    def draw_akva(self, gameDisplay):
        self.rect = pygame.Rect([self.x, self.y, 8, 16])

        self.blit_Akva = pygame.image.load("art_assets/Akva.png")
        gameDisplay.blit(self.blit_Akva, self.rect)

    def jahib(self, player, map_data):
        tile_x = (self.x // TILESIZE) + 1
        tile_y = (self.y // TILESIZE) + 1


        possible_dirs = []

        try:
            if map_data[tile_y][tile_x - 1] == 0:
                possible_dirs.append(1)
        except:
            pass

        try:
            if map_data[tile_y - 1][tile_x] == 0:
                possible_dirs.append(2)
        except:
            pass

        try:
            if map_data[tile_y][tile_x + 1] == 0:
                possible_dirs.append(3)
        except:
            pass

        try:
            if map_data[tile_y + 1][tile_x] == 0:
                possible_dirs.append(4)
        except:
            pass

        if self.x > player.x and 1 in possible_dirs:
            self.x -= self.x_spd

        if self.x < player.x and 3 in possible_dirs:
            self.x += self.x_spd

        if self.y < player.y and 4 in possible_dirs:
            self.y += self.y_spd

        elif self.y > player.y and 2 in possible_dirs:
            self.y -= self.y_speed


        self.rect = pygame.Rect([self.x, self.y, TILESIZE, TILESIZE])


    """# find normalized direction vector (dx, dy) between enemy and player
        dx, dy = self.x - player.x, self.y - player.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist
        # liigub mööda vektorit ühtalse kiirusega
        self.x += dx * self.speed
        self.y += dy * self.speed """



# tilesize=11;20
# akvasize=8;16

##movement


"""def akva_move():
    if (playerself.x - self.x) < 0:
        self.x -= 1
        print("cyka")
    elif (playerself.x - self.x) > 0:
        self.x += 1


xya
xyb=
def kaugus():
    if (xya - xyb) <= 100:
        jooks()
    elif (xya - xyb) >= 100:
        rip()

    if rip() == True:
        gameExit = True"""