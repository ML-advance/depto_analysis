# Define here the models for your scraped items
#
# See documentation in:
# https://docs.org/en/latest/topics/items.html

from scrapy import Item, Field


class ScrappingItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass


class Quote(Item):
    id = Field()
    name = Field()
    birthdate = Field()
    bio = Field()
    created_at = Field()


class Department(Item):
    title = Field()
    address = Field()
    description = Field()
    location = Field()
    price = Field()
    currency = Field()
    rooms = Field()
    bathrooms = Field()
    size_from = Field()
    size_to = Field()
    indicator = Field()
    url = Field()
