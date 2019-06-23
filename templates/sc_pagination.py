import scrapy


class Spider(scrapy.Spider):
    name = ''
    start_urls = ['']

    def parse(self, response):
        for item in response.css(''):

            yield data

        if response.css(''):
            yield scrapy.Request(
                response.css('css-to-next-page-href').extract_first()
                )
