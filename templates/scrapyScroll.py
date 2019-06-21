"""
Use for pages where offers are not dynamic and there is no pagination
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
