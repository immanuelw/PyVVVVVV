'''
img | containes the images for each environment as well as each entity

author | Immanuel Washington
'''
import glob
import pygame
import config as cf

all_imgs = glob.glob('./data/img/*.png') + glob.glob('./data/img/*.bmp') + glob.glob('./data/img/sprites/*.png')
img_dict = {img_name: pygame.image.load(img_name) for img_name in all_imgs}

imgs = {x_coord: {y_coord: pygame.image.load('./data/img/background/background_{x}-{y}_320x240.png'.format(x=x_coord, y=y_coord))\
                    for y_coord in range(7) if (x_coord, y_coord) in cf.level_array} for x_coord in range(7)}
