"""
05_dynamic -

@IDE:   PyCharm
@Author:石少全
@Date:2022/5/18 16:36 
@Description: 动画和时间的学习， pygame 我已经使用过了， 那就不需要使用


"""
import pygame

pygame.init()

WIN_WIDTH = 400
WIN_HEIHT = 600

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIHT))
pygame.display.set_caption('动画原理')
window.fill((255, 255, 255))
pygame.display.flip()

# 动画原理基础：一帧一帧的去计算
# 不断的去计算：后面需要进行去测试
# 多张图不断的去切换

# 不断的去改变球的坐标

# 1. 显示静态的球
y = 100
r = 50
pygame.draw.circle(window, (0, 255, 0), (100, y), r)
pygame.display.update()

# 游戏循环
num = 1
while True:

    # print('打印 2 ')
    # # 移动动画
    # pygame.draw.circle(window, (255, 255, 255), (100, y), 50)
    # y += 0.1
    # pygame.draw.circle(window, (0, 255, 0), (100, y), 50)
    # pygame.display.update()

    num += 1
    # 2. 缩放的动画
    # if num % 10 == 0:
    #     r += 1
    #     pygame.draw.circle(window, (255, 0, 0), (100,100), r)
    #     pygame.display.update()

    if num % 10 == 0:
        pygame.draw.circle(window, (255, 255, 255), (100, y), r)
        y += 1
        r += 1
        pygame.draw.circle(window, (0, 255, 0), (100, y), r)
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

# 线程 与 进程
# pygame
