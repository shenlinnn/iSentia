# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
from scrapy.exceptions import DropItem

class IsentiaPipeline(object):
    collection_name = 'Articles'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        ## connect to compose mongodb
        self.client = pymongo.MongoClient(self.mongo_uri,ssl_ca_certs = "./cert.pem")
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        ## insert item into db
        self.db[self.collection_name].insert(dict(item))
        return item


## check for duplicates and prevent them from inserting into db
class DuplicatesPipeline(object):
    def __init__(self):
        self.title_seen = set()

    def process_item(self, item, spider):
        if item['title'] in self.title_seen:
            raise DropItem("Repeated items found: %s" % item)
        else:
            self.title_seen.add(item['title'])
            return item