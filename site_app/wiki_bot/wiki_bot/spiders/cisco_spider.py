# -*- coding: utf-8 -*-
import scrapy
from wiki_bot.items import WikiBotItem

class InfoboxSpiderSpider(scrapy.Spider):
    name = "wiki_cisco"
    allowed_domains = ["https://en.wikipedia.org/wiki/Cisco_Systems"]
    start_urls = (
        'https://en.wikipedia.org/wiki/Cisco_Systems',
    )

    def parse_en(self, response):
        item = WikiBotItem()
        print "\n\n"
        print response
        print "\n\n"
        infobox = response.xpath("//table[contains(@class, 'infobox')]")
        item["name"] = infobox.xpath("./caption/text()").extract_first().strip()
        item["logo"] = infobox.xpath("./tr/td[contains(@class, 'logo')]/a[contains(@class, 'image')]/img/@src").extract_first().strip()
        item["nasdaq"] = infobox.xpath(".//li/a[@title='NASDAQ']/../a[2]/text()").extract_first().strip()
        print item["logo"]
        info_dict = {"no_header": []}
        for tr in response.xpath("//table[contains(@class, 'infobox')]/tr"):
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
