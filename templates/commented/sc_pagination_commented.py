"""
Use:
    Scrap pages with multiple elements of interest 
    with ability to crawl through pagination.
    
Note:
    Can be combined with sc_enter template to access data on other pages.
"""

import scrapy


class Spider(scrapy.Spider):
    name = ''  # spider call-tag
    start_urls = ['']  # initial url to crawl

    def parse(self, response):
        for item in response.css(''):
            
            # Scrap data
            
            yield data  # or yield request to auxilliary page

        if response.css('css-to-next-page-href'):  # basic next page condition
            yield scrapy.Request(
                response.css('css-to-next-page-href').extract_first()  # link to next page
                # Callback not neccesary, as by default parse is called
                # Meta may be used if required by script logic
                )
