"""
# author Liu shi hao
# date: 2019/11/27 15:24
# file_name: date_test

"""
# 在我们平常的代码中，经常需要和日期及时间打交道。
# 时间和日期处理相关的模块有：
# time、datetime以及calendar
#
# 格式化符号：一般这样写:"%Y%m%d %H%M%S"或者“%x %X”
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %j 年内的一天（001-366）
# %m 月份（01-12）
# %M 分钟数（00=59）
# %p 本地A.M.或P.M.的等价符
# %S 秒（00-59）
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %Z 当前时区的名称
# %% %号本身


# 日期时间——datetime
#
# 日期模块的引入：
import calendar
import time
from datetime import datetime

#
#
# 获取当前日期对象：年月日时分秒.毫微秒
# print(datetime.now())
#
# 自己设定年月日时分秒获取日期时间对象
# datetime(year, month, day ,hour, minute, second)
#
# print(datetime(2019, 12, 27, 16, 23, 27))
# 根据时间戳获取日期时间
# print(datetime.fromtimestamp(0))
#
#
# 日期时间格式化成字符串
# datetime.strftime(“%Y-%m-%d %H:%M:%S”)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# dt = datetime.now()
# t = dt.strftime("%Y{y}%m{m}%d{d} %H:%M:%S").format(y="年", m="月", d="日")
# m = dt.strftime("%Y{0}%m{1}%d{2} %H{3}%M{4}%S{5}").format("年", "月", "日", "时", "分", "秒")
# print(t)
# print(m)
# now = datetime.now()
# print(now.strftime("%x %X"), type(now.strftime("%x %X")))  # 国外的时间格式
# list_time = list(now.strftime("%x %X"))
# list_time[0:2], list_time[6:8] = list_time[6:8],list_time[0:2]
# print("".join(list_time))  # 国外的时间格式转中国格式
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 字符串转换日期 经常用于检测日期字符串的合法性，若日期不正常会出转换异常
dt = datetime.strptime("2017-10-01 00:00:00", "%Y-%m-%d %H:%M:%S")
#
# print(dt)
# 日期时间的运算
# 比较日期大小 > < >= <= != ==均可直接比较
# print(dt > datetime.strptime("2017-09-01 00:00:00", "%Y-%m-%d %H:%M:%S"))
# print(dt <= datetime.strptime("2017-09-01 00:00:00", "%Y-%m-%d %H:%M:%S"))
# 计算日期相差天数
# dt = datetime.strptime("2019-7-21 00:00:00", "%Y-%m-%d %H:%M:%S")
# print((dt - datetime.now()))
# print((dt - datetime.now()).days)
# print((dt - datetime.now()).seconds)
# print((dt - datetime.now()).seconds // 3600, (dt - datetime.now()).seconds % 3600 // 60,
#       (dt - datetime.now()).seconds % 60)  # 把不足一天的总秒数换成时分秒
# 计算n（天\小时\分钟\秒等）后的日期
import datetime as d_t  # 避免导入模块重名

# print(datetime.now() + d_t.timedelta(days=50, hours=0, minutes=0, seconds=-10000))

# 日历（Calendar）模块
# 此模块的函数都是日历相关的，例如打印某月的字符月历。
# 模块包含了以下内置函数：
# 年历：
# print(calendar.calendar(2000, w=2, l=1, c=6, m=3))
# calendar.prcal(2000, w=2, l=1, c=6, m=6)
# calendar.prmonth(2019,12)

# 某年的所有月历
# 默认3个月一行，c为月历间隔距离， w是日期间隔距离，l是每星期行数，一般默认即可
# print(calendar.calendar(2019))
# 最方便的写法：calendar.prcal(year[, w=2, l=1, c=6, m=3])  # 自动输出
#
# 月的周历：
# calendar.month(year, month[, w=2, l=1])
# 某月的所有周历
# w是日期间隔距离，l是每星期行数，一般默认即可
# print(calendar.month(2019, 7))
# 最方便写法：calendar.prmonth(year, month[, w=2, l=1])  # 自动输出
#
#
# 获取某月的周历嵌套列表：不在当月的日期记为0
# print(calendar.monthcalendar(2019, 12))
#
# 几个好使的功能：
# 判断闰年：
# print(calendar.isleap(2020))
#
# 判断间隔的年份[y1, y2)中的闰年数：
# print(calendar.leapdays(2000, 2020))
#
# 获取月份首天的星期数及总天数
# print(calendar.monthrange(2019, 12)[0]+1)  # 首天的星期数(中国)
# print(calendar.monthrange(2019, 12)[1])  # 总天数
# 返回两个整数。第一个是该月的第一天是星期几(0 - 6
# 对应周一 - 周日)，第二个是该月的天数
#
# 获取某日是星期几
# calendar.weekday(year, month, day)
# print(calendar.weekday(2019, 12, 4)+1)  # 星期几+1(中国)
# 根据日历上的某天获取时间戳
# 以便向其他日期时间转换：
# calendar.timegm(tupletime)
# 和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间戳（1970
# 纪元后经过的浮点秒数）。
#
#
#
#
# 模块模块的引入：import time
#
# time中常用函数:
# 程序休眠：例如爬取时速度不宜过快，可以休眠一会再继续
# for i in range(90):
#     print("*")
#     time.sleep(1)

# 线程休眠固定秒数后醒来继续执行
#
start = time.time()
for i in range(100000):
    print("*",end="")
end = time.time()
print(end - start)
# 计算程序运行时间：
# time.time()
# 返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
# 示例：
# 计算下面的程序花费了多少时间
# for i in range(1000000):
#     print(i)
#
# 方法：在代码段前后加上time.time() 计算时间差即可得到运行所需时间
# start = time.time()
# for i in range(1000000):
#     print(i)
#
# end = time.time()
# print(str.format("程序花费了{}毫秒", int((end - start)*1000)))
