# -*- coding:UTF-8 -*-

from rentHouse import RentSpider

g_spider = RentSpider()

if __name__ == '__main__':
    print(u'乘客请坐好，火车要起飞了...')
    # 鱼雷目标
    target_url = 'http://cd.58.com/chuzu/0/pn1/'
    while True:
        g_spider.crawl(target_url)
        target_url = g_spider.next_page(target_url)

