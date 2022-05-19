"""
06_dynamic_02 -

@IDE:   PyCharm
@Author:石少全
@Date:2022/5/18 17:14 
@Description: 动画的灵活运用


"""
# 东到后面就跑出去了
import  pygame

pygame.init()

WIN_WIDTH = 400
WIN_HEIHT = 600

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIHT))
pygame.display.set_caption('动画原理')
window.fill((255, 255, 255))
pygame.display.flip()

#
x, y = 200, 50
r = 50
y_speed = 1
pygame.draw.circle(window, (0, 255, 0), (x, y), r)
pygame.display.update()
num = 0

while True:
    num += 0.5
    if num % 10 == 0:
        pygame.draw.circle(window, (255, 255, 255), (x, y), r)
        y += y_speed

        # 检测边界
        if y >= WIN_HEIHT - r:
            y_speed = -1

        if y <= r:
            y_speed = 1
        pygame.draw.circle(window, (0, 255, 0), (x, y), r)
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()





