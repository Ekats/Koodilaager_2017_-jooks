import pygame
from map import *
import player
import enemy
import audio
from constants import *


gameExit = False

pygame.display.set_caption("Ööjooksu simulaator")
gameDisplay = pygame.display.set_mode((windowX,windowY))
jooksja = player.Jooksja(100,100)
akva = enemy.Akva(100,200)
kaart = Map(map,gameDisplay)
if __name__ == '__main__':

	pygame.init()
	clock = pygame.time.Clock()
	audio_manager = audio.Audio()
	audio_manager.play_background()

	while not gameExit:
		kaart.draw_map()
		jooksja.draw_player(gameDisplay)
		akva.draw_akva(gameDisplay)
		try:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					gameExit = True
				elif event.key == pygame.K_w:
					jooksja.move('up')
				elif event.key == pygame.K_s:
					jooksja.move('down')
				elif event.key == pygame.K_a:
					jooksja.move('left')
				elif event.key == pygame.K_d:
					jooksja.move('right')
			pygame.display.update()
		except:
			import pygame



pygame.quit()
quit()