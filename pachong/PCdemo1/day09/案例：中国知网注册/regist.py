'''
https://my.cnki.net/Register/CommonRegister.aspx#
'''

from selenium import webdriver
from PIL import Image
import time
from chaojiying import Chaojiying_Client

CHAOJIYING_USERNAME = 'Thompson'
CHAOJIYING_PWD = 'Thompson'
CHAOJIYING_SOFT_ID = '1bce712d583f72be3a40d5960a86c94f'

browser = webdriver.Chrome()
url = 'https://my.cnki.net/Register/CommonRegister.aspx'
browser.get(url)

user = browser.find_element_by_id('username')  # 用户名输入框
pwd = browser.find_element_by_id('txtPassword')  # 密码输入框
email = browser.find_element_by_id('txtEmail')  # email输入框
check_code = browser.find_element_by_id('txtOldCheckCode')  # 验证码输入框
verify = browser.find_element_by_id('checkcode')  # 验证码图片
btn_reg = browser.find_element_by_id('ButtonRegister')  # 登陆按钮

time.sleep(2)
user.send_keys('laoguo@163.com')
time.sleep(2)
pwd.send_keys('mimamima')
time.sleep(2)
email.send_keys('laoguo@163.com')

browser.save_screenshot('./images/zhiwang.png')
left = verify.location['x']
top = verify.location['y']
right = verify.location['x'] + verify.size['width']
bottom = verify.location['y'] + verify.size['height']
im = Image.open('./images/zhiwang.png')
im_crop = im.crop((left, top, right, bottom))
im_crop.save('./images/zwcaptchar.png')

chaojiying = Chaojiying_Client(CHAOJIYING_USERNAME, CHAOJIYING_PWD, CHAOJIYING_SOFT_ID)  # 用户中心>>软件ID 生成一个替换 96001
im = open('./images/zwcaptchar.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
dict_code = chaojiying.PostPic(im, 1004)
print(dict_code)
check_code.send_keys(dict_code['pic_str'])

# 模拟点击注册
# btn_reg.click()