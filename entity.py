'''
Py6V -- Pythonic VVVVVV
entity -- Various entities

Defines various entities that may be used throughout the game.
'''
import time
import pygame
from pygame.locals import *
from extrect import ExtRect
import config as cf
from img import img_dict

class Entity(pygame.sprite.Sprite):
	#A basic entity inherits all sprite properties.
	def __init__(self, image, dx=0, dy=0, etype=cf.ENT_OBSTACLE):
		self.image = img_dict[image]
		self.rect = ExtRect.wrap(self.image.get_rect())
		self.enttype = etype
		self.dx = dx
		self.dy = dy
		self.rect.bottomleft = (dx, dy)

	def draw(self, surf):
		surf.blit(self.image, self.rect.topleft)

	def SetPos(self, x, y):
		self.rect.center = (x, y)

	def SetSpike(self, x, y):
		self.rect.bottomleft = (x, y)

	def SetSpikeU(self, x, y):
		self.rect.topleft = (x, y)

class MovingEntity(Entity):
	def __init__(self, image, dx=0, dy=0, vx=0, vy=0, etype=cf.ENT_OBSTACLE):
		Entity.__init__(self, image, dx, dy, etype)
		self.vx = vx
		self.vy = vy

	def collide_area(self, area):
		if self.rect.left < area.left or self.rect.right > area.right:
			self.vx = -self.vx
		if self.rect.top < area.top or self.rect.bottom > area.bottom:
			self.vy = -self.vy

	def collide(self, geom):
		res = geom.test_rect(self.rect)
		for key, val in res.iteritems():
			depth, rect = val
			if depth != 0 and getattr(rect, 'ent', None) != self:
				if key in (cf.HITLEFT, cf.HITRIGHT):
					self.vx = -self.vx
				if key in (cf.HITTOP, cf.HITBOTTOM):
					self.vy = -self.vy

	def move(self):
		self.rect.move_ip(self.vx, self.vy)

	def update(self, gamearea, env=None):
		self.collide_area(gamearea)
		if env:
			self.collide(env.geometry)
		self.move()

class AnimatingEntity(Entity):
	def __init__(self, images, frametime, etype=cf.ENT_OBSTACLE):
		Entity.__init__(self, images[0], etype)
		self.images = images
		self.idx = 0
		self.frametime = frametime
		self.nextframe = time.time() + self.frametime

	def animate(self):
		if time.time() > self.nextframe:
			self.idx += 1
			if self.idx >= len(self.images):
				self.idx = 0 #loops character
			self.image = self.images[idx]
			self.nextframe = self.frametime + time.time()

	def update(self, gamearea, env=None):
		self.animate()

class MovingAnimatingEntity(MovingEntity, AnimatingEntity):
	def __init__(self, images, frametime, dx, dy, vx, vy, etype=cf.ENT_OBSTACLE):
		MovingEntity.__init__(self, images[0], dx, dy, vx, vy, etype)
		AnimatingEntity.__init__(self, images, frametime, etype)

	def update(self, gamearea, env=None):
		MovingEntity.update(self, gamearea, env)
		AnimatingEntity.update(self, gamearea, env)

class ScriptedEntity(Entity):
	def __init__(self, image, dx=0, dy=0):
		Entity.__init__(self, image, dx, dy, etype=cf.ENT_SCRIPTED)

	def set_solid_in(self, solid, env):
		if solid:
			env.geometry.add_rect(self.rect)
			self.rect.ent = self
		else:
			env.geometry.remove_rect(self.rect)

	def on_char_collide(self, char):
		pass
