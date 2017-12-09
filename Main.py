import pygame
from map import *
import player
import audio
from constants import *


gameExit = False

pygame.display.set_caption("Ööjooksu simulaator")
gameDisplay = pygame.display.set_mode((windowX,windowY))
jooksja = player.Jooksja(100,100)
kaart = Map(map,gameDisplay)
if __name__ == '__main__':

	pygame.init()
	clock = pygame.time.Clock()
	audio_manager = audio.Audio()
	audio_manager.play_background()

	while not gameExit:
		kaart.draw_map()
		jooksja.draw_player(gameDisplay)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				gameExit = True
		pygame.display.update()



pygame.quit()
quit()