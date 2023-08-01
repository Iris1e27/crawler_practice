# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class YelpSpiderPipeline:
    def process_item(self, item, spider):
        # 在这里处理Item，例如保存到数据库或文件
        # 这里仅打印一下
        print(item)
        return item


import csv


class CsvExportPipeline:
    def __init__(self):
        self.file = open('restaurants.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(
            ['Name', 'Address', 'Cuisine Tags', 'Rating', 'Features', 'Price Range', 'Detail URL',
             'Reservation Link', 'Source URL'])

    def process_item(self, item, spider):
        cuisine_tags = [tag for tag in item['cuisine_tags'] if tag is not None]
        features = [f for f in item['features'] if len(f) > 2]
        rating = item['rating'].strip()

        self.writer.writerow([
            item['name'],
            item['address'],
            ', '.join(cuisine_tags) if cuisine_tags else None,
            rating,
            ', '.join(features) if features else None,
            item['price_range'],
            item['detail_url'],
            item['reservation_link'],
            item['source_url']
        ])
        return item

    def close_spider(self, spider):
        self.file.close()
