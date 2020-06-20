import pymysql
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random
import requests
import hashlib


class ProxyIpPool:
    def __init__(self, crawl=True):
        '''
        初始化参数
        '''
        try:
            self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='py1911')
            self.cur = self.conn.cursor()
            self.id_list = []
            self.get_from_db()
            if crawl:
                self.browser = webdriver.Chrome()
                print("创建browser")
        except Exception as e:
            print(e)

    def get_from_db(self):
        ''''
        从数据库中读取已有的ip
        '''
        strsql = 'select * from proxyippool'
        self.cur.execute(strsql)
        results = self.cur.fetchall()
        for item in results:
            ip = item[1]
            port = item[2]
            # 此时id 是数据库中ipid
            id = item[3]
            protocal = item[4].lower()
            self.id_list.append(id)

    def down_ips(self, url):
        '''
        从网站批量获取代理ip
        :return:
        '''
        self.browser.get(url)
        ls = self.browser.find_elements_by_css_selector('table#ip_list > tbody > tr')
        # 去除标题行
        ls.pop(0)
        print(f'len:{len(ls)}')
        for item in ls:
            ip = item.find_elements_by_css_selector('td')[1].text
            port = item.find_elements_by_css_selector('td')[2].text
            protocal = item.find_elements_by_css_selector('td')[5].text
            protocal = protocal.lower()
            proxy = protocal + '://' + ip + ':' + port
            print(f'proxy:{proxy}')
            if self.check_ip(proxy, protocal):
                print(f'valid ip:{proxy}')
                self.save(ip, port, protocal)
            time.sleep(random.random())

    def check_ip(self, ip, protocal):
        '''
        检测ip的有效性
        :param ip:
        :return:
        '''
        # headers = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        # }
        # proxies = {'http', ip}
        # if protocal == "https":
        #     proxies = {'https', ip}
        # print(f'proxies:{proxies}')
        # try:
        #     print('check:', ip)
        #     # http://www.ip138.com/可以查询ip地址
        #     url = 'http://www.ip138.com/'
        #     code = requests.get(url, proxies=proxies, headers=headers, timeout=10).status_code
        #     if code == 200:
        #         return True
        #     return False
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        }
        proxies = {'http': ip}
        if protocal == 'https':
            proxies = {'https': ip}
        print(proxies)
        try:
            print('check:', ip)
            url = 'http://www.ip138.com/'
            code = requests.get(url, proxies=proxies, headers=headers, timeout=10).status_code
            if code == 200:
                return True
            else:
                return False
        except Exception as e:
            print('check_ip出错',e)

    def save(self, ip, port, protocal):
        '''
        存储代理ip
        :param ip:
        :param port:
        :return:
        '''
        print('begin save...')
        proxy = ip + ':' + port
        h = hashlib.md5()
        h.update(proxy.encode())
        id = h.hexdigest()
        if id not in self.id_list:
            try:
                srtsql = 'insert into proxyippool values (0,%s,%s,%s,%s)'
                params = [ip, port, id, protocal]
                self.cur.execute(srtsql, params)
                self.conn.commit()
                print('save successful:', proxy)
            except Exception as e:
                print(e)

    def get_proxy(self):
        '''
        随机提取有效的代理ip
        :return:
        '''
        if len(self.id_list) <= 0:
            return None
        id = random.choice(self.id_list)
        print(f'id:{id}')
        try:
            strsql = 'select * from proxyippool where idip="' + id + '"'
            self.cur.execute(strsql)
            result = self.cur.fetchone()
            if result:
                ip = result[1]
                port = result[2]
                protocal = result[4]
                proxy = protocal + '://' + ip + ':' + port
                if self.check_ip(proxy, protocal):
                    return protocal, proxy
                # 无效就删除该 ip 并继续获取
                self.del_ip(id)
                return self.get_proxy()
            return self.get_proxy()

        except Exception as e:
            print(e)

    def del_ip(self, id):
        ''''
        删除无效的代理ip
        '''
        try:
            strsql = 'delete from proxyippool where ipid="' + id + '"'
            self.cur.execute(strsql)
            self.conn.commit()
            self.id_list.remove(id)
            print('del record:', id)
        except Exception as e:
            print(e)

    def close(self):
        '''
        关闭
        :return:
        '''
        try:
            self.cur.close()
            self.conn.close()
            if self.browser:
                self.browser.quit()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # pool = ProxyIpPool()
    # for page in range(1,5):
    #
    #     url = 'https://www.xicidaili.com/nn/'+str(page)
    #     pool.down_ips(url)
    # pool.close()
    pool = ProxyIpPool(crawl=False)
    print('proxyip:', pool.get_proxy())
