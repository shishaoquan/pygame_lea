"""
example01 -

@IDE:   PyCharm
@Author:石少全
@Date:2022/5/17 10:00 
@Description: 


"""


# 在项目中 去练习
# Unity 3D  就当做 Python 学习
# 调参侠 --- API 调用者
# 游戏里面都是有图片的
# 调参侠是谁呀
# Python 写一个小游戏
# IOS 技术 OC

import pygame

# 初始化操作
#
pygame.init()

# 2. 创建游戏窗口的大小 --
window = pygame.display.set_mode((800, 800))

# 设置游戏名
pygame.display.set_caption('少全的游戏')

#


# 3. 不要结束
# 游戏保持一直运行的状态
# 去检测时间
while True:
    # 4. 检测时间
    for event in pygame.event.get():
        # 当出现 点击按钮被点击的事件
        # 越来越接近人类语言
        if event.type == pygame.QUIT:
            # 退出  线程 --- 保存数据 -- 游戏的进度
            # 游戏在退出时，做一些列保存的工作
            exit()














