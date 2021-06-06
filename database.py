import mysql.connector
from mysql.connector import Error

config = {
    'host' : 'localhost',
    'port' : 3306,
    'database' : 'chicago',
    'user' : 'root',
    'password' : 'chicagohomicides',
    'connection_timeout' : 180,
    'charset': 'utf8',
    'use_unicode': True,
    'get_warnings': True,
}
try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("select database();")
        

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")  
    