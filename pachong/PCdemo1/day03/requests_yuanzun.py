import requests
from bs4 import BeautifulSoup


def down(url):
    '''
    下载制定url的页面
    :param url:
    :return:
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = response.text
    return html


if __name__ == '__main__':
    url = 'https://www.biqudu.net/31_31729/'
    # 小说目录页面
    html = down(url)
    # print(html)
    # 提取小说章节的链接
    soup = BeautifulSoup(html, 'lxml')
    ls = soup.select('div#list > dl > dd')
    ls = ls[12:]
    print('len:', len(ls))

    base_url = 'https://www.biqudu.net'
    for item in ls:
        detail_url = base_url + item.select_one('a').get('href')
        # 请求章节的详情页面
        html = down(detail_url)
        # bs4做解析
        detail_soup = BeautifulSoup(html, 'lxml')
        # 标题
        title = detail_soup.select_one('div.bookname > h1').get_text()
        # print('title:', title)
        # 小说内容
        # 方式一：缺点：段落不分
        # content  =detail_soup.select_one('#content').get_text()
        # content = content.replace('readx();','')
        # content = content.replace('chaptererror();', '')
        # content = content.strip()
        # 方式二：
        content = detail_soup.select_one('#content')
        # 节点对象 ===> 字符串
        content = content.prettify()
        content = content.replace('(《》)', '')
        content = content.replace('<div id="content">', '')
        content = content.replace('<script>', '')
        content = content.replace('readx();', '')
        content = content.replace('</script>', '')
        content = content.replace('<br/>', '\n')
        content = content.replace('\n\n \n\n', '\n')
        content = content.replace('chaptererror();', '')
        content = content.replace('</div>', '')
        content = content.strip()
        # 获取最终正文
        # print('content:', content)
        print('=' * 200)
        # 存储文章
        with open("biquba/" + title + '.txt', 'a', encoding='utf-8') as file:
            file.write(content)
