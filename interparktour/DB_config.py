import pymysql as my

class DBHelper:
    conn = None
    def __init__(self):
        self.db_init()

    def db_init(self):
        self.conn = my.connect(
                        host='localhost',
                        user='root',
                        password='ahdrnffl*1216',
                        db='TEST_Crawler',
                        charset='utf8',
                        cursorclass=my.cursors.DictCursor )
    
    def db_free(self):
        if self.conn:
            self.conn.close()

    def insertCrawlingData(self, tourInfo):
        with self.conn.cursor() as cursor:
            sql = '''
            INSERT INTO Tour
            (t_title, t_grade, t_period, t_img_url, t_content)
            VALUES (%s,%s,%s,%s,%s)
            '''
            cursor.execute(sql, (tourInfo.t_title, tourInfo.t_grade, tourInfo.t_period, tourInfo.t_image, tourInfo.t_content))
            
            self.conn.commit()