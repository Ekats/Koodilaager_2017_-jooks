import pygame
from constants import *
<<<<<<< HEAD
gameDisplay = pygame.display.set_mode((windowX, windowY))
class Map():
    def __init__(self,map,gameDisplay):
        self.map = map


    def draw_map(self):
        self.thing = map.split('\n')
        if self.thing[0] == '':
            del self.thing[0]
        if self.thing[-1] == '':
            del self.thing[-1]
        celly = int(windowY / len(self.thing))
        cellx = int(windowX / len(self.thing[0]))
        for i in range(len(self.thing)):
            for j in range(len(self.thing[0])):
                if self.thing[i][j] == 'X':
                    pygame.draw.rect(gameDisplay, (255, 255, 255), (j*cellx, i*celly, cellx, celly))
                elif self.thing[i][j] == 'O':
                    pygame.draw.rect(gameDisplay, (218,165,32), (j * cellx, i * celly, cellx, celly))
                elif self.thing[i][j] == 'D':
                    pygame.draw.rect(gameDisplay, (165,42,42), (j * cellx, i * celly, cellx, celly))
                elif self.thing[i][j] == '/':
                    pygame.draw.rect(gameDisplay, (112, 128, 144), (j * cellx, i * celly, cellx, celly))
                elif self.thing[i][j] == 'T':
                    pygame.draw.rect(gameDisplay, (210, 180, 140), (j * cellx, i * celly, cellx, celly))
                elif self.thing[i][j] == 'C':
                    pygame.draw.rect(gameDisplay, (188,143,143), (j * cellx, i * celly, cellx, celly))
                elif self.thing[i][j] == 'G':
                    pygame.draw.rect(gameDisplay, (0, 255, 0), (j * cellx, i * celly, cellx, celly))
                elif self.thing[i][j] == 'R':
                    pygame.draw.rect(gameDisplay, (128, 128, 128), (j * cellx, i * celly, cellx, celly))
=======
pygame.init()
gameDisplay = pygame.display.set_mode([windowX, windowY])
bad = []
def draw_map():
    for i in range(len(thing)):
        for j in range(len(thing[0])):
            if thing[i][j] == 'X':
                pygame.draw.rect(gameDisplay, (255, 255, 255), (j*cellx, i*celly, cellx, celly))
                bad.append(j*cellx)
                bad.append(i*celly)
                bad.append(j*cellx + cellx)
                bad.append(i*celly + celly)
            elif thing[i][j] == 'O':
                pygame.draw.rect(gameDisplay, (218,165,32), (j * cellx, i * celly, cellx, celly))
            elif thing[i][j] == 'D':
                pygame.draw.rect(gameDisplay, (165,42,42), (j * cellx, i * celly, cellx, celly))
            elif thing[i][j] == '/':
                pygame.draw.rect(gameDisplay, (112, 128, 144), (j * cellx, i * celly, cellx, celly))
            elif thing[i][j] == 'T':
                pygame.draw.rect(gameDisplay, (210, 180, 140), (j * cellx, i * celly, cellx, celly))
            elif thing[i][j] == 'C':
                pygame.draw.rect(gameDisplay, (188,143,143), (j * cellx, i * celly, cellx, celly))
            elif thing[i][j] == 'G':
                pygame.draw.rect(gameDisplay, (0, 255, 0), (j * cellx, i * celly, cellx, celly))
            elif thing[i][j] == 'R':
                pygame.draw.rect(gameDisplay, (128, 128, 128), (j * cellx, i * celly, cellx, celly))
    pygame.display.update()
>>>>>>> 86b14bc08b21fb1a993db6a0416f8b9b4b9d26d9
