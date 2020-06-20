'''
案例：12306登陆
https://kyfw.12306.cn/otn/login/init
'''

from selenium import webdriver
from PIL import Image
import time
from chaojiying import Chaojiying_Client
from selenium.webdriver import ActionChains

CHAOJIYING_USERNAME = 'Thompson'
CHAOJIYING_PWD = 'Thompson'
CHAOJIYING_SOFT_ID = '1bce712d583f72be3a40d5960a86c94f'

browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://kyfw.12306.cn/otn/login/init'
browser.get(url)

user = browser.find_element_by_id('username')  # 用户名输入框
pwd = browser.find_element_by_id('password')  # 密码输入框

verify = browser.find_element_by_class_name('touclick-image')  # 验证码图片
btn_reg = browser.find_element_by_id('loginSub')  # 登陆按钮

time.sleep(2)
user.send_keys('laoguo@163.com')
time.sleep(2)
pwd.send_keys('mimamima')
time.sleep(2)

browser.save_screenshot('./images/12306.png')
left = verify.location['x']
top = verify.location['y']
right = verify.location['x'] + verify.size['width']
bottom = verify.location['y'] + verify.size['height']
# 从截取的图片中，再剪切出只包含验证码图片
im = Image.open('./images/12306.png')
im_crop = im.crop((left, top, right, bottom))
im_crop.save('./images/kyfw.png')

chaojiying = Chaojiying_Client(CHAOJIYING_USERNAME, CHAOJIYING_PWD, CHAOJIYING_SOFT_ID)  # 用户中心>>软件ID 生成一个替换 96001
im = open('./images/kyfw.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
dict_code = chaojiying.PostPic(im, 9004)
print(dict_code)

goods = dict_code['pic_str'].split('|')
for good in goods:
    good_x_y = good.split(',')
    print(good_x_y[0],good_x_y[1])
    x,y = int(good_x_y[0]),int(good_x_y[1])


    # 鼠标移动到指定坐标

    # actions.move_by_offset(x+708, y+315).perform()
    print("点击指定物品")
    ActionChains(browser).move_to_element_with_offset(verify, x, y).click().perform()

# 报错
chaojiying.PostPic(dict_code['pic_id'],codetype='utf8')


# 模拟点击注册
# btn_reg.click()