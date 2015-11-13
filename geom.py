'''
geom | defines a geometry object which contains a collection of rectangles defining each environment

author | Immanuel Washington

Classes
-------
Geometry | creates geometry object
'''
from __future__ import print_function
import pygame
from extrect import ExtRect
import config as cf

class Geometry(object):
	'''
	geometry object
	used to instantiate a container for all rects on screen

	Methods
	-------
	add_rect | adds rect to geometry object
	remove_rect | removes rect from geometry object
	test_rect | checks for intersections between rectangles
	debug_render | tests rendering of rects
	'''
	def __init__(self, rects=None):
		'''
		instantiates rects contained by geometry

		Parameters
		----------
		rects | Optional[list(object)]: list of rect objects in geometry --defaults to None
		'''
		self.rects = [] if rects is None else rects

	def add_rect(self, rect):
		'''
		adds rects to geometry

		Parameters
		----------
		rect | object : rect object
		'''
		self.rects.append(rect)
		print('added')

	def remove_rect(self, rect):
		'''
		removes rects from geometry

		Parameters
		----------
		rect | object : rect object
		'''
		self.rects.remove(rect)
		print('removed')

	def test_rect(self, rect):
		'''
		tests rect placement collisons

		Parameters
		----------
		rect | object : rect object

		Returns
		-------
		dict: dict of values of rects that have collisions
		'''
		d = {cf.HITLEFT: (0, None), cf.HITRIGHT: (0, None), cf.HITTOP: (0, None), cf.HITBOTTOM: (0, None)}
		for r in self.rects:
			coll = ExtRect.as_rect(rect).clip(ExtRect.as_rect(r))
			if not (coll.width or coll.height):
				#No intersection
				continue
			if coll.left == rect.left and d[cf.HITLEFT][0] < coll.width and coll.width < rect.width:
				d[cf.HITLEFT] = (coll.width, r)
			if coll.right == rect.right and d[cf.HITRIGHT][0] < coll.width and coll.width < rect.width:
				d[cf.HITRIGHT] = (coll.width, r)
			if coll.top == rect.top and d[cf.HITTOP][0] < coll.height and coll.height < rect.height:
				d[cf.HITTOP] = (coll.height, r)
			if coll.bottom == rect.bottom and d[cf.HITBOTTOM][0] < coll.height and coll.height < rect.height:
				d[cf.HITBOTTOM] = (coll.height, r)

		return d

	def debug_render(self, surf):
		'''
		attempts to draw each rect on surface object to debug

		Parameters
		----------
		surf | object: surface object
		'''
		for r in self.rects:
			pygame.draw.rect(surf, cf.GEOMDEBUG, ExtRect.as_rect(r), 1)
