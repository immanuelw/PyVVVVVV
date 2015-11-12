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
import config as cf
import levels as lv
from img import imgs, img_dict

def env_create(GAMERECT, g, bg, char):
	g.rects = lv.rect_dict[char.x_co][char.y_co]
	entities = tuple(ent for ent in lv.ent_list[char.x_co][char.y_co])
	env = [GAMERECT, g, imgs[char.x_co][char.y_co], bg, (char,) + entities]

	return env

if __name__ == '__main__':
	pygame.init()
	clk = pygame.time.Clock()

	window = pygame.display.set_mode((cf.GAMERECT.width * 2, cf.GAMERECT.height * 2))
	gamesurf = pygame.Surface((cf.GAMERECT.width, cf.GAMERECT.height))
	backbuf = pygame.Surface((window.get_width(), window.get_height()))

	g = Geometry()
	char = Character(color=cf.VIRIDIAN_BASE, x=50, y=188, x_co=1, y_co=3, pulsation=cf.VIRIDIAN_PULSATION, pulse_rate=cf.VIRIDIAN_PULSERATE)
	bg = Background('./data/img/bg_cross.png', cf.GAMERECT, 1, 0)

	old_x = char.x_co
	old_y = char.y_co

	#location of last room
	last_x, last_y = (6, 1)

	stopper = 0
	cooldown = 0
	endgame = 0

	envi = Environment(*env_create(cf.GAMERECT, g, bg, char))

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
			envi = Environment(*env_create(cf.GAMERECT, g, bg, char))

		gamesurf.fill(cf.BLACK)
		g.debug_render(gamesurf)

		if (char.x_co, char.y_co) == (last_x, last_y): #placeholder for specifying rooms in which active
			stopper += 1

		#can do selective physics by making rules only apply to certain list:
		#	create array where char.x_co, char.y_co have value which says how physics works

		envi.update()
		envi.draw(gamesurf)
		pygame.transform.scale(gamesurf, (backbuf.get_width(), backbuf.get_height()), backbuf)
		window.blit(backbuf, (0, 0))
		pygame.display.update()

		#char.set_hit_wall(False)
		#char.set_hit_floor(False)
		#print(char.vx, char.vy)
		if stopper < 1:
			for ev in pygame.event.get():
				if ev.type == QUIT:
					pygame.mixer.music.stop()
					pygame.quit()
					sys.exit()
				elif ev.type == KEYDOWN:
					if ev.key == K_LEFT:
						char.set_left()
						char.set_go_left(True)
						char.set_hit_wall(False) #Allow logic to figure out whether or not a wall is hit
						#char.set_hit_floor(False)
					elif ev.key == K_RIGHT:
						char.set_right()
						char.set_go_right(True)
						char.set_hit_wall(False) #Allow logic to figure out whether or not a wall is hit
						#char.set_hit_floor(False)
					elif ev.key in (K_UP, K_DOWN, K_SPACE) and char.hitfloor:
						char.flip()
						#char.set_hit_wall(False)
						char.set_hit_floor(False) #Allow logic to figure out whether or not a floor is hit
					#elif ev.key==K_f:
					#	char.set_hit_floor(not char.hitfloor)
					#elif ev.key==K_w:
					#	char.set_hit_wall(not char.hitwall)
					elif ev.key == K_s:
						char.set_sad(True)
					elif ev.key == K_h:
						char.set_sad(False)
					elif ev.key == K_k:
						char.kill()
					elif ev.key == K_r:
						char.revive()
				elif ev.type == KEYUP:
					if ev.key == K_LEFT:
						char.set_go_left(False)
					elif ev.key == K_RIGHT:
						char.set_go_right(False)
		elif stopper == 1:
			char.set_go_right(True)
			char.set_hit_wall(False)
			pygame.mixer.music.load('./data/snd/bgm/05 - Path Complete.mp3')
			pygame.mixer.music.play(0, 0.0)
		elif stopper == 40:
			char.set_go_right(False)
		else:
			for ev in pygame.event.get():
				if ev.type == QUIT:
					pygame.quit()
					sys.exit()
			endgame += 1
			if endgame >= 360:
				pygame.quit()
				sys.exit()
		clk.tick(cf.FRAMERATE)
