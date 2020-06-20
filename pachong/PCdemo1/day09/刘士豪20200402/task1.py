'''
level 2:
案例：柳州住建局
tesseract识别验证码图片
http://zjj.zhuzhou.gov.cn/c13948/


'''

import time

import pytesseract
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from PIL import Image

# 文本带背景


browser = webdriver.Chrome()
browser.get('http://zjj.zhuzhou.gov.cn/c13948/')
# 创建智能等待对象
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_all_elements_located((By.ID, 'img')))
browser.save_screenshot('./images/zhuzhou.png')

verify = browser.find_element_by_id('img')  # 验证码图片
# 确定验证码大小
left = verify.location['x']
top = verify.location['y']
right = verify.location['x'] + verify.size['width']
bottom = verify.location['y'] + verify.size['height']
im = Image.open('./images/zhuzhou.png')
im_crop = im.crop((left, top, right, bottom))
im_crop.save('./images/tesseract.png')


image = Image.open('./images/tesseract.png')
# 直接识别 无法识别
# text = pytesseract.image_to_string(image)
# 处理背景
image.show()
# 灰度化处理
gray = image.convert('L')
gray.show()
# 二值化处理
threshold = 190
bw = gray.point(lambda x: 0 if x > threshold else 255, '1')
bw.show()
# 此时只有0和255，0的就是想要的信息
text = pytesseract.image_to_string(gray)

print(text)
browser.close()