from weather_crawl.spiders.base_spider import BaseSpider
import scrapy

class HaNoiSpider(BaseSpider):

    name = 'ha_noi'

    def start_requests(self):
        for year in self.base_years:
            link = f"https://weatherspark.com/h/y/116009/{year}/Historical-Weather-during-{year}-in-Hanoi-Vietnam"
            yield scrapy.Request(url=link,
                                callback=self.parse_month_link,
                                meta={"city": "Ha Noi", "year": year})