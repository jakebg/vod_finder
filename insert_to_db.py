import mysql.connector
from mysql.connector import Error
from itertools import islice
from mysql_vod import *


filename = "ytplaylist.txt"
lines_to_read = 3


with open(filename, 'r') as filehandle:
    for lines in filehandle: 
        test = lines.split(';')
        print('''INSERT INTO vod (vod_title,streamer_id,link)
        VALUES ('%s', '%s', '%s');
        ''' % (test[0],test[1],test[2]))

        query = '''
        INSERT INTO vod (vod_title,streamer_id,link)
        VALUES ('%s', '%s', '%s');
        ''' % (test[0],test[1],test[2].rstrip())

        execute_query(connection, query)






# populate_vod = """
# INSERT INTO vod (vod_title,streamer_id,link)
# VALUES 
# ('[Grand Theft Auto V] "NoPixel RP | Yung Dab Sells Crack" (03/13/2019)',1,'https://www.youtube.com/watch?v=ww0W7l8SY9U'),
# ('[Grand Theft Auto V] "NoPixel RP - Yung Dab Joins a Gang" (03/14/2019)',1,'https://www.youtube.com/watch?v=e72WGuj4poA');

# """
