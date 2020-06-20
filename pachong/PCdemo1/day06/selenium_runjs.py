import time

from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://www.zhihu.com/explore")
time.sleep(2)
# print(browser.page_source)
# 执行js代码
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
time.sleep(3)
browser.close()