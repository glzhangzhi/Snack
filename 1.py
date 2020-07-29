import pygame
import sys
import random
import time
from pygame.locals import *
import copy

pygame.init()
WIDTH = 400
HEIGH = 400
DISPLAY = pygame.display.set_mode((WIDTH, HEIGH))
pygame.display.set_caption('Snack for AI')
FPSCLOCK = pygame.time.Clock()
BASICFONT = pygame.font.SysFont('SIMYOU.TFF', 80)

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREY = pygame.Color(150, 150, 150)


class Snack():
	def __init__(self):
		self.body = [[200, 80], [200, 60], [200, 40]]
		self.direction = 'd'

	def draw(self):
		for i in self.body:
			pygame.draw.rect(DISPLAY, WHITE, Rect(i[0], i[1], 19, 19))

	def up(self):
		temp = copy.deepcopy(self.body[0])
		temp[1] -= 20
		self.body.insert(0, temp)

	def down(self):
		temp = copy.deepcopy(self.body[0])
		temp[1] += 20
		self.body.insert(0, temp)

	def left(self):
		temp = copy.deepcopy(self.body[0])
		temp[0] -= 20
		self.body.insert(0, temp)

	def right(self):
		temp = copy.deepcopy(self.body[0])
		temp[0] += 20
		self.body.insert(0, temp)


class Food():
	def __init__(self):
		self.position = [100, 100]

	def grow(self, snack):
		while True:
			x = random.randrange(1, 20) * 20
			y = random.randrange(1, 20) * 20
			if not([x, y] in snack.body):
				break
		self.position[0] = x
		self.position[1] = y

	def draw(self):
		pygame.draw.rect(DISPLAY, RED, Rect(self.position[0], self.position[1], 20, 20))


def GameOver():
	GameOver_Surf = BASICFONT.render('Game Over', True, GREY)
	GameOver_Rect = GameOver_Surf.get_rect()
	GameOver_Rect.midtop = (200, 10)
	DISPLAY.blit(GameOver_Surf, GameOver_Rect)

	pygame.display.flip()
	time.sleep(1)
	pygame.quit()
	sys.exit()


def main():
	food = Food()
	snack = Snack()
	while True:

		if snack.body[0][0] < 0 or snack.body[0][0] > 380 or snack.body[0][1] < 0 or snack.body[0][1] > 380:
			GameOver()
		if snack.body[0] in snack.body[1:]:
			GameOver()

		DISPLAY.fill(BLACK)
		snack.draw()
		food.draw()
		pygame.display.flip()
		FPSCLOCK.tick(7)	

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if (event.key == K_UP) and snack.direction != 'd':
					snack.direction = 'u'
				if (event.key == K_DOWN) and snack.direction != 'u':
					snack.direction = 'd'
				if (event.key == K_LEFT) and snack.direction != 'r':
					snack.direction = 'l'
				if (event.key == K_RIGHT) and snack.direction != 'l':
					snack.direction = 'r'

		if snack.direction == 'l':
			snack.left()
		elif snack.direction == 'r':
			snack.right()
		elif snack.direction == 'u':
			snack.up()
		else:
			snack.down()

		if food.position == snack.body[0]:
			food.grow(snack)
		else:
			snack.body.pop()
		print(snack.body[0])



if __name__ == '__main__':
	main()