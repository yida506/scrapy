import  pymysql

class writeSQL:

    def __init__(self):
        self.client = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='yida506',
            db='mysqldb',
        )
        self.cur = self.client.cursor()

    def creat_table(self,tabel_name,sql):
        self.cur.execute('DROP TABLE IF EXISTS {}'.format(tabel_name))
        self.cur.execute(sql)


    def close_sql(self):
        self.client.close()

    def insert_data(self,sql):
        try:
            self.cur.execute(sql)
            self.client.commit()
        except:
            self.client.rollback()

    def search_data(self,sql):
        try:
            self.cur.execute(sql)
            results = self.cur.fetchall()
            print(len(results))
            return results[0]
        except:
            self.client.rollback()

    def update_data(self,sql):
        try:
            self.cur.execute(sql)
            self.client.commit()
        except:
            self.client.rollback()

if __name__ == '__main__':
    db = writeSQL()
    # tabel_name = 'ITEMS'
    # sql = '''CREATE TABLE ITEMS (
    # ID INT NOT NULL auto_increment,
    # CREATIONTIME CHAR(19),
    # PRODUCTS_ID BIGINT(50),
    # PRODUCTCOLOR CHAR(20),
    # PRODUCTSIZE CHAR(25),
    # SCORE INT,
    # CONTENT TEXT,
    # PRIMARY KEY(ID)
    # )
    # '''
    # db.creat_table(tabel_name,sql)
    # db.close_sql()
    tabel_name = 'PRODUCTS'
    sql = '''CREATE TABLE PRODUCTS(
    ID INT NOT NULL auto_increment,
    PRODUCTS_ID BIGINT(50),
    IS_SPIDERED BOOL,
    SHOP_NAME CHAR(40),
    PRICE INT,
    PRIMARY KEY(ID,PRODUCTS_ID)
    )
    '''
    db.creat_table(tabel_name,sql)
    db.close_sql()
    # sql = '''
    # SELECT SHOP_NAME FROM PRODUCTS WHERE SHOP_NAME REGEXP '二'
    # '''
    # sql = '''
    # SELECT PRODUCTS_ID FROM PRODUCTS WHERE IS_SPIDERED = FALSE
    # '''
    # sql = '''
    # DELETE FROM PRODUCTS WHERE SHOP_NAME REGEXP '二'
    # '''
    # sql = '''
    # DELETE FROM PRODUCTS WHERE PRICE < 1000
    # '''
    # sql = '''
    # SELECT * FROM PRODUCTS
    # '''
    # db.search_data(sql)
    # db.close_sql()