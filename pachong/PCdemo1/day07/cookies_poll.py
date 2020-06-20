from selenium import webdriver
import time
import random
import pymysql
import requests
import json


class CookiesPool:
    def __init__(self, crawl=True):
        # 初始化操作
        try:
            self.conn = pymysql.connect(host="localhost", port=3306, user='root', password='123456',
                                        db='lshmysql', charset='utf8')
            self.cur = self.conn.cursor()
            self.id_list = []
            self.get_from_db()
            if crawl:
                self.browser = webdriver.Chrome()
        except Exception as e:
            print(e)

    def get_from_db(self):
        '''
        从数据库读取已有的cookies信息
        :return:
        '''
        strsql = 'select*from dbcookies'
        self.cur.execute(strsql)
        results = self.cur.fetchall()
        for item in results:
            username = item[1]
            cookies = item[3]
            home_url = item[4]
            self.id_list.append(username)

    def gen_cookies(self, username, pwd):
        '''
        用给定的账户名和密码生成cookies
        :param username:
        :param pwd:
        :return:
        '''
        try:
            # 窗口最大化
            self.browser.maximize_window()
            self.browser.get("http://www.weibo.com/login.php")
            time.sleep(2)
            print('输入账户名....')
            elem_user = self.browser.find_element_by_id('loginname')
            # 清除输入框的内容
            elem_user.clear()
            elem_user.send_keys(username)
            time.sleep(3)
            print('输入密码...')
            elem_pwd = self.browser.find_element_by_name('password')
            elem_pwd.clear()
            elem_pwd.send_keys(pwd)
            time.sleep(3)
            elem_verify = self.browser.find_element_by_xpath('//div[@class="info_list verify clearfix"]')
            if elem_verify.get_attribute('style') != "display: none;":
                print('输入验证码....')
                v = input('请输入验证码：')
                time.sleep(3)
                elem_input_verify = self.browser.find_element_by_name('verifycode')
                elem_input_verify.send_keys(v)
            time.sleep(3)
            print('点击登陆...')
            submit_btn = self.browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
            submit_btn.click()
            time.sleep(10)
            cookies = self.browser.get_cookies()
            home_url = self.browser.current_url
            print('home_url:', home_url)
            return (cookies, home_url)
        except Exception as e:
            print('登陆失败...')
        return None

    def check_cookies(self, username, cookies, home_url):
        '''
        检测cookie的有效性
        :param username:
        :param cookies:
        :param home_url:
        :return:
        '''
        try:
            cookies = json.loads(cookies)
            print('cookies type:', type(cookies))
        except Exception as e:
            print('cookies不合法', username)
            self.del_cookies(username)
            print('删除cookies', username)
            print(e)
            return False

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
            }
            cookies = requests.utils.cookiejar_from_dict(cookies)
            response = requests.get(home_url, headers=headers, cookies=cookies, allow_redirects=False, timeout=5)
            print('statuscode:', response.status_code)
            if response.status_code == 200:
                print('cookies有效', username)
                return True
            else:
                print('cookies无效', username)
                return False
        except Exception as e:
            print(e)
            return False

    def save(self, username, password, cookies, home_url):
        '''
        存储cookies信息
        :param username:
        :param password:
        :param cookies:
        :param home_url:
        :return:
        '''
        if username not in self.id_list:
            try:
                d = {}
                for cookie in cookies:
                    d[cookie['name']] = cookie['value']
                cookies = json.dumps(d)
                strsql = 'insert into dbcookies VALUES (0,%s,%s,%s,%s)'
                params = (username, password, cookies, home_url)
                print('save:', params)
                self.cur.execute(strsql, params)
                self.conn.commit()
                self.id_list.append(username)
                print('save:', username)
            except Exception as e:
                print(e)

    def get_proxy(self):
        '''
        随机获取有效的cookies
        :return:
        '''
        if len(self.id_list) <= 0:
            return None
        username = random.choice(self.id_list)
        strsql = 'select * from dbcookies WHERE username="' + username + '"'
        self.cur.execute(strsql)
        result = self.cur.fetchone()
        if result != None:
            username = result[1]
            cookies = result[3]
            home_url = result[4]
            if self.check_cookies(username, cookies, home_url):
                try:
                    cookies = json.loads(cookies)
                    return cookies
                except Exception as e:
                    print(e)
                    self.del_cookies(username)
                    return self.get_proxy()
            else:
                self.del_cookies(username)
                return self.get_proxy()
        else:
            return self.get_proxy()

    def del_cookies(self, username):
        '''
        删除指定的无效的cookie
        :param username:
        :return:
        '''
        strsql = 'delete from dbcookies WHERE username="' + username + '"'
        self.cur.execute(strsql)
        self.conn.commit()
        self.id_list.remove(username)
        print('del cookies:', username)

    def close(self):
        '''
        断开和数据库连接，关闭浏览器对象等
        :return:
        '''
        try:
            self.cur.close()
            self.conn.close()
            self.browser.close()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    pool = CookiesPool()
    username = '3414018462@qq.com'
    password = 'qikuedu9527'
    result = pool.gen_cookies(username, password)
    print('result:', result)
    if result != None:
        cookies = result[0]
        home_url = result[1]
        pool.save(username, password, cookies, home_url)
        print(pool.get_proxy())
    pool.close()