import pygame 
import os, math, random

from Events.Manager import *
import Model.const as model_const
import View.const as view_const
from View.staticobject import *
import Controller.const as ctrl_const
from View.animation import *

class GraphicalView(object):

    def __init__(self, ev_manager, model):

        self.ev_manager = ev_manager
        self.ev_manager.register_listener(self)
        self.model = model
        self.is_init = False
        self.screen = None
        self.ani_enable = True

    def notify(self, event):

        if isinstance(event, EventEveryTick):
            if self.model.state == model_const.STATE_MENU:
                self.render_menu()
            elif self.model.state == model_const.STATE_PLAY:
                self.render_play()
            elif self.model.state == model_const.STATE_PAUSE:
                self.render_pause()
        elif isinstance(event, EventInitialize):
            self.initialize()
        elif isinstance(event, EventQuit):
            self.is_init = False
        elif isinstance(event, EventMoaiKingRadiation) and self.ani_enable:
            self.ani_list.append(Ani_Moai_King_Radiation(event.position))
        elif isinstance(event, EventMoaiKingRotation) and self.ani_enable:
            self.ani_list.append(Ani_Moai_King_Rotation(event.position, event.anti_clock))
        

    def render_menu(self):
        
        pygame.display.update()
        draw_king = False if self.ani_list else True
        self.menu_background.draw(self.screen, draw_king)
        self.update_ani()
        if len(self.ani_list): self.ani_enable = False
        else: self.ani_enable = True

    def render_play(self):

        pygame.display.update()
        self.play_background.draw(self.screen)
        self.update_ani()
        

    def render_pause(self):

        pygame.display.update()
        pause_font = pygame.font.Font(view_const.lionel_font, 200)
        text_pause = pause_font.render('Pause', 1, view_const.COLOR_BLACK)
        self.screen.fill(view_const.COLOR_TURQUOISE)
        self.screen.blit(text_pause, (250, 150))


    def initialize(self):

        pygame.font.init()
        pygame.display.set_caption(view_const.game_caption)
        self.screen = pygame.display.set_mode(view_const.screen_size)
        self.menu_background = View_Menu_background(self.model)
        self.play_background = View_Play_background(self.model)
        self.ani_list = []


        self.is_init = True
    
    def update_ani(self):
        camera = self.model.camera
        for ani in self.ani_list:
            ani.draw(self.screen, camera = camera)
            if ani.end: self.ani_list.remove(ani)

