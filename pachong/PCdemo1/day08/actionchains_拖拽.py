import os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
browser.maximize_window()
# 加载本地，os把相对路径转绝对路径
browser.get('file:///' + os.path.abspath('./data/dragDropMooTools.html'))
item1 = browser.find_element_by_xpath('//div[@id="content"]/div[1]')
item2 = browser.find_element_by_xpath('//div[@id="content"]/div[2]')
item3 = browser.find_element_by_xpath('//div[@id="content"]/div[3]')
item4 = browser.find_element_by_xpath('//div[@id="content"]/div[4]')
item5 = browser.find_element_by_xpath('//div[@id="content"]/div[5]')
item6 = browser.find_element_by_xpath('//div[@id="content"]/div[6]')
item7 = browser.find_element_by_xpath('//div[@id="content"]/div[7]')
item8 = browser.find_element_by_xpath('//div[@id="content"]/div[8]')
item9 = browser.find_element_by_xpath('//div[@id="content"]/div[9]')
time.sleep(5)

# 开始拖拽
# 生成ActionChains对象，需要参数browser
# 直接拖拽
actions = ActionChains(browser)
actions.drag_and_drop(item1, item7).perform()
time.sleep(5)

actions = ActionChains(browser)
actions.click_and_hold(item2).release(item8).perform()
time.sleep(5)

actions = ActionChains(browser)
actions.click_and_hold(item3).move_to_element(item9).release().perform()
time.sleep(5)

actions = ActionChains(browser)
actions.drag_and_drop_by_offset(item4, 200, 0).perform()
time.sleep(5)
browser.quit()
