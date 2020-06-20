# author:lsh
# datetime:2020/4/14 17:07 
'''
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
                                                                                                     
            '''
import requests
def down_video(url,path):
    with requests.get(url,stream=True) as response: # 使用字节流的方式下载
        print('开始下载视频……')
        # 数据块的大小
        chunk_size = 1024
        # 获取视频的大小
        content_size = int(response.headers['content-length'])
        print(f'content_size:{content_size}')
        with open(path,'wb')as file:
            n = 1
            for chunk in response.iter_content(chunk_size=chunk_size):
                loaded = n*chunk_size / content_size
                print(f'已下载：{loaded:%}')
                n += 1
                file.write(chunk)
    print("下载成功")



if __name__ == '__main__':
    url = 'https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo-transcode/7449615_2fa09a6b4b289a193fe100716ef60acd_3.mp4'
    path = 'data/2.mp4'

    down_video(url,path)