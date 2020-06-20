'''
B站登录验证码处理
'''
import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from PIL import Image


# <canvas class="geetest_canvas_bg geetest_absolute __web-inspector-hide-shortcut__" height="160" width="260"></canvas>


class Crack():
    def __init__(self, username, password):
        '''
        初始化操作
        '''
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.Border = 5
        self.username = username
        self.password = password

    def open(self):
        '''
        打开浏览器加载页面
        :return:
        '''
        url = 'https://passport.bilibili.com/login'
        self.wait = WebDriverWait(self.browser, 60)
        self.browser.get(url)
        # 用户名输入框
        input_user = self.wait.until(
            EC.presence_of_element_located((By.ID, 'login-username'))
        )
        input_user.clear()
        input_user.send_keys(self.username)

        time.sleep(3)

        # 密码输入框
        input_passwd = self.wait.until(
            EC.presence_of_element_located((By.ID, 'login-passwd'))
        )
        input_passwd.clear()
        input_passwd.send_keys(self.password)

        time.sleep(3)
        # 查找登录按钮
        login_btn = self.browser.find_element_by_xpath('//a[@class="btn btn-login"]')
        login_btn.click()

    def get_images(self):
        '''
        获取验证码图片
        :return:
        '''
        time.sleep(2)
        web_filename = './images/web.jpg'  # 页面截屏图片
        # 隐藏小图块
        myjs = 'document.getElementsByClassName("geetest_canvas_slice")[0].style.display="none";'
        self.browser.execute_script(myjs)
        # 截屏，包含带阴影的验证码的背景图
        self.browser.save_screenshot(web_filename)
        # 恢复显示小图块
        myjs = 'document.getElementsByClassName("geetest_canvas_slice")[0].style.display="block";'
        self.browser.execute_script(myjs)
        # 查找带阴影背景图的元素
        elem = self.browser.find_element_by_xpath('//canvas[@class="geetest_canvas_bg geetest_absolute"]')
        # 确定元素的位置和尺寸
        location = elem.location
        size = elem.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        print('验证码位置：', top, bottom, left, right)
        screen_shot = Image.open(web_filename)
        # 截取带阴影验证码背景图
        capcha = screen_shot.crop((left, top, right, bottom))  # crop()：裁剪图片
        bg_filename = './images/bzyzm.png'
        capcha.save(bg_filename)
        # 显示不带阴影的验证码背景图
        myjs = 'document.getElementsByClassName("geetest_canvas_fullbg")[0].style.display="block";'
        self.browser.execute_script(myjs)
        # 截屏，包含不带阴影验证码的背景图的图片
        self.browser.save_screenshot(web_filename)
        # 查找不带阴影的验证码背景图
        elem = self.browser.find_element_by_class_name("geetest_canvas_fullbg")
        # 确定元素的位置和尺寸
        location = elem.location
        size = elem.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        print('验证码位置：', top, bottom, left, right)
        screen_shot = Image.open(web_filename)
        # 截取不带阴影验证码背景图
        capcha = screen_shot.crop((left, top, right, bottom))  # crop()：裁剪图片
        bg_filename = './images/bzyzmfull.png'
        capcha.save(bg_filename)
        # 隐藏不带阴影的验证码背景图
        myjs = 'document.getElementsByClassName("geetest_canvas_fullbg")[0].style.display="none";'
        self.browser.execute_script(myjs)

    def get_gap(self):
        '''
        计算移动的距离，即阴影滑块的位置
        :return: distance
        '''
        # 加载验证码图片（包含带阴影和不带阴影的图片）
        bg_filename = 'images/bzyzm.png'
        bg_full_filename = 'images/bzyzmfull.png'
        bg_img = Image.open(bg_filename)
        bg_full_img = Image.open(bg_full_filename)
        left = 10
        # bg_full_img.size获取图片尺寸(元组类型),bg_img.size[0]宽,bg_img.size[1]高
        for i in range(left, bg_img.size[0]):
            for j in range(bg_img.size[1]):
                # 获取图片中指定位置的像素
                # load():加载Image对象的像素
                # 二维循环对比两张图片所有点的像素值，找到阴影滑块的位置
                pix1 = bg_img.load()[i, j]
                pix2 = bg_full_img.load()[i, j]
                # 允许像素偏差临界值
                threshold = 20
                # 判断RGB像素值是否在临界值内
                if abs(pix1[0] - pix2[0]) < threshold and abs(pix1[1] - pix2[1]) < threshold and abs(
                        pix1[2] - pix2[2]) < threshold:
                    # print("像素几乎相同,认为一种颜色")
                    pass
                else:
                    # 找到不同的了，这地方就是阴影滑块的颜色,left就是要移动的距离
                    left = i
                    return left

    def get_track(self, distance):
        '''
        根据距离，获取移动轨迹
        :param distance:需要移动滑块的总位移
        :return:track，列表内是每0.1s内需要移动的距离
        '''
        # 移动轨迹
        track = []
        # 当前的位移
        current = 0
        # 速度阈值（前面匀加速，后面匀减速）
        mid = distance * 0.7
        # 设置时间间隔
        t = 0.1
        # 初速度
        v = 0
        while current < distance:
            if current < mid:
                # 加速运动
                a = 40
            else:
                # 减速运动
                a = -24
            # 初速度
            v0 = v
            # 当前速度 v= v0+at
            v = v0 + a * t
            # t时间间隔内移动的位移 s = v0t + 1/2*at^2
            move = v0 * t + a * t ** 2 / 2
            # 当前的位移
            current += move
            # round()四舍五入
            track.append(round(move))

        print(current, distance)
        move = distance - current
        track.append(round(move))
        return track

    def move_to_gap(self,track:list):
        '''
        根据给定的轨迹模拟滑动滑块到缺口位置
        :return:
        '''
        slider = self.browser.find_element_by_xpath('//div[@class="geetest_slider_button"]')
        # 抓住滑动按钮
        ActionChains(self.browser).click_and_hold(slider).perform()
        # 开始按照轨迹滑动按钮
        while track:
            # 从列表头部获取一个元素（0.1s需要移动的位移），然后删除列表中改元素
            x = track.pop(0)
            # 开始按照轨迹滑动按钮
            ActionChains(self.browser).move_by_offset(xoffset=x,yoffset=0).perform()
        time.sleep(1.6)
        # 释放按钮
        print('release ...')
        ActionChains(self.browser).release(slider).perform()
        time.sleep(3)
        # self.browser.close()



if __name__ == '__main__':
    crack = Crack('123', '123')
    # 打开浏览器
    crack.open()
    crack.get_images()
    # 获取阴影滑块（滑块目标位置）
    gap = crack.get_gap()
    print('gap:',gap)
    # 生成移动轨迹列表
    track = crack.get_track(gap-crack.Border)
    # 拖动滑块到目标位置
    crack.move_to_gap(track)
