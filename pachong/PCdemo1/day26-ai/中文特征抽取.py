# author:lsh
# datetime:2020/4/28 15:58 
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
import jieba

from sklearn.feature_extraction.text import TfidfVectorizer

def cutword():
    '''
    每次
    :return:
    '''
    content1 = jieba.cut('今天很残酷，明天很残酷，后天很美好，很多人死在了明天晚上见不到后天的太阳。')
    content2 = jieba.cut('什么都想自己干，这个世界上你干不完。')
    content3 = jieba.cut('那些私下忠告我们，指出我们错误的人，才是真正的朋友。')
    con1 = []
    con2 = []
    con3 = []
    for word in content1:
        con1.append(word)
    for word in content2:
        con2.append(word)
    for word in content3:
        con3.append(word)
    # 将列表转换成字符串
    c1 = ''.join(con1)
    c2 = ''.join(con2)
    c3 = ''.join(con3)
    return c1,c2,c3


# tfid中文特征抽取
def tfidfvec():
    # 调用分词分割中文文章
    c1,c2,c3 = cutword()
    print( c1,c2,c3 )
    stopwords = ['很','在','，','。','的','上']
    tf = TfidfVectorizer(stop_words=stopwords)
    data = tf.fit_transform([c1,c2,c3])
    print(data.toarray())

tfidfvec()