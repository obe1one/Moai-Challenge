import pygame 
import os, math, random

from Events.Manager import *
import Model.const as model_const
import View.const as view_const
import Controller.const as ctrl_const

class Gem(object):

    __slots__ = ('position', 'center', 'radius', 'value', 'type', \
                 'is_polished', 'is_pointed', 'hp')

    def __init__(self, position, value, gem_type):
        self.position = position
        self.radius = model_const.init_gem_radius
        self.type = gem_type
        self.value = value
        self.hp = model_const.init_gem_hp
        self.center = [self.position[0] + self.radius, self.position[1] + self.radius]
        self.is_polished = False
        self.is_pointed = False
    
    def get_polished(self, ev_manager):
        self.is_polished = True
        self.is_pointed = False

    
    
