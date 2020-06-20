from fake_useragent import UserAgent

ua = UserAgent()
# 获取指定浏览器ua
print(ua.ie)
print(ua.chrom)
# 随机获取ua
print(ua.random)