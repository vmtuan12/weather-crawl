
from elasticsearch import Elasticsearch
import pandas as pd

client = Elasticsearch(
  "http://localhost:9200",
  basic_auth=("logstash_internal", "changeme"),
)

# client.info()

result = client.search(
    index="hcm",
    size=10000,
    scroll="1m"
)

counter = 0
scroll_id = result['_scroll_id']

data = {
    "id": [],
    "year": [],
    "month": [],
    "day": [],
    "hour": [],
    "city": [],
    "temperature": [],
    "url": []
}

while len(result['hits']['hits']):
    counter += len(result['hits']['hits'])

    for document in result['hits']['hits']:
        record = document["_source"]
        data["id"].append(record["id"])
        data["year"].append(record["year"])
        data["month"].append(record["month"])
        data["day"].append(record["day"])
        data["hour"].append(record["hour"])
        data["city"].append(record["city"])
        data["temperature"].append(record["temperature"])
        data["url"].append(record["url"])

    result = client.scroll(scroll_id=scroll_id, scroll="1m")
    scroll_id = result['_scroll_id']

print(counter)
df = pd.DataFrame(data)
df.to_csv("hcm.csv", index=False)