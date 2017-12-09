import pygame
from constants import *
pygame.init()
gameDisplay = pygame.display.set_mode([windowX, windowY])
def draw_map():
    for i in range(len(thing)):
        for j in range(len(thing[0])):
            if thing[i][j] == 'X':
                pygame.draw.rect(gameDisplay, (255, 255, 255), (j*cellx, i*celly, cellx, celly))
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
