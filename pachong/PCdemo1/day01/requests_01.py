import requests

# 请求抓取指定页面。返回相应对象
response = requests.get("https://www.baidu.com/")
print("对象类型:", type(response))

# 通过响应对象的属性和方法来获取相应的信息
# 查看请求地址
print(response.url)
# 查看请求的状态码
print(response.status_code)
# 编码信息
# 查看响应头部字符编码
print(response.encoding)
# 调用 chardet.detect()来识别文本编码
print(response.apparent_encoding)
# 响应内容
# 查看响应内容，response.content 返回的字节流数据
print(response.content)
print(response.content.decode('utf8'))
# 查看响应内容，response.text 返回的是 Unicode 格式的数据
print(response.text)
print("根据编码进行解码", response.content.decode(response.apparent_encoding))
# 如果还不行，最好加'ignore' （忽略部分错误）
print("根据编码进行解码", response.content.decode(response.apparent_encoding, "ignore"))
# 响应头

# 查看响应头
print('响应头：', response.headers)
# 查看请求头
print('请求头：', response.request.headers)

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}
response = requests.get("https://www.baidu.com/", headers=headers)
print('再次查看请求头：', response.request.headers)
