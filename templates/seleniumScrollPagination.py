"""
Use for pages where offers and pagination are dynamic
"""

import scrapy
from scrapy.utils.project import get_project_settings
from project.utils.context_manager_selenium import driver_manager
from time import sleep


class Spider(scrapy.Spider):
    name = ''
    start_urls = ['', ]
    default_driver = get_project_settings().get('DEFAULT_DRIVER')

    def parse(self, response):
        with driver_manager(self.default_driver) as driver:
            driver.get(self.start_urls[0])

            while True:

                for item in driver.find_elements_by_css_selector(''):
                    yield Item(
                        field1='',
                        field2='',
                        link=''
                    )

                sleep(1)
                driver.find_element_by_css_selector('').click()
