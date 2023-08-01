# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RestaurantItem(scrapy.Item):
    name = scrapy.Field()
    detail_url = scrapy.Field()
    address = scrapy.Field()
    cuisine_tags = scrapy.Field()
    features = scrapy.Field()
    rating = scrapy.Field()
    opening_hours = scrapy.Field()
    price_range = scrapy.Field()
    reservation_link = scrapy.Field()
    source_url = scrapy.Field()
