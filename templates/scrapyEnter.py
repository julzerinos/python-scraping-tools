"""
Use for pages where offers and pagination are not dynamic.
"""

import scrapy

class Spider(scrapy.Spider):
    name = ''
    start_urls = ['']

    def parse(self, response):
        for item in response.css(''):
            I = Item(
                field1='',
                field2='',
                link=''
            )

            yield scrapy.Request(
                I['link'],
                callback=self.offer,
                meta={'I': I}
                )

    def offer(self, response):
        I = response.meta.get('I')
        I['field3'] = ''
        yield I
