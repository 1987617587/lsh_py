# author:lsh
# datetime:2020/4/15 19:50 
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
案例：王者荣耀盒子英雄信息的爬取
并下载英雄图片，名称，背景故事，出装推荐描述及id，金币价格，搭档英雄，压制英雄，被压制英雄，对抗技巧
存储mongodb数据库
'''
import pymongo
import os
import re

import requests
import time
import random
import json

# try:
#     client = pymongo.MongoClient("localhost", 27017)
#     # 指向指定的数据库
#     db = client['wzry']
#     collec = db.hero
#
# except Exception as e:
#     print(e)

headers = {
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)',
}
base_url = 'http://gamehelper.gm825.com'
def get_hero():
    url ='/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=12A84CF38D43ACBCB630B0F61EA6C6B7&ovr=5.1.1&device=HUAWEI+_HUAWEI+MLA-AL10&net_type=1&client_id=Q%2Ft3pkcmtbETmZ7I%2BI%2FHpA%3D%3D&info_ms=Q%2F3EH69Etqj3fT9W9HrrMw%3D%3D&info_ma=XhmjJQaGbgGmK3n5sKqZBE5bcWNlcR9GOqaftQYDT%2FE%3D&mno=0&info_la=qma3PGAUEipKo9jsdzK7fA%3D%3D&info_ci=qma3PGAUEipKo9jsdzK7fA%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=XhmjJQaGbgGmK3n5sKqZBE5bcWNlcR9GOqaftQYDT%2FE%3D&os_level=22&os_id=80fa5b720bca1407&resolution=720_1280&dpi=240&client_ip=172.17.100.15&pdunid=b720bca140780fa5 HTTP/1.1'

    response = requests.get(base_url+url,  headers=headers)
    # json格式
    data = response.json()
    ls = data['list']
    # print(ls)
    for hero in ls:
        # print(hero)
        # print('-----'*9)
        hero_id = hero['hero_id']
        hero_name = hero['name']
        hero_cover = hero['cover']
        print(f'hero_id:{hero_id}')
        print(f'hero_name:{hero_name}')
        print(f'hero_cover:{hero_cover}')
        print('='*100)
        # down_photo(hero_cover, hero_name)
        get_hero_detail(hero_id)


    time.sleep(random.random())

def get_hero_detail(hero_id):
    url = '/wzry/hero/detail?&channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=12A84CF38D43ACBCB630B0F61EA6C6B7&ovr=5.1.1&device=HUAWEI+_HUAWEI+MLA-AL10&net_type=1&client_id=Q%2Ft3pkcmtbETmZ7I%2BI%2FHpA%3D%3D&info_ms=Q%2F3EH69Etqj3fT9W9HrrMw%3D%3D&info_ma=XhmjJQaGbgGmK3n5sKqZBE5bcWNlcR9GOqaftQYDT%2FE%3D&mno=0&info_la=qma3PGAUEipKo9jsdzK7fA%3D%3D&info_ci=qma3PGAUEipKo9jsdzK7fA%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=XhmjJQaGbgGmK3n5sKqZBE5bcWNlcR9GOqaftQYDT%2FE%3D&os_level=22&os_id=80fa5b720bca1407&resolution=720_1280&dpi=240&client_ip=172.17.100.15&pdunid=b720bca140780fa5 HTTP/1.1'
    params = {
        'hero_id': hero_id,
    }

    response = requests.get(base_url+url, params=params, headers=headers)
    # json格式
    data = response.json()
    info = data['info']
    # print(info)

    name = info['name']
    title = info['title']
    half_img = info['half_img']
    background_story = info['background_story']
    print('英雄：',name,'title:',title)
    be_restrained_heros = info['be_restrained_hero']
    be_restrained_hero_list = []
    for be_restrained_hero in be_restrained_heros:
        if be_restrained_hero:
            print('被压制英雄：',be_restrained_hero['name'])
            be_restrained_hero_list.append(be_restrained_hero)

    restrained_heros = info['restrained_hero']
    restrained_hero_list = []

    for restrained_hero in restrained_heros:
        if restrained_hero:
            print('压制英雄：', restrained_hero['name'])
            restrained_hero_list.append(restrained_hero)


    partner_heros = info['partner_hero']
    partner_hero_list = []
    for partner_hero in partner_heros:
        if partner_hero:
            print('搭档英雄：', partner_hero['name'])
            partner_hero_list.append(partner_hero)


    # 出装推荐描述及id，
    equip_choice = info['equip_choice']
    # 金币价格，
    gold_price = info['gold_price']
    # 对抗技巧
    hero_tips = info['hero_tips']

    # # 写入故事
    # with open('hero_story/'+name+'.txt','a',encoding='utf-8') as file:
    #     file.write(info['background_story'])
    # # 写入压制和搭档
    # with open('hero_story/' + name + '.txt', 'a', encoding='utf-8') as file:
    #     file.write(name,equip_choice,gold_price,gold_price)


    # 存储名称，背景故事，出装推荐描述及id，金币价格，搭档英雄，压制英雄，被压制英雄，对抗技巧
    # data = {
    #     'name': name,
    #     'background_story': background_story,
    #     # 出装推荐描述及id，金币价格，对抗技巧
    #     'equip_choice':equip_choice,
    #     'gold_price':gold_price,
    #     'hero_tips':hero_tips,
    #     'be_restrained_heros': be_restrained_heros,
    #     'restrained_heros': restrained_heros,
    #     'partner_heros': partner_heros,
    # }
    # collec.insert(data)

# 图片下载
def down_photo(img_url,hero_name):
    print(img_url, hero_name)
    print('=' * 9)
    img_response = requests.get(img_url)
    # 一个详情下的uid+id还是有重复的，再加上图片中的数字
    with open('images/' + hero_name + ".jpg", "wb")as file:
        # 字节流
        file.write(img_response.content)

if __name__ == '__main__':
    get_hero()

