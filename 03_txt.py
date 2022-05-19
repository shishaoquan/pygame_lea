"""
03_txt -

@IDE:   PyCharm
@Author:石少全
@Date:2022/5/17 10:56 
@Description: 


"""

import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('显示图片用')
# 设置北京颜色
window.fill((255, 255, 255))


# ========= 显示文字
# 创建字体对象
font = pygame.font.Font('files/kaiti_GB2312.ttf', 30)

# 2. 创建w
text = font.render('游戏你好', True, (255, 2, 2), (255, 255, 0))

# 3. 渲染到窗口上
window.blit(text, (0, 0))

# 4. 文字操作
# 操作文字对象
w, h = text.get_size()
print(w, h)
window.blit(text, (800 - w, 600 - h))

new_t1 = pygame.transform.scale(text, (200, 50))
window.blit(new_t1, (0, 60))

new_t2 = pygame.transform.rotozoom(text, 90, 2)
window.blit(new_t2, (0, 120))

pygame.display.flip()








while True:
    # ========== 游戏帧的刷新 ==========
    # 动画有切换 === 主场优势，优势在我
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()