"""
Use:
    Scrap static pages with multiple elements of interest 
    with ability to crawl page related to individual element of interest.
"""

import scrapy

class Spider(scrapy.Spider):
    name = ''  # spider call-tag
    start_urls = ['']  # initial url to crawl

    def parse(self, response):
        for item in response.css(''):
            
            # Scrap data

            yield scrapy.Request(
                link_to_page,
                callback=self.aux_page_parse,  # callback indicates method to run on page crawl
                meta={'data': data}  # meta enables data handling between method occurences
                )

    def aux_page_parse(self, response):
        data = response.meta.get('data')
        
        # Continue scraping
        
        yield data
