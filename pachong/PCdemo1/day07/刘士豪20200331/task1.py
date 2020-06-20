'''
案例：河南税务总局爬虫
http://henan.chinatax.gov.cn/003/index.html?NVG=0&LM_ID=1
爬取税务新闻，基层动态，媒体视点中标题，url，发布时间

'''

import random
import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
import time


def get_news(nums):
    print("开始提取信息",nums)
    # print(browser.page_source)
    ls = browser.find_elements_by_xpath('//*[@id="m_tab1_bd"]/ul['+str(nums)+']/li')
    print('len', len(ls))
    for news in ls:
        # title = news.find_element_by_xpath('.//a').text.strip()
        title = news.find_element_by_xpath('.//a').get_attribute('title')
        print(f"title:{title}")
        url = news.find_element_by_xpath('.//a').get_attribute('href')
        print(f"url:{url}")
        # pub_date = news.find_element_by_xpath('.//span').text.strip()
        pub_date = news.get_attribute('newsdate')
        print(f"pub_date:{pub_date}")



browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://henan.chinatax.gov.cn/003/index.html?NVG=0&LM_ID=1')
# 定位元素
btn1 = browser.find_element_by_xpath('//*[@id="m_tab1"]/div[1]/ul/li[1]/a')
btn2 = browser.find_element_by_xpath('//*[@id="m_tab1"]/div[1]/ul/li[2]/a')
btn3 = browser.find_element_by_xpath('//*[@id="m_tab1"]/div[1]/ul/li[3]/a')
actions = ActionChains(browser)
# 等待
time.sleep(3)
# 移动鼠标到btn1
actions.move_to_element(btn1).perform()
print(btn1.text)
# 获取税务新闻下的数据
get_news(1)
time.sleep(3)
# 生成新的actions对象
actions = ActionChains(browser)
# 移动鼠标到btn2
actions.move_to_element(btn2).perform()
print(btn2.text)
# 获取基层动态下的数据
get_news(2)
time.sleep(5)
# 移动鼠标到btn3
actions.move_to_element(btn3).perform()
print(btn3.text)
# 获取媒体视点下的数据
get_news(3)
time.sleep(5)
browser.close()



