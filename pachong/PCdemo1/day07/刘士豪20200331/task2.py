'''

案例：网易科技频道爬虫
http://tech.163.com/
爬取新闻标题，链接


'''


import random
import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
import json
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://tech.163.com/')


try:
    print("当前进入链接为：", browser, browser.current_url)
    # 返回页面的高度
    last_height = browser.execute_script('return document.body.scrollHeight;')
    while True:
        print("页面向下加载中……")
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        # 等待随机时间
        time.sleep(random.random() * 2 + 3)
        # 计算滚动之后的页面高度
        new_height = browser.execute_script('return document.body.scrollHeight;')
        print("当前页面高度", new_height)
        if new_height == last_height:
            print("到底了")
            break
        last_height = new_height

    print("加载结束")
    print("开始提取信息")
    ls = browser.find_elements_by_xpath('//div[@class="ndi_main"]/div[@class="data_row news_article clearfix"]')
    print('len', len(ls))
    with open('wangyi.txt','w',encoding='utf-8') as  file:
        for news in ls:
            title = news.find_element_by_xpath('.//div[@class="news_title"]//a').text.strip()
            print(f"title:{title}")
            url = news.find_element_by_xpath('.//div[@class="news_title"]//a').get_attribute('href')
            print(f"url:{url}")
            tag = news.find_element_by_xpath('.//div[@class="news_tag"]//a').text.strip()
            print(f"tag:{tag}")
            data = json.dumps({'title':title,'url':url,'tag':tag})+'\n'
            file.write(data)
except Exception as e:
    print(e)


