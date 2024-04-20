# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from kafka import KafkaProducer
import json

class WeatherCrawlPipeline:

    def open_spider(self, spider):
            
        self.producer = KafkaProducer(bootstrap_servers=['localhost:29092'], 
                                      value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        self.topic_hn = 'hn' 
        self.topic_dn = 'dn'
        self.topic_hcm = 'hcm'

    def process_item(self, item, spider):
        msg = ItemAdapter(item).asdict()

        if spider.name == 'da_nang':
            msg["id"] += "dn"
            self.producer.send(self.topic_dn, value=msg)
        elif spider.name == 'hcm':
            msg["id"] += "hcm"
            self.producer.send(self.topic_hcm, value=msg)
        else:
            msg["id"] += "hn"
            self.producer.send(self.topic_hn, value=msg)

        self.producer.flush()
        return item
