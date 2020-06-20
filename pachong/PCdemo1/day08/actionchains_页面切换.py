import os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')

time.sleep(5)
print(browser.window_handles)
browser.execute_script('window.open()')  # 打开新的窗口
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])  # 切换到第二个窗口
browser.get('http://www.taobao.com')
time.sleep(5)
browser.switch_to.window(browser.window_handles[0])  # 切换到第一个窗口
print(browser.window_handles)
print(browser.title)
time.sleep(5)
browser.switch_to.window(browser.window_handles[1])  # 切换到第二个窗口
print(browser.title)
time.sleep(2)

browser.get('http://python.org')  # 在第二个窗口进入新连接
time.sleep(2)
print(browser.title)

browser.quit()
