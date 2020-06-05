import pygame 
import os.path
import math, random

from Events.Manager import *
import Model.const as model_const
import View.const as view_const
import Controller.const as ctrl_const

class Ani_base(object):

    def __init__(self, image, position, exe_time):
        self.image = image
        self.position = position
        self.end = False
        self.counter = 0
        self.exe_time = exe_time
    
    def update(self, position = None):
        self.counter += 1
        if self.counter >= self.exe_time: self.end = True
        if position: self.position = position


class Ani_Radiation(Ani_base):

    def __init__(self, image, position, exe_time = 300, start_scale = (0, 0), end_scale = (1, 1)):
        #any scale :list[end width magnitute, end height magnitute]
        super().__init__(image, position, exe_time)
        self.start_scale = start_scale
        self.end_scale = end_scale

    def get_info(self, camera = [0, 0]):
        scale  = [b + (a - b) * self.counter / self.exe_time \
                  for a, b in zip(self.end_scale, self.start_scale)]
        origin_size = [pygame.Surface.get_width(self.image), pygame.Surface.get_height(self.image)]
        present_size = [int(a *b) for a, b in zip(origin_size, scale)]
        scl_image = None
        try:
            scl_image = pygame.transform.smoothscale(self.image, present_size)
        except:
            scl_image = pygame.transform.scale(image, present_size)
        new_pos = [a - (c - b)/2 - d for a, b, c, d in zip(self.position, origin_size, present_size, camera)]
        return (scl_image, new_pos)
    
    def draw(self, screen, camera = [0, 0], position = None):
        new_info = self.get_info(camera)
        screen.blit(new_info[0], new_info[1])
        self.update(position)


class Ani_Rotation(Ani_base):

    def __init__(self, image, position, exe_time = 300, start_angle = 0, end_angle = 360):
        #any angle:degree based
        #counter clockwise
        super().__init__(image, position, exe_time)
        self.start_angle = start_angle
        self.end_angle = end_angle

    def get_info(self, camera = [0, 0]):
        angle = self.start_angle + (self.end_angle - self.start_angle) * self.counter / self.exe_time
        origin_center = self.image.get_rect().center
        rotate_image = pygame.transform.rotate(self.image, angle)
        rotate_center = rotate_image.get_rect().center
        new_pos = [a + b - c - d for a, b, c, d in \
                   zip(self.position, origin_center, rotate_center, camera)]
        return (rotate_image, new_pos)
    
    def draw(self, screen, camera = [0, 0], position = None):
        new_info = self.get_info(camera)
        screen.blit(new_info[0], new_info[1])
        self.update(position)

class Ani_Moai_King_Radiation(Ani_Radiation):
    image = pygame.image.load(os.path.join(view_const.IMAGE_PATH, 'moai_king.png'))

    def __init__(self, position):
        self.zoom_in = Ani_Radiation(self.image, position, 300, (1, 1), (0, 0))
        self.zoom_out = Ani_Radiation(self.image, position, 300, (0, 0), (1, 1))
        self.end = False
    
    def draw(self, screen, camera = [0, 0], position = None):
        if self.zoom_in.end and self.zoom_out.end: self.end = True
        elif not self.zoom_in.end: self.zoom_in.draw(screen, camera)
        else: self.zoom_out.draw(screen, camera)
    

class Ani_Moai_King_Rotation(Ani_Rotation):
    image = pygame.image.load(os.path.join(view_const.IMAGE_PATH, 'moai_king.png'))

    def __init__(self, position, anti_clock = True):
        if anti_clock: super().__init__(self.image, position, 150, 0, 360)
        else: super().__init__(self.image, position, 150, 360, 0)






        
