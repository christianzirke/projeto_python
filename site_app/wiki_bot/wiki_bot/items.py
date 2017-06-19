import scrapy

class WikiBotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    infobox = scrapy.Field()
