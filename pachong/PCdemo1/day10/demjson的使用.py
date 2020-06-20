import demjson
import json
d = "{title:'小阿三的女人',id:'32',rate:'7.8'}"
# 不标准的json不能解析
# data = json.loads(d)
data = demjson.decode(d)
print(data)
print(data['title'])