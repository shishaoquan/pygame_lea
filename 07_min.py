"""
07_min -

@IDE:   PyCharm
@Author:石少全
@Date:2022/5/18 18:35 
@Description: 


"""

import pygame
import random

pygame.init()

WINTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WINTH, HEIGHT))
pygame.display.set_caption('少全的游戏')
window.fill((255, 255, 255))
pygame.display.flip()
font = pygame.font.Font('files/kaiti_GB2312.ttf', 30)
x = 0

count = 0
while True:
    for event in pygame.event.get():
        # 检测是否有 事件
        # 只有事件差生后
        count += 1
        print(count)
        # 不同的事件有不同的事情
        # event 的 type属性用来区分不同类型的事件
        # QUIT 点击关闭按钮这个事件
        # 鼠标事件
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('鼠标按下')
            print('鼠标按下', event.pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            print('鼠标谈起')
        elif event.type == pygame.MOUSEMOTION:
            print('鼠标移动')
            mx, my = event.pos
            r = random.randint(0, 255)
            pygame.draw.circle(window, (r, r, r), (mx, my), 100, 0)
            pygame.display.update()
        elif event.type == pygame.KEYDOWN:
            print('键盘按下', event.key, chr(event.key))
            if chr(event.key) == 'f':
                print('闪现')

            text = font.render(chr(event.key), True, (255, 0, 0))
            # window.fill((255, 255, 255))
            window.blit(text, (x, 0))
            x += 15

            pygame.display.update()
        elif event.type == pygame.KEYUP:
            print('按键谈起')

        # 键盘事件
        # 按键值的属性 -- kye
