#Plays a bit of music...

import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('test.wav')
pygame.mixer.music.play(0)
