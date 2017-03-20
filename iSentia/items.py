# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field

class IsentiaItem(scrapy.Item):
    ## defined Field for Item
    title = Field()
    link = Field()
    content = Field()
    author = Field()
    pass
