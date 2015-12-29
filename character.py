'''
character | creates character object

author | Immanuel Washington

Classes
---------
Character | defines character object
'''
from __future__ import print_function
import time
import random
import pygame
import config as cf
import levels as lv
from extrect import ExtRect
from img import img_dict

IMG_CHAR = pygame.image.load('./data/img/char.png')
IMG_CHAR_SAD = pygame.image.load('./data/img/char_sad.png')
IMG_CHAR_WALKING = pygame.image.load('./data/img/char_walking.png')
IMG_CHAR_WALKING_SAD = pygame.image.load('./data/img/char_walking_sad.png')

class Character(pygame.sprite.Sprite):
    '''
    instantaties character class that inherits all of pygame Sprite's properties

    Methods
    -------
    draw | draws character on screen
    set_color | sets character color
    set_frame_color | set character color
    set_base_color | sets character's base color
    set_pulsation | set pulsation
    set_pulse_rate | set pulse rate
    set_dir | sets character image direction
    set_left | changes character image to the left
    set_right | changes character image to the right
    flip | flips character model and changes gravity
    set_sad | sets image of character to sad or happy
    refresh_frames | switches back and forth between happy and sad images
    set_on_floor | set bool value to on floor
    set_on_wall | set bool value to on wall
    set_go_left | set bool value to left
    set_go_right | set bool value to right
    set_standing_on | set entity to add velocity to character
    set_vel | set velocity of character
    move | moves character with extra velocity
    move_delta | moves character
    kill | kill character
    revive | revive character
    restore_checkpoint | restore character position to last checkpoint
    set_checkpoint_here | set checkpoint position
    get_token | adds token to character
    teleport | teleports character to certain position
    accelerate | accelerates character
    normalize | changes screen upon moving past area boundaries
    set_sprite | sets sprite image
    pulsate | sets pulsate colors
    flicker | sets flicker colors and revives character
    collide | checks for collisions with rect objects
    collide_entities | checks for collisions with entity objects
    update | updates character object
    '''
    def __init__(self, color, x, y, x_co=1, y_co=3, check_x=1, check_y=3, checkpoint=((50, 188), False), last_checkpoint=None,
                        pulsation=0, pulse_rate=1, tokens=None, enttype=cf.ENT_CHARACTER):
        '''
        initializes attributes for the character object

        Parameters
        ----------
        color | object: color object
        x | int: x coordinate of object to place bottom-left point
        y | int: y coordinate of object to place bottom-left point
        x_co | Optional[int]: x value of level array -- defaults to 1
        y_co | Optional[int]: y value of level array -- defaults to 3
        check_x | Optional[int]: x value of level array for checkpoint -- defaults to 1
        check_y | Optional[int]: y value of level array for checkpoint -- defaults to 3
        checkpoint | tuple: tuple of coordinates of checkpoint and boolean value if character is flipped
        last_checkpoint | str: name of last checkpoint --defaults to None
        pulsation | int: pulsation number --defaults to 0
        pulse_rate | int: rate of pulsation -- defaults to 1
        tokens | list[str]: names of tokens collected --defaults to empty list
        enttype | int: entity type --defaults to cf.ENT_CHARACTER
        '''
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
        self.check_x = check_x #stores x_co if last checkpoint
        self.check_y = check_y
        self.x_co = x_co
        self.y_co = y_co
        #self.conveyerspeed = 3
        self.on_floor = False #vy constrained to 0
        self.on_wall = False #vx constrained to 0
        self.go_left = False #Apply negative accel x
        self.go_right = False #Apply positive accel x
        self.standing_on = None #An entity whose vx,vy is added to ours
        self.checkpoint = checkpoint
        self.last_checkpoint = last_checkpoint #id of last checkpoint
        self.tokens = [] if tokens is None else tokens
        self.teleportpoint = None
        self.set_color(color)
        self.enttype = enttype

    def draw(self, surf):
        '''
        draw image as surface object on screen

        Parameters
        ----------
        surf | object: surface object
        '''
        try:
            surf.blit(self.image, self.rect.topleft)
        except TypeError:
            print('The forward-mentioned rect is', self.rect, 'and the position is', self.rect.topleft)
            print('Now don\'t ask me why this is happening, I don\'t really know yet.')
            raise

    def set_color(self, color):
        '''
        sets character color

        Parameters
        ----------
        color | object: color object
        '''
        for frm in (self.frame1, self.frame2):
            pa = pygame.PixelArray(frm)
            pa.replace(self.old_color, color)
            del pa
        self.old_color = color

    def set_frame_color(self, frm, color):
        '''
        sets frame color

        Parameters
        ----------
        frm | object: image object
        color | object: color object
        '''
        pa = pygame.PixelArray(frm)
        pa.replace(self.old_color, color)
        del pa

    def set_base_color(self, color):
        '''
        sets character color

        Parameters
        ----------
        color | object: color object
        '''
        self.set_color(color)
        self.base_color = color

    def set_pulsation(self, pulsation):
        '''
        sets pulsation

        Parameters
        ----------
        pulsation | int: pulsation number
        '''
        self.pulsation = pulsation

    def set_pulse_rate(self, pulse_rate):
        '''
        sets pulse rate

        Parameters
        ----------
        pulse_rate | int: pulse rate
        '''
        self.pulse_rate = pulse_rate

    def set_dir(self, left):
        '''
        sets direction

        Parameters
        ----------
        left | bool: True if to left, False if to right
        '''
        if left != self.left:
            self.left = left
            self.frame1 = pygame.transform.flip(self.frame1, True, False)
            self.frame2 = pygame.transform.flip(self.frame2, True, False)

    def set_left(self):
        '''
        sets direction to left
        '''
        self.set_dir(True)

    def set_right(self):
        '''
        sets direction to right
        '''
        self.set_dir(False)

    def flip(self):
        '''
        flips the character image
        plays the jump sound
        reverses character gravity
        '''
        pygame.mixer.Sound('./data/snd/sfx/jump.wav').play()
        self.is_flipped = not self.is_flipped
        self.frame1 = pygame.transform.flip(self.frame1, False, True)
        self.frame2 = pygame.transform.flip(self.frame2, False, True)

    def set_sad(self, sad):
        '''
        sets character image to sad or happy

        Parameters
        ----------
        sad | bool: change to sad
        '''
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
        '''
        refreshes frames by switching from sad to happy
        '''
        if self.is_sad:
            self.set_sad(False)
            self.set_sad(True)
        else:
            self.set_sad(True)
            self.set_sad(False)

    def set_on_floor(self, on_floor):
        '''
        sets character bool value to on floor or not

        Parameters
        ----------
        on_floor | bool: is character on floor
        '''
        self.on_floor = on_floor
        if on_floor:
            self.vy = 0
            self.next_frame = time.time() + cf.WALK_ANIM_TIME

    def set_on_wall(self, on_wall):
        '''
        sets character bool value to on wall or not

        Parameters
        ----------
        on_wall | bool: is character on wall
        '''
        self.on_wall = on_wall
        if on_wall:
            self.vx = 0

    def set_go_left(self, go_left):
        '''
        sets character to go left

        Parameters
        ----------
        go_left | bool : is character going left
        '''
        self.go_left = go_left
        if go_left:
            self.next_frame = time.time() + cf.WALK_ANIM_TIME

    def set_go_right(self, go_right):
        '''
        sets character to go right

        Parameters
        ----------
        go_right | bool : is character going right
        '''
        self.go_right = go_right
        if go_right:
            self.next_frame = time.time() + cf.WALK_ANIM_TIME

    def set_standing_on(self, ent):
        '''
        sets entity character adds velocity from

        Parameters
        ----------
        ent | object: entity object
        '''
        self.standing_on = ent

    def set_vel(self, vx, vy):
        '''
        sets character velocity

        Parameters
        ----------
        vx | int: x velocity
        vy | int: y velocity
        '''
        if not self.on_wall:
            self.vx = vx
        if not self.on_floor:
            self.vy = vy

    def move(self):
        '''
        moves character
        '''
        if self.standing_on:
            self.rect.move_ip(self.standing_on.vx + self.vx, self.standing_on.vy + self.vy)
        else:
            self.rect.move_ip(self.vx, self.vy)

    def move_delta(self, x, y):
        '''
        moves character

        Parameters
        ----------
        x | int: x amount to move character
        y | int: y amount to move character
        '''
        self.rect.move_ip(x, y)

    def kill(self):
        '''
        kill character and set next revive time
        play death sound
        '''
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
        '''
        revive character
        set back to last checkpoint
        '''
        if self.is_dead:
            self.is_dead = False
            self.is_sad = self.was_sad
            self.refresh_frames()
            self.x_co = self.check_x
            self.y_co = self.check_y
            self.restore_checkpoint()

    def restore_checkpoint(self):
        '''
        set character to most recent checkpoint
        '''
        if self.checkpoint is not None:
            if self.checkpoint[1] != self.is_flipped:
                self.flip()
            self.rect.bottomleft = self.checkpoint[0]
            self.vx = 0
            self.vy = 0
            self.set_on_floor(False)
            self.set_on_wall(False)

    def set_checkpoint_here(self, ent):
        '''
        set checkpoint and plays sound

        Parameters
        ----------
        ent | object: checkpoint entity object
        '''
        if self.last_checkpoint != ent.name:
            pygame.mixer.Sound('./data/snd/sfx/save.wav').play()
            self.last_checkpoint = ent.name
            self.check_x = self.x_co
            self.check_y = self.y_co
            self.checkpoint = (self.rect.bottomleft, self.is_flipped)

    def get_token(self, ent):
        '''
        adds token to character

        Parameters
        ----------
        ent | object: token entity object
        '''
        if ent.name not in self.tokens:
            pygame.mixer.Sound('./data/snd/sfx/souleyeminijingle.wav').play()
            self.tokens.append(ent.name)
            self.tokens = list(set(self.tokens))

    def teleport(self):
        '''
        teleport character
        play teleport sound
        '''
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
    #   '''
    #   add conveyer velocity to character
    #
    #   Parameters
    #   ----------
    #   on_floor | bool: is character on floor
    #   '''
    #   self.on_floor = on_floor
    #   if on_floor:
    #       self.vx += self.conveyerspeed
    #       self.next_frame = time.time() + cf.WALK_ANIM_TIME

    def accelerate(self):
        '''
        accelerates character
        '''
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

    def normalize(self, gamearea):
        '''
        changes screen if character exceeds screen area bounds
        '''
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
        '''
        sets sprite image
        '''
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
        '''
        pulsates character color
        '''
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

    def flicker(self, env):
        '''
        flickers character image and refreshes breakaway blocks

        Parameters
        ----------
        env | object: environment object
        '''
        if time.time() > self.next_frame:
            self.next_frame = time.time() + random.uniform(cf.DEAD_FLICKER_MIN, cf.DEAD_FLICKER_MAX)
            if self.image == self.frame1:
                self.image = self.frame2
            else:
                self.image = self.frame1
        if time.time() > self.next_revive:
            self.revive()
            if env:
                env.entities = set((self,) + tuple(ent for ent in lv.ent_list[self.x_co][self.y_co]))
                for ent in env.entities:
                    if ent.enttype == cf.ENT_BREAKAWAY:
                        if getattr(ent, 'is_breaking', False):
                            env.add_entity(ent)
                        ent.is_breaking = False
                        ent.counter = 0
                        ent.image = img_dict['./data/img/plat_o.png']

    def collide(self, geom):
        '''
        checks for collision with rect objects

        Parameters
        ----------
        geom | object: geometry object
        '''
        #We're doing a preemptive collision test now -- the below code was unsatisfactory
        colinfo = geom.test_rect(self.rect)
        if colinfo[cf.HITTOP][0] and self.is_flipped: #One does not simply headstand!
            if getattr(colinfo[cf.HITTOP][1], 'obstacle', False):
                self.kill()
            ent = getattr(colinfo[cf.HITTOP][1], 'ent', None)
            if ent:
                self.set_standing_on(ent)
                if ent.enttype == cf.ENT_BREAKAWAY:
                    self.breakaway(ent)
            self.move_delta(0, colinfo[cf.HITTOP][0])
            self.set_on_floor(True)

        if colinfo[cf.HITBOTTOM][0] and not self.is_flipped:
            if getattr(colinfo[cf.HITBOTTOM][1], 'obstacle', False):
                self.kill()
            ent = getattr(colinfo[cf.HITBOTTOM][1], 'ent', None)
            if ent:
                self.set_standing_on(ent)
                if ent.enttype == cf.ENT_BREAKAWAY:
                    self.breakaway(ent)
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
        #   self.set_on_floor(True)

        #if colinfo[cf.HITLEFT][0] or colinfo[cf.HITRIGHT][0]:
        #   self.set_on_wall(True)

        ##Now interpolate any remaining movement axes over time to the next collision
        #nextrect = self.rect.move(self.vx, self.vy) #FIXME -- lerp
        #colinfo = geom.test_rect(nextrect)

        #if colinfo[cf.HITTOP][0] and self.vy < 0:
        #   self.vy += colinfo[cf.HITTOP][0]
        #if colinfo[cf.HITBOTTOM][0] and self.vy > 0:
        #   self.vy -= colinfo[cf.HITBOTTOM][0]
        #if colinfo[cf.HITLEFT][0] and self.vx < 0:
        #   self.vx += colinfo[cf.HITLEFT][0]
        #if colinfo[cf.HITRIGHT][0] and self.vx > 0:
        #   self.vx -= colinfo[cf.HITRIGHT][0]

    def breakaway(self, ent):
        '''
        sets breakaway entity attributes

        Parameters
        ----------
        ent | breakaway entity object
        '''
        is_breaking = getattr(ent, 'is_breaking', False)
        if not is_breaking:
            ent.counter = 0
            ent.is_breaking = True

    def collide_entities(self, ents):
        '''
        checks for collison with entitites and performs appropriate action

        Parameters
        ----------
        ents | list[object]: list of entity objects
        '''
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
                self.get_token(ent)
            elif ent.enttype == cf.ENT_CHECKPOINT:
                self.set_checkpoint_here(ent)
            elif ent.enttype == cf.ENT_SCRIPTED:
                ent.on_char_collide(self)
            elif ent.enttype == cf.ENT_PORTAL:
                self.teleport()
            #elif ent.enttype == cf.ENT_INVERTER:
            #   self.flip()
            #elif ent.enttype in (cf.ENT_CONVEYER_A, cf.ENT_CONVEYER_B):
            #   self.conveyer()
            elif ent.enttype == cf.ENT_BREAKAWAY:
                self.breakaway(ent)
            elif ent.enttype == cf.ENT_EMPTY:
                pass

    def update(self, gamearea, env=None):
        '''
        updates character entity

        Parameters
        ----------
        gamearea | object: area object
        env | Optional[object]: environment object --defaults to None
        '''
        if self.is_dead:
            self.flicker(env)
        else:
            self.accelerate()
            self.move()
            self.normalize(gamearea)
            self.pulsate()
            self.set_sprite()
        if env:
            self.collide(env.geometry)
            self.collide_entities(env.entities)
