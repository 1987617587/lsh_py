"""
# author Liu shi hao
# date: 2019/11/30 9:09
# file_name: maini

"""
import random

import pygame, sys
import traceback
import pygame.locals

# import bullet
# import supply
from sateday import myplane, enemy, bullet, supply

pygame.init()
pygame.mixer.init()

bg_size = width, height = 512, 768
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("飞机大战")

background = pygame.image.load("images/bg/bg5.jpg").convert()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 音乐
# pygame.mixer.music.load("music/bg_music.mp3")
# pygame.mixer.music.set_volume(0.2)
# pygame.mixer.music.load("music/7029.mp3")
# pygame.mixer.music.set_volume(0.2)
# pygame.mixer.music.load("music/7789.mp3")
# pygame.mixer.music.set_volume(0.2)

my_over_sound = pygame.mixer.music.load("music/big_eye.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.load("music/8226.wav")
pygame.mixer.music.set_volume(0.2)


def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)


def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)


def add_big_enemies(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)


def inc_speed(target, inc):
    for each in target:
        each.speed += inc


def main():
    # 统计玩家得分
    score = 0
    score_font = pygame.font.Font("images\Font.ttf", 36)
    # 标志是否暂停游戏
    paused = False
    pause_nor_image = pygame.image.load("images/pause_nor.png").convert_alpha()
    pause_pressed_image = pygame.image.load("images/pause_pressed.png").convert_alpha()
    resume_nor_image = pygame.image.load("images/resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load("images/resume_pressed.png").convert_alpha()
    paused_rect = pause_nor_image.get_rect()
    paused_rect.left, paused_rect.top = width - paused_rect.width - 10, 10
    paused_image = pause_nor_image

    # 设置难度级别
    level = 1
    # 全屏炸弹，大招
    bomb_image = pygame.image.load("bomb.png").convert_alpha()
    bomb_rect = bomb_image.get_rect()
    bomb_font = pygame.font.Font("images\Font.ttf", 48)
    bomb_num = 3
    # 每30秒发放一个补给包
    bullet_supply = supply.BulletSupply(bg_size)
    bomb_supply = supply.BombSupply(bg_size)
    SUPPLY_TIME = pygame.USEREVENT
    pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)
    # 超级子弹定时器
    DOUBLE_BULLET_YIME = pygame.USEREVENT + 1

    # 标志是否使用超级子弹
    is_double_bullet = False

    # 播放音乐
    pygame.mixer.music.play(-1)
    # 生成我方飞机
    me = myplane.MyPlane(bg_size)
    # 生成敌方飞机
    enemies = pygame.sprite.Group()
    # 小飞机
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 15)
    # 中飞机
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 4)
    # 大飞机
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 1)
    # 生成普通子弹
    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 5
    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet1(me.rect.midtop))

    # 生成超级子弹
    bullet2 = []
    bullet2_index = 0
    BULLET2_NUM = 5
    for i in range(BULLET2_NUM):
        bullet2.append(bullet.Bullet2(me.rect.midtop))
    # 用于延迟
    switch_image = True
    delay = 100
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    paused = not paused
                    if paused:
                        pygame.time.set_timer(SUPPLY_TIME, 0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pygame.time.set_timer(SUPPLY_TIME, 30 * 3000)
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()

            elif event.type == pygame.MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image = resume_pressed_image
                    else:
                        paused_image = pause_pressed_image
                else:
                    if paused:
                        paused_image = resume_nor_image
                    else:
                        paused_image = pause_nor_image

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if bomb_num:
                        bomb_num -= 1
                        # 爆炸音效(暂无)
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.active = False
            elif event.type == SUPPLY_TIME:
                # 发送补给音效（无）
                if random.choice([True, False]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()

            elif event.type == DOUBLE_BULLET_YIME:
                is_double_bullet = False
                pygame.time.set_timer(DOUBLE_BULLET_YIME,0)


        screen.blit(background, (0, 0))
        if not paused:
            me.move()  # 玩家飞机移动
            # 绘制补给并检测是否获得
            if bomb_supply.active:  # 全屏轰炸
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.spritecollide(bomb_supply, me, True):
                    # 获得补给音效（无）
                    if bomb_num < 3:
                        bomb_num += 1
                    bomb_supply.active = False
            if bullet_supply.active:  # 超级子弹
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.spritecollide(bullet_supply, me, True):
                    # 获得超级子弹补给音效（无）
                    is_double_bullet = True
                    pygame.time.set_timer(DOUBLE_BULLET_YIME,18*1000)  # 超级武器只能支持18秒使用时间
                    bullet_supply.active = False
            # 毁灭画像索引
            e1_destroy_index = 0
            e2_destroy_index = 0
            e3_destroy_index = 0
            me_destroy_index = 0

            if not (delay % 10):

                # 发射子弹音效（无）
                if is_double_bullet:
                    bullets = bullet2
                    # bullets[bullet2_index].move()
                    bullets[bullet2_index].reset(me.rect.midtop)
                    bullet2_index = (bullet2_index + 1) % BULLET2_NUM
                else:
                    bullets = bullet1
                    # bullets[bullet1_index].move()
                    bullets[bullet1_index].reset(me.rect.midtop)
                    bullet1_index = (bullet1_index + 1) % BULLET1_NUM

                # 检测子弹是否击中敌机
                for b in bullets:
                    if b.active:
                        b.move()
                        screen.blit(b.image, b.rect)
                        enemy_hit = pygame.sprite.spritecollide(b, enemies, False)
                        if enemy_hit:
                            b.active = False
                            for e in enemy_hit:
                                if e in mid_enemies or big_enemies:
                                    e.mp -= 1
                                    if e.mp == 0:
                                        e.active = False
                                else:
                                    e.active = False
            # 出现大飞机
            for each in big_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.images, each.rect)  # 可以用两张图片显示喷火效果
                    # 绘制血量
                    pygame.draw.line(screen, BLACK,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.right, each.rect.top - 5), 2)
                    # 当生命大于20% 血条绿色，其他红色
                    mp_remain = each.mp / enemy.BigEnemy.mp
                    if mp_remain > 0.2:
                        mp_color = GREEN
                    else:
                        mp_color = RED
                    pygame.draw.line(screen, mp_color,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.left + each.rect.width * mp_remain, each.rect.top - 5), 2)

                    #
                    # # boss登场时，提前发出警告
                    # if each.rect.bottom == -50:
                    #     # 指定音乐播放

                else:
                    # 毁灭
                    # my_over_sound.play()
                    if delay % 8:
                        screen.blit(each.destroy_images[e3_destroy_index], each.rect)
                        e3_destroy_index = (e3_destroy_index + 1) % 6
                    if e3_destroy_index == 0:
                        score += 1000
                        # boss 出现的音效停止
                        each.reset()

            # 出现中飞机
            for each in mid_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.images, each.rect)
                    # 绘制血量
                    pygame.draw.line(screen, BLACK,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.right, each.rect.top - 5), 2)
                    # 当生命大于20% 血条绿色，其他红色
                    mp_remain = each.mp / enemy.MidEnemy.mp
                    if mp_remain > 0.2:
                        mp_color = GREEN
                    else:
                        mp_color = RED
                    pygame.draw.line(screen, mp_color,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.left + each.rect.width * mp_remain, each.rect.top - 5), 2)
                else:
                    # 毁灭
                    # my_over_sound.play()
                    if delay % 8:
                        screen.blit(each.destroy_images[e2_destroy_index], each.rect)
                        e2_destroy_index = (e2_destroy_index + 1) % 6
                    if e2_destroy_index == 0:
                        score += 500
                        each.reset()
            # 出现小飞机
            for each in small_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.images, each.rect)
                else:
                    # 毁灭
                    # my_over_sound.play()
                    if delay % 8:
                        screen.blit(each.destroy_images[e1_destroy_index], each.rect)
                        e1_destroy_index = (e1_destroy_index + 1) % 6
                    if e1_destroy_index == 0:
                        score += 100
                        each.reset()
            # 碰撞检测（我方飞机是否被撞）
            enemies_down = pygame.sprite.spritecollide(me, enemies, False)
            if enemies_down:
                me.active = False
                for e in enemies_down:
                    e.active = False

            # 绘制我方飞机
            # 切换图片
            if me.active:
                if switch_image:
                    screen.blit(me.image1, me.rect)
                else:
                    screen.blit(me.image2, me.rect)
            else:
                # 毁灭
                # my_over_sound.play()
                if not (delay % 3):
                    screen.blit(me.destroy_images[me_destroy_index], me.rect)
                    me_destroy_index = (me_destroy_index + 1) % 6
                    if me_destroy_index == 0:
                        print("Game Over!")
                        running = False

            # 绘制剩余的全屏轰炸（大招）图标
            bomb_text = bomb_font.render(f"X{bomb_num}", True, WHITE)
            text_rect = bomb_text.get_rect()
            screen.blit(bomb_image, (10, height - 10 - bomb_rect.height))
            screen.blit(bomb_text, (20 + bomb_rect.width, height - 5 - text_rect.height))

        # 绘制暂停按钮
        screen.blit(paused_image, paused_rect)
        score_text = score_font.render(f"Score{score}", True, WHITE)
        screen.blit(score_text, (10, 5))
        # 根据得分增加难度
        if level == 1 and score > 10000:
            level = 2
            # 换飞机换地图等
            # 增加敌机
            add_small_enemies(small_enemies, enemies, 3)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 1)
            # 提速
            inc_speed(small_enemies, 2)
        if level == 2 and score > 20000:
            level = 3
            # 换飞机换地图等
            # 增加敌机
            add_small_enemies(small_enemies, enemies, 6)
            add_mid_enemies(mid_enemies, enemies, 4)
            add_big_enemies(big_enemies, enemies, 2)
            # 提速
            inc_speed(small_enemies, 4)
            inc_speed(mid_enemies, 2)

        delay -= 1
        if not (delay % 5):
            switch_image = not switch_image
        if not delay:
            delay = 100
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
