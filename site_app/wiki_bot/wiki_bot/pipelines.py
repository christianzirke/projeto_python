import json
import codecs

class WikiBotPipeline(object):
    # define the fields for your item here like:
    # name = scrapy.Field()
    def process_item(self, item, spider):
        return item

    def __init__(self):
        self.file = codecs.open('scraped_data_utf8.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_close(self, spider):
        self.file.close()
