"""
微博自动登录
"""
import random
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
        time.sleep(10)
        # 此时browser拥有登陆过的所有信息
        return browser
        # browser.close()
    except Exception as e:
        print(e, "登陆失败")
        return None


def crawl(browser, url):
    """

    :param browser: 自动登录之后返回的
    :param url: 指定爬取的页面
    :return:
    """
    try:
        print("加载指定微博")
        browser.maximize_window()
        browser.get(url)
        # 返回页面的高度
        last_height = browser.execute_script('return document.body.scrollHeight;')
        while True:
            print("页面向下加载中……")
            browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            # 等待随机时间
            time.sleep(random.random() * 5 + 1)
            # 计算滚动之后的页面高度
            new_height = browser.execute_script('return document.body.scrollHeight;')
            print("当前页面高度", new_height)
            if new_height == last_height:
                print("到底了")
                break
            last_height = new_height

        print("加载结束")
        print("开始提取信息")
        ls = browser.find_elements_by_xpath('//div[@class="WB_detail"]')
        print(f"len:{len(ls)}")
        for item in ls:
            name = item.find_element_by_xpath('.//div[@class="WB_info"]/a[@class="W_f14 W_fb S_txt1"]').text
            print(f"name:{name}")
            pub_time = item.find_element_by_xpath('.//div[@class="WB_from S_txt2"]/a').text.strip()
            print(f"pub_time:{pub_time}")
            # 内容可能不存在
            content = item.find_elements_by_xpath('.//div[@class="WB_text W_f14"]')
            if len(content) > 0:
                content = content[0].text.strip()
            else:
                content = "空"
            print(f"content:{content}")
            print("=" * 100)

    except Exception as e:
        print("请求失败", e)


if __name__ == '__main__':
    username = '1711960368@qq.com'
    pwd = '1711960368i'

    browser = login(username, pwd)
    url = 'https://weibo.com/xiena?is_hot=1'
    crawl(browser, url)
