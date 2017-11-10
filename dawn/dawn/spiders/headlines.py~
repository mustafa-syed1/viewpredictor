# -*- coding: utf-8 -*-
import scrapy
from dawn.items import DawnItem

class HeadlinesSpider(scrapy.Spider):
    name = 'headlines'
    allowed_domains = ['https://www.dawn.com/latest-news']
    start_urls =['https://www.dawn.com/latest-news/']

    def parse(self, response):

    	headlines=response.xpath('//div[3]/div/main/div/div/div[position()]/article[position()]')
   	for n in headlines:
   		headline=n.xpath('h2/a/text()').extract_first()
   		date=n.xpath('span/span[2]/@title').extract_first()
            	dawnitem=DawnItem()
        	dawnitem["news"]=headline
        	dawnitem["time"]=date
		yield dawnitem
