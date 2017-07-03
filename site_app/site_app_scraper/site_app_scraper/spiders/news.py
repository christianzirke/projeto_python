# -*- coding: utf-8 -*-
import scrapy
import requests
import urlparse
from datetime import datetime
from site_app_scraper.items import NewsBotItem

class NewsSpider(scrapy.Spider):
    name = "news_spider"
    allowed_domains = ["http://quotes.wsj.com"]
    start_urls = (
        'http://quotes.wsj.com/',
    )

    def parse_news(self, response):
        for news in response.xpath("//ul[contains(@id, 'newsSummary_c')]/li"):
            item = NewsBotItem()
            date_str = news.xpath(".//li[contains(@class, 'cr_dateStamp')]/text()").extract_first().strip()
            item["date"] = datetime.strptime(date_str, "%m/%d/%y")
            headline = news.xpath(".//span[contains(@class, 'headline')]/a")
            item["headline_text"] = headline.xpath("./text()").extract_first().strip()
            item["headline_link"] = headline.xpath("./@href").extract_first().strip()
            item["company"] = response.meta["company_id"]
            yield item


    def parse(self, response):
        request = requests.get("http://localhost:8000/get_companies_codes")
        codes = request.json()
        for company_id in codes:
            url = urlparse.urljoin(response.url, codes[company_id])
            meta = {"company_id": company_id}
            yield scrapy.Request(url, callback = self.parse_news, dont_filter=True, meta=meta)
