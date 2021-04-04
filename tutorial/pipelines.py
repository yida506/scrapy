# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import pymysql

class TutorialPipeline:
    def process_item(self, item, spider):
        return item

class writeMysql:

    def __init__(self):
        self.client = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='yida506',
            db='mysqldb',
        )
        self.cur = self.client.cursor()

    def process_item(self, item, spider):
        insert_sql, params = item.get_insert_sql()

        self.cur.execute(insert_sql, params)
        self.client.commit()
        return item

    def handle_error(self, failure, item, spider):
        print(failure)