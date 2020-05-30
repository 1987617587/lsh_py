# author:lzt
# date: 2019/12/13 11:19
# file_name: ftp_client
from ftplib import FTP

ftp = FTP(host="localhost")
ftp.login(user="lzt", passwd="123")
print(ftp.pwd())
ftp.cwd("aaa")
print(ftp.pwd())
print(ftp.dir("/"))
