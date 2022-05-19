"""
08_anniudianji -

@IDE:   PyCharm
@Author:石少全
@Date:2022/5/19 8:29 
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

font = pygame.font.Font('files/kaiti_GB2312.ttf', 30)


# 确定按钮
bx1, by1, bw, bh = 30, 100, 100, 50
pygame.draw.rect(window, (255, 0, 0), (bx1, by1, bw, bh))
text = font.render('确定', True, (255, 255, 255))
tw1, th1 = text.get_size()


window.blit(text, (bx1 + bw/2 - tw1 / 2, by1 + bh/2 - th1/2))
bx2, by2, bw, bh = 30, 200, 100, 50
# 取消按钮
pygame.draw.rect(window, (0, 255, 0), (bx2, by2, bw, bh))
text2 = font.render('取消', True, (255, 255, 255))
tw2, th2 = text2.get_size()
window.blit(text2, (bx2 + bw/2 - tw2 / 2, by2 + bh/2 - th2/2))
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if bx1 <= mx <= bx1 + bw and by1 <= my <= by1 + bh:
                # 按钮点击的放映
                pygame.draw.rect(window, (111, 111, 111), (bx1, by1, bw, bh))
                window.blit(text, (bx1 + bw/2 - tw1 / 2, by1 + bh/2 - th1/2))
                pygame.display.update()
                print('确定按钮被点击')
            if bx2 <= mx <= bx2 + bw and by2 <= my <= by2 + bh:
                print('取消按钮被点击')

        if event.type == pygame.MOUSEBUTTONUP:
                pygame.draw.rect(window, (255, 0, 0), (bx1, by1, bw, bh))
                window.blit(text, (bx1 + bw / 2 - tw1 / 2, by1 + bh / 2 - th1 / 2))
                pygame.display.update()

                # pygame.draw.rect(window, (255, 0, 0), (bx1, by1, bw, bh))
                # window.blit(text, (bx1 + bw / 2 - tw1 / 2, by1 + bh / 2 - th1 / 2))
                # pygame.display.update()

        # 取消按钮
