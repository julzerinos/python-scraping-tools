import scrapy


class Spider(scrapy.Spider):
    name = ''
    start_urls = ['']

    def parse(self, response):
        for item in response.css(''):

            yield data
            
