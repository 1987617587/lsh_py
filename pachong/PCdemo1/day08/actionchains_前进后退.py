import os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
# 加载本地，os把相对路径转绝对路径
browser.get('http://www.baidu.com')

time.sleep(5)
browser.find_element_by_link_text("新闻").click()
time.sleep(5)
print(browser.title)

browser.back()
time.sleep(5)
print(browser.title)
browser.forward()
print(browser.title)
time.sleep(5)
browser.quit()
