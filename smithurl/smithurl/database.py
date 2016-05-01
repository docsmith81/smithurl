import pymysql

connection = pymysql.connect(host='aa1umvpzcwrqqf5.cyjsfa15axuh.us-east-1.rds.amazonaws.com',user='smithurl',password='..Wide..Open',db='ebdb')

def collision_detector(short_url):
    with connection.cursor() as cursor:
        sql = "SELECT shorturl FROM urls WHERE shorturl = %s"
        return cursor.execute(sql, (short_url))
        cursor.close()

def insert_entry(long_url,short_url):
    with connection.cursor() as cursor:
        sql = "insert into urls (entry_date,longurl,shorturl) values (now(),%s,%s)"
        cursor.execute(sql, (long_url,short_url))
        cursor.close()
    connection.commit()

def url_lookup(short_url):
    with connection.cursor() as cursor:
        sql = "SELECT longurl FROM urls WHERE shorturl = %s"
        cursor.execute(sql, (short_url))
        result = cursor.fetchone()
        if result:
            return ''.join(map(str,result))
        cursor.close()