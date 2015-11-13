'''
Py6V -- Pythonic VVVVVV
env -- Environment

Defines the Environment.

An Environment is instantiated once per Map tile, including scrolling
tiles (handled by ScrollingEnvironments). It contains all the geometry
and rendering data needed to render that one tile, along with a
collection of all the entities in that tile.
'''
import pygame
#from pygame.locals import *
import config as cf
from img import img_dict

class Environment(object):
	def __init__(self, area, geometry, image, background, entities):
		self.area = area
		self.geometry = geometry
		self.image = image
		self.background = background
		self.entities = set(entities)
		self.characters = set()
		self.checkpoints = set()
		self.dodebugdraw = False
		for ent in self.entities:
			#Call it a hack...
			if ent.enttype == cf.ENT_PLATFORM:
				geometry.add_rect(ent.rect)
				ent.rect.ent = ent
			elif ent.enttype == cf.ENT_CHARACTER:
				self.characters.add(ent)
			elif ent.enttype == cf.ENT_CHECKPOINT:
				self.checkpoints.add(ent)

	def draw(self, surf):
		self.background.draw(surf)
		surf.blit(self.image, (0, 0))
		for ent in self.entities:
			ent.draw(surf)

	def add_entity(self, ent):
		if ent.enttype == cf.ENT_PLATFORM:
			self.geometry.add_rect(ent.rect)
			ent.rect.ent = ent
		elif ent.enttype == cf.ENT_CHARACTER:
			self.characters.add(ent)
		self.entities.add(ent)

	def remove_entity(self, ent):
		self.geometry.remove_rect(ent.rect)
		self.characters.discard(ent)
		self.entities.discard(ent)

	def update(self):
		char = tuple(self.characters)[0]
		for ent in self.entities:
			#if ent in self.checkpoints:
			#	if ent.rect.bottom == char.rect.bottom + 16 and char.rect.left <= ent.rect.right and char.rect.left >= ent.rect.left:
			#		ent.image = img_dict['./data/img/checkpoint.png']
			#	else:
			#		ent.image = img_dict['./data/img/checkpointBW.png']
			ent.update(self.area, self)
