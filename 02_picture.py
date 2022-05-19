"""
02_picture -

@IDE:   PyCharm
@Author:石少全
@Date:2022/5/17 10:24 
@Description: 


"""
import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('显示图片用')
# 设置北京颜色
window.fill((255, 255, 255))

# ====== 游戏开始页面静态效果 ============

# 1. 加载图片
image1 = pygame.image.load('files/baoerjie.jpg')
# 2. 渲染图片
# 左上角作为坐标原点,
window.blit(image1, (0, 0))

# 3. 操作图片
w, h = image1.get_size()
print(w, h)

window.blit(image1, (300, 300))

# 对图片进行旋转和缩放
# 朋
new_image1 = pygame.transform.scale(image1, (100, 100))
window.blit(new_image1, (0, 300))
new_image2 = pygame.transform.rotozoom(image1, 45, 0.5)
window.blit(new_image2, (0, 400))
# 3. 刷新显示页面    -- 第一次刷新
pygame.display.flip()


# pygame.display.update() -- 第一次以后的刷新

while True:
    # ========== 游戏帧的刷新 ==========
    # 动画有切换 === 主场优势，优势在我
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()