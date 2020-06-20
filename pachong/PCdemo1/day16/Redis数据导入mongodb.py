# author:lsh
# datetime:2020/4/15 9:45 
'''
                                 .::::.                                               _oo0oo_
                               .::::::::.                                            o8888888o
                              :::::::::::                                            88" . "88
                           ..:::::::::::'                                            (| -_- |)
                        '::::::::::::'                                               0\  =  /0
                          .::::::::::                                              ___/`---'\___
                     '::::::::::::::..                                           .' \\|     |# '.
                          ..::::::::::::.                                       / \\|||  :  |||# \
                        ``::::::::::::::::                                     / _||||| -:- |||||- \
                         ::::``:::::::::'        .:::.                        |   | \\\  -  #/ |   |
                        ::::'   ':::::'       .::::::::.                      | \_|  ''\---/''  |_/ |
                      .::::'      ::::     .:::::::'::::.                     \  .-\__  '-'  ___/-. /
                     .:::'       :::::  .:::::::::' ':::::.                 ___'. .'  /--.--\  `. .'___
                    .::'        :::::.:::::::::'      ':::::.            ."" '<  `.___\_<|>_/___.' >' "".
                   .::'         ::::::::::::::'         ``::::.         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
               ...:::           ::::::::::::'              ``::.        \  \ `_.   \_ __\ /__ _/   .-` /  /
              ```` ':.          ':::::::::'                  ::::..      `-.____`.___ \_____/___.-`___.-'
                                 '.:::::'                    ':'````..                `=---='
                            女神保佑         永无BUG                            佛祖保佑         永无BUG
                                                                                                     
'''
import redis, pymongo
import json


def main():
    # 创建数据库连接
    try:
        # 指定 Redis 数据库信息
        rediscli = redis.StrictRedis(host='localhost', port=6379)
        # 指定 MongoDB 数据库信息
        # server = 'localhost'
        # port = '27017'
        # dbname = 'admin'
        # user = 'admin'
        # pwd = '123'
        # uri = 'mongodb://' + user + ':' + pwd + '@' + server + ':' + port + '/' + dbname
        # mongocli = pymongo.MongoClient(uri)
        mongocli = pymongo.MongoClient(host='localhost', port=27017)
        # 创建数据库名
        db = mongocli['people']
        # 创建表名
        sheet = db['people_news']
    except Exception as e:
        print(e)

    while True: # 死循环一直执行可以便爬取边转存
        # FIFO（新进先出） 模式为 blpop，LIFO（后进先出）模式为 brpop，获取键值
        source, data = rediscli.blpop(["people:items"])
        item = json.loads(data)
        sheet.insert(item)


if __name__ == '__main__':
    main()
