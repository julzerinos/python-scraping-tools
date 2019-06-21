from scrapy.commands import ScrapyCommand
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor, defer
from scrapy.settings import Settings
import inspect

import settings as settings
# Flake8 ignore issues related to star import
from spiders import *  # noqa: F403 F401


class CrawlSequential(ScrapyCommand):

    requires_project = True

    def syntax(self):
        return '[spiders]'

    def short_desc(self):
        return 'Runs all or selected spiders sequentially'

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

    def evaluate_args(self, args, spider_list):
        '''Method selects specified spiders and returns as new list'''
        if not args:
            return spider_list
        new_spider_list = (spider for spider in spider_list if any(arg in spider.name for arg in args))
        invalid_args = set(args).difference({spider.name for spider in new_spider_list})
        if invalid_args:
            raise NameError(
                'At least one of the given spider names is invalid: ' + ', '.join(invalid_args))
        return new_spider_list

    def run(self, args, opts):
        '''Runs the command'''
        spiders = self.evaluate_args(args, self.get_spiders())
        if not spiders:
            raise ValueError('No spider names match the spider database')
        crawler_settings = Settings()
        crawler_settings.setmodule(settings)
        runner = CrawlerRunner(crawler_settings)

        @defer.inlineCallbacks
        def crawl():
            for spider in spiders:
                yield runner.crawl(spider)
            reactor.stop()

        crawl()
        reactor.run()
