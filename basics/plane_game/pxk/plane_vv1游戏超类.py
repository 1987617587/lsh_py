# 导入模块
import pygame, sys

pygame.init()

# 加载音乐
pygame.mixer.music.load("sound/gameMusic.mp3")
# 播放音乐
pygame.mixer.music.play(-1)

# 设置标题
pygame.display.set_caption("飞机大战")

logo = pygame.image.load("logo.png")
# 设置图标
pygame.display.set_icon(logo)

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 768


# 游戏的超级父类
class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image, speed):
        super().__init__()
        # 加载图片
        self.image = pygame.image.load(image)
        # 通过图片获取坐标位置
        self.rect = self.image.get_rect()
        # 运动速度
        self.speed = speed

    def move(self):
        print("移动了")

    def event(self):
        print("发生事件了")
        # 获取所有事件
        e_list = pygame.event.get()
        # 判断事件是否存在
        if len(e_list) > 0:
            # 对事件进行遍历循环
            for e in e_list:
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def update(self):
        self.move()
        self.event()


# 创建背景类型
class BackgroundImageSprite(GameSprite):
    def move(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -SCREEN_HEIGHT


background_image1 = BackgroundImageSprite("images/bg/bg5.jpg", 5)
background_image2 = BackgroundImageSprite("images/bg/bg5.jpg", 5)
# 设置背景图2的y值
background_image2.rect.y = -SCREEN_HEIGHT

# #创建实例对象
# background_image = GameSprite("images/bg/bg5.jpg",0)
# print(background_image)
# background_image.move()
# background_image.update()
# print(background_image.image)
# print(background_image.speed)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# 创建一个精灵组
resource = pygame.sprite.Group(background_image1, background_image2)

# 控制每秒播放帧数
clock = pygame.time.Clock()
while True:
    clock.tick(24)
    # 精灵组调用每个精灵的update方法
    resource.update()
    # 精灵组将所有精灵渲染到游戏窗口中
    resource.draw(screen)

    pygame.display.update()
