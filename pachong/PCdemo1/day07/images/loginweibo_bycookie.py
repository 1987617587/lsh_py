from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.delete_all_cookies()
url = 'https://weibo.com/u/5936659854/home?wvr=5'
# 把登陆之后的cookie信息拿过来
strcookies = 'SINAGLOBAL=7417371983178.273.1585555298716; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFKxBG9p7Qa7DsIQCFGTyzC5JpX5KzhUgL.Fo-4e0qcSK.RSKB2dJLoIEXLxKBLBonL1KqLxK.L1KMLBoBLxKqLB.eL1hzLxKqLBo-L1h2LxKnL1h5L1h-t; wvr=6; UOR=,,www.baidu.com; Ugrow-G0=589da022062e21d675f389ce54f2eae7; SUB=_2A25zhq22DeRhGeNH6FQX9SfEzjiIHXVQ9Zh-rDV8PUNbmtAKLVD8kW9NStTryUikMc093xa9_OzUcBhF0ixm9zYu; SUHB=0oUofDFnBGtt95; ALF=1617170789; SSOLoginState=1585634790; TC-V5-G0=eb26629f4af10d42f0485dca5a8e5e20; _s_tentry=login.sina.com.cn; Apache=5306743983581.004.1585634792699; ULV=1585634792730:3:3:3:5306743983581.004.1585634792699:1585556855663; wb_view_log_5936659854=1920*10801; TC-Page-G0=1ae767ccb34a580ffdaaa3a58eb208b8|1585634848|1585634792; webim_unReadCount=%7B%22time%22%3A1585636054447%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D'
# 使用字典推导式，加上差分，把strcookie转换成字典格式cookies_dict
cookies_dict = {item.split('=')[0]: item.split('=')[1] for item in strcookies.split(';')}
print(cookies_dict)

try:
    browser.get(url)
    for item in cookies_dict.items():
        browser.add_cookie({
            'domain': 'weibo.com',  # 表示cookie所在的域
            'name': item[0].strip(),  #
            'value': item[1],
            'expires': '',  # 设置过期时间
            'path': '/',  # 表示cookie所在的目录
            'httpOnly': False,  # 如果此属性为True,则只有在http请求头中有此信息，不能通过document.cookie来获取cookie的值
            'HostOnly': False,  # 获取cookie时，首先会检测domai是否匹配，其次检测path,secure,httpOnly等属性是否匹配
            # 如果HostOnly为True,只有当前域名和domain属性完全相同才会进入流程
            # 如果HostOnly为False,只要符合规则的域名都可以0进入流程
            'Secure':False,
        })
except Exception as e:
    print(e)
# browser.get(url)
# browser.add_cookie()
