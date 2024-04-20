from weather_crawl.spiders.base_spider import BaseSpider
import scrapy

class HoChiMinhSpider(BaseSpider):

    name = 'hcm'

    def start_requests(self):
        for year in self.base_years:
            link = f"https://weatherspark.com/h/y/116950/{year}/Historical-Weather-during-{year}-in-Ho-Chi-Minh-City-Vietnam"
            yield scrapy.Request(url=link,
                                callback=self.parse_month_link,
                                meta={"city": "HCM", "year": year})