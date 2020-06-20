'''

案例：新浪体育爬虫
http://sports.sina.com.cn/
向下拉动滚动条3次，
爬取新闻标题，链接
'''
import random
import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://sports.sina.com.cn/')


try:
    print("当前进入链接为：", browser, browser.current_url)
    # 返回页面的高度
    last_height = browser.execute_script('return document.body.scrollHeight;')
    for i in range(3):
        print("页面向下加载中……")
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        # 等待随机时间
        time.sleep(random.random() * 2 + 3)
        # 计算滚动之后的页面高度
        new_height = browser.execute_script('return document.body.scrollHeight;')
        print("当前页面高度", new_height)


    print("下拉三次加载结束")
    print("开始提取信息")
    ls = browser.find_elements_by_xpath('//div[@class="ty-card ty-card-type1 clearfix"]')
    print('len', len(ls))
    for news in ls:
        title = news.find_element_by_xpath('.//h3[@class="ty-card-tt"]//a').text.strip()
        print(f"title:{title}")
        url = news.find_element_by_xpath('.//h3[@class="ty-card-tt"]//a').get_attribute('href')
        print(f"url:{url}")
        pub_date = news.find_element_by_xpath('.//span[@class="ty-card-tip2-i ty-card-time"]').text.strip()
        print(f"pub_date:{pub_date}")
except Exception as e:
    print(e)


