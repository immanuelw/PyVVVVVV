'''
env | defines the environment object which holds all entities on the screen

author | Immanuel Washington

Classes
-------
Environment | creates environment object
'''
import config as cf
from img import img_dict

class Environment(object):
	'''
	environment object
	used to instantiate a container for all entities on screen and main image

	Methods
	-------
	draw | draws environment
	add_entity | adds entity to environment
	remove_entity | removes entity from environment
	update | updates all entities
	'''
	def __init__(self, area, background, geometry, image, entities):
		'''
		assigns area object, geometry object, image, background object, and list of entities

		Parameters
		----------
		area | object: screen area rect object
		background | background object
		geometry | object: geometry object
		image | object: level image object
		entities | list: list of entities
		'''
		self.area = area
		self.background = background
		self.geometry = geometry
		self.image = image
		self.entities = set(entities)
		self.characters = set()
		self.checkpoints = set()
		self.do_debug_draw = False
		for ent in self.entities:
			#Call it a hack...
			if ent.enttype == cf.ENT_PLATFORM:
				geometry.add_rect(ent.rect)
				ent.rect.ent = ent
			elif ent.enttype == cf.ENT_BREAKAWAY:
				geometry.add_rect(ent.rect)
				ent.rect.ent = ent
			elif ent.enttype == cf.ENT_CHARACTER:
				self.characters.add(ent)
			elif ent.enttype == cf.ENT_CHECKPOINT:
				self.checkpoints.add(ent)

	def draw(self, surf):
		'''
		draw image as surface object on screen

		Parameters
		----------
		surf | object: surface object
		'''
		self.background.draw(surf)
		surf.blit(self.image, (0, 0))
		for ent in self.entities:
			ent.draw(surf)

	def add_entity(self, ent):
		'''
		adds entity to environment
		adds entity rect to geometry

		Parameters
		----------
		ent | object: entity object
		'''
		if ent.enttype == cf.ENT_PLATFORM:
			self.geometry.add_rect(ent.rect)
			ent.rect.ent = ent
		elif ent.enttype == cf.ENT_CHARACTER:
			self.characters.add(ent)
		self.entities.add(ent)

	def remove_entity(self, ent):
		'''
		removes entity from environment
		removes entity rect from geometry

		Parameters
		----------
		ent | object: entity object
		'''
		self.geometry.remove_rect(ent.rect)
		self.characters.discard(ent)
		self.entities.discard(ent)

	def update(self):
		'''
		updates all entities contained in environment
		changes checkpoint image
		'''
		remove_ents = []
		char = tuple(self.characters)[0]
		for ent in self.entities:
			if ent.enttype == cf.ENT_CHECKPOINT:
				if char.last_checkpoint == ent.name:
					if ent.image == img_dict['./data/img/checkpointBW.png']:
						ent.image = img_dict['./data/img/checkpoint.png']
					elif ent.image == img_dict['./data/img/checkpointUBW.png']:
						ent.image = img_dict['./data/img/checkpointU.png']
				else:
					if ent.image == img_dict['./data/img/checkpoint.png']:
						ent.image = img_dict['./data/img/checkpointBW.png']
					elif ent.image == img_dict['./data/img/checkpointU.png']:
						ent.image = img_dict['./data/img/checkpointUBW.png']
			elif ent.enttype == cf.ENT_TOKEN:
				if ent.name in char.tokens:
					ent.image = img_dict['./data/img/empty.png']
			elif ent.enttype == cf.ENT_BREAKAWAY:
				is_breaking = getattr(ent, 'is_breaking', False)
				if is_breaking:
					ent.counter +=1
					if ent.counter == 15:
						ent.image = img_dict['./data/img/plat_p.png']
					elif ent.counter == 30:
						ent.counter = 0
						ent.is_breaking = False
						ent.image = img_dict['./data/img/plat_o.png']
						remove_ents.append(ent)
			ent.update(self.area, self)

		for ent in remove_ents:
			self.remove_entity(ent)
