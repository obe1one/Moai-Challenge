import pygame
import os.path, os

run = True

pygame.init()
screen = pygame.display.set_mode((300, 300))
image_path = os.path.join(os.path.join('View', 'image', 'brave.png'))

class player(object):

    def __init__(self, position):
        self.image = pygame.image.load(image_path)
        self.position = position
        self.ani = False
    def draw(self, screen, time):
        if time == 2500: self.ani = False
        if not self.ani: screen.blit(self.image, self.position)
        else:
            scal = (1 + time / 2500)
            
            scl_image  = pygame.transform.scale(self.image, (int(60 * scal), int(60 * scal)))
            new_pos = [self.position[0] - int(30 * (scal-1)), self.position[1] - int(30 * (scal-1))]
            screen.blit(scl_image, new_pos)
            
bi = image = pygame.image.load(os.path.join(image_path))
pygame.draw.rect(bi, (0, 0, 0), (0, 0, 20, 20))


p1 = player([100, 100])
time = 0

while run:
    time += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                p1.ani = True
                time = 0
                print('press')
    pygame.display.update()
    screen.fill((255, 255, 255))
    screen.blit(bi, (0, 0))
    

    

    
pygame.quit()
    