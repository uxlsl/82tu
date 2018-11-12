# -*- coding: utf-8 -*-

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from .all import MySpider


class UpdateSpider(MySpider):
    name = 'update'

    rules = (
        Rule(LinkExtractor(allow=('/Cl/Ht\d\.html', '/Cl/Ht\d_\d+.html'), deny=())),
        Rule(LinkExtractor(allow=('/Ct/Ht\d.html', )), callback='parse_item'),  # 只前十页
    )
