import os

#basic info
STATE_MENU = 1
STATE_PLAY = 2
STATE_PAUSE = 3
STATE_END = 4
game_time = 50000000

#direction
dir_mapping = [
    [0, 0], 
    [0, -1],
    [0.7, -0.7],
    [1, 0],
    [0.7, 0.7],
    [0, 1],
    [-0.7, 0.7],
    [-1, 0],
    [-0.7, -0.7]
]

#player
init_player_position = [135, 135]
init_player_radius = 30
init_player_speed = 1

#gems
init_gem_radius = 22
init_gem_hp = 10

#camera
cmr_line = (360, 270)
