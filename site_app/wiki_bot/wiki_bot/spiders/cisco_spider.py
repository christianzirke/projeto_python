# -*- coding: utf-8 -*-
import scrapy
import wikipedia
import json
from wiki_bot.items import WikiBotItem

class InfoboxSpiderSpider(scrapy.Spider):
    name = "wiki_cisco"
    allowed_domains = ["https://en.wikipedia.org/wiki/Cisco_Systems"]
    start_urls = (
        'https://en.wikipedia.org/wiki/Cisco_Systems',
    )

    def parse_en(self, response):
        item = WikiBotItem()
        infobox = response.xpath("//table[contains(@class, 'infobox')]")
        item["name"] = infobox.xpath("./caption/text()").extract_first().strip()
        item["logo"] = infobox.xpath("./tr/td[contains(@class, 'logo')]/a[contains(@class, 'image')]/img/@src").extract_first().strip()
        item["nasdaq"] = infobox.xpath(".//li/a[@title='NASDAQ']/../a[2]/text()").extract_first().strip()
        item["wikipedia"] = {"link": "https://en.wikipedia.org/wiki/Cisco_Systems"}
        for tr in response.xpath("//table[contains(@class, 'infobox')]/tr"):
            table_head = tr.xpath("./th/text()").extract_first()
            table_content = tr.xpath("./td").extract_first()
            if table_head == "Founded" or table_head == "Headquarters" or table_head == "Founders":
                item["wikipedia"][table_head] = table_content.replace("/wiki/", "https://en.wikipedia.org/wiki/")

        item["wikipedia"]["summary"] = wikipedia.summary(item["name"], sentences=2)
        item["wikipedia"] = json.dumps(item["wikipedia"])
        return item

    def parse(self, response):
        item = self.parse_en(response)
        yield item
