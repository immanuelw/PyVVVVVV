'''
levels | defines the entities to place in each level, saves to json if ran as script

author | Immanuel Washington
'''
import json
import pygame
from entity import MovingEntity
import config as cf
from rects import rect_list
from img import imgs, img_dict

rect_dict = {x_co: {y_co: [pygame.Rect(*rect) for rect in rect_list[x_co][y_co]] for y_co in range(7) if (x_co, y_co) in cf.level_array} for x_co in range(7)}

ent_dict = \
{0:
	{1:
		[{'name': 'checkpoint1', 'image': './data/img/checkpointBW.png', 'dx': 64, 'dy': 108, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'checkpoint2', 'image': './data/img/checkpointBW.png', 'dx': 284, 'dy': 220, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'spikesU_4_0', 'image': './data/img/spikesU4.png', 'dx': 120, 'dy': 32, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_4_1', 'image': './data/img/spikesU4.png', 'dx': 232, 'dy': 32, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_4_2', 'image': './data/img/spikesU4.png', 'dx': 0, 'dy': 143, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_4_3', 'image': './data/img/spikesU4.png', 'dx': 88, 'dy': 143, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_4_4', 'image': './data/img/spikesU4.png', 'dx': 176, 'dy': 143, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_5_0', 'image': './data/img/spikesU5.png', 'dx': 264, 'dy': 143, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_4_0', 'image': './data/img/spikes4.png', 'dx': 176, 'dy': 107, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_4_1', 'image': './data/img/spikes4.png', 'dx': 44, 'dy': 219, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_4_2', 'image': './data/img/spikes3.png', 'dx': 132, 'dy': 219, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_4_3', 'image': './data/img/spikes4.png', 'dx': 220, 'dy': 219, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE}],
	2:
		[{'name': 'checkpoint3', 'image': './data/img/checkpointBW.png', 'dx': 288, 'dy': 204, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'platv1', 'image': './data/img/plat_o.png', 'dx': 140, 'dy': 100, 'vx': 0, 'vy': 1, 'etype': cf.ENT_PLATFORM},
		{'name': 'platv2', 'image': './data/img/plat_o.png', 'dx': 170, 'dy': 120, 'vx': 0, 'vy': 1, 'etype': cf.ENT_PLATFORM},
		{'name': 'platv3', 'image': './data/img/plat_o.png', 'dx': 200, 'dy': 140, 'vx': 0, 'vy': 1, 'etype': cf.ENT_PLATFORM},
		{'name': 'spikesU_4_5', 'image': './data/img/spikesU4.png', 'dx': 92, 'dy': 63, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_5_1', 'image': './data/img/spikesU5.png', 'dx': 212, 'dy': 31, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_8_0', 'image': './data/img/spikesU8.png', 'dx': 132, 'dy': 31, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_4_4', 'image': './data/img/spikes4.png', 'dx': 92, 'dy': 188, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_5_0', 'image': './data/img/spikes5.png', 'dx': 212, 'dy': 220, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_8_0', 'image': './data/img/spikes8.png', 'dx': 132, 'dy': 220, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE}],
	3:
		[{'name': 'checkpoint4', 'image': './data/img/checkpointBW.png', 'dx': 64, 'dy': 108, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'checkpointU1', 'image': './data/img/checkpointUBW.png', 'dx': 64, 'dy': 164, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'yes1', 'image': './data/img/sprites/sprite_YES_2.png', 'dx': 132, 'dy': 52, 'vx': 0, 'vy': 1, 'etype': cf.ENT_OBSTACLE},
		{'name': 'yes2', 'image': './data/img/sprites/sprite_YES_2.png', 'dx': 264, 'dy': 52, 'vx': 0, 'vy': 1, 'etype': cf.ENT_OBSTACLE},
		{'name': 'yes3', 'image': './data/img/sprites/sprite_YES_2.png', 'dx': 182, 'dy': 112, 'vx': 0, 'vy': 1, 'etype': cf.ENT_OBSTACLE},
		{'name': 'yes4', 'image': './data/img/sprites/sprite_YES_2.png', 'dx': 132, 'dy': 224, 'vx': 0, 'vy': 1, 'etype': cf.ENT_OBSTACLE},
		{'name': 'yes5', 'image': './data/img/sprites/sprite_YES_2.png', 'dx': 182, 'dy': 148, 'vx': 0, 'vy': 1, 'etype': cf.ENT_OBSTACLE}],
	4:
		[{'name': 'checkpoint5', 'image': './data/img/checkpointBW.png', 'dx': 60, 'dy': 124, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'checkpoint6', 'image': './data/img/checkpointBW.png', 'dx': 280, 'dy': 220, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'plat1', 'image': './data/img/plat_o.png', 'dx': 100, 'dy': 70, 'vx': 0, 'vy': 0, 'etype': cf.ENT_BREAKAWAY},
		{'name': 'plat2', 'image': './data/img/plat_o.png', 'dx': 140, 'dy': 70, 'vx': 0, 'vy': 0, 'etype': cf.ENT_BREAKAWAY},
		{'name': 'plath1', 'image': './data/img/plat_o.png', 'dx': 52, 'dy': 166, 'vx': 1, 'vy': 0, 'etype': cf.ENT_PLATFORM},
		{'name': 'spikesU_5_2', 'image': './data/img/spikesU5.png', 'dx': 52, 'dy': 159, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_5_3', 'image': './data/img/spikesU5.png', 'dx': 102, 'dy': 159, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_5_4', 'image': './data/img/spikesU5.png', 'dx': 152, 'dy': 159, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_5_5', 'image': './data/img/spikesU5.png', 'dx': 200, 'dy': 159, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_8_1', 'image': './data/img/spikesU8.png', 'dx': 92, 'dy': 63, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_4_5', 'image': './data/img/spikes4.png', 'dx': 120, 'dy': 116, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_5_1', 'image': './data/img/spikes5.png', 'dx': 132, 'dy': 212, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_5_2', 'image': './data/img/spikes5.png', 'dx': 182, 'dy': 212, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE}],
	5:
		[{'name': 'checkpoint7', 'image': './data/img/checkpointBW.png', 'dx': 122, 'dy': 124, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'reddisc', 'image': './data/img/sprites/sprite_reddisc_1.png', 'dx': 184, 'dy': 188, 'vx': 0, 'vy': 1, 'etype': cf.ENT_OBSTACLE}]
	},
1:
	{1:
		[{'name': 'bus', 'image': './data/img/sprites/sprite_BUS_3.png', 'dx': 320, 'dy': 60, 'vx': 1, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_7_0', 'image': './data/img/spikesU7.png', 'dx': 80, 'dy': 143, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_7_1', 'image': './data/img/spikesU7.png', 'dx': 250, 'dy': 143, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_8_2', 'image': './data/img/spikesU8.png', 'dx': 0, 'dy': 143, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_8_3', 'image': './data/img/spikesU8.png', 'dx': 170, 'dy': 143, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_5_3', 'image': './data/img/spikes5.png', 'dx': 0, 'dy': 108, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_5_4', 'image': './data/img/spikes5.png', 'dx': 50, 'dy': 108, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_5_5', 'image': './data/img/spikes5.png', 'dx': 220, 'dy': 108, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_5_6', 'image': './data/img/spikes5.png', 'dx': 270, 'dy': 108, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE}],
	2:
		[{'name': 'trinket1', 'image': './data/img/sprites/sprite_trinket.png', 'dx': 270, 'dy': 172, 'vx': 0, 'vy': 0, 'etype': cf.ENT_TOKEN},
		{'name': 'man1', 'image': './data/img/sprites/sprite_man_2.png', 'dx': 124, 'dy': 224, 'vx': 0, 'vy': 1, 'etype': cf.ENT_OBSTACLE},
		{'name': 'man2', 'image': './data/img/sprites/sprite_man_2.png', 'dx': 184, 'dy': 214, 'vx': 0, 'vy': 1, 'etype': cf.ENT_OBSTACLE},
		{'name': 'man3', 'image': './data/img/sprites/sprite_man_2.png', 'dx': 240, 'dy': 224, 'vx': 0, 'vy': 1, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_2_0', 'image': './data/img/spikesU2.png', 'dx': 150, 'dy': 91, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_2_1', 'image': './data/img/spikesU2.png', 'dx': 210, 'dy': 91, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_3_0', 'image': './data/img/spikesU3.png', 'dx': 174, 'dy': 37, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_5_6', 'image': './data/img/spikesU5.png', 'dx': 234, 'dy': 47, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_8_4', 'image': './data/img/spikesU8.png', 'dx': 68, 'dy': 37, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE}],
	3:
		[],
	4:
		[],
	5:
		[{'name': 'checkpoint8', 'image': './data/img/checkpointBW.png', 'dx': 12, 'dy': 204, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'green1', 'image': './data/img/sprites/sprite_green_1.png', 'dx': 84, 'dy': 110, 'vx': 1.5, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'green2', 'image': './data/img/sprites/sprite_green_1.png', 'dx': 124, 'dy': 150, 'vx': 1.5, 'vy': 0, 'etype': cf.ENT_OBSTACLE}]
	},
2:
	{1:
		[{'name': 'checkpoint9', 'image': './data/img/checkpointBW.png', 'dx': 152, 'dy': 108, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'checkpointU2', 'image': './data/img/checkpointUBW.png', 'dx': 52, 'dy': 148, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'spikes_3_0', 'image': './data/img/spikes3.png', 'dx': 80, 'dy': 92, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_8_1', 'image': './data/img/spikes8.png', 'dx': 0, 'dy': 92, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE}],
	2:
		[{'name': 'plat3', 'image': './data/img/plat_o.png', 'dx': 200, 'dy': 116, 'vx': 0, 'vy': 0, 'etype': cf.ENT_PLATFORM},
		{'name': 'plat4', 'image': './data/img/plat_o.png', 'dx': 150, 'dy': 52, 'vx': 0, 'vy': 0, 'etype': cf.ENT_PLATFORM},
		{'name': 'spikesU_5_7', 'image': './data/img/spikesU5.png', 'dx': 132, 'dy': 47, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_5_8', 'image': './data/img/spikesU5.png', 'dx': 182, 'dy': 47, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_5_7', 'image': './data/img/spikes5.png', 'dx': 270, 'dy': 140, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_8_2', 'image': './data/img/spikes8.png', 'dx': 190, 'dy': 140, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE}],
	3:
		[{'name': 'checkpointA', 'image': './data/img/checkpointBW.png', 'dx': 32, 'dy': 204, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'spikes_4_6', 'image': './data/img/spikes4.png', 'dx': 170, 'dy': 206, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_6_0', 'image': './data/img/spikes6.png', 'dx': 110, 'dy': 206, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE}],
	4:
		[{'name': 'checkpointB', 'image': './data/img/checkpointBW.png', 'dx': 198, 'dy': 180, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'trinket2', 'image': './data/img/sprites/sprite_trinket.png', 'dx': 40, 'dy': 140, 'vx': 0, 'vy': 0, 'etype': cf.ENT_TOKEN},
		{'name': 'spikesU_3_1', 'image': './data/img/spikesU3.png', 'dx': 164, 'dy': 95, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_5_9', 'image': './data/img/spikesU5.png', 'dx': 68, 'dy': 95, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_2_0', 'image': './data/img/spikes2.png', 'dx': 52, 'dy': 172, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_6_1', 'image': './data/img/spikes6.png', 'dx': 120, 'dy': 172, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE}],
	5:
		[{'name': 'checkpointC', 'image': './data/img/checkpointBW.png', 'dx': 110, 'dy': 188, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'checkpointU3', 'image': './data/img/checkpointUBW.png', 'dx': 202, 'dy': 68, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'spikesU_3_2', 'image': './data/img/spikesU3.png', 'dx': 160, 'dy': 37, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_6_0', 'image': './data/img/spikesU6.png', 'dx': 100, 'dy': 37, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_6_2', 'image': './data/img/spikes6.png', 'dx': 132, 'dy': 204, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE}]
	},
3:
	{0:
		[],
	1:
		[{'name': 'spikesU_4_6', 'image': './data/img/spikesU4.png', 'dx': 140, 'dy': 163, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_8_5', 'image': './data/img/spikesU8.png', 'dx': 56, 'dy': 48, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_8_6', 'image': './data/img/spikesU8.png', 'dx': 184, 'dy': 48, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_3_1', 'image': './data/img/spikes3.png', 'dx': 82, 'dy': 91, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_3_2', 'image': './data/img/spikes3.png', 'dx': 208, 'dy': 91, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_4_7', 'image': './data/img/spikes4.png', 'dx': 140, 'dy': 128, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE}],
	2:
		[{'name': 'checkpointU4', 'image': './data/img/checkpointUBW.png', 'dx': 24, 'dy': 52, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'checkpointU5', 'image': './data/img/checkpointUBW.png', 'dx': 280, 'dy': 52, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'spikesU_4_7', 'image': './data/img/spikesU4.png', 'dx': 140, 'dy': 47, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_7_0', 'image': './data/img/spikes7.png', 'dx': 0, 'dy': 140, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_7_1', 'image': './data/img/spikes7.png', 'dx': 70, 'dy': 140, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_7_2', 'image': './data/img/spikes7.png', 'dx': 180, 'dy': 140, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_7_3', 'image': './data/img/spikes7.png', 'dx': 250, 'dy': 140, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE}],
	3:
		[{'name': 'checkpointD', 'image': './data/img/checkpointBW.png', 'dx': 52, 'dy': 204, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT}],
	4:
		[],
	5:
		[{'name': 'checkpointU6', 'image': './data/img/checkpointUBW.png', 'dx': 186, 'dy': 212, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'stop1', 'image': './data/img/sprites/sprite_STOP_2.png', 'dx': 192, 'dy': 166, 'vx': 0, 'vy': 1.5, 'etype': cf.ENT_OBSTACLE},
		{'name': 'stop2', 'image': './data/img/sprites/sprite_STOP_2.png', 'dx': 42, 'dy': 166, 'vx': 0, 'vy': 1.5, 'etype': cf.ENT_OBSTACLE},
		{'name': 'stop3', 'image': './data/img/sprites/sprite_STOP_2.png', 'dx': 118, 'dy': 50, 'vx': 0, 'vy': 1, 'etype': cf.ENT_OBSTACLE}]
	},
4:
	{1:
		[{'name': 'checkpointE', 'image': './data/img/checkpointBW.png', 'dx': 152, 'dy': 108, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'checkpointU7', 'image': './data/img/checkpointUBW.png', 'dx': 38, 'dy': 84, 'vx': 0, 'vy': 0, 'etype': cf.ENT_CHECKPOINT},
		{'name': 'ghost', 'image': './data/img/sprites/sprite_ghost_1.png', 'dx': 212, 'dy': 128, 'vx': 0, 'vy': 1, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_2_2', 'image': './data/img/spikesU2.png', 'dx': 187, 'dy': 47, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_7_2', 'image': './data/img/spikesU7.png', 'dx': 244, 'dy': 47, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_5_8', 'image': './data/img/spikes5.png', 'dx': 199, 'dy': 129, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE}],
	2:
		[{'name': 'plat5', 'image': './data/img/plat_o.png', 'dx': 132, 'dy': 88, 'vx': 0, 'vy': 0, 'etype': cf.ENT_BREAKAWAY},
		{'name': 'spikesU_4_8', 'image': './data/img/spikesU4.png', 'dx': 180, 'dy': 32, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_3_3', 'image': './data/img/spikes3.png', 'dx': 132, 'dy': 132, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_3_4', 'image': './data/img/spikes3.png', 'dx': 190, 'dy': 132, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_4_8', 'image': './data/img/spikes4.png', 'dx': 50, 'dy': 140, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_5_9', 'image': './data/img/spikes5.png', 'dx': 0, 'dy': 140, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE}]
	},
5:
	{1:
		[{'name': 'walker1', 'image': './data/img/sprites/sprite_walker_2.png', 'dx': 272, 'dy': 204, 'vx': 1.5, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'walker2', 'image': './data/img/sprites/sprite_walker_2.png', 'dx': 284, 'dy': 92, 'vx': 1.5, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_2_3', 'image': './data/img/spikesU2.png', 'dx': 8, 'dy': 47, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_4_9', 'image': './data/img/spikesU4.png', 'dx': 68, 'dy': 47, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_4_A', 'image': './data/img/spikesU4.png', 'dx': 212, 'dy': 47, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikesU_4_B', 'image': './data/img/spikesU4.png', 'dx': 292, 'dy': 47, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE},
		{'name': 'spikes_3_5', 'image': './data/img/spikes3.png', 'dx': 135, 'dy': 124, 'vx': 0, 'vy': 0, 'etype': cf.ENT_OBSTACLE}]
	},
6:
	{1:
		[{'name': 'gc', 'image': './data/img/gamecomplete.png', 'dx': 0, 'dy': 48, 'vx': 0, 'vy': 0, 'etype': cf.ENT_TOKEN}]
	}
}

sprite = MovingEntity(image='./data/img/sprite1.png', vx=1, vy=1, etype=cf.ENT_OBSTACLE)
portal1 = MovingEntity(image='./data/img/warptoken.bmp', vx=0, vy=0, etype=cf.ENT_PORTAL)
portal2 = MovingEntity(image='./data/img/warptoken2.bmp', vx=0, vy=0, etype=cf.ENT_PORTAL)


#ent_list = {x_co: {y_co: [MovingEntity(image=ent['image'], dx=ent['dx'], dy=ent['dy'], vx=ent['vx'], vy=ent['vy'], etype=ent['etype'])\
#							for ent in ent_dict[x_co][y_co]] for y_co in range(7) if (x_co, y_co) in cf.level_array} for x_co in range(7)}
ent_list = {x_co: {y_co: [MovingEntity(**ent) for ent in ent_dict[x_co][y_co]] for y_co in range(7) if (x_co, y_co) in cf.level_array}\
																				for x_co in range(7)}

if __name__ == '__main__':
	backup_path = './storage/ents.json'
	with open(backup_path, 'w') as bkup:
		json.dump(ent_dict, bkup, sort_keys=True, indent=4)
