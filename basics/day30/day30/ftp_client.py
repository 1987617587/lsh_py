"""
# author Liu shi hao
# date: 2019/12/13 11:19
# file_name: ftp_client

"""
from ftplib import FTP
f = FTP(host="127.0.0.1",user="lsh",passwd="123")
# f.login()
print(f.pwd())
print(f.cwd("aaa"))
print(f.dir("/"))