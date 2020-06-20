"""
百度自动搜索
"""
import time

from selenium import webdriver
url = 'https://www.baidu.com'
browser = webdriver.Chrome()
browser.get(url)
time.sleep(3)

# 定位搜索框
input = browser.find_element_by_id('kw')
# 向输入框输入信息
input.send_keys("奇酷信息")
time.sleep(1)
# 找到点击按钮
btn_submit = browser.find_element_by_id('su')
# 点击
btn_submit.click()
time.sleep(2)
# 打印当前url
print(browser.current_url)
# 关闭浏览器
browser.quit()

