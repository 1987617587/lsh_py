"""
微博自动登录
"""
import time

from selenium import webdriver


def login(username, pwd):
    try:
        browser = webdriver.Chrome()
        # 窗口最大化
        browser.maximize_window()
        browser.get("https://weibo.com/login.php")
        time.sleep(2)
        elem_username = browser.find_element_by_id('loginname')
        # 清除输入框内容
        elem_username.clear()
        print("正在输入用户名")
        elem_username.send_keys(username)
        time.sleep(3)
        elem_pwd = browser.find_element_by_name('password')
        elem_pwd.clear()
        print("正在输入密码")
        elem_pwd.send_keys(pwd)
        time.sleep(3)
        # 验证码
        elem_verify = browser.find_element_by_xpath('//div[@class="info_list verify clearfix"]')
        if elem_verify.get_attribute('style') != 'display: none;':
            print('需要输入验证码')
            v = input('请输入验证码：')
            time.sleep(3)
            elem_input_verify = browser.find_element_by_name('verifycode')
            elem_input_verify.send_keys(v)

        time.sleep(3)
        print('点击登录')
        submit_btn = browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
        submit_btn.click()
        time.sleep(100)
        browser.close()
    except Exception as e:
        print(e, "登陆失败")


if __name__ == '__main__':
    username = '1711960368@qq.com'
    pwd = '1711960368i'

    login(username, pwd)

# url = 'https://weibo.com/'
# browser = webdriver.Chrome()
# browser.get(url)
# time.sleep(3)
#
# # 定位搜索框
# input = browser.find_element_by_id('kw')
# # 向输入框输入信息
# input.send_keys("奇酷信息")
# time.sleep(1)
# # 找到点击按钮
# btn_submit = browser.find_element_by_id('su')
# # 点击
# btn_submit.click()
# time.sleep(2)
# # 打印当前url
# print(browser.current_url)
# # 关闭浏览器
# browser.quit()
