import os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
browser.get('https://www.douban.com/')
# 此处注意iframe
loginframe = browser.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[@class="login"]/iframe')
# browser.switch_to_frame(loginframe)
browser.switch_to.frame(loginframe)
print(browser.page_source)
time.sleep(2)
# 切换登录方式（选择密码登录）
tag_btn = browser.find_element_by_xpath('//li[@class="account-tab-account"]')
tag_btn.click()
time.sleep(2)

# 查找账户名输入框
input_user = browser.find_element_by_id('username')
input_user.clear()
input_user.send_keys('3414018462@qq.com')
time.sleep(2)
# 查找密码输入框
input_pwd = browser.find_element_by_id('password')
input_pwd.clear()
input_pwd.send_keys('qikuedu9527')
time.sleep(2)
# 查找登录按钮
login_btn = browser.find_element_by_xpath('//div[@class="account-form"]/div[@class="account-form-field-submit "]/a')
# 模拟点击登录
login_btn.click()
# 处理验证码 TODO
# 生成登陆之后的快照
browser.save_screenshot('images/douban.png')
with open('data/douban2.html','w',encoding='utf-8') as file:
    file.write(browser.page_source)
