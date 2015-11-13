'''
extrect | defines an extended rect object that can have atrributes assigned to it

author | Immanuel Washington

Classes
-------
Entity | creats base entity
MovingEntity | entity object that can move
AnimatingEntity | entity object that changes its image
MovingAnimatingEntity | entity object that can move and change its image
ScriptedEntity | entity object that follows scripted sequence
'''
import time
import pygame
from extrect import ExtRect
import config as cf
from img import img_dict

class Entity(pygame.sprite.Sprite):
	'''
	base entity object which inherits all properties of sprites

	Methods
	-------
	draw | draws entity onto surface
	'''
	def __init__(self, image, dx=0, dy=0, etype=cf.ENT_OBSTACLE, name=''):
		'''
		instantiates an entity object by assigning its image and position

		Parameters
		----------
		image | str: path to image file
		dx | Optional[int]: x coordinate of object to place bottom-left point --defaults to 0
		dy | Optional[int]: y coordinate of object to place bottom-left point --defaults to 0
		etype | Optional[int]: value of entity assigned in config file --defaults to cf.ENT_OBSTACLE
		name | Optional[str]: id of entity --defaults to ''
		'''
		self.image = img_dict[image]
		self.rect = ExtRect.wrap(self.image.get_rect())
		self.enttype = etype
		self.dx = dx
		self.dy = dy
		self.rect.bottomleft = (dx, dy)
		self.name = name

	def draw(self, surf):
		'''
		draw image as surface object on screen

		Parameters
		----------
		surf | object: surface object
		'''
		surf.blit(self.image, self.rect.topleft)

class MovingEntity(Entity):
	'''
	moving entity object which inherits all properties of entity object

	Methods
	-------
	collide_area | checks for collision with edge of screen
	collide | checks for entity collisions
	move | moves entity according to its velocity
	update | updates entity
	'''
	def __init__(self, image, dx=0, dy=0, vx=0, vy=0, etype=cf.ENT_OBSTACLE, name=''):
		'''
		instantiates a moving entity object by assigning its image, position, and velocity

		Parameters
		----------
		image | str: path to image file
		dx | Optional[int]: x coordinate of object to place bottom-left point --defaults to 0
		dy | Optional[int]: y coordinate of object to place bottom-left point --defaults to 0
		vx | Optional[int]: x velocity of object --defaults to 0
		vy | Optional[int]: y velocity of object --defaults to 0
		etype | Optional[int]: value of entity assigned in config file --defaults to cf.ENT_OBSTACLE
		name | Optional[str]: id of entity --defaults to ''
		'''
		Entity.__init__(self, image, dx, dy, etype, name)
		self.vx = vx
		self.vy = vy

	def collide_area(self, area):
		'''
		checks if entity has collided with edge of screen and reverses direction of velocity

		Parameters
		----------
		area | object: area object
		'''
		if self.rect.left < area.left or self.rect.right > area.right:
			self.vx = -self.vx
		if self.rect.top < area.top or self.rect.bottom > area.bottom:
			self.vy = -self.vy

	def collide(self, geom):
		'''
		checks for collision between entities and other objects in geometry

		Parameters
		----------
		geom | object: geometry object
		'''
		res = geom.test_rect(self.rect)
		for key, val in res.iteritems():
			depth, rect = val
			if depth != 0 and getattr(rect, 'ent', None) != self:
				if key in (cf.HITLEFT, cf.HITRIGHT):
					self.vx = -self.vx
				if key in (cf.HITTOP, cf.HITBOTTOM):
					self.vy = -self.vy

	def move(self):
		'''
		moves object's rect according to its velocity
		'''
		self.rect.move_ip(self.vx, self.vy)

	def update(self, gamearea, env=None):
		'''
		updates entity

		Parameters
		----------
		gamearea | object: area object
		env | Optional[object]: environment object --defaults to None
		'''
		self.collide_area(gamearea)
		if env:
			self.collide(env.geometry)
		self.move()

class AnimatingEntity(Entity):
	'''
	animated entity object which inherits all properties of entity object

	Methods
	-------
	animate | changes images for entity in a cycle
	update | updates entity
	'''
	def __init__(self, images, frame_time, etype=cf.ENT_OBSTACLE, name=''):
		'''
		instantiates an animated entity object by assigning images and frame_time

		Parameters
		----------
		images | list[object]: list of image objects
		frame_time | float: amount of time between frames
		etype | Optional[int]: value of entity assigned in config file --defaults to cf.ENT_OBSTACLE
		name | Optional[str]: id of entity --defaults to ''
		'''
		Entity.__init__(self, images[0], etype, name)
		self.images = images
		self.idx = 0
		self.frame_time = frame_time
		self.next_frame = time.time() + self.frame_time

	def animate(self):
		'''
		cycles through images
		'''
		if time.time() > self.next_frame:
			self.idx += 1
			if self.idx >= len(self.images):
				self.idx = 0 #loops character
			self.image = self.images[idx]
			self.next_frame = self.frame_time + time.time()

	def update(self, gamearea, env=None):
		'''
		updates entity

		Parameters
		----------
		gamearea | object: area object
		env | Optional[object]: environment object --defaults to None
		'''
		self.animate()

class MovingAnimatingEntity(MovingEntity, AnimatingEntity):
	'''
	moving animated entity object which inherits all properties of moving entity object and animated entity object

	Methods
	-------
	update | updates entity
	'''
	def __init__(self, images, frame_time, dx, dy, vx, vy, etype=cf.ENT_OBSTACLE, name=''):
		'''
		instantiates a moving animated entity object by assigning its image, position, and velocity
		also instantiates by assigning images and frame_time

		Parameters
		----------
		images | list[object]: list of image objects
		frame_time | float: amount of time between frames
		dx | Optional[int]: x coordinate of object to place bottom-left point --defaults to 0
		dy | Optional[int]: y coordinate of object to place bottom-left point --defaults to 0
		vx | Optional[int]: x velocity of object --defaults to 0
		vy | Optional[int]: y velocity of object --defaults to 0
		etype | Optional[int]: value of entity assigned in config file --defaults to cf.ENT_OBSTACLE
		name | Optional[str]: id of entity --defaults to ''
		'''
		MovingEntity.__init__(self, images[0], dx, dy, vx, vy, etype, name)
		AnimatingEntity.__init__(self, images, frame_time, etype, name)

	def update(self, gamearea, env=None):
		'''
		updates entity

		Parameters
		----------
		gamearea | object: area object
		env | Optional[object]: environment object --defaults to None
		'''
		MovingEntity.update(self, gamearea, env)
		AnimatingEntity.update(self, gamearea, env)

class ScriptedEntity(Entity):
	'''
	scripted entity object which inherits all properties of entity object

	Methods
	-------
	set_solid_in | sets entity rect
	on_char_collide | decides what to do when colliding with character
	'''
	def __init__(self, image, dx=0, dy=0, name=''):
		'''
		instantiates a scripted entity object by assigning its image and position

		Parameters
		----------
		image | str: path to image file
		dx | Optional[int]: x coordinate of object to place bottom-left point --defaults to 0
		dy | Optional[int]: y coordinate of object to place bottom-left point --defaults to 0
		name | Optional[str]: id of entity --defaults to ''
		'''
		Entity.__init__(self, image, dx, dy, etype=cf.ENT_SCRIPTED, name='')

	def set_solid_in(self, solid, env):
		'''
		checks if entity is solid and adds rect to environment if so

		solid | bool: if scripted entity is solid
		env | object: environment object
		'''
		if solid:
			env.geometry.add_rect(self.rect)
			self.rect.ent = self
		else:
			env.geometry.remove_rect(self.rect)

	def on_char_collide(self, char):
		'''
		checks if entity collides with character
		does nothing

		Parameters
		----------
		char | object: character object
		'''
		pass
