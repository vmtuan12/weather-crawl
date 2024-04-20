from weather_crawl.spiders.base_spider import BaseSpider
import scrapy

class DaNangSpider(BaseSpider):

    name = 'da_nang'

    def start_requests(self):
        for year in self.base_years:
            link = f"https://weatherspark.com/h/y/119966/{year}/Historical-Weather-during-{year}-in-Da-Nang-Vietnam"
            yield scrapy.Request(url=link,
                                callback=self.parse_month_link,
                                meta={"city": "Da Nang", "year": year})