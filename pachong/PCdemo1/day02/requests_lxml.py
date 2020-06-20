from lxml import etree

# 加载外部文件，解析
html = etree.parse('hello.html')
print(html)
print(etree.tostring(html).decode())
print('获取所有li标签：')
result = html.xpath('//li')  # 整个文档中查找
print(result)
result = html.xpath('/li')  # 在根节点中查找li，根节点是div，找不到
print(result)
print('获取所有li下所有的a标签：')
result = html.xpath('//li/a')  # 整个文档中查找li下的子节点a
print(result)
result = html.xpath('//li//a')  # 整个文档中查找li下的子孙节点a
print(result)
print('获取href为‘link1.html’的a标签：')
result = html.xpath('//a[@href="link1.html"]')  # 整个文档中查找并且href='link1.html'
print(result)
print('获取li的class属性：')
result = html.xpath('//li/@class')  # 整个文档中li的class属性
print(result)
print('获取li的class属性为：‘item-inactive’下的a的href')
result = html.xpath('//li[@class="item-inactive"]/a/@href')
print(result)
# print('获取class属性包含item的li：')
# result = html.xpath('//li[contains(@class),"item"]')
# print(result)
print('获取最后一个li下面的a的href：')
result = html.xpath('//li[last()]/a/@href')
print(result)

print('获取倒数第二个li下面的a的文本：')
result = html.xpath('//li[last()-1]/a/text()')
print(result)

print('获取第三个li：')
elem = html.xpath('//li[3]')[0]
print(elem)

print('获取elem前面的兄弟节点：')
ls = elem.xpath('./preceding-sibling::*')
print(len(ls))
for each in ls:
    print(each.xpath("./a/text()"))

print('获取elem后面的兄弟节点：')
ls = elem.xpath('./following-sibling::*')
print(len(ls))
for each in ls:
    print(each.xpath("./a/text()"))