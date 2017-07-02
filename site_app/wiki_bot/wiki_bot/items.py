import scrapy

class WikiBotItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    logo = scrapy.Field()
    nasdaq = scrapy.Field()
    wikipedia = scrapy.Field()
