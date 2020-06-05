import pygame 
import os, math, random

from Events.Manager import *
import Model.const as model_const
import View.const as view_const
import Controller.const as ctrl_const
from Model.GameObjects.player import *
from Model.GameObjects.brick import *
from Model.GameObjects.gem import *



class GameEngine(object):

    def __init__(self, ev_manager):

        self.ev_manager = ev_manager
        self.ev_manager.register_listener(self)
        self.running = False
        self.state = None
        self.timer = None
        self.clock = pygame.time.Clock()
        self.camera = [0, 0]

        self.player = Player()
        self.brick_list = []
        self.gem_list = []
        self.init_brick_boundary()
        

    def notify(self, event):
        
        if isinstance(event, EventEveryTick):
            if self.state == model_const.STATE_MENU:
                self.update_menu()
            elif self.state == model_const.STATE_PLAY:
                self.update_game()
        elif isinstance(event, EventInitialize):
            pass
        elif isinstance(event, EventQuit):
            self.running = False
        elif isinstance(event, EventStateChange):
            if event.state == model_const.STATE_MENU:
                self.state = model_const.STATE_MENU
            elif event.state == model_const.STATE_PLAY:
                self.state = model_const.STATE_PLAY
            elif event.state == model_const.STATE_PAUSE:
                self.state = model_const.STATE_PAUSE
            elif event.state == model_const.STATE_END:
                self.ev_manager.post(EventQuit())
        elif isinstance(event, EventMove):
            self.player.update_direction(event.direction)
        elif isinstance(event, EventCameraMove):
            self.camera[0] = event.direction[0] if event.direction[0] else self.camera[0]
            self.camera[1] = event.direction[1] if event.direction[1] else self.camera[1]
        elif isinstance(event, EventPickGem):
            self.gem_list.remove(event.gem)
        elif isinstance(event, EventMouseMotion):
            self.update_mouse_state(event.position, event.state)

        if self.timer is not None and not self.timer:
            self.ev_manager.post(EventQuit())


    def update_menu(self):
        pass

    def update_game(self):
        self.player.update(self, self.ev_manager)
        self.update_camera()
        self.update_gems()
        self.timer -= 1
    
    def update_gems(self):
        if not (self.timer % 500):
            gen_type = random.randint(0, 2)
            pos = [random.randint(50, 1385), random.randint(50, 1025)]
            self.gem_list.append(Gem(pos, 0, gen_type))
        if len(self.gem_list) > 20:
            self.gem_list.remove(self.gem_list[0])

    
    def update_camera(self):
        pos = self.player.position
        cmrl = model_const.cmr_line
        delt_x = pos[0] - cmrl[0] if cmrl[0] <= pos[0] <= \
                 cmrl[0] + view_const.map_size[0] / 2 else 0
        delt_y = pos[1] - cmrl[1] if cmrl[1] <= pos[1] <= \
                 cmrl[1] + view_const.map_size[1] / 2 else 0
        self.ev_manager.post(EventCameraMove((delt_x, delt_y)))
    
    def update_mouse_state(self, mouse_pos, mouse_state):
        for gem in self.gem_list:
            gem_center = [a - b for a, b in zip(gem.center, self.camera)]
            if self.distance(mouse_pos, gem_center) < gem.radius:
                gem.is_pointed = True
                if mouse_state[0]: gem.hp -= 1
                if not gem.hp: gem.get_polished(self.ev_manager)
            else: gem.is_pointed = False
    
    def init_brick_boundary(self):
        self.brick_list = []
        map_size = view_const.map_size
        bl = view_const.brick_length
        for i in range(int(map_size[0] / bl)):
            self.brick_list.append(Brick((i * bl, map_size[1] - bl)))
            self.brick_list.append(Brick((i * view_const.brick_length, 0)))
        for i in range(1, int(map_size[1] / bl - 1)):
            self.brick_list.append(Brick((0, i * bl)))
            self.brick_list.append(Brick((map_size[0] - bl, i * view_const.brick_length)))
        self.brick_list.append(Brick((270, 270)))
    
    def distance(self, a, b):
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    def run(self):

        self.running = True
        self.ev_manager.post(EventInitialize())
        self.state = model_const.STATE_MENU
        self.timer = model_const.game_time

        while self.running:
            self.ev_manager.post(EventEveryTick())









        