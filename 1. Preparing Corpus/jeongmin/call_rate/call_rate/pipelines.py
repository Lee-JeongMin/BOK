# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# from scrapy.exporters import CsvItemExporter


# class CallRatePipeline:
#     def process_item(self, item, spider):
#         with open('./call_rate.csv', 'wb') as f:
#             expoter = CsvItemExporter(f, encoding='utf-8')
#             expoter.export_item(item)
#         return item

from __future__ import unicode_literals
from scrapy.exporters import JsonItemExporter, CsvItemExporter

class CallRatePipeline(object):
    def __init__(self):
        self.file = open("call_rate.csv", 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()
 
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
         
    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()   #파일 CLOSE 


