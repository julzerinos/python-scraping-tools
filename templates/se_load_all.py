"""
Use:
    Pages where a "Load more"/"Load all" button exists
    and must be clicked once or more times
    to access all desired content.

Notes:
    After pre-loading, offers may be scraped by Scrapy.
"""

from time import sleep

import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.selector import Selector

from utils.context_manager_selenium import driver_manager


class Spider(scrapy.Spider):
    name = ''
    start_urls = ['', ]
    default_driver = get_project_settings().get('DEFAULT_DRIVER')

    def parse(self, response):
        with driver_manager(self.default_driver) as driver:
            driver.get(self.start_urls[0])

            while True:
                if not load_condition:
                    break
                sleep(1)
                driver.find_element_by_css_selector('css-to-load-button').click()

            response = Selector(text=driver.page_source.encode('utf-8'))
            for item in response.css(''):
                
                # Scrap data
                
                yield data
