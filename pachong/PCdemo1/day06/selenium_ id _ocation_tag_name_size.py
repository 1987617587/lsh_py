import time

from selenium import webdriver

# 生成浏览器对象
browser = webdriver.Chrome()
# 请求页面
browser.get('https://www.baidu.com/')
logo = browser.find_element_by_xpath('//div[@id="lg"]/img[@class="index-logo-src"]')
print(logo.id)
print(logo.tag_name)
print(logo.location)
print(logo.size)
