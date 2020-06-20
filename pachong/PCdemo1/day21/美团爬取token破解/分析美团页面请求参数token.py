# author:lsh
# datetime:2020/4/21 9:51 
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
import base64, zlib, json


def decode_token(token):
    '''
    破解美团的_token
    :param token:二进制压缩 base64编码过的token值
    :return:
    '''
    # base64解码
    token_decode = base64.b64encode(token.encode())
    print(token_decode)
    # 二进制的解压缩
    token_string = zlib.decompress(token_decode)
    return token_string


if __name__ == '__main__':
    token = 'eJx1j1uPqjAUhf9LXyG25Y7JPCCoqQIqRUeZzANCGYQR0YK3yfnvp5PMvJzkJDtZX9deWdn9AheSgyFGyEZIBld2AUOAB2hgABl0XGx0y9RUDSkmUgwZZP94liaD/WXjgeEbVlQkK7r+/u1EwnjDtoJkjCz0Lv+yJljRxHyniAiBsutaPoSQl4MjO3R92gyy0xEK5uUBZhhDccl/QkC0HGPRIrT+0fRHu993IH4kKvjhoxHEZre8WuPF7emsSgZpmRQS3aiUNMdRX89c06uccFYrRCHm9CRFveOrq63zcffqHd+ei6Yzl15ZldnaZLHrnsZkntDQKMjr0pAKU4PF7RHor24xN+wHCUhqVeuYVmp+1p5tPwqTfRsxNsY+ne17lfV+vKvoLj+0+jnPPq8kpmONW5OQPk580V7dbMqUCYvSRXoN8cQoLAdv9U2S1H0dwqdtts9mxPwyiyG/ezz4vHdBlIfz6U2dBpJU2SlZYtxDyVlES+pbL+DPX925lSI='
    result = decode_token(token).decode()
    result = json.loads(result)
    print(result)
    print('+'*6)
    sign = result['sign']
    sign = decode_token(sign).decode()
    print(sign)
