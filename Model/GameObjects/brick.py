import pygame 
import os, math, random

from Events.Manager import *
import Model.const as model_const
import View.const as view_const
import Controller.const as ctrl_const

class Brick(object):

    __slots__ = ('position')

    def __init__(self, position):
        self.position = position
    
    def update(self):
        pass

