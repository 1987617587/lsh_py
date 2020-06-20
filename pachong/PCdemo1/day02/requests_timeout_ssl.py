import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

url = "https://www.12306.cn/mormhweb/"
response = requests.get(url, headers=headers, timeout=1, verify=True)
print(response.text)
print(response.url)
