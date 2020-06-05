import os.path
import pygame

DIR_STOP = 0
DIR_U = 1
DIR_RU = 2
DIR_R = 3
DIR_RD = 4
DIR_D = 5
DIR_LD = 6
DIR_L = 7
DIR_LU = 8

key_list = [pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a]

key_num = 4
dir_num = 9

dir_val = [1, 3, 5, 11]
dir_hash = [0, 1, 4, 3, 8, 5, 16, 11, 12]