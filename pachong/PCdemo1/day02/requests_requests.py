"""
http的常见请求方法
"""

import requests

# print(requests.get('http://httpbin.org/get').text)
# print(requests.post('http://httpbin.org/post').text)
# print(requests.put('http://httpbin.org/put').text)
# print(requests.delete('http://httpbin.org/delete').text)
# print(requests.head('http://httpbin.org/get').text)
print(requests.options('http://httpbin.org/get').text)
