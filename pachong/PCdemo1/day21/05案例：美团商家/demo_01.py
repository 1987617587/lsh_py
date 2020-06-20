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

def decode_token(token):
    '''
    破解_token
    :param token:
    :return:
    '''
    # base64解码
    token_decode = base64.b64decode(token.encode())
    # 二进制解压缩
    token_string = zlib.decompress(token_decode)
    return token_string

if __name__ =='__main__':
    #token = 'eJx1j0tvozAUhf+Lt0GxHfPMjkmBkKQ0D5tAR10Q4pYQwiM4kDCa/z6upl3MYqQrnePvHh1d/wJX/wimGCELIQV0/AqmAI/RWAcKEK3caKahEqIRXbMMBaT/MkuV7HANn8D0J7YmSCG6/vZJthL8JRiZ6E359qr0E1XOZ8qXIZAJUbdTCNthfOEncUvKcVpdoPRtdoIpxlBe8p8QkC0XKluknr80+VLx/X6WP5IV7emjlI4v+mNO8Ys9OJuMj3Z9s7da4j3s9OzuKsZQ5Nh3TQu2RXlooKM69cPdPewl/aBlv1zopWbwwYyH0e29+pHtzdhObZflPCrvMwt21uh9fa93qyKf9+0qvdHZmm+WjdgkXRj7eRWHnqezuVHcQ+zirq7onEQzdkmGoWGvT9doqZ3tOKDNyiAsS6L1S5aTpJiYgx9SoZWNEW9JJHP9bcEamMPJtnYDZNHWCxyuHl7zTqh8ka+9Mpk/9jo5irpG/jMPStMJWDECv/8AOHqXVA=='
    token = 'eJyFj0tvm0AUhf/LbIs8TzBYygIMMfiFzcOkrrKIgdhABhzAgIn63ztRk0VXla50vjn36OjOB6idBMwwQhpCEujSGswAnqCJAiTQNmIjq1NGmSwjjRIJxP94GDMqgVN9MMHsF9YIkohKnj8dTxh/HYxU9Cx9MxNMmJjPlCNC4NK212YGYTNOeJq1t5dyElccCm4uGYwxhteSQHHN/4NAlPJAlAotvvTlS9vv90Z8ULQ12bkUlC77ZAywq4/W3kjn06ttXKfjxd1mc3m/4nsnr1y2zcbs+IRz9ZT7th6tK6tyjUWss+79NX4K0qG1laVilj89musbvS+SHym1ltMUUlmF9lt/Ho6KlytH/soXPPRWRRwSaFutOV/q9aOv3rt2W9UxITu/PlAeGPcEl0rRev0Nnd70Q7CNqvJ9zXM8d53hFNqdd0DJmkW+ES4GGspsoBF7jJw6bXaQanLebBo1VTYmzzeNd4MmiyzZ187Jsd4lvCzKfSjfSdcba1VbdeeHB/D7Dw1HnRM='
    result = decode_token(token).decode()
    result = json.loads(result)
    print(result)
    print('='*500)
    sign = result['sign']
    sign = decode_token(sign).decode()
    print(sign)




