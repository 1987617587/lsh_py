# author:lsh
# datetime:2020/4/14 16:27 
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

from pybloom_live import BloomFilter
# 最多就是1000
bf = BloomFilter(capacity=1000)
url1 = 'https://www.baidu.com/'
url2 = 'https://www.taobao.com/'
bf.add(url1)
print(url1 in bf)
print(url2 in bf)

from pybloom_live import ScalableBloomFilter
# 最多就是1000
bf = ScalableBloomFilter(initial_capacity=100,mode=ScalableBloomFilter.LARGE_SET_GROWTH,error_rate=0.01)
url1 = 'https://www.baidu.com/'
url2 = 'https://www.taobao.com/'
bf.add(url1)
print(url1 in bf)
print(url2 in bf)