"""
On how to deal with particularly tricky iframes:
*This requires Selenium.

The most important line is
    driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))

This tells the selenium driver to focus on the iframe, as the iframe is treated
as a seperate webpage.

Of course, it is possible to find and scrap the source of the iframe,
but sometimes the source is blocked or too complicated.

General example below
"""

import scrapy
from scrapy.utils.project import get_project_settings
from time import sleep
from project.utils.context_manager_selenium import driver_manager


class Spider(scrapy.Spider):
    name = ''
    start_urls = ['']
    default_driver = get_project_settings().get('DEFAULT_DRIVER')

    def parse(self, response):
        with driver_manager(self.default_driver) as driver:
            while True:
                driver.get(self.start_urls[0])
                sleep(1)
                driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))

                for item in driver.find_elements_by_css_selector(''):
                    yield Item(
                        field1='',
                        field2='',
                        link=''
                    )

                if False:
                    break
