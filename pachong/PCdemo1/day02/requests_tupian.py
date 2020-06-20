import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
response = requests.get("http://c1.haibao.cn/img/600_0_100_1/1549794487.7856/fa60e1e7264e6082569d729e4ee302dd.jpg",
                        headers=headers)
with open('./images/img.jpg', 'wb') as file:
    file.write(response.content)
