# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrappingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Quote(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    birthdate = scrapy.Field()
    bio = scrapy.Field()
    created_at = scrapy.Field()
