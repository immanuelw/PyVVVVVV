'''
Py6V -- Pythonic VVVVVV
geom -- Geometry

Defines the Geometry class.

Because of our simplistic world, a Geometry is a region defined by a collection
of rectangles. At any time another rectangle can be tested against it, and it
will return a dict mapping a HIT* constant to the tuple (penetration, rect),
such that if the rectangle is moved by penetration pixels to the opposite
direction (e.g. right for HITLEFT), the rectangle will no longer be inside (but
will be flush with) the surface. If two opposing sides are penetrating, there is
no way the rectangle can fit into the geometry. The rect itself is returned so
that any attributes stored on it may be accessed. An entry (0, None) represents
no hit on that axis.
'''
import pygame
from pygame.locals import *
from extrect import ExtRect
import config as cf

class Geometry(object):
	def __init__(self, rects=None):
		self.rects = [] if rects is None else rects

	def add_rect(self, rect):
		self.rects.append(rect)

	def remove_rect(self, rect):
		try:
			self.rects.remove(rect)
		except ValueError:
			pass

	def test_rect(self, rect):
		d = {cf.HITLEFT: (0, None), cf.HITRIGHT: (0, None), cf.HITTOP: (0, None), cf.HITBOTTOM: (0, None)}
		for r in self.rects:
			coll = ExtRect.as_rect(rect).clip(ExtRect.as_rect(r))
			if not (coll.width or coll.height):
				#No intersection
				continue
			if coll.left == rect.left and d[cf.HITLEFT][0] < coll.width and coll.width < rect.width:
				d[cf.HITLEFT]=(coll.width, r)
			if coll.right == rect.right and d[cf.HITRIGHT][0] < coll.width and coll.width < rect.width:
				d[cf.HITRIGHT] = (coll.width, r)
			if coll.top == rect.top and d[cf.HITTOP][0] < coll.height and coll.height < rect.height:
				d[cf.HITTOP] = (coll.height, r)
			if coll.bottom == rect.bottom and d[cf.HITBOTTOM][0] < coll.height and coll.height < rect.height:
				d[cf.HITBOTTOM] = (coll.height, r)

		return d

	def debug_render(self, surf):
		for r in self.rects:
			pygame.draw.rect(surf, cf.GEOMDEBUG, ExtRect.as_rect(r), 1)
