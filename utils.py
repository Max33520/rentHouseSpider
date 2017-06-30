# -*- coding:UTF-8 -*-

from lxml import etree
import requests

proxy_pool = {}
# 是否代理
proxy = False


def html_dom(html_url):
    """
    通过url获取dom结构为xpath准备
    :param html_url: 网页地址
    :return: 成功返回dom_tree 网页dom，失败返回None
    """
    print(u'兄弟们go go!肢解他')
    global proxy
    global proxy_pool
    try:
        if proxy:
            proxy_pool = {
                "http": "61.152.81.193:9100",
                # "http": "89.40.114.26:1189"
            }
        response = requests.get(html_url, allow_redirects=False,  proxies=proxy_pool)
        if response.status_code == 200:
            html = response.content.decode('utf-8')
            dom_tree = etree.HTML(html)
        elif response.status_code != 200:
            proxy = True
        else:
            print(u'对方网站不理你，并向你扔了一个状态码：' + str(response.status_code))
            dom_tree = None

        return dom_tree
    except BaseException as e:
        print(e)
        return None


def away_rn(str_rn):
    """
    去除\r \n 空格
    :param str_rn:目标
    :return:
    """
    return str_rn.replace('\s', '').replace('\n', '').replace(' ', '')


def check_proxy_ok():
    """
    检查代理是否可用
    :return: 成功True，失败False
    """
    try:
        # ip_url = 'http://ipinfo.io'
        ip_url = 'http://httpbin.org/ip'
        response = requests.get(ip_url, proxies=proxy_pool)
        proxy_ip = response.json()['origin'].split(',')
        if len(proxy_ip) > 1:
            print(u'车票可以用编号是：'+proxy_ip[1])
            return True
    except BaseException as e:
        print(e)
        return False


