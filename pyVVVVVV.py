#Testing the entire Environment
from __future__ import print_function
import sys
import random
import pygame
from pygame.locals import *
from character import Character
from geom import Geometry
from bg import Background
from env import Environment
from entity import Entity, MovingEntity, AnimatingEntity, MovingAnimatingEntity
from config import *
from levels import *

def env_create(x_co, y_co):
	g.rects = rect_dict[x_co][y_co]
	entities = tuple(ent for ent in ent_list[x_co][y_co])
	env = [GAMERECT, g, imgs[x_co][y_co], bg, (char,) + entities]

	return env

if __name__ == '__main__':
	pygame.init()
	clk = pygame.time.Clock()

	window = pygame.display.set_mode((GAMERECT.width * 2, GAMERECT.height * 2))
	gamesurf = pygame.Surface((GAMERECT.width, GAMERECT.height))
	backbuf = pygame.Surface((window.get_width(), window.get_height()))

	g = Geometry()
	char = Character(VIRIDIAN_BASE)
	char.SetPulsation(VIRIDIAN_PULSATION)
	char.SetPulseRate(VIRIDIAN_PULSERATE)
	char.SetSpike(50, 188)
	#char.SetSpike(90, 50)
	char.x_co = 1
	char.y_co = 3

	g = Geometry()

	old_x = char.x_co
	old_y = char.y_co

	#location of last room
	last_x = 6
	last_y = 1

	stopper = 0
	cooldown = 0
	endgame = 0

	envi = Environment(*env_create(char.x_co, char.y_co))

	if random.randint(0, 1) == 0:
		pygame.mixer.music.load('./data/snd/bgm/07 - Positive Force.mp3')
	else:
		pygame.mixer.music.load('./data/snd/bgm/10 - Potential for Anything.mp3')

	pygame.mixer.music.play(-1, 0.0)

	#title of game
	pygame.display.set_caption('VVVVVV')

	while True:
		#switches environments upon moving screens, NEEDS CHECKPOINT FIXING?
		if old_x != char.x_co or old_y != char.y_co:
			#print('changed screen to', char.x_co, '-', char.y_co)
			old_x = char.x_co
			old_y = char.y_co
			envi = Environment(*env_create(char.x_co, char.y_co))

		gamesurf.fill(BLACK)
		g.DebugRender(gamesurf)

		if (char.x_co == last_x) and (char.y_co == last_y): #placeholder for specifying rooms in which active
			stopper += 1

		#can do selective physics by making rules only apply to certain list:
		#	create array where char.x_co, char.y_co have value which says how physics works

		envi.update()
		envi.draw(gamesurf)
		pygame.transform.scale(gamesurf, (backbuf.get_width(), backbuf.get_height()), backbuf)
		window.blit(backbuf, (0, 0))
		pygame.display.update()

		#char.SetHitWall(False)
		#char.SetHitFloor(False)
		#print(char.vx, char.vy)
		if stopper < 1:
			for ev in pygame.event.get():
				if ev.type == QUIT:
					#print(eval('env_%d_%d()' %(char.x_co, char.y_co))[1])
					pygame.mixer.music.stop()
					pygame.quit()
					sys.exit()
				elif ev.type == KEYDOWN:
					if ev.key == K_LEFT:
						char.SetLeft()
						char.SetGoLeft(True)
						char.SetHitWall(False) #Allow logic to figure out whether or not a wall is hit
						#char.SetHitFloor(False)
					elif ev.key == K_RIGHT:
						char.SetRight()
						char.SetGoRight(True)
						char.SetHitWall(False) #Allow logic to figure out whether or not a wall is hit
						#char.SetHitFloor(False)
					elif ev.key in (K_UP, K_DOWN, K_SPACE) and char.hitfloor:
						char.Flip()
						#char.SetHitWall(False)
						char.SetHitFloor(False) #Allow logic to figure out whether or not a floor is hit
					#elif ev.key==K_f:
					#	char.SetHitFloor(not char.hitfloor)
					#elif ev.key==K_w:
					#	char.SetHitWall(not char.hitwall)
					elif ev.key == K_s:
						char.SetSad(True)
					elif ev.key == K_h:
						char.SetSad(False)
					elif ev.key == K_k:
						char.Kill()
					elif ev.key == K_r:
						char.Revive()
				elif ev.type == KEYUP:
					if ev.key == K_LEFT:
						char.SetGoLeft(False)
					elif ev.key == K_RIGHT:
						char.SetGoRight(False)
		elif stopper == 1:
			char.SetGoRight(True)
			char.SetHitWall(False)
			pygame.mixer.music.load('./data/snd/bgm/05 - Path Complete.mp3')
			pygame.mixer.music.play(0, 0.0)
		elif stopper == 40:
			char.SetGoRight(False)
		else:
			for ev in pygame.event.get():
				if ev.type == QUIT:
					pygame.quit()
					sys.exit()
			endgame += 1
			if endgame >= 360:
				pygame.quit()
				sys.exit()
		clk.tick(FRAMERATE)
