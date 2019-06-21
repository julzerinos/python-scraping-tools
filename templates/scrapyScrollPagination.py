"""
Use for pages with static offers and static pagination.
"""

import scrapy


class Spider(scrapy.Spider):
    name = ''
    start_urls = ['']

    def parse(self, response):
        for item in response.css(''):
            yield Item(
                field1='',
                field2='',
                link=''
            )

        if response.css('css-to-next-page-href'):
            yield scrapy.Request(
                response.css('css-to-next-page-href').extract_first()
                )
