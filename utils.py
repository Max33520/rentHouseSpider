# -*- coding:UTF-8 -*-

from lxml import etree
import requests

def htmlDom(html_url):
    '''
    通过url获取dom结构为xpath准备
    param
        html_url 网页地址
    return
        成功返回dom_tree 网页dom，失败返回None
    '''
    print u'兄弟们go go!肢解他'
    response = requests.get(html_url)
    if response.status_code == 200:
        html = response.content.decode('utf-8')
        dom_tree = etree.HTML(html)
    else:
        print u'对方网站不理你，并向你扔了一个状态码：' + str(response.status_code)
        dom_tree =  None
    
    return dom_tree
   
def funckRN(str_rn):
    '''
    去除\r \n 空格
    '''

    return str_rn.replace('\s','').replace('\n','').replace(' ','')
