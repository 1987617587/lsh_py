""""

对讯代理源码进行封装


"""
import sys
import time
import hashlib
import requests
import urllib3
import random
from lxml import etree

# 关闭警示信息的
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def down(url):
    """
    下载给定的url页面信息
    :param url:
    :return:
    """
    orderno = "ZF201910273585ew6xSN"
    secret = "1219111fc423464f9f1d3fde3ae6856a"
    # 代理ip和端口号
    ip = "forward.xdaili.cn"
    port = "80"
    ip_port = ip + ":" + port
    # 提供最多转发三次机会
    nums = 0
    while nums <= 3:
        timestamp = str(int(time.time()))  # 时间戳
        string = ""
        string = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp
        md5_string = hashlib.md5(string.encode()).hexdigest()  # md5哈希，得到固定长度的字符
        sign = md5_string.upper()  # 转大写字母
        # 构成认证信息
        auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp
        proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
        headers = {"Proxy-Authorization": auth,
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
        try:
            response = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
            if response.status_code == 200:
                return response
            else:
                nums += 1

        except Exception as e:
            time.sleep(random.random())
            nums += 1
            print(e)
    # 次数用尽，返回None
    return None


if __name__ == '__main__':
    url = 'https://www.speedtest.cn/'
    r = down(url)
    if r:
        html = r.content.decode(r.apparent_encoding)
        print(html)
    else:
        print("未获得数据")
