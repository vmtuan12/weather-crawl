from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from weather_crawl.spiders import hn_spider, dn_spider, hcm_spider

settings = get_project_settings()
process = CrawlerProcess(settings)

process.crawl(hn_spider.HaNoiSpider)
process.crawl(dn_spider.DaNangSpider)
process.crawl(hcm_spider.HoChiMinhSpider)

process.start()