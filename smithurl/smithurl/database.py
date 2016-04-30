import pymysql

connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             cursorclass=pymysql.cursors.DictCursor)

def collision_detector(short_url):
    