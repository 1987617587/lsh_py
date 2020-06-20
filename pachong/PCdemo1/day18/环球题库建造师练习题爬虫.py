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
'''
值爬取了其中一个章节
'''
import os
import re

import requests


headers = {
    'User-Agent': 'NewsApp/54.6 Android/4.4.2 (lenovo/Lenovo K8 Note)',
    'Accept-Encoding': 'gzip',
}

def get_page():
    url = 'http://tikuapi.hqwx.com/qbox_api/v1/pratice/build_homework?_appid=tk_jianzaoshi&_os=1&_v=4.3.2&_t=1587041879816&edu24ol_token=34ad018173b4180482b2fb66301571d17ffa3e6f0152d27f4747fee1d713f322470781e2afb5f22dbe1d156eb4d869b3aed9a626a680b13a79447c464e9754672f55ce2a354764f58e57a46ed2a475eb89&box_id=5383&tech_id=7096&obj_id=62355&obj_type=1&mode=0&num=60'


    response = requests.get( url, headers=headers)

    data = response.json()['data']
    # print(data)
    name = data['exerciseInfo']['name']
    print(f'章节：{name}')
    num = data['exerciseInfo']['num']
    print(f'num：{num}')
    for question in data['questionList']:

        title = question['title']
        topic_list = question['topic_list'][0]['option_list']
        q_id = question['topic_list'][0]['q_id']
        print(f'title:{title}')
        print(f'q_id:{q_id}')
        print(f'topic_list:{topic_list}')


if __name__ == '__main__':
    get_page()
