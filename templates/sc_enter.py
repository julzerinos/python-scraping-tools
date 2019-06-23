import scrapy


class Spider(scrapy.Spider):
    name = ''
    start_urls = ['']

    def parse(self, response):
        for item in response.css(''):

            yield scrapy.Request(
                link,
                callback=self.aux_page_parse,
                meta={'data': data}
                )

    def aux_page_parse(self, response):
        data = response.meta.get('data')

        yield data
