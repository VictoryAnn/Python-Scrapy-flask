import scrapy
from scrapy.http import Request
from TEST.items import DetailItem
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import html5lib
import sys


class MySpider(scrapy.Spider):

    # 设置name
    name = "spidertieba"
    # 设定域名
    allowed_domains = ["tieba.baidu.com"]
    # 填写爬取地址
    start_urls = [

    ]
    #动态添加start_urls
    for i in range(1,100):
        pn = 0 + 50*i
        url = "http://tieba.baidu.com/f?kw=%E6%9D%AD%E5%B7%9E%E7%94%B5%E5%AD%90%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6&ie=utf-8&pn=" + str(pn)
        start_urls.append(url)

    # 编写爬取方法
    def parse(self, response):
       html = response.body
       #解析文本
       soup = BeautifulSoup(html,'html5lib')
       #提取链接
       sites = soup.find_all('div','threadlist_title pull_left j_th_tit ')
       for site in sites:
            #地址拼接
            link = urljoin('http://tieba.baidu.com',site.a.attrs['href'])
            yield Request(link,callback=self.parse_item)
    def parse_item(self,response):
        item = DetailItem()
        soup = BeautifulSoup(response.body,'html5lib')
        sites1 = soup.find_all('div','core_title core_title_theme_bright')
        for site in sites1:
            item['title'] = site.h1['title']
            item['link'] = response.url
        yield item