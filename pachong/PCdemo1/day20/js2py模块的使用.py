# author:lsh
# datetime:2020/4/20 11:18 
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
import js2py

un ='''
function sample(x)
{
 return "Hi " + x +" !"
}
'''
print(js2py.eval_js(un)("world"))
# python 获取 js 内部的变量
gen_guid="""
function createGuid() {
 return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
}
var guid1 = createGuid() + createGuid() + "-" + createGuid() + "-" + createGuid() + createGuid() +
"-" + createGuid() + createGuid() + createGuid();
"""
context = js2py.EvalJs()
context.execute(gen_guid)
guid=context.guid1 # 将 guid1 传递到 Python 中
print(guid)
# 编码问题
# ‘utf8’ codec can’t decode byte 0xe4 in position 28: invalid continuation byte
# 使用 decode(‘latin1’)解码 js
# get_docid = js2py.eval_js(js.decode('latin1'))
