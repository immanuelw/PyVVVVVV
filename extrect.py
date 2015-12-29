'''
extrect | defines an extended rect object that can have atrributes assigned to it

author | Immanuel Washington

Classes
-------
ExtRect | creates extended rect object
'''
import pygame

class ExtRect(object):
    '''
    extended rect object

    Methods
    -------
    wrap | allows wrapping of object
    as_rect | returns rect object
    __getattr__ | gets attributes
    __setattr__ | sets attributes
    '''
    def __init__(self, *args, **kwargs):
        self._rect = pygame.Rect(*args, **kwargs)

    @classmethod
    def wrap(cls, obj):
        '''
        allows wrapping of rect object
        '''
        if isinstance(obj, ExtRect):
            return obj
        return cls(obj)

    @classmethod
    def as_rect(cls, obj):
        '''
        returns rect object of extended rect
        '''
        if isinstance(obj, pygame.Rect):
            return obj
        return obj._rect

    def __getattr__(self, attr):
        '''
        gets attribute

        Parameters
        ----------
        attr | ???: attribute to be grabbed

        Returns
        -------
        ???: value of attribute
        '''
        return getattr(self._rect, attr)

    def __setattr__(self, attr, val):
        '''
        sets attribute

        Parameters
        ----------
        attr | ???: attribute to be changed
        val | ???: value to assign to attribute
        '''
        if hasattr(pygame.Rect, attr):
            setattr(self._rect, attr, val)
        else:
            object.__setattr__(self, attr, val)
