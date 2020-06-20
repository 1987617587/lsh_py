from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('file:///' + os.path.abspath('./data/mouseover.html'))
# 定位元素
btn1 = browser.find_element_by_xpath('//div[@class="btn1"]')
btn2 = browser.find_element_by_xpath('//div[@class="btn2"]')
actions = ActionChains(browser)
# 等待
time.sleep(3)
# 移动鼠标到btn1
actions.move_to_element(btn1).perform()
print(btn1.text)
time.sleep(3)
# 生成新的actions对象
actions = ActionChains(browser)
# 鼠标移动到（10，50）也即是btn2上
actions.move_by_offset(10, 50).perform()
print(btn2.text)
time.sleep(3)
actions = ActionChains(browser)
# 从btn2移动到btn1
actions.move_to_element_with_offset(btn2, 10, -50).perform()
print(btn1.text)
time.sleep(3)
browser.close()
