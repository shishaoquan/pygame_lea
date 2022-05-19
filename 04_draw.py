"""
04_draw -

@IDE:   PyCharm
@Author:石少全
@Date:2022/5/17 11:11 
@Description: 


"""

import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('显示图形')
# 设置北京颜色
window.fill((255, 255, 255))

# =========== 进行画图 ===========
# 1. 花知晓
pygame.draw.line(window, (255, 0, 0), (100, 10), (200, 10), width=3)

# 画折现
# 列表 与 元组
points = [(100, 100), (200, 345), (233, 442), (345, 456)]
pygame.draw.lines(window, (0, 255, 0), True, points, width=5)
#

pygame.draw.circle(window, (255, 0, 0), (200, 200), 100, width=2)


# 画矩形
pygame.draw.rect(window, (0, 255, 0), (100, 70, 100, 100), width=10)


# 画椭圆
#
pygame.draw.ellipse(window, (0, 255, 255), (100, 70, 100, 100), width=10)

# 画的方式是不一样的
pygame.draw.arc(window, (0, 0, 255), (100, 70, 100, 100), 0, 3.1415926, width= 1 )
pygame.display.flip()




while True:
    # ========== 游戏帧的刷新 ==========
    # 动画有切换 === 主场优势，优势在我
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()