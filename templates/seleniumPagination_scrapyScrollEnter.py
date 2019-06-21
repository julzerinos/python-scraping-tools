"""
Use for pages where pagination is dynamic, but offers are not.

Warning: Do not enter offers for websites with very large pagination,
because Selenium will wait for Scrapy to crawl the offer pages
and will crash mid-scraping.
"""

import scrapy
from utils.context_manager_selenium import driver_manager
from scrapy.utils.project import get_project_settings
from scrapy.selector import Selector
from time import sleep


class Spider(scrapy.Spider):
    name = ''
    start_urls = ['', ]
    default_driver = get_project_settings().get('DEFAULT_DRIVER')

    def parse(self, response):
        with driver_manager(self.default_driver) as driver:
            driver.get(self.start_urls[0])

            while True:

                response = Selector(text=driver.page_source.encode('utf-8'))
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

                sleep(1)
                driver.find_element_by_css_selector('css-to-next-page').click()

    def offer(self, response):
        I = response.meta.get('I')
        I['field3'] = ''
        yield I

