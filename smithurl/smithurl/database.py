import pymysql
import boto.route53

connection = pymysql.connect(host='localhost',user='root',password='y0y0M@!',db='urldb')

def collision_detector(short_url):
    with connection.cursor() as cursor:
        sql = "SELECT shorturl FROM urls WHERE shorturl = %s"
        return cursor.execute(sql, (short_url))
    connection.close()

def insert_entry(long_url,short_url):
    with connection.cursor() as cursor:
        sql = "insert into urls (entry_date,longurl,shorturl) values (now(),%s,%s)"
        cursor.execute(sql, (long_url,short_url))
    connection.commit()
    connection.close()

def send_to_route53(short_url):
    connection = boto.route53.connect_to_region('us-east-1')