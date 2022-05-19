"""
09_fengzhuangleijiuhaole -

@IDE:   PyCharm
@Author:石少全
@Date:2022/5/19 9:01 
@Description: 


"""

import pygame

pygame.init()
WINTH = 800
HEIGH = 600
window = pygame.display.set_mode((WINTH, HEIGH))
pygame.display.set_caption('少全的游戏')
window.fill((255, 255, 255))
pygame.display.flip()


# 按住不放   xiangshang
tank_up = pygame.image.load('files/baoerjie.jpg')
tank_x, tank_y = 200, 240
window.blit(tank_up, (200, 240))
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if chr(event.key) == 'w':
                pass



















