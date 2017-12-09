import pygame
import map
import player
import audio



windowX = 800
windowY = 600
gameDisplay = pygame.display.set_mode((windowX,windowY))

gameExit = False

pygame.display.set_caption("Ööjooksu simulaator")

if __name__ == '__main__':
	pygame.init()
	clock = pygame.time.Clock()
	audio_manager = audio.Audio()
	#audio_manager.play_background()

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				gameExit = True
		gameDisplay.fill((0, 0, 0))
		pygame.display.update()

pygame.quit()
quit()