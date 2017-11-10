# -*- coding: utf-8 -*-
import scrapy
import bs4
import requests
import re
class ScraperSpider(scrapy.Spider):
    name = 'scraper'
    allowed_domains = ['https://www.geo.tv/latest-news']
    start_urls = ['https://www.geo.tv/latest-news']

    def parse(self, response):
        html=response.body	
	
	soup=bs4.BeautifulSoup(html,'lxml')
	
	hrefs=soup.find_all('div',{'class' : 'video-list'})
	website=2
	for tag in hrefs:
		links=tag.find_all('a',{'class' : 'open-section'})
		i=0  		
		for link in links:
    			linc=link['href']
			#print linc    			
			if i!=0:
				yield scrapy.Request(linc,callback=self.parsenews,dont_filter=True)
			i=i+1
	
	
    def parsenews(self,response):
	html=response.body
	soup=bs4.BeautifulSoup(html,'lxml')
	content=soup.find_all('div',{'class':'story-area'})
	for tag in content:
		
		title=tag.find('h1').text
		date=tag.find('p',{ 'class' :'post-date-time'})
			
		authors= tag.find_all('span',{ 'class':'author_agency'})
		paragraphs=tag.find_all('p',{'class':""})
		
				
		title=title.replace('\n',"")
		date=date.text
		author=''
		for writer in authors:
			author+=''.join(writer.get_text())+','
		paragraph=''
		#print author
		for p in paragraphs:
			paragraph+=''.join(p.findAll(text=True))
		#print paragraph
		yield {
		    "title" :  title ,
		    "date" : date,
		    "author" : author,
		    "paragraph" : paragraph
			} 
	website=1	
	if website<=30:
		url = 'https://www.geo.tv/latest-news'+website
		yield scrapy.Request(url,callback=self.parse,dont_filter=True)	
		website+1
