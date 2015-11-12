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
from rects import rect_list
from img import imgs, img_dict

window = pygame.display.set_mode((GAMERECT.width * 2, GAMERECT.height * 2))
gamesurf = pygame.Surface((GAMERECT.width, GAMERECT.height))
backbuf = pygame.Surface((window.get_width(), window.get_height()))

char = Character(VIRIDIAN_BASE)
char.SetPulsation(VIRIDIAN_PULSATION)
char.SetPulseRate(VIRIDIAN_PULSERATE)

g = Geometry()

rect_dict = {x_co: {y_co: [pygame.Rect(*rect) for rect in rect_list[x_co][y_co]] for y_co in range(7) if (x_co, y_co) in level_array} for x_co in range(7)}

bg = Background('./data/img/bg_cross.png', GAMERECT, 1, 0)

plat1 = MovingEntity(image='./data/img/plat_o.png', dx=100, dy=70, vx=0, vy=0, etype=ENT_PLATFORM)
plat2 = MovingEntity(image='./data/img/plat_o.png', dx=120, dy=70, vx=0, vy=0, etype=ENT_PLATFORM)
plat3 = MovingEntity(image='./data/img/plat_o.png', dx=200, dy=116, vx=0, vy=0, etype=ENT_PLATFORM)
plat4 = MovingEntity(image='./data/img/plat_o.png', dx=150, dy=52, vx=0, vy=0, etype=ENT_PLATFORM)
plat5 = MovingEntity(image='./data/img/plat_o.png', dx=132, dy=88, vx=0, vy=0, etype=ENT_PLATFORM)

platv1 = MovingEntity(image='./data/img/plat_o.png', dx=140, dy=100, vx=0, vy=1, etype=ENT_PLATFORM)
platv2 = MovingEntity(image='./data/img/plat_o.png', dx=170, dy=120, vx=0, vy=1, etype=ENT_PLATFORM)
platv3 = MovingEntity(image='./data/img/plat_o.png', dx=200, dy=140, vx=0, vy=1, etype=ENT_PLATFORM)

plath1 = MovingEntity(image='./data/img/plat_o.png', dx=52, dy=166, vx=1, vy=0, etype=ENT_PLATFORM)

sprite = MovingEntity(image='./data/img/sprite1.png', vx=1, vy=1, etype=ENT_OBSTACLE)

checkpoint1 = MovingEntity(image='./data/img/checkpointBW.png', dx=64, dy=108, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpoint2 = MovingEntity(image='./data/img/checkpointBW.png', dx=284, dy=220, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpoint3 = MovingEntity(image='./data/img/checkpointBW.png', dx=288, dy=204, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpoint4 = MovingEntity(image='./data/img/checkpointBW.png', dx=64, dy=108, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpoint5 = MovingEntity(image='./data/img/checkpointBW.png', dx=60, dy=124, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpoint6 = MovingEntity(image='./data/img/checkpointBW.png', dx=280, dy=220, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpoint7 = MovingEntity(image='./data/img/checkpointBW.png', dx=122, dy=124, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpoint8 = MovingEntity(image='./data/img/checkpointBW.png', dx=12, dy=204, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpoint9 = MovingEntity(image='./data/img/checkpointBW.png', dx=152, dy=108, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointA = MovingEntity(image='./data/img/checkpointBW.png', dx=32, dy=204, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointB = MovingEntity(image='./data/img/checkpointBW.png', dx=198, dy=180, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointC = MovingEntity(image='./data/img/checkpointBW.png', dx=110, dy=188, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointD = MovingEntity(image='./data/img/checkpointBW.png', dx=52, dy=204, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointE = MovingEntity(image='./data/img/checkpointBW.png', dx=152, dy=108, vx=0, vy=0, etype=ENT_CHECKPOINT)

checkpointU1 = MovingEntity(image='./data/img/checkpointUBW.png', dx=64, dy=164, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointU2 = MovingEntity(image='./data/img/checkpointUBW.png', dx=52, dy=148, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointU3 = MovingEntity(image='./data/img/checkpointUBW.png', dx=202, dy=68, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointU4 = MovingEntity(image='./data/img/checkpointUBW.png', dx=24, dy=52, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointU5 = MovingEntity(image='./data/img/checkpointUBW.png', dx=280, dy=52, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointU6 = MovingEntity(image='./data/img/checkpointUBW.png', dx=186, dy=212, vx=0, vy=0, etype=ENT_CHECKPOINT)
checkpointU7 = MovingEntity(image='./data/img/checkpointUBW.png', dx=38, dy=84, vx=0, vy=0, etype=ENT_CHECKPOINT)

trinket1 = MovingEntity(image='./data/img/sprites/sprite_trinket.png', dx=270, dy=172, vx=0, vy=0, etype=ENT_TOKEN)
trinket2 = MovingEntity(image='./data/img/sprites/sprite_trinket.png', dx=40, dy=140, vx=0, vy=0, etype=ENT_TOKEN)

portal1 = MovingEntity(image='./data/img/warptoken.bmp', vx=0, vy=0, etype=ENT_PORTAL)
portal2 = MovingEntity(image='./data/img/warptoken2.bmp', vx=0, vy=0, etype=ENT_PORTAL)

bus = MovingEntity(image='./data/img/sprites/sprite_BUS_3.png', dx=320, dy=60, vx=1, vy=0, etype=ENT_OBSTACLE)

green1 = MovingEntity(image='./data/img/sprites/sprite_green_1.png', dx=84, dy=110, vx=1.5, vy=0, etype=ENT_OBSTACLE)
green2 = MovingEntity(image='./data/img/sprites/sprite_green_1.png', dx=124, dy=150, vx=1.5, vy=0, etype=ENT_OBSTACLE)

reddisc = MovingEntity(image='./data/img/sprites/sprite_reddisc_1.png', dx=184, dy=188, vx=0, vy=1, etype=ENT_OBSTACLE)

stop1 = MovingEntity(image='./data/img/sprites/sprite_STOP_2.png', dx=192, dy=166, vx=0, vy=1.5, etype=ENT_OBSTACLE)
stop2 = MovingEntity(image='./data/img/sprites/sprite_STOP_2.png', dx=42, dy=166, vx=0, vy=1.5, etype=ENT_OBSTACLE)
stop3 = MovingEntity(image='./data/img/sprites/sprite_STOP_2.png', dx=118, dy=50, vx=0, vy=1, etype=ENT_OBSTACLE)

walker1 = MovingEntity(image='./data/img/sprites/sprite_walker_2.png', dx=272, dy=204, vx=1.5, vy=0, etype=ENT_OBSTACLE)
walker2 = MovingEntity(image='./data/img/sprites/sprite_walker_2.png', dx=284, dy=92, vx=1.5, vy=0, etype=ENT_OBSTACLE)

yes1 = MovingEntity(image='./data/img/sprites/sprite_YES_2.png', dx=132, dy=52, vx=0, vy=1, etype=ENT_OBSTACLE)
yes2 = MovingEntity(image='./data/img/sprites/sprite_YES_2.png', dx=264, dy=52, vx=0, vy=1, etype=ENT_OBSTACLE)
yes3 = MovingEntity(image='./data/img/sprites/sprite_YES_2.png', dx=182, dy=112, vx=0, vy=1, etype=ENT_OBSTACLE)
yes4 = MovingEntity(image='./data/img/sprites/sprite_YES_2.png', dx=132, dy=224, vx=0, vy=1, etype=ENT_OBSTACLE)
yes5 = MovingEntity(image='./data/img/sprites/sprite_YES_2.png', dx=182, dy=148, vx=0, vy=1, etype=ENT_OBSTACLE)

ghost = MovingEntity(image='./data/img/sprites/sprite_ghost_1.png', dx=212, dy=128, vx=0, vy=1, etype=ENT_OBSTACLE)

man1 = MovingEntity(image='./data/img/sprites/sprite_man_2.png', dx=124, dy=224, vx=0, vy=1, etype=ENT_OBSTACLE)
man2 = MovingEntity(image='./data/img/sprites/sprite_man_2.png', dx=184, dy=214, vx=0, vy=1, etype=ENT_OBSTACLE)
man3 = MovingEntity(image='./data/img/sprites/sprite_man_2.png', dx=240, dy=224, vx=0, vy=1, etype=ENT_OBSTACLE)

gc = MovingEntity(image='./data/img/gamecomplete.png', dx=0, dy=48, vx=0, vy=0, etype=ENT_TOKEN)


spikes_2_0 = MovingEntity(image='./data/img/spikes2.png', dx=52, dy=172, vx=0, vy=0, etype=ENT_OBSTACLE)

spikes_3_0 = MovingEntity(image='./data/img/spikes3.png', dx=80, dy=92, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_3_1 = MovingEntity(image='./data/img/spikes3.png', dx=82, dy=91, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_3_2 = MovingEntity(image='./data/img/spikes3.png', dx=208, dy=91, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_3_3 = MovingEntity(image='./data/img/spikes3.png', dx=132, dy=132, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_3_4 = MovingEntity(image='./data/img/spikes3.png', dx=190, dy=132, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_3_5 = MovingEntity(image='./data/img/spikes3.png', dx=135, dy=124, vx=0, vy=0, etype=ENT_OBSTACLE)

spikes_4_0 = MovingEntity(image='./data/img/spikes4.png', dx=176, dy=107, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_4_1 = MovingEntity(image='./data/img/spikes4.png', dx=44, dy=219, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_4_2 = MovingEntity(image='./data/img/spikes3.png', dx=132, dy=219, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_4_3 = MovingEntity(image='./data/img/spikes4.png', dx=220, dy=219, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_4_4 = MovingEntity(image='./data/img/spikes4.png', dx=92, dy=188, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_4_5 = MovingEntity(image='./data/img/spikes4.png', dx=120, dy=116, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_4_6 = MovingEntity(image='./data/img/spikes4.png', dx=170, dy=206, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_4_7 = MovingEntity(image='./data/img/spikes4.png', dx=140, dy=128, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_4_8 = MovingEntity(image='./data/img/spikes4.png', dx=50, dy=140, vx=0, vy=0, etype=ENT_OBSTACLE)

spikes_5_0 = MovingEntity(image='./data/img/spikes5.png', dx=212, dy=220, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_5_1 = MovingEntity(image='./data/img/spikes5.png', dx=132, dy=212, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_5_2 = MovingEntity(image='./data/img/spikes5.png', dx=182, dy=212, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_5_3 = MovingEntity(image='./data/img/spikes5.png', dx=0, dy=108, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_5_4 = MovingEntity(image='./data/img/spikes5.png', dx=50, dy=108, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_5_5 = MovingEntity(image='./data/img/spikes5.png', dx=220, dy=108, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_5_6 = MovingEntity(image='./data/img/spikes5.png', dx=270, dy=108, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_5_7 = MovingEntity(image='./data/img/spikes5.png', dx=270, dy=140, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_5_8 = MovingEntity(image='./data/img/spikes5.png', dx=199, dy=129, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_5_9 = MovingEntity(image='./data/img/spikes5.png', dx=0, dy=140, vx=0, vy=0, etype=ENT_OBSTACLE)

spikes_6_0 = MovingEntity(image='./data/img/spikes6.png', dx=110, dy=206, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_6_1 = MovingEntity(image='./data/img/spikes6.png', dx=120, dy=172, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_6_2 = MovingEntity(image='./data/img/spikes6.png', dx=132, dy=204, vx=0, vy=0, etype=ENT_OBSTACLE)

spikes_7_0 = MovingEntity(image='./data/img/spikes7.png', dx=0, dy=140, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_7_1 = MovingEntity(image='./data/img/spikes7.png', dx=70, dy=140, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_7_2 = MovingEntity(image='./data/img/spikes7.png', dx=180, dy=140, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_7_3 = MovingEntity(image='./data/img/spikes7.png', dx=250, dy=140, vx=0, vy=0, etype=ENT_OBSTACLE)

spikes_8_0 = MovingEntity(image='./data/img/spikes8.png', dx=132, dy=220, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_8_1 = MovingEntity(image='./data/img/spikes8.png', dx=0, dy=92, vx=0, vy=0, etype=ENT_OBSTACLE)
spikes_8_2 = MovingEntity(image='./data/img/spikes8.png', dx=190, dy=140, vx=0, vy=0, etype=ENT_OBSTACLE)


spikesU_2_0 = MovingEntity(image='./data/img/spikesU2.png', dx=150, dy=91, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_2_1 = MovingEntity(image='./data/img/spikesU2.png', dx=210, dy=91, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_2_2 = MovingEntity(image='./data/img/spikesU2.png', dx=187, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_2_3 = MovingEntity(image='./data/img/spikesU2.png', dx=8, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)

spikesU_3_0 = MovingEntity(image='./data/img/spikesU3.png', dx=174, dy=37, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_3_1 = MovingEntity(image='./data/img/spikesU3.png', dx=164, dy=95, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_3_2 = MovingEntity(image='./data/img/spikesU3.png', dx=160, dy=37, vx=0, vy=0, etype=ENT_OBSTACLE)

spikesU_4_0 = MovingEntity(image='./data/img/spikesU4.png', dx=120, dy=32, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_1 = MovingEntity(image='./data/img/spikesU4.png', dx=232, dy=32, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_2 = MovingEntity(image='./data/img/spikesU4.png', dx=0, dy=143, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_3 = MovingEntity(image='./data/img/spikesU4.png', dx=88, dy=143, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_4 = MovingEntity(image='./data/img/spikesU4.png', dx=176, dy=143, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_5 = MovingEntity(image='./data/img/spikesU4.png', dx=92, dy=63, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_6 = MovingEntity(image='./data/img/spikesU4.png', dx=140, dy=163, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_7 = MovingEntity(image='./data/img/spikesU4.png', dx=140, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_8 = MovingEntity(image='./data/img/spikesU4.png', dx=180, dy=32, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_9 = MovingEntity(image='./data/img/spikesU4.png', dx=68, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_A = MovingEntity(image='./data/img/spikesU4.png', dx=212, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_4_B = MovingEntity(image='./data/img/spikesU4.png', dx=292, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)

spikesU_5_0 = MovingEntity(image='./data/img/spikesU5.png', dx=264, dy=143, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_5_1 = MovingEntity(image='./data/img/spikesU5.png', dx=212, dy=31, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_5_2 = MovingEntity(image='./data/img/spikesU5.png', dx=52, dy=159, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_5_3 = MovingEntity(image='./data/img/spikesU5.png', dx=102, dy=159, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_5_4 = MovingEntity(image='./data/img/spikesU5.png', dx=152, dy=159, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_5_5 = MovingEntity(image='./data/img/spikesU5.png', dx=200, dy=159, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_5_6 = MovingEntity(image='./data/img/spikesU5.png', dx=234, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_5_7 = MovingEntity(image='./data/img/spikesU5.png', dx=132, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_5_8 = MovingEntity(image='./data/img/spikesU5.png', dx=182, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_5_9 = MovingEntity(image='./data/img/spikesU5.png', dx=68, dy=95, vx=0, vy=0, etype=ENT_OBSTACLE)

spikesU_6_0 = MovingEntity(image='./data/img/spikesU6.png', dx=100, dy=37, vx=0, vy=0, etype=ENT_OBSTACLE)

spikesU_7_0 = MovingEntity(image='./data/img/spikesU7.png', dx=80, dy=143, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_7_1 = MovingEntity(image='./data/img/spikesU7.png', dx=250, dy=143, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_7_2 = MovingEntity(image='./data/img/spikesU7.png', dx=244, dy=47, vx=0, vy=0, etype=ENT_OBSTACLE)

spikesU_8_0 = MovingEntity(image='./data/img/spikesU8.png', dx=132, dy=31, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_8_1 = MovingEntity(image='./data/img/spikesU8.png', dx=92, dy=63, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_8_2 = MovingEntity(image='./data/img/spikesU8.png', dx=0, dy=143, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_8_3 = MovingEntity(image='./data/img/spikesU8.png', dx=170, dy=143, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_8_4 = MovingEntity(image='./data/img/spikesU8.png', dx=68, dy=37, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_8_5 = MovingEntity(image='./data/img/spikesU8.png', dx=56, dy=48, vx=0, vy=0, etype=ENT_OBSTACLE)
spikesU_8_6 = MovingEntity(image='./data/img/spikesU8.png', dx=184, dy=48, vx=0, vy=0, etype=ENT_OBSTACLE)

#{1: {3: [{'img_file': 'filename', 'dx': 174, 'dy': 37, 'vx': 0, 'vy': 0, 'etype': 2}, ...], 4: ...}. 2: {...}}
#{'filename': pygame_image_object}
#ent_list = {x_co: {y_co: (MovingEntity(image=ent['img_file'], dx=ent['dx'], dy=ent['dy'], vx=ent['vx'], vy=ent['vy'], etype=ent['etype'])\
#							for ent in ent_dict[x_co][y_co]) for y_co in range(7) if (x_co, y_co) in level_array} for x_co in range(7)}


def env_0_1():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[0][1]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[0][1], bg, (char, checkpoint1, checkpoint2, spikesU_4_0, spikesU_4_1, spikesU_4_2, spikesU_4_3, spikesU_4_4, spikes_4_0, spikes_4_1, spikes_4_2, spikes_4_3)]

	return env

def env_0_2():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[0][2]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[0][2], bg, (char, checkpoint3, platv1, platv2, platv3,
											spikesU_4_5, spikesU_8_0, spikesU_5_1, spikes_4_4, spikes_5_0, spikes_8_0)]

	return env

def env_0_3():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[0][3]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[0][3], bg, (char, checkpoint4, checkpointU1, yes1, yes2, yes3, yes4, yes5)]

	return env

def env_0_4():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[0][4]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[0][4], bg, (char, checkpoint5, checkpoint6, plat1, plat2, plath1,
											spikesU_5_2, spikesU_5_3, spikesU_5_4, spikesU_5_5, spikesU_8_1,
											spikes_4_5, spikes_5_1, spikes_5_2)]

	return env

def env_0_5():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[0][5]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[0][5], bg, (char, checkpoint7, reddisc)]

	return env

def env_1_1():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[1][1]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[1][1], bg, (char, bus,
										spikesU_7_0, spikesU_7_1, spikesU_8_2, spikesU_8_3, spikes_5_3, spikes_5_4, spikes_5_5, spikes_5_6)]

	return env

def env_1_2():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[1][2]]
	
	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[1][2], bg, (char, trinket1, man1, man2, man3, spikesU_2_0, spikesU_2_1, spikesU_3_0, spikesU_5_6, spikesU_8_4)]

	return env


def env_create(x_co, y_co):
	g.rects = rect_dict[x_co][y_co]]
	#stuff = tuple(ent for ent in ent_list[x_co][y_co])
	stuff = (gc,)
	env = [GAMERECT, g, imgs[x_co][y_co], bg, (char,)+stuff]

	return env

def env_1_3():
	g.rects = rect_dict[1][3]
	#g.rects = [pygame.Rect(*rect) for rect in rect_list[1][3]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[1][3], bg, (char,)]

	return env

def env_1_4():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[1][4]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[1][4], bg, (char,)]

	return env

def env_1_5():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[1][5]]
	
	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[1][5], bg, (char, checkpoint8, green1, green2)]

	return env

def env_2_1():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[2][1]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[2][1], bg, (char, checkpoint9, checkpointU2, spikes_3_0, spikes_8_1)]

	return env

def env_2_2():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[2][2]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[2][2], bg, (char, plat3, plat4, spikesU_5_7, spikesU_5_8, spikes_5_7, spikes_8_2)]

	return env

def env_2_3():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[2][3]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[2][3], bg, (char, checkpointA, spikes_4_6, spikes_6_0)]

	return env

def env_2_4():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[2][4]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[2][4], bg, (char, checkpointB, trinket2, spikesU_3_1, spikesU_5_9, spikes_2_0, spikes_6_1)]

	return env

def env_2_5():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[2][5]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[2][5], bg, (char, checkpointC, checkpointU3, spikesU_3_2, spikesU_6_0, spikes_6_2)]

	return env

def env_3_0():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[3][0]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[3][0], bg, (char,)]

	return env

def env_3_1():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[3][1]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[3][1], bg, (char, spikesU_4_6, spikesU_8_5, spikesU_8_6, spikes_3_1, spikes_3_2, spikes_4_7)]

	return env

def env_3_2():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[3][2]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[3][2], bg, (char, checkpointU4, checkpointU5, spikesU_4_7, spikes_7_0, spikes_7_1, spikes_7_2, spikes_7_3)]

	return env

def env_3_3():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[3][3]]
	
	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[3][3], bg, (char, checkpointD)]

	return env

def env_3_4():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[3][4]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[3][4], bg, (char,)]

	return env

def env_3_5():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[3][5]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[3][5], bg, (char, checkpointU6, stop1, stop2, stop3)]

	return env

def env_4_1():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[4][1]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[4][1], bg, (char, checkpointE, checkpointU7, ghost, spikesU_2_2, spikesU_7_2, spikes_5_8)]

	return env

def env_4_2():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[4][2]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[4][2], bg, (char, plat5, spikesU_4_8, spikes_3_3, spikes_3_4, spikes_4_8, spikes_5_9)]

	return env

def env_5_1():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[5][1]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[5][1], bg, (char, walker1, walker2, spikesU_2_3, spikesU_4_9, spikesU_4_A, spikesU_4_B, spikes_3_5)]

	return env

def env_6_1():
	g.rects = [pygame.Rect(*rect) for rect in rect_list[6][1]]

	#initalizes all parts of screen
	env = [GAMERECT, g, imgs[6][1], bg, (char, gc)]

	return env
