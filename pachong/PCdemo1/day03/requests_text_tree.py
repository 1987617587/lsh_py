from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# 方式一：创建BeautifulSoup对象
soup = BeautifulSoup(html, "lxml")
# print(soup)
print(soup.head.contents)
print(soup.body.contents)
print(len(soup.body.contents))

print(soup.head.childern)
print("=" * 30)
for child in soup.body.children:
    print(child)

print(soup.a)
print(soup.a.contents)
for child in soup.a.contents:
    print(child, type(child))

# CSS选择器
print("通过标签名查找：")
print(soup.select_one('head'))
print(soup.select_one('title'), type(soup.select_one('title')))
print(soup.select_one('a'))
print(soup.select('a'))
print(soup.select('p'))
# 查找不存在元素 返回None,[]
print(soup.select('pa'))

# 通过类名查找
print("通过类名查找:")
print((soup.select('.title')))
print((soup.select('.sister')))

# 通过id 查找
print("通过id查找:")
print((soup.select('#link1')))

# 组合查找
print("组合查找：")
print(soup.select('p .sister'))  # 空格等价xpath中的// 子孙关系
print(soup.select('body .sister'))  # 空格等价xpath中的//
# 能找到
print(soup.select('body > p >  #link1'))  # >等价xpath中的/ 父子关系
print(soup.select('body > p >  .sister'))  # >等价xpath中的/ 父子关系
# 找不到
print(soup.select('body > #link1'))  # >等价xpath中的/ 父子关系

# 属性和文本的获取
print("属性")
print(soup.select_one('a#link1').attrs['href'])
print(soup.select_one('a#link1')['href'])
print(soup.select_one('a#link1').get('href'))
print("文本")
# 文本类型是str
txt = soup.select('title')[0].get_text()
print(txt, type(txt))
# 文本类型不是str
txt2 = soup.select('title')[0].string
print(txt, type(txt2))

ls = soup.select('body > p > a')
for each in ls:
    # print(each.string)
    print(each.get_text())