import requests
import execjs


def translate(query):
    with open('baidu.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    sign = ctx.call('e', query)
    url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
    data = {
        'from': 'en',
        'to': 'zh',
        'query': query,
        'simple_means_flag': '3',
        'sign': sign,
        'token': '7bf76fb8124617aef3fc4702a68c21ca',
        'domain': 'common'
    }
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
        'Cookie': 'BIDUPSID=F8EDA351967B69A1E54DCA091C920F63; PSTM=1579790173; BAIDUID=F8EDA351967B69A12969867A8C9BD3B3:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; cflag=13%3A3; BDUSS=U95ZzZJbndqRDRwOUhPN0h5LXFWLUd0YnFiaWJFVkJYN0pDODhicldXfkFZYjVlSVFBQUFBJCQAAAAAAAAAAAEAAADLCZCau7W6otfTu7nKx7u1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMDUll7A1JZec; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[xoix5KwSHTc]=9xWipS8B-FspA7EnHc1QhPEUf; delPer=0; PSINO=1; H_PS_PSSID=; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1587379163,1587380969,1587384112; yjs_js_security_passport=2789cd34e0722d260a7c1e1432391a9676d902bc_1587384490_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1587384694; __yjsv5_shitong=1.0_7_b86597026377934ed645ad0e3d64e99dee5f_300_1587384697868_223.89.132.29_328cd807'
    }
    response = requests.post(url, data=data, headers=headers)
    target = response.json()['trans_result']['data'][0]['dst']
    return target


if __name__ == '__main__':
    content = input('请输入要翻译的单词:')
    result = translate(content)
    print(result)
