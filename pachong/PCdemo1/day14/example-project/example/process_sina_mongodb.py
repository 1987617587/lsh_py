"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/10'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

import json
import redis
import pymongo

def main():
    # 指定Redis数据库信息
    rediscli = redis.StrictRedis(host='192.168.10.132',port=6379, password='123456',db=0)
    # 指定MongoDB数据库信息
    uri = 'mongodb://admin:123@localhost:27017/admin'
    mongocli = pymongo.MongoClient(uri)
    # 创建数据库名
    db = mongocli['sina']
    # 创建表名
    sheet = db['news']

    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop(["sina:items"])
        item = json.loads(data.decode('utf-8'))
        sheet.insert(item)

        try:
            print("Processing: <%s>" % item['content'])
        except KeyError as e:
            print("Error procesing: %r" % e)

if __name__ == '__main__':
    main()