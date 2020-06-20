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
# 方式二：打开本地的html文件
# soup = BeautifulSoup(open('story.html'), 'lxml')
# print(soup)
# print(type(soup))  # <class 'bs4.BeautifulSoup'>

# Bs4的四大对象
# 1.Tag
# Tag的获取
print("Tag的获取:")
# <class 'bs4.element.Tag'>
print(soup.title, type(soup.title))
print(soup.head, type(soup.head))
# 如果标签有多个对象，返回第一个
print(soup.a, type(soup.a))
print(soup.p, type(soup.p))
# 属性 name 和 attrs
print(f"name属性:{soup.title.name}")
print(f"name属性:{soup.head.name}")

print(f"attrs属性:{soup.p.attrs}")  # attrs属性:{'class': ['title'], 'name': 'dromouse'}
# 返回的是字典,那么我们就可以进行以下操作
print(soup.p.attrs['name'])
print(soup.p.attrs['class'])
print(f"attrs属性:{soup.a.attrs}")
print(soup.a.attrs['href'])
print(soup.a.attrs['class'])
print(soup.a.attrs['id'])
# 可以省略attrs，获取标签的属性
print(soup.a['href'])
print(soup.a['class'])
print(soup.a['id'])
# 同样可以使用get获取
print(soup.a.get("href"))
print(soup.a.get("class"))
print(soup.a.get("id"))
# 属性修改
soup.a['class'] = ['title2']
print(soup.a['class'])
# 删除属性
print(soup.a)
del soup.a['class']
print(soup.a)

# 2.NavigableString
print("获取tag内部的文本")
print(soup.p.string, type(soup.p.string))
# 获取tag内部的文本
# The Dormouse's story <class 'bs4.element.NavigableString'>


# 3. BeautifulSoup
print(soup.name, type(soup))
print(soup.attrs)  # 本身属性为空
# [document] <class 'bs4.BeautifulSoup'>
# {}


# 4. Comment
# Comment 对象是一个特殊类型的 NavigableString 对象，其输出注释但丌包含注释符号
print(soup.a)
print(soup.a.string)
print(type(soup.a.string))
# <a href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
#  Elsie
# <class 'bs4.element.Comment'>
