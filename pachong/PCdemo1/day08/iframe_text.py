import os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
browser.get('file:///' + os.path.abspath('data/iframesTest.html'))

time.sleep(3)
print(browser.page_source)
# print(browser.current_url)
frames = browser.find_elements_by_tag_name("iframe")

# 切换iframe
print('='*20)
browser.switch_to_frame(frames[0])
print(browser.page_source)
browser.quit()
