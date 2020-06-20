import pymongo

# 创建MangoDB连接
try:
    # 创建MongoClient对象 建立和MongoDB的连接
    client = pymongo.MongoClient('localhost', 27017)
    # 指定数据库名字
    db = client['db_pachong']
    # 指定集合的名称
    collec = db.mycollec
except Exception as e:
    print(e)

# 文档的插入
collec.insert([{'name': "马云", 'age': 50, 'corp': 'ali'},
               {'name': '马化腾', 'age': 40, 'corp': 'tenxun'}
               ])
collec.insert({'name': "丁磊", 'age': 48, 'corp': '网易'})
collec.insert_one({'name': "张朝阳", 'age': 52, 'corp': '搜狐'})
# 查询
result = collec.find_one()
print(result['name'])
for cur in collec.find():
    print(cur['name'])

print(collec.find_one({'age':50}).get('name'))
print(collec.find_one({'name':'丁磊'}).get('name'))
print(collec.find())
