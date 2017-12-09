import pygame
from random import randint


class Audio():
	def __init__(self) -> object:
		pygame.mixer.pre_init(44100, 16, 2, 4096)
		pygame.mixer.init()
		self.bg_sound = pygame.mixer.music.load("audiofiles/soundtrack.mp3")

	def play_background(self):  # Background music
		pygame.mixer.music.play(-1)
	# self.bg_sound.play(-1)