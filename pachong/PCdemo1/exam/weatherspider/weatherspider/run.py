
from scrapy import cmdline
name = 'weather'
cmd = 'scrapy crawl {0}'.format(name)

if __name__ == '__main__':
    cmdline.execute(cmd.split())





