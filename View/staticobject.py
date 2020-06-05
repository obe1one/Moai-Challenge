import pygame
import os.path
import numpy as np

import View.const as view_const

class Object_base(object):

    def __init__(self, model):
        self.model = model

class Item_base(Object_base):

    def __init__(self, model):
        self.model = model
        self.image = None
    
    def draw(self, screen, position, camera = [0, 0]):
        new_pos = [a - b for a, b in zip(position, camera)]
        screen.blit(self.image, new_pos)

    def rotate_center(self, angle):
        origin_rect = self.image.get_rect()
        rotate_image = pygame.transform.rotate(self.image, angle)
        rotate_rect = origin_rect.copy()
        rotate_rect.center = rotate_image.get_rect().center
        rotate_image = rotate_image.subsurface(rotate_rect).copy()
        return rotate_image

class View_Menu_background(Object_base):

    def __init__(self, model):
        self.model = model
        self.caption_font = pygame.font.Font(view_const.typhoon_font, 200)
        self.brick = View_Brick(model)
        self.moai_king = pygame.image.load(os.path.join(view_const.IMAGE_PATH, 'moai_king.png'))
        
    def draw(self, screen, draw_king):
        screen.fill(view_const.COLOR_MINT)
        for i in range(-1, 21):
            self.brick.draw(screen, (30 + i * view_const.brick_length, 450))
            self.brick.draw(screen, (30 + i * view_const.brick_length, 495))
        
        if draw_king: screen.blit(self.moai_king, (345, 52))

class View_Play_background(Object_base):

    def __init__(self, model):
        self.model = model
        self.font = pygame.font.Font(view_const.lionel_font, 60)
        self.info_bar = View_Play_info_bar(model)
        self.player = View_Player(model)
        self.brick = View_Brick(model)
        self.gem = View_Gem(model)
        self.moai = View_Moai(model)
        self.altar = View_Altar(model)
        self.mine = View_Mine(model)
        self.mine_outline = View_Mine_Outline(model)
    
    def draw(self, screen):
        camera = self.model.camera
        screen.fill(view_const.COLOR_GREEN)
        self.altar.draw(screen, (45, 45), camera)
        for brick in self.model.brick_list:
            self.brick.draw(screen, brick.position, camera)
        for gem in self.model.gem_list:
            if gem.is_polished: self.gem.draw(screen, gem.position, gem.type, camera)    
            else:
                self.mine.draw(screen, gem.position, gem.type, camera)
                if gem.is_pointed: self.mine_outline.draw(screen, gem.position, camera)
        self.player.draw(screen, camera)
        self.moai.draw(screen, (45, 900), camera)
        
        self.info_bar.draw(screen)

class View_Play_info_bar(Object_base):

    def __init__(self, model):
        self.model = model
        self.font = pygame.font.Font(view_const.fira_sans_font, 30)
        self.mini_map = View_Play_mini_map(model)
        self.gem = View_Gem(model)

    def draw(self, screen):
        pygame.draw.rect(screen, view_const.COLOR_ORANGE, (720, 0, 240, 540))
        self.mini_map.draw(screen)
        for i in range(3):
            self.gem.draw(screen, (720, 180 + 45 * i), i)
            text_gem_score = self.font.render('x  ' + str(self.model.player.value[i]), 1, view_const.COLOR_BLACK)
            screen.blit(text_gem_score, (765, 185 + 45 * i))
        text_time = self.font.render(str(self.model.timer), 1, view_const.COLOR_BLACK)
        screen.blit(text_time, (720, 315))
        pygame.draw.rect(screen, view_const.COLOR_BLACK, (720, 0, 240, 540), 5)
        pygame.draw.line(screen, view_const.COLOR_BLACK, (720, 180),(960, 180), 5)

class View_Play_mini_map(Object_base):

    def __init__(self, model):
        self.model = model
        self.screen = pygame.Surface(view_const.mini_map_size, pygame.SRCALPHA)

    def draw(self, screen):
        self.screen.fill((255, 255, 255, 128))
        for brick in self.model.brick_list:
            new_pos = self.position_mapping(brick.position)
            pygame.draw.rect(self.screen, view_const.COLOR_DARKGRAY, new_pos + [8, 8])
        for gem in self.model.gem_list:
            new_pos = self.position_mapping(gem.position)
            pygame.draw.rect(self.screen, view_const.GEM_COLOR[gem.type], new_pos + [3, 3])
        new_pos = self.position_mapping(self.model.player.position)
        pygame.draw.rect(self.screen, view_const.COLOR_BLACK, new_pos + [8, 8])
        screen.blit(self.screen, (720, 0))
        
    
    def position_mapping(self, position):
        return [position[0] / 6, position[1] / 6]

class View_Brick(Item_base):

    def __init__(self, model):
        self.model = model
        self.image = pygame.image.load(os.path.join(view_const.IMAGE_PATH, 'grey_brick.png'))

class View_Moai(Item_base):

    def __init__(self, model):
        self.model = model
        self.image = pygame.image.load(os.path.join(view_const.IMAGE_PATH, 'moai.png'))

class View_Gem(Item_base):

    def __init__(self, model):
        self.model = model
        self.image = (pygame.image.load(os.path.join(view_const.IMAGE_PATH, 'amethyst.png')), \
                      pygame.image.load(os.path.join(view_const.IMAGE_PATH, 'ruby.png')), \
                      pygame.image.load(os.path.join(view_const.IMAGE_PATH, 'sapphire.png')))

    def draw(self, screen, position, gem_type, camera= [0, 0]):
        new_pos = [a - b for a, b in zip(position, camera)]
        screen.blit(self.image[gem_type], new_pos)

class View_Mine(View_Gem):

    def __init__(self, model):
        self.model = model
        self.image = (pygame.image.load(os.path.join(view_const.IMAGE_PATH, 'ame_mine.png')), \
                      pygame.image.load(os.path.join(view_const.IMAGE_PATH, 'ruby_mine.png')), \
                      pygame.image.load(os.path.join(view_const.IMAGE_PATH, 'sap_mine.png')))

class View_Mine_Outline(Item_base):

    def __init__(self, model):
        self.model = model
        self.image = pygame.image.load(os.path.join(view_const.IMAGE_PATH, 'mine_outline.png'))

class View_Player(Item_base):

    def __init__(self, model):
        self.model = model
        self.image = pygame.image.load(os.path.join(view_const.IMAGE_PATH, 'brave.png'))
    
    def draw(self, screen, camera = [0, 0]):
        angle = 135 - 45 * self.model.player.direction if self.model.player.direction else \
                135 - 45 * self.model.player.last_direction
        rotate_image = self.rotate_center(angle)
        new_pos = [self.model.player.position[0]-camera[0], \
                   self.model.player.position[1]-camera[1]]
        screen.blit(rotate_image, new_pos)

class View_Altar(Item_base):

    def __init__(self, model):
        self.model = model
        self.image = pygame.image.load(os.path.join(view_const.IMAGE_PATH, 'altar.png'))


        

