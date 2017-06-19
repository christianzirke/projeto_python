# -*- coding: utf-8 -*-
import scrapy
from wiki_bot.items import WikiBotItem

class InfoboxSpiderSpider(scrapy.Spider):
    name = "wiki"
    allowed_domains = ["https://en.wikipedia.org/wiki/Facebook"]
    start_urls = (
        'https://en.wikipedia.org/wiki/Facebook',
    )

    def parse_pt(infobox_pt):
        for tr in response.xpath("//table[contains(@class, 'infobox')]/tr"):
            print "\n"
            print "\n"
            for td in tr.xpath("./td"):
                print "\n"
                print td.xpath(".").extract_first()
                print "\n"

    def parse_en(self, response):
        print "\n\n"
        print response
        print "\n\n"
        infobox = response.xpath("//table[contains(@class, 'infobox')]/tr")
        item = WikiBotItem()
        info_dict = {"no_header": []}
        for tr in infobox:
            table_head = tr.xpath("./th").extract_first()
            table_content = tr.xpath("./td").extract_first()
            if table_head is not None and table_content is not None:
               head = tr.xpath('./th/node()').extract_first().strip();
               text = tr.xpath("./td").extract_first().strip()
               info_dict[head] = text
            elif table_head is not None:
               info_dict[tr.xpath('./th/node()').extract_first().strip()] = ""
            elif table_content is not None:
               info_dict["no_header"] = tr.xpath("./td").extract_first().strip()

        item["infobox"] = info_dict
        return item

    def parse(self, response):
        item = self.parse_en(response)
        yield item
