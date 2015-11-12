'''
Py6V -- Pythonic VVVVVV
character -- Character sprites

Defines the sprites which are used to render characters.
'''
from __future__ import print_function
import time
import random
import pygame
from extrect import ExtRect
import config as cf

IMG_CHAR = pygame.image.load('./data/img/char.png')
IMG_CHAR_SAD = pygame.image.load('./data/img/char_sad.png')
IMG_CHAR_WALKING = pygame.image.load('./data/img/char_walking.png')
IMG_CHAR_WALKING_SAD = pygame.image.load('./data/img/char_walking_sad.png')

class Character(pygame.sprite.Sprite):
	def __init__(self, color, x, y, x_co=1, y_co=3, pulsation=0, pulse_rate=1, enttype=cf.ENT_CHARACTER):
		pygame.sprite.Sprite.__init__(self)
		self.frame1 = IMG_CHAR.copy()
		self.frame2 = IMG_CHAR_WALKING.copy()
		self.next_frame = 0
		self.image = self.frame1
		self.rect = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
		self.rect.bottomleft = (x, y)
		self.left = False #Heading left?
		self.is_flipped = False #Inverted?
		self.old_color = cf.WHITE
		self.base_color = color
		self.pulsation = pulsation
		self.pulse_rate = pulse_rate
		self.pulse_cur = 0
		self.is_pulse_rising = True
		self.is_dead = False
		self.is_sad = False
		self.was_sad = False
		self.next_revive = 0
		self.vx = 0
		self.vy = 0
		self.check_x = 1 #stores x_co if last checkpoint
		self.check_y = 3
		self.x_co = x_co
		self.y_co = y_co
		#self.conveyerspeed = 3
		self.on_floor = False #vy constrained to 0
		self.on_wall = False #vx constrained to 0
		self.go_left = False #Apply negative accel x
		self.go_right = False #Apply positive accel x
		self.standingon = None #An entity whose vx,vy is added to ours
		self.checkpoint = None
		self.teleportpoint = None
		self.tokens = 0
		#self.breakaway = 0
		self.set_color(color)
		self.enttype = enttype

	def draw(self, surf):
		try:
			surf.blit(self.image, self.rect.topleft)
		except TypeError:
			print('The forward-mentioned rect is', self.rect, 'and the position is', self.rect.topleft)
			print('Now don\'t ask me why this is happening, I don\'t really know yet.')
			raise

	def set_color(self, color):
		for frm in (self.frame1, self.frame2):
			pa = pygame.PixelArray(frm)
			pa.replace(self.old_color, color)
			del pa
		self.old_color = color

	def set_frame_color(self, frm, color):
		pa = pygame.PixelArray(frm)
		pa.replace(self.old_color, color)
		del pa

	def set_base_color(self, color):
		self.set_color(color)
		self.base_color = color

	def set_pulsation(self, pulsation):
		self.pulsation = pulsation

	def set_pulse_rate(self, pulse_rate):
		self.pulse_rate = pulse_rate

	def set_dir(self, left):
		if left != self.left:
			self.left = left
			self.frame1 = pygame.transform.flip(self.frame1, True, False)
			self.frame2 = pygame.transform.flip(self.frame2, True, False)

	def set_left(self):
		self.set_dir(True)

	def set_right(self):
		self.set_dir(False)

	def flip(self):
		pygame.mixer.Sound('./data/snd/sfx/jump.wav').play()
		self.is_flipped = not self.is_flipped
		self.frame1 = pygame.transform.flip(self.frame1, False, True)
		self.frame2 = pygame.transform.flip(self.frame2, False, True)

	def set_sad(self, sad):
		self.is_sad = sad
		if sad:
			self.frame1 = IMG_CHAR_SAD.copy()
			self.frame2 = IMG_CHAR_WALKING_SAD.copy()
		else:
			self.frame1 = IMG_CHAR.copy()
			self.frame2 = IMG_CHAR_WALKING.copy()
		color = self.old_color
		self.old_color = cf.WHITE
		self.set_color(color)
		self.frame1 = pygame.transform.flip(self.frame1, self.left, self.is_flipped)
		self.frame2 = pygame.transform.flip(self.frame2, self.left, self.is_flipped)

	def refresh_frames(self):
		if self.is_sad:
			self.set_sad(False)
			self.set_sad(True)
		else:
			self.set_sad(True)
			self.set_sad(False)

	def set_on_floor(self, on_floor):
		self.on_floor = on_floor
		if on_floor:
			self.vy = 0
			self.next_frame = time.time() + cf.WALK_ANIM_TIME

	def set_on_wall(self, on_wall):
		self.on_wall = on_wall
		if on_wall:
			self.vx = 0

	def set_go_left(self, go_left):
		self.go_left = go_left
		if go_left:
			self.next_frame = time.time() + cf.WALK_ANIM_TIME

	def set_go_right(self, go_right):
		self.go_right = go_right
		if go_right:
			self.next_frame = time.time() + cf.WALK_ANIM_TIME

	def set_standing_on(self, ent):
		self.standingon = ent

	def set_spike(self, x, y):
		self.rect.bottomleft = (x, y)

	def set_vel(self, vx, vy):
		if not self.on_wall:
			self.vx = vx
		if not self.on_floor:
			self.vy = vy

	def move(self):
		if self.standingon:
			self.rect.move_ip(self.standingon.vx + self.vx, self.standingon.vy + self.vy)
		else:
			self.rect.move_ip(self.vx, self.vy)

	def move_delta(self, x, y):
		self.rect.move_ip(x, y)

	def kill(self):
		if not self.is_dead:
			self.is_dead = True
			self.was_sad = self.is_sad
			self.set_sad(True)
			pygame.mixer.Sound('./data/snd/sfx/hurt.wav').play()
			self.set_color(cf.DEAD)
			self.set_frame_color(self.frame2, cf.DEADDARK)
			self.next_frame = time.time() + random.uniform(cf.DEAD_FLICKER_MIN, cf.DEAD_FLICKER_MAX)
			self.next_revive = time.time() + cf.REVIVE_TIME

	def revive(self):
		if self.is_dead:
			self.is_dead = False
			self.is_sad = self.was_sad
			self.refresh_frames()
			self.x_co = self.check_x
			self.y_co = self.check_y
			#print(self.x_co, self.check_x)
			self.restore_checkpoint()
			#self.breakaway = 0

	def restore_checkpoint(self):
		if self.checkpoint is not None:
			if self.checkpoint[1] != self.is_flipped:
				self.flip()
			self.rect.center = self.checkpoint[0]
			self.vx = 0
			self.vy = 0
			self.set_on_floor(False)
			self.set_on_wall(False)

	def set_checkpoint_here(self):
		#pygame.mixer.Sound('./data/snd/sfx/save.wav').play()
		self.check_x = self.x_co
		self.check_y = self.y_co
		self.checkpoint = (self.rect.center, self.is_flipped)
		#self.is_checkpoint_set(True)

	def set_checkpoint(self, x, y):
		self.checkpoint = ((x, y), self.is_flipped)

	def teleport(self):
		pygame.mixer.Sound('./data/snd/sfx/teleport.wav').play()
		if self.teleportpoint is not None:
			if self.teleportpoint[1] != self.is_flipped:
				self.flip()
			self.rect.center = self.teleportpoint[0]
			self.vx = 0
			self.vy = 0
			self.set_on_floor(False)
			self.set_on_wall(False)

	#def conveyer(self, on_floor):
	#	self.on_floor = on_floor
	#	if on_floor:
	#		self.vx += self.conveyerspeed
	#		self.next_frame = time.time() + cf.WALK_ANIM_TIME

	#def breakaway(self):
		#want it to remove images in order(or place), and then finally remove rect.

	def accelerate(self):
		if self.on_wall:
			self.vx = 0
		else:
			ax = ((1 if self.go_right else 0) - (1 if self.go_left else 0)) * cf.XACCEL
			if ax == 0: #We want to stop moving...
				if self.vx > 0:
					ax = -cf.XDECEL
				elif self.vx < 0:
					ax = cf.XDECEL
			self.vx += ax

			#Clip to terminal velocity
			if self.vx > cf.XTERM:
				self.vx = cf.XTERM
			elif self.vx < -cf.XTERM:
				self.vx = -cf.XTERM

		#Similar logic (but easier) logic on y
		if self.on_floor:
			self.vy = 0
		else:
			self.vy += cf.YGRAV * (-1 if self.is_flipped else 1)
			if self.vy > cf.YTERM:
				self.vy = cf.YTERM
			elif self.vy < -cf.YTERM:
				self.vy = -cf.YTERM

	def normalize(self, gamearea):#loops character
		if self.is_flipped:#y
			if self.rect.bottom < 0:
				self.y_co += 1
				self.rect.top = gamearea.bottom
		else:
			if self.rect.top > gamearea.bottom:
				self.y_co -= 1
				self.rect.bottom = 0
		if self.rect.right < 0:#x
			self.x_co -= 1
			self.rect.left = gamearea.right
		if self.rect.left > gamearea.right:
			self.x_co += 1
			self.rect.right = 0

	def set_sprite(self):
		#if self.vx and not self.vy:
		if self.on_floor and self.vx:
			if time.time() > self.next_frame:
				self.next_frame = time.time() + cf.WALK_ANIM_TIME
				if self.image == self.frame1:
					self.image = self.frame2
				else:
					self.image = self.frame1
		else:
			self.image = self.frame1

	def pulsate(self):
		if self.pulsation != 0:
			if self.is_pulse_rising:
				if self.pulse_cur >= self.pulsation:
					self.is_pulse_rising = False
				else:
					self.pulse_cur += self.pulse_rate
			else:
				if self.pulse_cur <= 0:
					self.is_pulse_rising = True
				else:
					self.pulse_cur -= self.pulse_rate
			self.set_color(self.base_color + pygame.Color(int(self.pulse_cur), int(self.pulse_cur), int(self.pulse_cur)))

	def flicker(self):
		if time.time() > self.next_frame:
			self.next_frame = time.time() + random.uniform(cf.DEAD_FLICKER_MIN, cf.DEAD_FLICKER_MAX)
			if self.image == self.frame1:
				self.image = self.frame2
			else:
				self.image = self.frame1
		if time.time() > self.next_revive:
			self.revive()

	def collide(self, geom):
		#We're doing a preemptive collision test now -- the below code was unsatisfactory
		colinfo = geom.test_rect(self.rect)
		if colinfo[cf.HITTOP][0] and self.is_flipped: #One does not simply headstand!
			if getattr(colinfo[cf.HITTOP][1], 'obstacle', False):
				self.kill()
			ent = getattr(colinfo[cf.HITTOP][1], 'ent', None)
			if ent:
				self.set_standing_on(ent)
			self.move_delta(0, colinfo[cf.HITTOP][0])
			self.set_on_floor(True)

		if colinfo[cf.HITBOTTOM][0] and not self.is_flipped:
			if getattr(colinfo[cf.HITBOTTOM][1], 'obstacle', False):
				self.kill()
			ent = getattr(colinfo[cf.HITBOTTOM][1], 'ent', None)
			if ent:
				self.set_standing_on(ent)
			self.move_delta(0, -colinfo[cf.HITBOTTOM][0])
			self.set_on_floor(True)

		if not (colinfo[cf.HITTOP][0] or colinfo[cf.HITBOTTOM][0]):
			#Hey, there's the possibility we're no longer standing on the floor...lessee
			exprect = self.rect.inflate(2, 2)
			col = geom.test_rect(exprect)
			if not (col[cf.HITTOP][0] or col[cf.HITBOTTOM][0]):
				self.set_on_floor(False)
				self.set_standing_on(None)

		#Update with new collision info
		if colinfo[cf.HITTOP][0] or colinfo[cf.HITBOTTOM][0]:
			colinfo = geom.test_rect(self.rect)

		if colinfo[cf.HITLEFT][0]:
			if getattr(colinfo[cf.HITLEFT][1], 'obstacle', False):
				self.kill()
			self.move_delta(colinfo[cf.HITLEFT][0], 0)
			self.set_on_wall(True)

		if colinfo[cf.HITRIGHT][0]:
			if getattr(colinfo[cf.HITRIGHT][1], 'obstacle', False):
				self.kill()
			self.move_delta(-colinfo[cf.HITRIGHT][0], 0)
			self.set_on_wall(True)

		if not (colinfo[cf.HITLEFT][0] or colinfo[cf.HITRIGHT][0]):
			#Hey, there's the possibility we're not hitting the wall
			exprect = self.rect.inflate(2, 2)
			col = geom.test_rect(exprect)
			if not (col[cf.HITLEFT][0] or col[cf.HITRIGHT][0]):
				self.set_on_wall(False)

		##Test for any collisions just outside our rect right now, and set appropriate movement constraints
		#exprect = self.rect.inflate(2, 2)
		#colinfo = geom.test_rect(exprect)

		#if colinfo[cf.HITTOP][0] or colinfo[cf.HITBOTTOM][0]:
		#	self.set_on_floor(True)

		#if colinfo[cf.HITLEFT][0] or colinfo[cf.HITRIGHT][0]:
		#	self.set_on_wall(True)

		##Now interpolate any remaining movement axes over time to the next collision
		#nextrect = self.rect.move(self.vx, self.vy) #FIXME -- lerp
		#colinfo = geom.test_rect(nextrect)

		#if colinfo[cf.HITTOP][0] and self.vy < 0:
		#	self.vy += colinfo[cf.HITTOP][0]
		#if colinfo[cf.HITBOTTOM][0] and self.vy > 0:
		#	self.vy -= colinfo[cf.HITBOTTOM][0]
		#if colinfo[cf.HITLEFT][0] and self.vx < 0:
		#	self.vx += colinfo[cf.HITLEFT][0]
		#if colinfo[cf.HITRIGHT][0] and self.vx > 0:
		#	self.vx -= colinfo[cf.HITRIGHT][0]

	def collide_entities(self, ents):
		for ent in ents:
			if ent.enttype == cf.ENT_CHARACTER:
				continue #Never collide

			coll = self.rect.clip(ExtRect.as_rect(ent.rect))
			if not (coll.width or coll.height):
				continue #Not colliding

			if ent.enttype == cf.ENT_PLATFORM:
				#As a hack, this kind of entity usually inserts its own rect into the Geometry's
				#rects (and updates it in place), so we don't have to worry about collisions.
				#See collide for more info.
				pass
			elif ent.enttype == cf.ENT_OBSTACLE:
				self.kill()
			elif ent.enttype == cf.ENT_TOKEN:
				pygame.mixer.Sound('./data/snd/sfx/souleyeminijingle.wav').play()
				self.tokens += 1
			elif ent.enttype == cf.ENT_CHECKPOINT:
				self.set_checkpoint_here()
			elif ent.enttype == cf.ENT_SCRIPTED:
				ent.on_char_collide(self)
			elif ent.enttype == cf.ENT_PORTAL:
				self.teleport()
			#elif ent.enttype == cf.ENT_INVERTER:
			#	self.flip()
			#elif ent.enttype == cf.ENT_CONVEYER_A:
			#	self.conveyer()
			#elif ent.enttype == cf.ENT_CONVEYER_B:
			#	self.conveyer()
			#elif ent.enttype == cf.ENT_BREAKAWAY:
			#	self.breakaway += 1
			elif ent.enttype == cf.ENT_EMPTY:
				pass

	def update(self, gamearea, env=None):
		if self.is_dead:
			self.flicker()
		else:
			self.accelerate()
			self.move()
			self.normalize(gamearea)
			self.pulsate()
			self.set_sprite()
		if env:
			self.collide(env.geometry)
			self.collide_entities(env.entities)
