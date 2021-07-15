import pygame
import sys
import random
from win32api import GetSystemMetrics
import os
import time
import keyboard

os.environ['SDL_VIDEO_CENTERED'] = '1' # Centers window

class Constants:
	WIDTH = GetSystemMetrics(0)
	HEIGHT = GetSystemMetrics(1)

	BUZZING = "assets/buzzing.mp3"
	BACKROOMS_IMG = pygame.transform.scale(pygame.image.load("assets/backrooms.jpg"), (WIDTH, HEIGHT))
	REC_IMG = pygame.transform.scale(pygame.image.load("assets/rec.png"), (WIDTH, HEIGHT))
	REC2_IMG = pygame.transform.scale(pygame.image.load("assets/rec2.png"), (WIDTH, HEIGHT))

pygame.init()
win = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT), pygame.NOFRAME) # No frame with screen resolution as window size

pygame.mixer.music.load(Constants.BUZZING) # Load infinite buzzing sound
pygame.mixer.music.play(-1) # Play forever

draw_counter = 0

def draw_screen():
	global draw_counter

	win.blit(Constants.BACKROOMS_IMG, (0,0))

	if draw_counter == 0:
		win.blit(Constants.REC_IMG, (0,0))
		draw_counter = 1
	elif draw_counter:
		win.blit(Constants.REC2_IMG, (0,0))
		draw_counter = 0

	time.sleep(1.5)

	pygame.display.flip()

while True:
	if keyboard.is_pressed("q"):
		pygame.quit()
		sys.exit()

	draw_screen()
