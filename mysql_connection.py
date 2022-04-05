import mysql.connector

def get_connection():
    connection=mysql.connector.connect(
    host = 'dbfoot.cnsfwt1k1yag.ap-northeast-2.rds.amazonaws.com',
    database='who_am_i',
    user='hoosl',
    password='1026')

    return connection


# MySQL에서 python 연결 코드
# use mysql;
# create user 'hoosl'@'%' identified by '1026';
# grant all on who_am_i.* to 'hoosl'@'%';