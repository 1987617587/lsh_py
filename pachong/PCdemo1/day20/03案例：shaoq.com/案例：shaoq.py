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

import execjs
import re
import os

js = '''
    var AC_ = 'u';
    var ae_ = 'R';
    var AF_ = '2';
    var AI_ = '0';
    var aj_ = 'o';
    var aK_ = '6';
    var AQ_ = '%';
    var aQ_ = '4';
    var Ar_ = 'p';
    var aU_ = 'C';
    var ax_ = '8';
    var Az_ = '1';
    var Be_ = 't';
    var bG_ = 'l';
    var bJ_ = '8';
    var Bj_ = '9';
    var bq_ = '0';
    var bR_ = 'E';
    var bT_ = 't';
    var cB_ = '8';
    var ci_ = 'i';
    var CJ_ = '0';
    var cl_ = '8';
    var ct_ = 'A';
    var cv_ = 'm';
    var DA_ = 'l';
    var DB_ = 'R';
    var di_ = '4';
    var DL_ = '9';
    var Dp_ = '8';
    var DQ_ = 'B';
    var du_ = '%';
    var DU_ = '3';
    var DZ_ = 'n';
    var dZ_ = 't';
    var Ex_ = 'c';
    var FD_ = 'd';
    var fd_ = 'u';
    var fF_ = 't';
    var fH_ = '7';
    var fj_ = 'h';
    var FM_ = 'e';
    var Fp_ = 'r';
    var ft_ = '4';
    var FV_ = 'a';
    var fY_ = 'w';
    var Fz_ = '%';
    var Gc_ = 'V';
    var gF_ = 'p';
    var Gk_ = 'l';
    var gl_ = 'o';
    var gZ_ = '4';
    var Gz_ = 't';
    var Hb_ = '%';
    var hC_ = '%';
    var HD_ = '%';
    var he_ = 'o';
    var HN_ = 'B';
    var HP_ = 'E';
    var hq_ = '1';
    var hR_ = 'C';
    var HZ_ = '%';
    var IA_ = 'S';
    var ID_ = '9';
    var id_ = 'l';
    var ig_ = '%';
    var Ig_ = '%';
    var In_ = '9';
    var Io_ = '%';
    var Iq_ = 'u';
    var ir_ = 'o';
    var iV_ = 't';
    var jc_ = '%';
    var jl_ = '8';
    var jQ_ = 'C';
    var jS_ = 'y';
    var jv_ = 'f';
    var jy_ = '4';
    var kC_ = 'i';
    var KL_ = 'i';
    var Kq_ = 'A';
    var KR_ = '1';
    var kv_ = 'U';
    var ky_ = '%';
    var Ky_ = '8';
    var le_ = '5';
    var LE_ = 'I';
    var lK_ = 'B';
    var lL_ = 'A';
    var Lm_ = ';';
    var Lq_ = 'l';
    var lr_ = '%';
    var Lr_ = '8';
    var Ls_ = '%';
    var mH_ = 'a';
    var Mk_ = 'd';
    var mo_ = 'a';
    var Mq_ = '4';
    var mR_ = 'p';
    var Mx_ = '%';
    var mX_ = 'g';
    var mx_ = 't';
    var nj_ = 'E';
    var NK_ = '7';
    var nu_ = 'e';
    var nV_ = 'n';
    var nX_ = 'e';
    var Ny_ = 'C';
    var oC_ = ';';
    var oc_ = 'h';
    var od_ = 'E';
    var Oe_ = 'e';
    var OL_ = 'd';
    var OP_ = '1';
    var or_ = 'w';
    var OS_ = 'a';
    var oT_ = 'C';
    var ov_ = 'e';
    var OX_ = 'c';
    var Pb_ = '%';
    var Pd_ = ';';
    var pd_ = 'n';
    var pE_ = 'e';
    var pl_ = '%';
    var pq_ = '%';
    var PQ_ = 't';
    var Pr_ = 'm';
    var PT_ = 'A';
    var Pw_ = 'C';
    var Qe_ = 'E';
    var qk_ = '5';
    var ql_ = 'V';
    var QN_ = '9';
    var Qr_ = '%';
    var qX_ = 'E';
    var rD_ = '%';
    var rd_ = 'A';
    var Rl_ = 'd';
    var RN_ = 'e';
    var Ro_ = 'n';
    var ro_ = 't';
    var rs_ = 'o';
    var Rx_ = 'E';
    var Sb_ = 'e';
    var sE_ = 't';
    var Sg_ = 'D';
    var SJ_ = 'o';
    var ss_ = 'e';
    var St_ = 'o';
    var sz_ = '9';
    var tB_ = '0';
    var tc_ = 'g';
    var TG_ = ';';
    var tg_ = '8';
    var TP_ = 'e';
    var tQ_ = '6';
    var TR_ = 'e';
    var Ts_ = ';';
    var tW_ = 'B';
    var ua_ = 'd';
    var UD_ = 'r';
    var uE_ = 'E';
    var Uf_ = 'r';
    var UG_ = '8';
    var UM_ = '%';
    var up_ = 's';
    var UQ_ = 'o';
    var Uu_ = 'i';
    var uw_ = '%';
    var VB_ = '%';
    var vc_ = '%';
    var vE_ = 'E';
    var VH_ = '%';
    var VJ_ = 'e';
    var vK_ = 't';
    var vl_ = '9';
    var VS_ = '8';
    var Vv_ = ';';
    var vZ_ = '%';
    var WG_ = 'B';
    var wi_ = 'r';
    var wK_ = '%';
    var wO_ = '%';
    var Wq_ = 'A';
    var WU_ = 'B';
    var xE_ = 'B';
    var Xf_ = 's';
    var xh_ = '5';
    var XH_ = 'F';
    var xj_ = 'p';
    var XL_ = ';';
    var XM_ = '%';
    var xM_ = '5';
    var xq_ = 'i';
    var xV_ = 'f';
    var yb_ = 'B';
    var YB_ = 'e';
    var yg_ = ';';
    var YI_ = 'E';
    var YJ_ = 'E';
    var yk_ = '%';
    var Yk_ = 'u';
    var YL_ = 'e';
    var yM_ = 'F';
    var YM_ = 'n';
    var ym_ = 'y';
    var Yn_ = '4';
    var Yq_ = 'w';
    var YR_ = ';';
    var Ys_ = 'r';
    var yT_ = '0';
    var Yw_ = 'A';
    var Za_ = 'l';
    var ZC_ = '%';
    var ZG_ = '%';
    var zG_ = 'F';
    var zj_ = 'c';
    var zT_ = '%';
    var Zx_ = 'P';
    var zY_ = ';';
    var zz_ = '8';
    //var xe_ = jE_('Zs_');
    var si_ = '_';
    var qe_ = '3';
    var GR_ = '_';
    var lJ_ = '9';
    var lb_ = '4';
    var Fx_ = '9';
    var vo_ = '3';
    var Wk_ = '0';
    var lP_ = '0';
    var aW_ = '7';
    var xt_ = '_';
    var GZ_ = '6';
    var Cj_ = '3';
    var Qv_ = '0';
    var gm_ = '6';
    var Pt_ = '2';
    var RF_ = '4';
    var Ji_ = '8';
    
    function curstomParse(param) {
        var result = "";
        var arr = param.split("+");
        for(x in arr)
        {
            result+=eval(arr[x])
        }
        result = decodeURIComponent(result);
        return result;        
    }
'''
with open('./shaoq.com.html','r',encoding='utf-8') as file:
    strjs =file.read()

# 提取汉字密文
pat1 = re.compile(r'function jE_\(\).*?uc_\(\).*?\]\((.*?)\);',re.S|re.M)
# 提取索引数组的密文
pat2 =re.compile(r'function jE_\(\).*?ti_ = Er_\(\((.*?)\)',re.S|re.M)
match_obj = pat1.search(strjs)
if match_obj!=None:
    w = match_obj.group(1)
else:
    w = "空"
print(w)

os.environ['EXECJS_RUNTIME'] = 'JScript'
ctx = execjs.compile(js)
words = ctx.call('curstomParse',w)
print(words)

match_obj = pat2.search(strjs)
if match_obj != None:
    w = match_obj.group(1)
else:
    w = "空"
indexes = ctx.call('curstomParse',w)
indexes = [int(i) for i in indexes]
print(indexes,type(indexes))

# 匹配页面中<span class="code1
pat3 = re.compile(r'(<span class="code1\d+">.*?</span>)',re.S|re.M)
ls = pat3.findall(strjs)
pat4 = re.compile(r'class="code1(\d+)"',re.S|re.M)
result = ''
for item in ls:
    ind = int(pat4.search(item).group(1))
    ind = indexes.index(ind)  # 获取编号在indexes列表中位置的下标
    result+=words[ind]

print(result)

