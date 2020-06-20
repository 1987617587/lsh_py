"""
模拟POST请求
有道翻译
"""
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
# 使用旧版（新版需要破解）
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"


def translate(word):
    form_date = {
        "i": word,
        "from": " AUTO",
        "to": " AUTO",
        "smartresult": " dict",
        "client": " fanyideskweb",
        "salt": " 15850354134937",
        "sign": " 8891440537f41f43464b6bb9acf76928",
        "ts": " 1585035413493",
        "bv": " 7bcd9ea3ff9b319782c2a557acee9179",
        "doctype": " json",
        "version": " 2.1",
        "keyfrom": " fanyi.web",
        "action": " FY_BY_REALTlME",
        "typoResult": 'false'

    }
    response = requests.post(url, data=form_date, headers=headers)

    print(response.text)
    translate_result = response.json()
    print("翻译结果：", translate_result["translateResult"][0][0]['tgt'])


if __name__ == '__main__':
    word = input("请输入单词：")

    translate(word)
