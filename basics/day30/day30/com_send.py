"""
# author Liu shi hao
# date: 2019/12/13 11:45
# file_name: com_send

"""

import smtplib
from email.mime.text import MIMEText
# smtp服务器
smtpserver = 'smtp.qq.com'
# 发送方信息
user = '253462876@qq.com'  # 如果使用MailEnable做邮件服务器，那么可以在该软件中查看用户名 一般该软件用户名会去掉.com ，比如boss@qiku
passwd = 'udpvgkkavddzbgfa' # 授权码
# 接收方信息
receiver = "377588092@qq.com"
message = MIMEText("又失败了！", "plain", "utf-8")
message["from"] = user
message["to"] = receiver
message["subject"] = "测试邮件"
server = smtplib.SMTP(host=smtpserver, port=465)
server.login(user, passwd)
server.sendmail(from_addr=user, to_addrs=receiver, msg=message.as_string())
server.quit()
print("finish")
