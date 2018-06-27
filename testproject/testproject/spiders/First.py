# -*- coding: utf-8 -*-
import scrapy


class FirstSpider(scrapy.Spider):
    name = 'First'
    allowed_domains = ['https://jp.techcrunch.com/']
    start_urls = ['http://https://jp.techcrunch.com//']

    def parse(self, response):
        pass
