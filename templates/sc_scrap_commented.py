"""
Use:
    Scrap pages with multiple elements of interest.
"""

import scrapy


class Spider(scrapy.Spider):
    name = ''  # spider call-tag
    start_urls = ['']  # initial url to crawl

    def parse(self, response):
        for item in response.css(''):
            
            # Scrap data
            
            yield data
            
