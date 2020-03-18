# author:lzt
# date: 2019/12/13 11:38
# file_name: smtp_test
import smtplib
from email.mime.text import MIMEText


def send_email():
    # smtp服务器
    smtpserver = 'smtp.qq.com'
    # 发送方信息
    user = '1987617587@qq.com'  # 如果使用MailEnable做邮件服务器，那么可以在该软件中查看用户名 一般该软件用户名会去掉.com ，比如boss@qiku
    passwd = 'vvvminhjdhxtifja'  # 授权码
    # 接收方信息
    receiver = "1719866818@qq.com"
    # message = MIMEText("axcd", "plain", "utf-8")
    html = "<h1>参见小仙女</h1> 我是 你的二狗子 <i>今日份爱你</i>"
    message = MIMEText(html, 'html', 'utf-8')
    message["from"] = user
    message["to"] = receiver
    message["subject"] = "测试邮件"
    server = smtplib.SMTP_SSL(host=smtpserver, port=465)
    server.login(user, passwd)
    server.sendmail(from_addr=user, to_addrs=receiver, msg=message.as_string())
    server.quit()
    print("finish")
