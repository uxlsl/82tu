# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from a82tu.utils import get_movie_list

class MySpider(CrawlSpider):
    name = 'all'
    allowed_domains = ['82tu.cc']
    start_urls = ['http://www.82tu.cc']

    rules = (
        Rule(LinkExtractor(allow=('/Cl/Ht\d\.html', '/Cl/Ht\d_\d.html'), deny=())),
        Rule(LinkExtractor(allow=('/Ct/Ht\d+.html', )), callback='parse_item'),
    )

    def parse_item(self, response):
        title = response.css('#main > div.view > div.info > h1::text').extract_first()
        for info, url in get_movie_list(response.text):
            yield {
                    'title': title,
                    'info': info,
                    'url': url
                    }
