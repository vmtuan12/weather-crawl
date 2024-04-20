from typing import Any
import scrapy
import weather_crawl.spiders.xpath_constant as xpath

from scrapy.http import Request, Response

class BaseSpider(scrapy.Spider):

    domain_name = 'https://weatherspark.com'

    base_years = [x for x in range(2014, 2025)]

    time_mapping = {
        "12:00 AM": "0:00",
        "12:30 AM": "0:30",
        "1:00 AM": "1:00",
        "1:30 AM": "1:30",
        "2:00 AM": "2:00",
        "2:30 AM": "2:30",
        "3:00 AM": "3:00",
        "3:30 AM": "3:30",
        "4:00 AM": "4:00",
        "4:30 AM": "4:30",
        "5:00 AM": "5:00",
        "5:30 AM": "5:30",
        "6:00 AM": "6:00",
        "6:30 AM": "6:30",
        "7:00 AM": "7:00",
        "7:30 AM": "7:30",
        "8:00 AM": "8:00",
        "8:30 AM": "8:30",
        "9:00 AM": "9:00",
        "9:30 AM": "9:30",
        "10:00 AM": "10:00",
        "10:30 AM": "10:30",
        "11:00 AM": "11:00",
        "11:30 AM": "11:30",
        "12:00 PM": "12:00",
        "12:30 PM": "12:30",
        "1:00 PM": "13:00",
        "1:30 PM": "13:30",
        "2:00 PM": "14:00",
        "2:30 PM": "14:30",
        "3:00 PM": "15:00",
        "3:30 PM": "15:30",
        "4:00 PM": "16:00",
        "4:30 PM": "16:30",
        "5:00 PM": "17:00",
        "5:30 PM": "17:30",
        "6:00 PM": "18:00",
        "6:30 PM": "18:30",
        "7:00 PM": "19:00",
        "7:30 PM": "19:30",
        "8:00 PM": "20:00",
        "8:30 PM": "20:30",
        "9:00 PM": "21:00",
        "9:30 PM": "21:30",
        "10:00 PM": "22:00",
        "10:30 PM": "22:30",
        "11:00 PM": "23:00",
        "11:30 PM": "23:30"
    }

    def fahrenheit_to_celsius(self, temperature: str) -> float:
        fahrenheit = float(temperature[:-2])
        celsius = (fahrenheit - 32) * 5/9
        return round(celsius, 1)

    def start_requests(self):
        pass

    def parse_month_link(self, response):
        dis_xpath = xpath.LIST_MONTH_OF_YEAR
        metadata = response.meta
        list_link = response.xpath(dis_xpath + '/@href').getall()

        for index, href in enumerate(list_link):
                metadata["month"] = index + 1
                yield scrapy.Request(url=(self.domain_name + href), 
                                    callback=self.parse_day_link,
                                    meta=metadata)
            
    def parse_day_link(self, response):
        dis_xpath = xpath.LIST_DAY_OF_MONTH
        metadata = response.meta
        metadata["month"] = response.meta.get("month")
        list_link = response.xpath(dis_xpath + '/@href').getall()

        for index, href in enumerate(list_link):
            metadata["day"] = index + 1
            yield scrapy.Request(url=(self.domain_name + href), 
                                callback=self.parse_weather,
                                meta=metadata)

    def parse_weather(self, response: Response, **kwargs: Any):
        # header = response.xpath(xpath.DAY_TIME_HEADER)
        time = response.xpath(xpath.DAY_TIME_VALUE + '/text()').getall()
        temperature = response.xpath(xpath.DAY_TIME_TEMPERATURE + '/text()').getall()
        # wind = response.xpath(xpath.DAY_TIME_WIND + '/text()').getall()

        hour_map = {}

        for index, single_time in enumerate(time):
            hour_map[single_time.strip()] = {
                "temperature": temperature[index].strip(),
                # "wind": wind[index].strip()
            }

        year = response.meta.get("year")
        month = response.meta.get("month")
        day = response.meta.get("day")

        city = response.meta.get("city")

        err_index = 0
        for hour in hour_map:

            try:
                converted_hour = self.time_mapping.get(hour)
                yield {
                    "city": city,
                    "year": year,
                    "month": month,
                    "day": day,
                    "hour": converted_hour,
                    "temperature": self.fahrenheit_to_celsius(temperature=hour_map[hour]["temperature"]),
                    # "wind_speed": hour_map[hour]["wind"],
                    "url": response.url,
                    "id": f"{day}-{month}-{year}-{converted_hour}-"
                }
            except:
                yield {
                    "city": city,
                    "year": year,
                    "month": month,
                    "day": day,
                    "hour": None,
                    "temperature": None,
                    # "wind_speed": hour_map[hour]["wind"],
                    "url": response.url,
                    "id": f"{day}-{month}-{year}-err{err_index}-"
                }
                err_index += 1