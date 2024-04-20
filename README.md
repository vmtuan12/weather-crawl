# Weather crawl

Temperature of Ha Noi, Da Nang, HCM city in 10 years, from 2014 to 2024.<br>
Source: [Weather Spark](https://weatherspark.com/)

> [!NOTE]  
> This project is using proxy for crawling, but I will not push my proxies on this repo :grin:. Turn the proxy setting off in weather_crawl/settings.py by commenting the DOWNLOADER_MIDDLEWARES, or go to weather_crawl/middlewares.py and change the method WeatherCrawlDownloaderMiddleware.process_request
