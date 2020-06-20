# author:lsh
# datetime:2020/4/16 16:57 
"""
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
                                                                                                     
"""
import os
import re

import requests
import time
import random
import json
import xlwt  # excel文档的写操作

headers = {
    'User-Agent': 'NewsApp/54.6 Android/4.4.2 (lenovo/Lenovo K8 Note)',
    'Accept-Encoding': 'gzip',
}
base_url = 'http://tikuapi.hqwx.com'
def get_page():
    url = '/qbox_api/v1/paper/get_paper?_appid=tk_jianzaoshi&_os=1&_v=4.3.2&_t=1587038188219&edu24ol_token=34ad018173b4180482b2fb66301571d17ffa3e6f0152d27f4747fee1d713f322478ee73f48194750e4d41b177e93f861d790ccf91c81281852ca562fcde819afbf3dba13ebf647a655f67c9cdbb114c760&box_id=5380&paper_id=42587 HTTP/1.1'
    params = {
        '_appid': 'tk_jianzaoshi',
        '_os': 1,
        '_v': '4.3.2',
        '_t': 1587038188219,
        'edu24ol_token': '34ad018173b4180482b2fb66301571d17ffa3e6f0152d27f4747fee1d713f322478ee73f48194750e4d41b177e93f861d790ccf91c81281852ca562fcde819afbf3dba13ebf647a655f67c9cdbb114c760',
        'box_id': 5380,
        'paper_id': 42587,
    }

    # response = requests.get(url, params=params, headers=headers)
    response = requests.get(base_url + url, params=params, headers=headers)
    # html = response.text
    # print(html)
    # json格式
    data = response.json()['data']
    # print(data)
    title = data['paper_info']['title']
    id = data['paper_info']['id']
    question_id_arr = []
    # 把多选和单选题的id 拿过来
    arr1 = data['question_list']['group_list'][0]['question_id_list']
    arr2 = data['question_list']['group_list'][1]['question_id_list']
    question_id_arr = arr1 + arr2
    # print(question_id_arr)
    # 列表拆分20个一组，并转字符串拼接
    for i in range(int(len(question_id_arr) / 20) - 1):
        print(question_id_arr[10 * i:20 + i * 10])
        new_question_id_arr = question_id_arr[10 * i:20 + i * 10]
        s = ''
        for question_id in new_question_id_arr:
            s += str(question_id)
            s += ','
        # print(s[:-1])
        question_id_str = s[:-1]
        get_question_list(question_id_str)


def get_question_list(question_id_str):
    url = '/qbox_api/v1/question/get_question_list'
    # url = '/qbox_api/v1/question/get_question_list?_appid=tk_jianzaoshi&_os=1&_v=4.3.2&_t=1587039155183&edu24ol_token=34ad018173b4180482b2fb66301571d17ffa3e6f0152d27f4747fee1d713f322478ee73f48194750e4d41b177e93f861d790ccf91c81281852ca562fcde819afbf3dba13ebf647a655f67c9cdbb114c760&boxId=5380&question_ids=2809581%2C2809592%2C2809598%2C2809601%2C2809608%2C2809613%2C2809622%2C2814800%2C2814801%2C2814803%2C2809625%2C'
    params = {
        '_appid': 'tk_jianzaoshi',
        '_os': 1,
        '_v': '4.3.2',
        '_t': 1587039155183,
        'edu24ol_token': '34ad018173b4180482b2fb66301571d17ffa3e6f0152d27f4747fee1d713f322478ee73f48194750e4d41b177e93f861d790ccf91c81281852ca562fcde819afbf3dba13ebf647a655f67c9cdbb114c760',
        'box_id': 5380,
        # 'question_ids': '2809581,2809592,2809598,2809601,2809608,2809613,2809622,2814800,2814801,2814803,2809625,2809628,2809633,2809641,2809645,2814814,2814818,2809662,2814822,2814825'
        'question_ids':question_id_str
    }
    response = requests.get(base_url + url, params=params, headers=headers)
    data = response.json()['data']
    # print(data)
    for question in data:
        title = question['title']
        topic_list = question['topic_list'][0]['option_list']
        q_id = question['topic_list'][0]['q_id']
        print(f'title:{title}')
        print(f'q_id:{q_id}')
        print(f'topic_list:{topic_list}')


if __name__ == '__main__':
    get_page()
