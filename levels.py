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

imgs = {x_coord: {y_coord: pygame.image.load('./data/img/background/background_{x}-{y}_320x240.png'.format(x=x_coord, y=y_coord))\
					for y_coord in range(7) if (x_coord, y_coord) in level_array} for x_coord in range(7)}

window = pygame.display.set_mode((GAMERECT.width * 2, GAMERECT.height * 2))
gamesurf = pygame.Surface((GAMERECT.width, GAMERECT.height))
backbuf = pygame.Surface((window.get_width(), window.get_height()))

char = Character(VIRIDIAN_BASE)
char.SetPulsation(VIRIDIAN_PULSATION)
char.SetPulseRate(VIRIDIAN_PULSERATE)

g = Geometry()

bgimg = pygame.image.load('./data/img/bg_cross.png')
bg = Background(bgimg, GAMERECT, 1, 0)

platimg = pygame.image.load('./data/img/plat_o.png')
plat1 = MovingEntity(platimg, dx=100, dy=70, vx=0, vy=0, etype=ENT_PLATFORM)
plat2 = MovingEntity(platimg, dx=120, dy=70, vx=0, vy=0, etype=ENT_PLATFORM)
plat3 = MovingEntity(platimg, dx=200, dy=116, vx=0, vy=0, etype=ENT_PLATFORM)
plat4 = MovingEntity(platimg, dx=150, dy=52, vx=0, vy=0, etype=ENT_PLATFORM)
plat5 = MovingEntity(platimg, dx=132, dy=88, vx=0, vy=0, etype=ENT_PLATFORM)

platv1 = MovingEntity(platimg, dx=140, dy=100, vx=0, vy=1, etype=ENT_PLATFORM)
platv2 = MovingEntity(platimg, dx=170, dy=120, vx=0, vy=1, etype=ENT_PLATFORM)
platv3 = MovingEntity(platimg, dx=200, dy=140, vx=0, vy=1, etype=ENT_PLATFORM)

plath1 = MovingEntity(platimg, dx=52, dy=166, vx=1, vy=0, etype=ENT_PLATFORM)

spriteimg = pygame.image.load('./data/img/sprite1.png')
sprite = MovingEntity(spriteimg, vx=1, vy=1, etype=ENT_OBSTACLE)

checkpointimg1 = pygame.image.load('./data/img/checkpointBW.png')
checkpointimgU = pygame.image.load('./data/img/checkpointUBW.png')
checkpointimg2 = pygame.image.load('./data/img/checkpoint.png')

checkpoint1 = MovingEntity(checkpointimg1, dx=64, dy=108, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpoint2 = MovingEntity(checkpointimg1, dx=284, dy=220, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpoint3 = MovingEntity(checkpointimg1, dx=288, dy=204, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpoint4 = MovingEntity(checkpointimg1, dx=64, dy=108, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpoint5 = MovingEntity(checkpointimg1, dx=60, dy=124, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpoint6 = MovingEntity(checkpointimg1, dx=280, dy=220, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpoint7 = MovingEntity(checkpointimg1, dx=122, dy=124, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpoint8 = MovingEntity(checkpointimg1, dx=12, dy=204, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpoint9 = MovingEntity(checkpointimg1, dx=152, dy=108, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointA = MovingEntity(checkpointimg1, dx=32, dy=204, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointB = MovingEntity(checkpointimg1, dx=198, dy=180, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointC = MovingEntity(checkpointimg1, dx=110, dy=188, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointD = MovingEntity(checkpointimg1, dx=52, dy=204, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointE = MovingEntity(checkpointimg1, dx=152, dy=108, vx=0, vy=0, etype=ENT_CHECKPOINT)

checkpointU1 = MovingEntity(checkpointimgU, dx=64, dy=164, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointU2 = MovingEntity(checkpointimgU, dx=52, dy=148, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointU3 = MovingEntity(checkpointimgU, dx=202, dy=68, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointU4 = MovingEntity(checkpointimgU, dx=24, dy=52, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointU5 = MovingEntity(checkpointimgU, dx=280, dy=52, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointU6 = MovingEntity(checkpointimgU, dx=186, dy=212, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointU7 = MovingEntity(checkpointimgU, dx=38, dy=84, vx=0, vy=0, etype=ENT_CHECKPOINT)

trinketimg = pygame.image.load('./data/img/sprites/sprite_trinket.png')
trinket = MovingEntity(trinketimg, dx=270, dy=172, vx=0, vy=0, etype=ENT_TOKEN)
trinket2 = MovingEntity(trinketimg, dx=40, dy=140, vx=0, vy=0, etype=ENT_TOKEN)

portalimg = pygame.image.load('./data/img/warptoken.bmp')
portal = MovingEntity(portalimg, vx=0, vy=0, etype=ENT_PORTAL)
portalimg2 = pygame.image.load('./data/img/warptoken2.bmp')
portal2 = MovingEntity(portalimg2, vx=0, vy=0, etype=ENT_PORTAL)

emptyimg = pygame.image.load('./data/img/background/tiles/tile_maker.png')
empty = MovingEntity(emptyimg, vx=0, vy=0, etype=ENT_EMPTY)

busimg = pygame.image.load('./data/img/sprites/sprite_BUS_3.png')
bus = MovingEntity(busimg, dx=320, dy=60, vx=1, vy=0, etype=ENT_OBSTACLE)

greenimg = pygame.image.load('./data/img/sprites/sprite_green_1.png')
green1 = MovingEntity(greenimg, dx=84, dy=110, vx=1.5, vy=0, etype=ENT_OBSTACLE)
green2 = MovingEntity(greenimg, dx=124, dy=150, vx=1.5, vy=0, etype=ENT_OBSTACLE)

reddiscimg = pygame.image.load('./data/img/sprites/sprite_reddisc_1.png')
reddisc = MovingEntity(reddiscimg, dx=184, dy=188, vx=0, vy=1, etype=ENT_OBSTACLE)

stopimg = pygame.image.load('./data/img/sprites/sprite_STOP_2.png')
stop1 = MovingEntity(stopimg, dx=192, dy=166, vx=0, vy=1.5, etype=ENT_OBSTACLE)
stop2 = MovingEntity(stopimg, dx=42, dy=166, vx=0, vy=1.5, etype=ENT_OBSTACLE)
stop3 = MovingEntity(stopimg, dx=118, dy=50, vx=0, vy=1, etype=ENT_OBSTACLE)

walkerimg = pygame.image.load('./data/img/sprites/sprite_walker_2.png')
walker1 = MovingEntity(walkerimg, dx=272, dy=204, vx=1.5, vy=0, etype=ENT_OBSTACLE)
walker2 = MovingEntity(walkerimg, dx=284, dy=92, vx=1.5, vy=0, etype=ENT_OBSTACLE)

yesimg = pygame.image.load('./data/img/sprites/sprite_YES_2.png')
yes1 = MovingEntity(yesimg, dx=132, dy=52, vx=0, vy=1, etype=ENT_OBSTACLE)
yes2 = MovingEntity(yesimg, dx=264, dy=52, vx=0, vy=1, etype=ENT_OBSTACLE)
yes3 = MovingEntity(yesimg, dx=182, dy=112, vx=0, vy=1, etype=ENT_OBSTACLE)
yes4 = MovingEntity(yesimg, dx=132, dy=224, vx=0, vy=1, etype=ENT_OBSTACLE)
yes5 = MovingEntity(yesimg, dx=182, dy=148, vx=0, vy=1, etype=ENT_OBSTACLE)

ghostimg = pygame.image.load('./data/img/sprites/sprite_ghost_1.png')
ghost = MovingEntity(ghostimg, dx=212, dy=128, vx=0, vy=1, etype=ENT_OBSTACLE)

manimg = pygame.image.load('./data/img/sprites/sprite_man_2.png')
man1 = MovingEntity(manimg, dx=124, dy=224, vx=0, vy=1, etype=ENT_OBSTACLE)
man2 = MovingEntity(manimg, dx=184, dy=214, vx=0, vy=1, etype=ENT_OBSTACLE)
man3 = MovingEntity(manimg, dx=240, dy=224, vx=0, vy=1, etype=ENT_OBSTACLE)

gcimg = pygame.image.load('./data/img/gamecomplete.png')
gc = MovingEntity(gcimg, dx=0, dy=48, vx=0, vy=0, etype=ENT_TOKEN)

spikesimgs = [pygame.image.load('./data/img/spikes{num}.png'.format(num=num)) for num in range(1, 9)]
spikesUimgs = [pygame.transform.flip(spikesimg.copy(), False, True) for spikesimg in spikesimgs]
spikes = {num + 1: [MovingEntity(spikesimg, vx=0, vy=0, etype=ENT_OBSTACLE) for _ in range(10)] for num, spikesimg in enumerate(spikesimgs)}
spikesU = {num + 1: [MovingEntity(spikesUimg, vx=0, vy=0, etype=ENT_OBSTACLE) for _ in range(10)] for num, spikesUimg in enumerate(spikesUimgs)}

def env_0_1():
	g.AddRect(pygame.Rect(0, 0, 52, 92))
	g.AddRect(pygame.Rect(0, 92, 176, 40))
	g.AddRect(pygame.Rect(176, 106, 40, 26))
	g.AddRect(pygame.Rect(216, 106, 102, 26))
	g.AddRect(pygame.Rect(216, 92, 64, 16))
	g.AddRect(pygame.Rect(40, 133, 48, 15))
	g.AddRect(pygame.Rect(128, 133, 48, 15))
	g.AddRect(pygame.Rect(216, 133, 48, 15))
	g.AddRect(pygame.Rect(92, 10, 228, 20))
	g.AddRect(pygame.Rect(92, 21, 28, 15))
	g.AddRect(pygame.Rect(160, 21, 172, 15))
	g.AddRect(pygame.Rect(272, 21, 148, 15))
	g.AddRect(pygame.Rect(0, 219, 320, 21))
	g.AddRect(pygame.Rect(0, 204, 44, 15))
	g.AddRect(pygame.Rect(84, 204, 48, 15))
	g.AddRect(pygame.Rect(172, 204, 48, 15))
	g.AddRect(pygame.Rect(260, 1204, 60, 15))

	spikesU[4][0].SetSpike(120, 31)
	spikesU[4][1].SetSpike(232, 31)
	spikesU[4][2].SetSpike(0, 142)
	spikesU[4][3].SetSpike(88, 142)
	spikesU[4][4].SetSpike(176, 142)
	spikesU[5][0].SetSpike(264, 142)
	spikes[4][0].SetSpike(176, 107)
	spikes[4][1].SetSpike(44, 219)
	spikes[4][2].SetSpike(132, 219)
	spikes[4][3].SetSpike(220, 219)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[0][1], bg, (char, checkpoint1, checkpoint2, spikesU[4][0], spikesU[4][1], spikes[4][0], spikesU[4][2],
		spikesU[4][3], spikesU[4][4], spikesU[5][0], spikes[4][1], spikes[4][2], spikes[4][3])]

	return env

def env_0_2():
	g.AddRect(pygame.Rect(0, 0, 52, 240))
	g.AddRect(pygame.Rect(52, 100, 80, 40))
	g.AddRect(pygame.Rect(92, 0, 40, 52))
	g.AddRect(pygame.Rect(132, 0, 136, 20))
	g.AddRect(pygame.Rect(268, 0, 52, 52))
	g.AddRect(pygame.Rect(92, 188, 40, 32))
	g.AddRect(pygame.Rect(132, 218, 136, 22))
	g.AddRect(pygame.Rect(268, 188, 52, 52))

	spikesU[4][0].SetSpike(92, 62)
	spikes[4][0].SetSpike(92, 188)
	spikesU[8][0].SetSpike(132, 30)
	spikesU[5][0].SetSpike(212, 30)
	spikes[8][0].SetSpike(132, 220)
	spikes[5][0].SetSpike(212, 220)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[0][2], bg, (char, checkpoint3,
											spikes[4][0], spikesU[4][0], spikesU[8][0], spikes[5][0], spikes[8][0], spikesU[5][0],
											platv1, platv2, platv3)]

	return env

def env_0_3():
	g.AddRect(pygame.Rect(0, 0, 52, 240))
	g.AddRect(pygame.Rect(52, 92, 130, 56))
	g.AddRect(pygame.Rect(202, 92, 58, 56))
	g.AddRect(pygame.Rect(182, 116, 40, 8))
	g.AddRect(pygame.Rect(92, 16, 40, 36))
	g.AddRect(pygame.Rect(152, 16, 72, 36))
	g.AddRect(pygame.Rect(284, 16, 16, 36))
	g.AddRect(pygame.Rect(300, 0, 20, 240))
	g.AddRect(pygame.Rect(92, 0, 228, 16))
	g.AddRect(pygame.Rect(92, 188, 40, 40))
	g.AddRect(pygame.Rect(152, 188, 148, 52))
	g.AddRect(pygame.Rect(92, 228, 64, 12))

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[0][3], bg, (char, checkpoint4, checkpointU1, yes1, yes2, yes3, yes4, yes5)]

	return env

def env_0_4():
	g.AddRect(pygame.Rect(0, 0, 52, 240))
	g.AddRect(pygame.Rect(92, 0, 228, 52))
	g.AddRect(pygame.Rect(180, 52, 48, 12))
	g.AddRect(pygame.Rect(52, 108, 68, 8))
	g.AddRect(pygame.Rect(160, 92, 11, 8))
	g.AddRect(pygame.Rect(52, 116, 200, 32))
	g.AddRect(pygame.Rect(252, 92, 68, 72))
	g.AddRect(pygame.Rect(92, 204, 40, 12))
	g.AddRect(pygame.Rect(236, 204, 84, 36))
	g.AddRect(pygame.Rect(92, 216, 144, 24))

	spikesU[8][0].SetSpike(92, 62)
	spikes[4][0].SetSpike(120, 116)
	spikesU[5][0].SetSpike(52, 158)
	spikesU[5][1].SetSpike(102, 158)
	spikesU[5][2].SetSpike(152, 158)
	spikesU[5][3].SetSpike(200, 158)
	spikes[5][0].SetSpike(132, 212)
	spikes[5][1].SetSpike(182, 212)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[0][4], bg, (char, checkpoint5, checkpoint6, spikesU[8][0], spikes[5][0], spikesU[5][0],
		spikesU[5][1], spikesU[5][2], spikesU[5][3], spikes[5][0], spikes[5][1], plat1, plat2, plath1)]

	return env

def env_0_5():
	g.AddRect(pygame.Rect(0, 0, 320, 36))
	g.AddRect(pygame.Rect(300, 36, 20, 96))
	g.AddRect(pygame.Rect(0, 36, 100, 112))
	g.AddRect(pygame.Rect(100, 108, 80, 40))
	g.AddRect(pygame.Rect(0, 148, 52, 82))
	g.AddRect(pygame.Rect(92, 188, 228, 52))
	g.AddRect(pygame.Rect(204, 76, 56, 112))
	g.AddRect(pygame.Rect(147, 58, 26, 17))

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[0][5], bg, (char, checkpoint7, reddisc)]

	return env

def env_1_1():
	g.AddRect(pygame.Rect(0, 0, 320, 36))
	g.AddRect(pygame.Rect(0, 204, 320, 240))
	g.AddRect(pygame.Rect(0, 107, 320, 26))
	g.AddRect(pygame.Rect(150, 133, 20, 15))
	g.AddRect(pygame.Rect(100, 92, 220, 15))

	spikes[5][0].SetSpike(0, 108)
	spikes[5][1].SetSpike(50, 108)
	spikes[5][2].SetSpike(220, 108)
	spikes[5][3].SetSpike(270, 108)
	spikesU[8][0].SetSpike(0, 142)
	spikesU[7][0].SetSpike(80, 142)
	spikesU[8][1].SetSpike(170, 142)
	spikesU[7][1].SetSpike(250, 142)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[1][1], bg, (char, spikes[5][0], spikes[5][1], spikes[5][2], spikes[5][3], spikesU[8][0],
		 spikesU[7][0], spikesU[8][1], spikesU[7][1], bus)]

	return env

def env_1_2():
	g.AddRect(pygame.Rect(0, 0, 320, 36))
	g.AddRect(pygame.Rect(0, 36, 68, 16))
	g.AddRect(pygame.Rect(148, 36, 24, 8))
	g.AddRect(pygame.Rect(208, 36, 24, 8))
	g.AddRect(pygame.Rect(148, 56, 24, 24))
	g.AddRect(pygame.Rect(208, 56, 24, 24))
	g.AddRect(pygame.Rect(0, 188, 124, 36))
	g.AddRect(pygame.Rect(140, 188, 44, 36))
	g.AddRect(pygame.Rect(200, 188, 40, 36))
	g.AddRect(pygame.Rect(256, 188, 28, 36))
	g.AddRect(pygame.Rect(284, 36, 36, 188))
	g.AddRect(pygame.Rect(0, 224, 320, 16))
	
	spikesU[8][0].SetSpike(68, 36)
	spikesU[3][0].SetSpike(174, 36)
	spikesU[5][0].SetSpike(234, 46)
	spikesU[2][0].SetSpike(150, 90)
	spikesU[2][1].SetSpike(210, 90)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[1][2], bg, (char, trinket, spikesU[8][0], spikesU[3][0], spikesU[5][0], spikesU[2][0], spikesU[2][1], man1, man2, man3)]

	return env

def env_1_3():
	g.AddRect(pygame.Rect(0, 0, 11, 240))
	g.AddRect(pygame.Rect(11, 0, 309, 12))
	g.AddRect(pygame.Rect(187, 12, 133, 88))
	g.AddRect(pygame.Rect(12, 188, 308, 52))
	#g.AddRect(pygame.Rect(x-start, y-start, x-length, y-length))

	empty.SetSpike(130, 187)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[1][3], bg, (char, empty)]

	return env

def env_1_4():
	g.AddRect(pygame.Rect(0, 0, 320, 52))
	g.AddRect(pygame.Rect(284, 52, 36, 152))
	g.AddRect(pygame.Rect(0, 204, 284, 36))
	g.AddRect(pygame.Rect(0, 92, 244, 72))
	#g.AddRect(pygame.Rect(x-start, y-start, x-length, y-length))

	empty.SetSpike(130, 187)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[1][4], bg, (char, empty)]

	return env

def env_1_5():
	g.AddRect(pygame.Rect(0, 0, 20, 132))
	g.AddRect(pygame.Rect(20, 0, 300, 36))
	g.AddRect(pygame.Rect(108, 36, 212, 16))
	g.AddRect(pygame.Rect(108, 52, 152, 32))
	g.AddRect(pygame.Rect(220, 84, 40, 96))
	g.AddRect(pygame.Rect(284, 108, 36, 132))
	g.AddRect(pygame.Rect(196, 220, 88, 20))
	g.AddRect(pygame.Rect(0, 188, 44, 52))
	g.AddRect(pygame.Rect(44, 76, 40, 164))
	g.AddRect(pygame.Rect(84, 172, 112, 68))
	
	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[1][5], bg, (char, checkpoint8, green1, green2)]

	return env

def env_2_1():
	g.AddRect(pygame.Rect(0, 0, 132, 36))
	g.AddRect(pygame.Rect(188, 0, 132, 52))
	g.AddRect(pygame.Rect(188, 52, 40, 40))
	g.AddRect(pygame.Rect(0, 92, 228, 40))
	g.AddRect(pygame.Rect(0, 204, 52, 36))
	g.AddRect(pygame.Rect(92, 132, 136, 108))
	g.AddRect(pygame.Rect(284, 92, 36, 148))

	spikes[8][0].SetSpike(0, 92)
	spikes[3][0].SetSpike(80, 92)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[2][1], bg, (char, checkpoint9, checkpointU2, spikes[8][0], spikes[3][0])]

	return env

def env_2_2():
	g.AddRect(pygame.Rect(0, 0, 132, 240))
	g.AddRect(pygame.Rect(132, 0, 188, 36))
	g.AddRect(pygame.Rect(188, 140, 132, 100))

	spikesU[5][0].SetSpike(132, 46)
	spikesU[5][1].SetSpike(182, 46)
	spikes[8][0].SetSpike(190, 140)
	spikes[5][0].SetSpike(270, 140)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[2][2], bg, (char, spikesU[5][0], spikesU[5][1], spikes[8][0], spikes[5][0], plat3, plat4)]

	return env

def env_2_3():
	g.AddRect(pygame.Rect(0, 0, 320, 100))
	g.AddRect(pygame.Rect(0, 188, 110, 52))
	g.AddRect(pygame.Rect(210, 188, 110, 52))
	g.AddRect(pygame.Rect(110, 206, 100, 34))

	spikes[6][0].SetSpike(110, 206)
	spikes[4][0].SetSpike(170, 206)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[2][3], bg, (char, spikes[6][0], spikes[4][0], checkpointA)]

	return env

def env_2_4():
	g.AddRect(pygame.Rect(0, 0, 196, 84))
	g.AddRect(pygame.Rect(0, 84, 68, 14))
	g.AddRect(pygame.Rect(0, 100, 12, 72))
	g.AddRect(pygame.Rect(0, 172, 12, 68))
	g.AddRect(pygame.Rect(12, 164, 40, 13))
	g.AddRect(pygame.Rect(10, 160, 160, 12))
	g.AddRect(pygame.Rect(180, 164, 40, 8))
	g.AddRect(pygame.Rect(220, 0, 320, 240))
	g.AddRect(pygame.Rect(124, 84, 40, 8))

	spikesU[3][0].SetSpike(164, 95)
	spikesU[5][0].SetSpike(68, 95)
	spikes[6][0].SetSpike(120, 172)
	spikes[2][0].SetSpike(52, 172)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[2][4], bg, (char, checkpointB, trinket2, spikesU[3][0], spikes[6][0], spikesU[5][0], spikes[2][0])]

	return env

def env_2_5():
	g.AddRect(pygame.Rect(0, 0, 100, 52))
	g.AddRect(pygame.Rect(100, 0, 90, 26))
	g.AddRect(pygame.Rect(190, 26, 126, 26))
	g.AddRect(pygame.Rect(60, 52, 40, 92))
	g.AddRect(pygame.Rect(0, 108, 32, 64))
	g.AddRect(pygame.Rect(0, 172, 132, 32))
	g.AddRect(pygame.Rect(0, 204, 192, 36))
	g.AddRect(pygame.Rect(220, 92, 40, 148))
	g.AddRect(pygame.Rect(260, 124, 60, 116))

	spikesU[6][0].SetSpike(100, 36)
	spikesU[3][0].SetSpike(160, 36)
	spikes[6][0].SetSpike(132, 204)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[2][5], bg, (char, checkpointC, checkpointU3, spikesU[6][0], spikesU[3][0], spikes[6][0])]

	return env

def env_3_0():
	g.AddRect(pygame.Rect(0, 0, 116, 36))
	g.AddRect(pygame.Rect(76, 36, 40, 128))
	g.AddRect(pygame.Rect(204, 0, 116, 36))
	g.AddRect(pygame.Rect(294, 36, 40, 128))
	g.AddRect(pygame.Rect(92, 164, 136, 16))

	empty.SetSpike(130,187)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[3][0], bg, (char, empty)]

	return env

def env_3_1():
	g.AddRect(pygame.Rect(0, 0, 140, 36))
	g.AddRect(pygame.Rect(0, 36, 56, 16))
	g.AddRect(pygame.Rect(180, 0, 140, 36))
	g.AddRect(pygame.Rect(264, 36, 56, 16))
	g.AddRect(pygame.Rect(0, 76, 82, 164))
	g.AddRect(pygame.Rect(82, 90, 34, 150))
	g.AddRect(pygame.Rect(204, 90, 34, 150))
	g.AddRect(pygame.Rect(238, 76, 82, 154))
	g.AddRect(pygame.Rect(140, 128, 40, 24))

	spikesU[8][0].SetSpike(56, 47)
	spikesU[8][1].SetSpike(184, 47)
	spikes[3][0].SetSpike(82, 91)
	spikes[3][1].SetSpike(208, 91)
	spikes[4][1].SetSpike(140, 128)
	spikesU[4][0].SetSpike(140, 162)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[3][1], bg, (char, spikesU[8][0], spikesU[8][1], spikes[3][0], spikes[3][1], spikes[4][1], spikesU[4][0])]

	return env

def env_3_2():
	g.AddRect(pygame.Rect(0, 0, 320, 36))
	g.AddRect(pygame.Rect(0, 140, 140, 100))
	g.AddRect(pygame.Rect(180, 140, 140, 100))

	spikesU[4][0].SetSpike(140, 46)
	spikes[7][0].SetSpike(0, 140)
	spikes[7][1].SetSpike(70, 140)
	spikes[7][2].SetSpike(180, 140)
	spikes[7][3].SetSpike(250, 140)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[3][2], bg, (char, checkpointU4, checkpointU5, spikesU[4][0], spikes[7][0], spikes[7][1], spikes[7][2], spikes[7][3])]

	return env

def env_3_3():
	g.AddRect(pygame.Rect(0, 188, 320, 52))
	g.AddRect(pygame.Rect(284, 0, 56, 188))
	g.AddRect(pygame.Rect(0, 0, 36, 100))
	g.AddRect(pygame.Rect(36, 60, 112, 50))
	g.AddRect(pygame.Rect(60, 96, 88, 36))
	
	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[3][3], bg, (char, checkpointD)]

	return env

def env_3_4():
	g.AddRect(pygame.Rect(0, 0, 36, 240))
	g.AddRect(pygame.Rect(284, 0, 36, 240))

	empty.SetSpike(130, 187)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[3][4], bg, (char, empty)]

	return env

def env_3_5():
	g.AddRect(pygame.Rect(284, 0, 36, 240))
	g.AddRect(pygame.Rect(0, 0, 115, 52))
	g.AddRect(pygame.Rect(115, 0, 34, 8))
	g.AddRect(pygame.Rect(149, 0, 135, 52))
	g.AddRect(pygame.Rect(0, 124, 40, 116))
	g.AddRect(pygame.Rect(40, 168, 204, 28))
	g.AddRect(pygame.Rect(70, 124, 120, 44))
	g.AddRect(pygame.Rect(220, 124, 24, 44))

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[3][5], bg, (char, checkpointU6, stop1, stop2, stop3)]

	return env

def env_4_1():
	g.AddRect(pygame.Rect(0, 204, 320, 36))
	g.AddRect(pygame.Rect(0, 108, 36, 96))
	g.AddRect(pygame.Rect(0, 0, 132, 68))
	g.AddRect(pygame.Rect(60, 68, 72, 96))
	g.AddRect(pygame.Rect(132, 92, 64, 72))
	g.AddRect(pygame.Rect(196, 128, 56, 36))
	g.AddRect(pygame.Rect(252, 92, 68, 72))
	g.AddRect(pygame.Rect(188, 0, 132, 26))
	g.AddRect(pygame.Rect(202, 36, 42, 8))

	spikesU[2][0].SetSpike(187, 46)
	spikesU[7][0].SetSpike(244, 46)
	spikes[5][0].SetSpike(199, 128)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[4][1], bg, (char, checkpointE, checkpointU7, spikesU[2][0], spikesU[7][0], spikes[5][0], ghost)]

	return env

def env_4_2():
	g.AddRect(pygame.Rect(0, 0, 180, 36))
	g.AddRect(pygame.Rect(180, 0, 40, 21))
	g.AddRect(pygame.Rect(220, 0, 100, 132))
	g.AddRect(pygame.Rect(188, 132, 132, 108))
	g.AddRect(pygame.Rect(0, 140, 92, 36))
	g.AddRect(pygame.Rect(92, 76, 40, 164))
	g.AddRect(pygame.Rect(132, 132, 32, 40))

	spikes[5][0].SetSpike(0, 140)
	spikes[4][0].SetSpike(50, 140)
	spikes[3][0].SetSpike(132, 132)
	spikes[3][1].SetSpike(190, 132)
	spikesU[4][0].SetSpike(180, 31)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[4][2], bg, (char, spikes[5][0], spikes[4][0], spikesU[4][0], spikes[3][0], spikes[3][1], plat5)]

	return env

def env_5_1():
	g.AddRect(pygame.Rect(0, 0, 320, 36))
	g.AddRect(pygame.Rect(28, 36, 40, 16))
	g.AddRect(pygame.Rect(108, 36, 104, 16))
	g.AddRect(pygame.Rect(252, 36, 40, 16))
	g.AddRect(pygame.Rect(0, 204, 320, 36))
	g.AddRect(pygame.Rect(0, 92, 84, 72))
	g.AddRect(pygame.Rect(84, 92, 24, 36))
	g.AddRect(pygame.Rect(108, 92, 24, 72))
	g.AddRect(pygame.Rect(132, 124, 56, 40))
	g.AddRect(pygame.Rect(188, 92, 22, 36))
	g.AddRect(pygame.Rect(210, 92, 26, 36))
	g.AddRect(pygame.Rect(236, 92, 84, 72))

	spikesU[2][0].SetSpike(8, 46)
	spikesU[4][0].SetSpike(68, 46)
	spikesU[4][1].SetSpike(212, 46)
	spikesU[4][2].SetSpike(292, 46)
	spikes[3][0].SetSpike(135, 124)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[5][1], bg, (char, spikesU[2][0], spikesU[4][0], spikesU[4][1], spikesU[4][2], spikes[3][0], walker1, walker2)]

	return env

def env_6_1():
	g.AddRect(pygame.Rect(0, 0, 320, 36))
	g.AddRect(pygame.Rect(284, 36, 36, 136))
	g.AddRect(pygame.Rect(156, 172, 164, 68))
	g.AddRect(pygame.Rect(0, 204, 100, 36))
	g.AddRect(pygame.Rect(0, 92, 36, 16))
	g.AddRect(pygame.Rect(0, 108, 68, 16))
	g.AddRect(pygame.Rect(0, 124, 100, 16))
	g.AddRect(pygame.Rect(0, 140, 132, 16))
	g.AddRect(pygame.Rect(0, 156, 156, 24))
	g.AddRect(pygame.Rect(156, 168, 4, 80))

	empty.SetSpike(130, 187)

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[6][1], bg, (char, empty, gc)]

	return env
