'''
bg | defines the basic set of backgrounds

author | Immanuel Washington

Classes
-------
Background | creates background object
'''
import pygame
from img import img_dict

class Background(object):
    '''
    background image object
    used to scroll a background image

    Methods
    -------
    draw | draws background
    scroll | scrolls background picture
    '''
    def __init__(self, image, area, dx, dy):
        '''
        assigns image, area object, and coordinates of background image

        Parameters
        ----------
        image | str: path of background image
        area | object: screen area rect object
        dx | int: x coordinate of image to place bottom-left point
        dy | int: y coordinate of image to place bottom-left point
        '''
        self.image = img_dict[image]
        self.area = area
        self.dx = dx
        self.dy = dy

    def draw(self, surf):
        '''
        draw image as surface object on screen

        Parameters
        ----------
        surf | object: surface object
        '''
        surf.blit(self.image, (0, 0))
        #self.image.scroll(self.dx, self.dy)
        self.scroll()

    def scroll(self):
        '''
        scrolls background image across the screen
        '''
        #Ouch.
        img2 = self.image.copy()
        pa2 = pygame.PixelArray(img2)
        pa = pygame.PixelArray(self.image)
        if self.dx:
            pa[self.dx:, :] = pa[0:-self.dx, :]
            pa[0:self.dx, :] = pa2[-(self.dx + 1):-1, :]
        if self.dy:
            pa[:, self.dy:] = pa[:, 0:-self.dy]
            pa[:, 0:self.dy] = pa2[:,- (self.dy + 1):-1]
        del pa, pa2, img2 #in that order
