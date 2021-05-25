import mysql.connector
from mysql.connector import Error
import pandas as pd


pw = ""

def create_connection(host_name, user_name,user_password,db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            auth_plugin='mysql_native_password',
            database=db_name
        )
        print("Connection Successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("query exectued")
    except Error as err:
        print(f"error: '{err}'")

def read_query(connection,query):
    cursor = connection.cursor()
    result = None 
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}' ")

# https://www.freecodecamp.org/news/connect-python-with-sql/

db='vodfinder'

connection = create_connection("127.0.0.1", "root", pw, db)




# populate_vod = """
# INSERT INTO vod (vod_title,streamer_id,link)
# VALUES 
# ('[Grand Theft Auto V] "NoPixel RP | Yung Dab Sells Crack" (03/13/2019)',1,'https://www.youtube.com/watch?v=ww0W7l8SY9U'),
# ('[Grand Theft Auto V] "NoPixel RP - Yung Dab Joins a Gang" (03/14/2019)',1,'https://www.youtube.com/watch?v=e72WGuj4poA');

# """

# execute_query(connection,populate_vod)
