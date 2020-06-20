import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.maximize_window()
# 加载本地页面
browser.get('file:///' + os.path.abspath('./data/clicks.html'))
time.sleep(5)
click_btn = browser.find_element_by_id('dianji')
dbclick_btn = browser.find_element_by_class_name('shuang')
# 链式写法
# ActionChains(browser).click(click_btn).double_click(dbclick_btn).perform()

# 分布写法
actions = ActionChains(browser)
# actions.click(click_btn)
# 或者
click_btn.click()
time.sleep(4)
actions.double_click(dbclick_btn)
actions.perform()
time.sleep(6)
browser.close()
