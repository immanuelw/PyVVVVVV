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


spikes_2_0 = MovingEntity(spikesimgs[1], dx=52, dy=172, vx=0, vy=0, etype=ENT_OBSTACLE)

spikes_3_0 = MovingEntity(spikesimgs[2], dx=80, dy=92, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_3_1 = MovingEntity(spikesimgs[2], dx=82, dy=91, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_3_2 = MovingEntity(spikesimgs[2], dx=208, dy=91, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_3_3 = MovingEntity(spikesimgs[2], dx=132, dy=132, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_3_4 = MovingEntity(spikesimgs[2], dx=190, dy=132, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_3_5 = MovingEntity(spikesimgs[2], dx=135, dy=124, vx=0, vy=0, etype=ENT_OBSTACLE)

spikes_4_0 = MovingEntity(spikesimgs[3], dx=176, dy=107, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_4_1 = MovingEntity(spikesimgs[3], dx=44, dy=219, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_4_2 = MovingEntity(spikesimgs[3], dx=132, dy=219, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_4_3 = MovingEntity(spikesimgs[3], dx=220, dy=219, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_4_4 = MovingEntity(spikesimgs[3], dx=92, dy=188, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_4_5 = MovingEntity(spikesimgs[3], dx=120, dy=116, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_4_6 = MovingEntity(spikesimgs[3], dx=170, dy=206, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_4_7 = MovingEntity(spikesimgs[3], dx=140, dy=128, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_4_8 = MovingEntity(spikesimgs[3], dx=50, dy=140, vx=0, vy=0, etype=ENT_OBSTACLE)

spikes_5_0 = MovingEntity(spikesimgs[4], dx=212, dy=220, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_5_1 = MovingEntity(spikesimgs[4], dx=132, dy=212, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_5_2 = MovingEntity(spikesimgs[4], dx=182, dy=212, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_5_3 = MovingEntity(spikesimgs[4], dx=0, dy=108, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_5_4 = MovingEntity(spikesimgs[4], dx=50, dy=108, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_5_5 = MovingEntity(spikesimgs[4], dx=220, dy=108, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_5_6 = MovingEntity(spikesimgs[4], dx=270, dy=108, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_5_7 = MovingEntity(spikesimgs[4], dx=270, dy=140, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_5_8 = MovingEntity(spikesimgs[4], dx=199, dy=129, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_5_9 = MovingEntity(spikesimgs[4], dx=0, dy=140, vx=0, vy=0, etype=ENT_OBSTACLE)

spikes_6_0 = MovingEntity(spikesimgs[5], dx=110, dy=206, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_6_1 = MovingEntity(spikesimgs[5], dx=120, dy=172, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_6_2 = MovingEntity(spikesimgs[5], dx=132, dy=204, vx=0, vy=0, etype=ENT_OBSTACLE)

spikes_7_0 = MovingEntity(spikesimgs[6], dx=0, dy=140, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_7_1 = MovingEntity(spikesimgs[6], dx=70, dy=140, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_7_2 = MovingEntity(spikesimgs[6], dx=180, dy=140, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_7_3 = MovingEntity(spikesimgs[6], dx=250, dy=140, vx=0, vy=0, etype=ENT_OBSTACLE)

spikes_8_0 = MovingEntity(spikesimgs[7], dx=132, dy=220, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_8_1 = MovingEntity(spikesimgs[7], dx=0, dy=92, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_8_2 = MovingEntity(spikesimgs[7], dx=190, dy=140, vx=0, vy=0, etype=ENT_OBSTACLE)


spikesU_2_0 = MovingEntity(spikesUimgs[1], dx=150, dy=91, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_2_1 = MovingEntity(spikesUimgs[1], dx=210, dy=91, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_2_2 = MovingEntity(spikesUimgs[1], dx=187, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_2_3 = MovingEntity(spikesUimgs[1], dx=8, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)

spikesU_3_0 = MovingEntity(spikesUimgs[2], dx=174, dy=37, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_3_1 = MovingEntity(spikesUimgs[2], dx=164, dy=95, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_3_2 = MovingEntity(spikesUimgs[2], dx=160, dy=37, vx=0, vy=0, etype=ENT_OBSTACLE)

spikesU_4_0 = MovingEntity(spikesUimgs[3], dx=120, dy=32, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_1 = MovingEntity(spikesUimgs[3], dx=232, dy=32, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_2 = MovingEntity(spikesUimgs[3], dx=0, dy=143, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_3 = MovingEntity(spikesUimgs[3], dx=88, dy=143, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_4 = MovingEntity(spikesUimgs[3], dx=176, dy=143, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_5 = MovingEntity(spikesUimgs[3], dx=92, dy=63, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_6 = MovingEntity(spikesUimgs[3], dx=140, dy=163, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_7 = MovingEntity(spikesUimgs[3], dx=140, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_8 = MovingEntity(spikesUimgs[3], dx=180, dy=32, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_9 = MovingEntity(spikesUimgs[3], dx=68, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_A = MovingEntity(spikesUimgs[3], dx=212, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_B = MovingEntity(spikesUimgs[3], dx=292, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)

spikesU_5_0 = MovingEntity(spikesUimgs[4], dx=264, dy=143, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_5_1 = MovingEntity(spikesUimgs[4], dx=212, dy=31, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_5_2 = MovingEntity(spikesUimgs[4], dx=52, dy=159, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_5_3 = MovingEntity(spikesUimgs[4], dx=102, dy=159, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_5_4 = MovingEntity(spikesUimgs[4], dx=152, dy=159, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_5_5 = MovingEntity(spikesUimgs[4], dx=200, dy=159, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_5_6 = MovingEntity(spikesUimgs[4], dx=234, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_5_7 = MovingEntity(spikesUimgs[4], dx=132, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_5_8 = MovingEntity(spikesUimgs[4], dx=182, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_5_9 = MovingEntity(spikesUimgs[4], dx=68, dy=95, vx=0, vy=0, etype=ENT_OBSTACLE)

spikesU_6_0 = MovingEntity(spikesUimgs[5], dx=100, dy=37, vx=0, vy=0, etype=ENT_OBSTACLE)

spikesU_7_0 = MovingEntity(spikesUimgs[6], dx=80, dy=143, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_7_1 = MovingEntity(spikesUimgs[6], dx=250, dy=143, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_7_2 = MovingEntity(spikesUimgs[6], dx=244, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)

spikesU_8_0 = MovingEntity(spikesUimgs[7], dx=132, dy=31, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_8_1 = MovingEntity(spikesUimgs[7], dx=92, dy=63, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_8_2 = MovingEntity(spikesUimgs[7], dx=0, dy=143, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_8_3 = MovingEntity(spikesUimgs[7], dx=170, dy=143, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_8_4 = MovingEntity(spikesUimgs[7], dx=68, dy=37, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_8_5 = MovingEntity(spikesUimgs[7], dx=56, dy=48, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_8_6 = MovingEntity(spikesUimgs[7], dx=184, dy=48, vx=0, vy=0, etype=ENT_OBSTACLE)

#spikes = {num + 1: [MovingEntity(spikesimg, vx=0, vy=0, etype=ENT_OBSTACLE) for _ in range(10)] for num, spikesimg in enumerate(spikesimgs)}
#spikesU = {num + 1: [MovingEntity(spikesUimg, vx=0, vy=0, etype=ENT_OBSTACLE) for _ in range(10)] for num, spikesUimg in enumerate(spikesUimgs)}

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

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[0][1], bg, (char, checkpoint1, checkpoint2, spikesU_4_0, spikesU_4_1, spikesU_4_2, spikesU_4_3, spikesU_4_4, spikes_4_0, spikes_4_1, spikes_4_2, spikes_4_3)]

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

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[0][2], bg, (char, checkpoint3, platv1, platv2, platv3,
											spikesU_4_5, spikesU_8_0, spikesU_5_1, spikes_4_4, spikes_5_0, spikes_8_0)]

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

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[0][4], bg, (char, checkpoint5, checkpoint6, plat1, plat2, plath1,
											spikesU_5_2, spikesU_5_3, spikesU_5_4, spikesU_5_5, spikesU_8_1,
											spikes_4_5, spikes_5_1, spikes_5_2)]

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

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[1][1], bg, (char, bus,
										spikesU_7_0, spikesU_7_1, spikesU_8_2, spikesU_8_3, spikes_5_3, spikes_5_4, spikes_5_5, spikes_5_6)]

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
	
	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[1][2], bg, (char, trinket, man1, man2, man3, spikesU_2_0, spikesU_2_1, spikesU_3_0, spikesU_5_6, spikesU_8_4)]

	return env

def env_1_3():
	g.AddRect(pygame.Rect(0, 0, 11, 240))
	g.AddRect(pygame.Rect(11, 0, 309, 12))
	g.AddRect(pygame.Rect(187, 12, 133, 88))
	g.AddRect(pygame.Rect(12, 188, 308, 52))

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[1][3], bg, (char,)]

	return env

def env_1_4():
	g.AddRect(pygame.Rect(0, 0, 320, 52))
	g.AddRect(pygame.Rect(284, 52, 36, 152))
	g.AddRect(pygame.Rect(0, 204, 284, 36))
	g.AddRect(pygame.Rect(0, 92, 244, 72))

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[1][4], bg, (char,)]

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

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[2][1], bg, (char, checkpoint9, checkpointU2, spikes_3_0, spikes_8_1)]

	return env

def env_2_2():
	g.AddRect(pygame.Rect(0, 0, 132, 240))
	g.AddRect(pygame.Rect(132, 0, 188, 36))
	g.AddRect(pygame.Rect(188, 140, 132, 100))

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[2][2], bg, (char, plat3, plat4, spikesU_5_7, spikesU_5_8, spikes_5_7, spikes_8_2)]

	return env

def env_2_3():
	g.AddRect(pygame.Rect(0, 0, 320, 100))
	g.AddRect(pygame.Rect(0, 188, 110, 52))
	g.AddRect(pygame.Rect(210, 188, 110, 52))
	g.AddRect(pygame.Rect(110, 206, 100, 34))

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[2][3], bg, (char, checkpointA, spikes_4_6, spikes_6_0)]

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

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[2][4], bg, (char, checkpointB, trinket2, spikesU_3_1, spikesU_5_9, spikes_2_0, spikes_6_1)]

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

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[2][5], bg, (char, checkpointC, checkpointU3, spikesU_3_2, spikesU_6_0, spikes_6_2)]

	return env

def env_3_0():
	g.AddRect(pygame.Rect(0, 0, 116, 36))
	g.AddRect(pygame.Rect(76, 36, 40, 128))
	g.AddRect(pygame.Rect(204, 0, 116, 36))
	g.AddRect(pygame.Rect(294, 36, 40, 128))
	g.AddRect(pygame.Rect(92, 164, 136, 16))

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[3][0], bg, (char,)]

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

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[3][1], bg, (char, spikesU_4_6, spikesU_8_5, spikesU_8_6, spikes_3_1, spikes_3_2, spikes_4_7)]

	return env

def env_3_2():
	g.AddRect(pygame.Rect(0, 0, 320, 36))
	g.AddRect(pygame.Rect(0, 140, 140, 100))
	g.AddRect(pygame.Rect(180, 140, 140, 100))

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[3][2], bg, (char, checkpointU4, checkpointU5, spikesU_4_7, spikes_7_0, spikes_7_1, spikes_7_2, spikes_7_3)]

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

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[3][4], bg, (char,)]

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

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[4][1], bg, (char, checkpointE, checkpointU7, ghost, spikesU_2_2, spikesU_7_2, spikes_5_8)]

	return env

def env_4_2():
	g.AddRect(pygame.Rect(0, 0, 180, 36))
	g.AddRect(pygame.Rect(180, 0, 40, 21))
	g.AddRect(pygame.Rect(220, 0, 100, 132))
	g.AddRect(pygame.Rect(188, 132, 132, 108))
	g.AddRect(pygame.Rect(0, 140, 92, 36))
	g.AddRect(pygame.Rect(92, 76, 40, 164))
	g.AddRect(pygame.Rect(132, 132, 32, 40))

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[4][2], bg, (char, plat5, spikesU_4_8, spikes_3_3, spikes_3_4, spikes_4_8, spikes_5_9)]

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

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[5][1], bg, (char, walker1, walker2, spikesU_2_3, spikesU_4_9, spikesU_4_A, spikesU_4_B, spikes_3_5)]

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

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[6][1], bg, (char, gc)]

	return env
