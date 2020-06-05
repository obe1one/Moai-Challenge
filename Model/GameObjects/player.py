import pygame 
import os, math, random

from Events.Manager import *
import Model.const as model_const
import View.const as view_const
import Controller.const as ctrl_const

class Player(object):
    __slots__ = ('position', 'center', 'direction', 'last_direction', \
                 'speed', 'radius', 'value')

    def __init__(self):
        self.position = model_const.init_player_position
        self.radius = model_const.init_player_radius
        self.center = [self.position[0]+self.radius, self.position[1]+self.radius]
        self.direction = 0
        self.last_direction = ctrl_const.DIR_R
        self.speed = model_const.init_player_speed
        self.value = [0, 0, 0]
    
    def update_direction(self, new_dir):
        self.last_direction = self.direction if self.direction else self.last_direction
        self.direction = new_dir
    
    def pick_gem(self, gem_list, ev_manager):
        for gem in gem_list:
            min_dis = self.radius + gem.radius - 15
            dis = math.sqrt((self.center[0] - gem.center[0]) ** 2 + \
                            (self.center[1] - gem.center[1]) ** 2)
            if dis < min_dis and gem.is_polished:
                ev_manager.post(EventPickGem(gem))
                self.value[gem.type] += 1
    
    def is_touch_brick(self, brick_position, new_x, new_y):
        brick_radius = view_const.brick_length
        radius = self.radius - 10
        cent_x = new_x + self.radius; cent_y = new_y + self.radius
        new_pos = [[cent_x-radius, cent_y], [cent_x-radius, cent_y+radius], \
                   [cent_x, cent_y+radius], [cent_x+radius, cent_y+radius], \
                   [cent_x+radius, cent_y], [cent_x+radius, cent_y-radius], \
                   [cent_x, cent_y-radius], [cent_x-radius, cent_y-radius]]
        for pos in new_pos:
            if brick_position[0] <= pos[0] <= brick_position[0]+brick_radius and \
               brick_position[1] <= pos[1] <= brick_position[1]+brick_radius:
               return False
        return True


    def update_position(self, model):
        x_enable = True; y_enable = True
        delt_x = self.speed * model_const.dir_mapping[self.direction][0]
        delt_y = self.speed * model_const.dir_mapping[self.direction][1]
        for brick in model.brick_list:
            if not self.is_touch_brick(brick.position, self.position[0]+delt_x, self.position[1]):
                x_enable = False
            if not self.is_touch_brick(brick.position, self.position[0], self.position[1]+delt_y):
                y_enable = False
            if not x_enable and not y_enable: break
        if not x_enable: delt_x = 0
        if not y_enable: delt_y = 0
        self.position[0] += delt_x
        self.position[1] += delt_y
        self.center = [self.position[0]+self.radius, self.position[1]+self.radius]

    def update(self, model, ev_manager):
        self.update_position(model)
        self.pick_gem(model.gem_list, ev_manager)
        
        