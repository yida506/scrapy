import scrapy
import json
from ..items import tutorialItem,ProductItem
from ..sql import writeSQL

# class QuotesSpider(scrapy.Spider):
#     name = 'jd'
#     page_nums = 1
#     db = writeSQL()
#     start_id = db.search_data(sql = '''
#     SELECT PRODUCTS_ID FROM PRODUCTS WHERE IS_SPIDERED = FALSE
#     ''')[0]
#     db.close_sql()
#     start_urls = ['https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=%s&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'%start_id]
#     url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=%s&score=1&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1'
#     def parse(self, response):
#         db = writeSQL()
#         current_id = db.search_data(sql='''
#             SELECT PRODUCTS_ID FROM PRODUCTS WHERE IS_SPIDERED = FALSE
#             ''')[0]
#         db.close_sql()
#         html = response.text.replace('fetchJSON_comment98(', '').replace(');', '')
#         df = json.loads(html)
#         # print(df)
#         results = df['comments']
#         # print(results)
#         for i in range(len(results)):
#             item = tutorialItem()
#             item['content'] = results[i]['content']
#             item['creationTime'] = results[i]['creationTime']
#             item['id'] = results[i]['id']
#             item['productColor'] = results[i]['productColor']
#             item['productSize'] = results[i]['productSize']
#             item['score'] = results[i]['score']
#             # print('creationTime:',type(item['creationTime']),len(item['creationTime']))
#             # print('id:', type(item['id']), len(str(item['id'])))
#             # print('productColor:', type(item['productColor']), len(item['productColor']))
#             # print('productSize:', type(item['productSize']), len(item['productSize']))
#             # print('score:', type(item['score']), len(str(item['score'])))
#             # print('content:', type(item['content']), len(item['content']))
#             yield item
#         if self.page_nums < 50:
#             self.page_nums += 1
#             new_url = self.url%(current_id,self.page_nums)
#             print(new_url)
#             yield scrapy.http.Request(url=new_url,callback=self.parse,dont_filter=True)
#         else:
#             db = writeSQL()
#             db.update_data(sql='''
#             UPDATE PRODUCTS SET IS_SPIDERED = TRUE WHERE PRODUCTS_ID = %s
#             '''%current_id
#             )
#             new_id = db.search_data(sql='''
#             SELECT PRODUCTS_ID FROM PRODUCTS WHERE IS_SPIDERED = FALSE
#             ''')[0]
#             db.close_sql()
#             self.page_nums=0
#             next_url = self.url%(new_id,self.page_nums)
#             yield scrapy.http.Request(url=next_url,callback=self.parse,dont_filter=True)
#
#
class ProductsSpider(scrapy.Spider):
    name = 'product'
    # allow_domains = ['search.jd.com/']
    start_urls = ['https://search.jd.com/Search?keyword=%E8%8B%B9%E6%9E%9C%E6%89%8B%E6%9C%BA&qrst=1&wq=%E8%8B%B9%E6%9E%9C%E6%89%8B%E6%9C%BA&ev=exbrand_Apple%5E&page={}'.format(i) for i in range(2)]

    def parse(self,response):
        ids = response.xpath('//*[@id="J_goodsList"]/ul/li')
        for i in ids:
            products_id = i.xpath('@data-sku').get()
            shop_name = i.xpath('.//span[@class="J_im_icon"]/a/text()').get()
            price =  i.xpath('.//div[@class="p-price"]/strong/i/text()').get()
            # print(products_id)
            # print(shop_name)
            # print(price)
            product = ProductItem()
            product['products_id'] = products_id
            product['is_spidered'] = False
            product['shop_name'] = shop_name
            product['price'] = price
            yield product

