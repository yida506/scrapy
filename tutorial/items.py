# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class tutorialItem(scrapy.Item):
    # define the fields for your item here like:
    content = scrapy.Field()
    creationTime = scrapy.Field()
    id = scrapy.Field()
    productColor = scrapy.Field()
    productSize = scrapy.Field()
    score = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = '''
        INSERT INTO ITEMS(CREATIONTIME,PRODUCTS_ID,PRODUCTCOLOR,PRODUCTSIZE,SCORE,CONTENT) VALUES (%s,%s,%s,%s,%s,%s)
        '''

        params = (self['creationTime'],self['id'],self['productColor'],self['productSize'],self['score'],self['content'])
        return insert_sql, params

class ProductItem(scrapy.Item):

    products_id = scrapy.Field()
    is_spidered = scrapy.Field()
    shop_name = scrapy.Field()
    price = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = '''
        INSERT INTO PRODUCTS(PRODUCTS_ID,IS_SPIDERED,SHOP_NAME,PRICE) VALUES (%s,%s,%s,%s)
        '''

        params = (self['products_id'],self['is_spidered'],self['shop_name'],self['price'])
        return insert_sql, params
