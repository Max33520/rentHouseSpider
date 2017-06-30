# -*- coding:UTF-8 -*-

import utils
from retrying import retry


class RentSpider(object):

    @retry(stop_max_attempt_number=7)
    def crawl(self, url):
        """
        爬取网页内容
        :param url: 网页url
        :return: 内容
        """

        print(u'瞄准，目标就是这货：' + url)
        crawl_res = utils.html_dom(url)
        title = crawl_res.xpath('//div[@class="des"]/h2/a/text()')[0]
        house = {
            'title':  utils.away_rn(title)
                }
        print(house)
     
    @retry(stop_max_attempt_number=7)
    def next_page(self, url):
        """
        获取下一页链接
        :param url: 网站url
        :return: 成功返回下一页链接，失败返回None
        """
        print(u'本站是：' + url)
        html = utils.html_dom(url)
        if len(html):
            next_url = html.xpath('//a[@class="next"]/@href')[0]
        else:
            print(u'列车中途出轨，不知道往哪里开...')
            next_url = None
        print(u'下一站即将到达：' + next_url)
        return next_url
