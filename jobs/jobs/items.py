# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    salary=scrapy.Field()
    num=scrapy.Field()
    edu=scrapy.Field()
    exp=scrapy.Field()
    area=scrapy.Field()
