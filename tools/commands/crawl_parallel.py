from scrapy.commands import ScrapyCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import inspect

import settings as settings
# Flake8 ignore issues related to star import
from spiders import *  # noqa: F403 F401


class CrawlParallel(ScrapyCommand):

    requires_project = True

    def short_desc(self):
        return 'Runs all spiders parallely'

    def get_spiders(self):
        '''Retrieves the list of available spider classes'''
        modules = list(filter(inspect.ismodule, globals().values()))
        classes = []
        for module in modules:
            for object_ in dir(module):
                spider_class = getattr(module, object_)
                if inspect.isclass(spider_class) and object_.endswith('Spider'):
                    classes.append(spider_class)
        return classes

    def run(self, args, opts):
        '''Runs the command'''

        spiders = self.get_spiders()

        crawler_settings = Settings()
        crawler_settings.setmodule(settings)
        process = CrawlerProcess(settings=crawler_settings)

        for spider_class in spiders:
            process.crawl(spider_class)

        process.start()
