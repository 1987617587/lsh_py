import sqlite3
conn = sqlite3.connect('mycookies.db')
print('创建数据库成功')

c = conn.cursor()

print("Opened database successfully")

# 创建表可以使用神器navcat设计表
#
# c.execute('''CREATE TABLE COOKIES
#        (ID INT PRIMARY KEY     NOT NULL,
#        USERNAME           VARCHAR    NOT NULL,
#        PASSWORD            VARCHAR     NOT NULL,
#        COOKIES        VARCHAR,
#        HOME_URL        VARCHAR);''')
# print("创建表成功")
# conn.commit()

print("准备向表中插入数据")
# c.execute("INSERT INTO COOKIES (ID,USERNAME,PASSWORD,COOKIES,HOME_URL) \
#       VALUES (0, 'admin', '123456', 'Norway', 'http://www.baid.com')")

# id 可以忽略，主键默认自增长
c.execute("INSERT INTO COOKIES (USERNAME,PASSWORD,COOKIES,HOME_URL) \
      VALUES ( ?, ?, ?, ?)",('lsh', '123456', 'asd', 'http://www.baid.com'))
conn.commit()


# print("修改数据")
# c.execute("UPDATE COOKIES set username = 'lsh' where ID=1")
# conn.commit()
#
# print("删除数据")
# c.execute("DELETE from COOKIES where ID=1;")
# conn.commit()

print("查询数据")
cursor = c.execute("SELECT id, username from COOKIES")
for row in cursor:
    print('id:',row[0])
    print('username:',row[1])

conn.close()