import pygame 
import os, math, random

from Events.Manager import *
import Model.const as model_const
import View.const as view_const
import Controller.const as ctrl_const


class Control(object):

    def __init__(self, ev_manager, model):

        self.ev_manager = ev_manager
        self.ev_manager.register_listener(self)
        self.model = model
        self.control_keys = {}

    def notify(self, event):

        if isinstance(event, EventEveryTick):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.ev_manager.post(EventQuit())
                else:
                    if self.model.state == model_const.STATE_MENU:
                        self.ctrl_menu(event)
                    elif self.model.state == model_const.STATE_PLAY:
                        self.ctrl_play(event)
                    elif self.model.state == model_const.STATE_PAUSE:
                        self.ctrl_pause(event)

        elif isinstance(event, EventInitialize):
            self.initialize()

    def initialize(self):
        pass

    def ctrl_menu(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.ev_manager.post(EventQuit())
            elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                self.ev_manager.post(EventStateChange(model_const.STATE_PLAY))
            elif event.key == pygame.K_BACKSPACE:
                self.ev_manager.post(EventMoaiKingRadiation([345, 52]))
            elif event.key == pygame.K_RSHIFT:
                self.ev_manager.post(EventMoaiKingRotation([345, 52], True))
            elif event.key == pygame.K_LSHIFT:
                self.ev_manager.post(EventMoaiKingRotation([345, 52], False))

    def ctrl_play(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.ev_manager.post(EventStateChange(model_const.STATE_MENU))
            elif event.key == pygame.K_SPACE:
                self.ev_manager.post(EventStateChange(model_const.STATE_PAUSE))
        
        self.ev_manager.post(EventMouseMotion(pygame.mouse.get_pos(), pygame.mouse.get_pressed()))
            
        
        key_status = pygame.key.get_pressed()
        key_value = 0
        key_dir = 0
        for i in range(ctrl_const.key_num):
            if key_status[ctrl_const.key_list[i]]:
                key_value += ctrl_const.dir_val[i]
        key_dir = ctrl_const.dir_hash.index(key_value) if key_value in ctrl_const.dir_hash else 0
        self.ev_manager.post(EventMove(key_dir))
        


    def ctrl_pause(self, event):
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.ev_manager.post(EventQuit())
            elif event.key == pygame.K_SPACE:
                self.ev_manager.post(EventStateChange(model_const.STATE_PLAY))





    