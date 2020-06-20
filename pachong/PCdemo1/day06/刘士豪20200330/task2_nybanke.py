"""
level 2:
案例：农业银行国泰基金爬虫
https://ewealth.abchina.com/fund/150010.htm
提取基金名称，涨幅，周涨幅，月涨幅，季涨幅，年涨幅
"""
import random
import time

from selenium import webdriver


# 生成浏览器对象
browser = webdriver.Chrome()
# 请求页面
browser.get('https://ewealth.abchina.com/fund/150010.htm')

elem_day_up = browser.find_elements_by_xpath('//*[@id="FundChanged"]/fonts[1]')[0].text
print(elem_day_up)

elem_week_up = browser.find_element_by_xpath('//*[@id="FundChanged"]/fonts[2]').text
print(elem_week_up)
elem_month_up = browser.find_elements_by_xpath('//*[@id="FundChanged"]/fonts[3]')[0].text
print(elem_month_up)
elem_quarter_up = browser.find_elements_by_xpath('//*[@id="FundChanged"]/fonts[4]')[0].text
print(elem_quarter_up)
elem_yearup = browser.find_elements_by_xpath('//*[@id="FundChanged"]/fonts[5]')[0].text
print(elem_yearup)
browser.close()