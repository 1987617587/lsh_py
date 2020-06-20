#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             佛祖保佑       永无BUG
import base64
import zlib
import json
import datetime


def gen_sign(page):
    '''
    生成sign参数
    :param page:
    :return:
    '''
    str1 = "areaId=0&cateId=11&cityName=深圳&dinnerCountAttrId=&optimusCode=10&originUrl=https://sz.meituan.com/meishi/c11/&page={}&partner=126&platform=1&riskLevel=1&sort=&userId=&uuid=f77c42de4b1f426d89fb.1587433475.1.0.0"
    str2 = "areaId=0&cateId=11&cityName=深圳&dinnerCountAttrId=&optimusCode=10&originUrl=https://sz.meituan.com/meishi/c11/pn{}/&page={}&partner=126&platform=1&riskLevel=1&sort=&userId=&uuid=f77c42de4b1f426d89fb.1587433475.1.0.0"
    if page == 1:
        s = str1.format(str(page))
    else:
        s = str2.format(str(page), str(page))
    # 编码
    s = s.encode()
    # 二进制压缩
    s = zlib.compress(s)
    # base64编码
    s = base64.b64encode(s)
    # 转换为字符串
    s = str(s, encoding='utf-8')
    return s


def gen_token(page):
    '''
    生成token
    :param page:
    :return:
    '''
    ts = int(datetime.datetime.now().timestamp() * 1000)
    if page == 1:
        bI = ['https://sz.meituan.com/meishi/c11/', 'https://sz.meituan.com/']
    else:
        url1 = 'https://sz.meituan.com/meishi/c11/pn{}/'.format(str(page))
        bI = [url1, 'https://sz.meituan.com/meishi/c11/']

    token_dict = {
        'rId': 100900,
        'ver': '1.0.6',
        'ts': ts,
        'cts': ts + 10 * 1000,
        'brVD': [1920, 366],
        'brR': [[1920, 1080], [1920, 1040], 24, 24],
        # 'bI': ['https://sz.meituan.com/meishi/c11/', 'https://sz.meituan.com/'],
        'bI': bI,
        'mT': [],
        'kT': [],
        'aT': [],
        'tT': [],
        'aM': '',
        #'sign': 'eJwdjT1OAzEQhe+SwqW9s3GyAckFSoUU0XEAx55NRlnbq/E4EpyFSyAKTgTnwKJ6n57ez8Yz+ufoBhW8YAcAFUjeXnxC9/v9+fPxpSLljHwsLcuTCPeQKqtQavVYIjoYVGG6UH7lxV1F1vpoTH3XCUmazzqUZDrXK5kAYNTqL73UhaXPOhj3al28zIVTt5nq7YR3XDrXwuJUq/j/2RpFN09TsGNEe4bZjvt4eJjPGnaHyW63dtpp0IMeNn8ENUl+'
        'sign':gen_sign(page),
    }
    # 编码
    encode = str(token_dict).encode()
    # 二进制压缩
    compress = zlib.compress(encode)
    # base64编码
    b_encode = base64.b64encode(compress)
    # 转成字符串
    token  = str(b_encode,encoding='utf-8')
    return token


if __name__ == "__main__":
    print(gen_token(1))
