'''

http://pccz.court.gov.cn/pcajxxw/gkaj/gkaj?lx=999


提取标题，链接，案件类型，日期，经办法院，被申请人，申请人
爬取10页，存储为excel文件
'''


# 新建管道2
import xlwt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import re

# 页面请求
import pymysql
import requests
# 数据提取
from bs4 import BeautifulSoup
from lxml import etree
# 数据存储
import csv
# 打开文件，避免空行
import codecs
# 设置爬取的随机延迟
import time
import random

from day02.requests_xundaili import down

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
}



# 提取标题，链接，案件类型，日期，经办法院，被申请人，申请人
# Title, detail_url, case_type, pud_date, handling _court, respondent, applicant
try:
    # 生成workbook 对象  execl文档的对象
    xls = xlwt.Workbook()
    # 新建execl文档中的sheet
    sheet1 = xls.add_sheet('pccz')
    row = 1
    # 添加字段标题，链接，案件类型，日期，经办法院，被申请人，申请人
    sheet1.write(0, 0, '序号')
    sheet1.write(0, 1, '标题')
    sheet1.write(0, 2, '链接')
    sheet1.write(0, 3, '案件类型')
    sheet1.write(0, 4, '日期')
    sheet1.write(0, 5, '经办法院')
    sheet1.write(0, 6, '被申请人')
    sheet1.write(0, 7, '申请人')

except Exception as e:
    print(e)


browser = webdriver.Chrome()
browser.maximize_window()
# 定义等待条件
wait = WebDriverWait(browser, 60)
try:
    browser.get("http://pccz.court.gov.cn/pcajxxw/gkaj/gkaj?lx=999")
    # 等待搜索结果中的条目加载完成
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.clearfix'))
    )
    # 等待加载页数元素
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.pageBtnWrap'))
    )

    total = 10
    page = 1

    while True:
        print(f"正在加载第{page}页")
        # 等待搜索结果中的条目加载完成
        wait.until(
            # EC.presence_of_element_located((By.CSS_SELECTOR, '.jsTj.w1008'))
            EC.presence_of_element_located((By.CSS_SELECTOR, '.cbt'))
        )
        # 等待搜索结果中的条目加载完成
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.pageBtnWrap'))
        )
        # print(browser.page_source)
        ls = browser.find_elements_by_xpath('//li[@class="clearfix"]')
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(random.random())
        print(f'len:{len(ls)}')
        for item in ls:
            # 添加字段标题，链接，案件类型，日期，经办法院，被申请人，申请人
            # title, detail_url, case_type, pud_date, handling_court, respondent, applicant
            title = item.find_element_by_xpath('./div[1]/h4[@class="cbt"]/a').text.strip()
            print(f'title:{title}')
            detail_url = item.find_element_by_xpath('./div[1]/h4[@class="cbt"]/a').get_attribute('href')
            print(f'detail_url:{detail_url}')
            case_type = item.find_element_by_xpath('.//span[@class="ajlx"]').text.strip()
            print(f'case_type:{case_type}')
            pud_date = item.find_element_by_xpath('.//span[@class="date"]').text.strip()
            print(f'pud_date:{pud_date}')

            handling_court = item.find_element_by_xpath('./div[@class="center"]/p[1]').text.strip()
            print(f'handling_court:{handling_court}')
            respondent = item.find_element_by_xpath('./div[@class="center"]/p[2]').text.strip()
            print(f'respondent:{respondent}')
            applicant = item.find_element_by_xpath('./div[@class="center"]/p[3]').text.strip()
            print(f'applicant:{applicant}')
            print('=' * 99)
            # 存储
            print(row,type(title),type(detail_url),type(pud_date))
            sheet1.write(row, 0, row)
            sheet1.write(row, 1, title)
            sheet1.write(row, 2, detail_url)
            sheet1.write(row, 3, case_type)
            sheet1.write(row, 4, pud_date)
            sheet1.write(row, 5, handling_court)
            sheet1.write(row, 6, respondent)
            sheet1.write(row, 7, applicant)
            xls.save('pccz.xls')
            print("存储成功")
            row += 1
            
        # 翻页
        page += 1
        if page <= total:
            # 通过页面跳转输入框进行翻页
            tb_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#kkpager_btn_go_input'))
            )
            tb_input.clear()
            tb_input.send_keys(str(page))
            time.sleep(3)
            # 按钮
            search_btn = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#kkpager_btn_go'))
            )

            search_btn.click()
        else:
            break
        time.sleep(random.random())


except Exception as e:
    print(e)
finally:
    browser.quit()



