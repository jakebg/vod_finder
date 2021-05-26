import mysql.connector
from mysql.connector import Error
from itertools import islice
from mysql_vod import *
from enum import Enum
import re

# September 4, 2020 (1/2)
# Clint Steven Vods
# ((January)?|(February)?|(March)?|(April)?|(May)?|(June)?|(July)?|(August)?|(September)?|(October)?|(November)?|(December)?)?\D?(\d{1,2}\D?)?\D?(19[7-9]\d|20\d{2})\s(\(\d{1,2}\/\d\))?

# (04/25/2019)
# MoonMOON
# [0-9]{2}\/[0-9]{2}\/[0-9]{4}

re_date1 = "[0-9]{2}\/[0-9]{2}\/[0-9]{4}"
# add \s?(\(\d{1,2}\/\d\))? for parts of videos
re_date2 = '((January)?|(February)?|(March)?|(April)?|(May)?|(June)?|(July)?|(August)?|(September)?|(October)?|(November)?|(December)?)\D(\d{1,2}\D?),\D?(19[7-9]\d|20\d{2})'
re_date3 = "[0-9]{2}.[0-9]{2}.[0-9]{4}"
re_list = [re_date1, re_date2, re_date3]

filename = 'test_get_db.txt'
game_list = ['Grand Theft Auto V', 
    'Skyrim', 
    "Tony Hawk's Pro Skater",
    'Animal Crossing',
    'Sekiro: Shadows Die Twice',
    "One Hour One Life",
    'Mario Royale',
    'Divinity: Original Sin II']


def parse_title(parse_line):
    print(parse_line)

    if any((match := string) in parse_line for string in game_list):
        game_result = match
    else:
        game_result = 'NOGAME'

    for x in re_list:
        result = re.search(x,parse_line)
        if result:
            date_result = result.group(0)
            break;
        else:
            date_result = 'NULL'
            #print('Date not found.')

    # print('Game: ', game_result)
    # print('Date: ', date_result)

    return date_result, game_result


def read_from_db_file():
    query = '''SELECT vod_title FROM vod WHERE game is NULL AND vod_title!='Deleted video';'''

    query_select = read_query(connection, query)

    with open(filename, 'w') as f:
        for listitem in query_select:
            f.write('%s\n'%listitem)

# YYYY-MM-DD
# April 19, 2020
# 05/24/2019
def change_date_format(date):
    import datetime

    if re.search(re_date1,date):
        # FORM OF 05/24/2019
        date_time_obj = datetime.datetime.strptime(date, '%m/%d/%Y')
        new_date = date_time_obj.date()

    elif re.search(re_date2,date):
        # FORM OF April 19, 2020
        date_time_obj = datetime.datetime.strptime(date, '%B %d, %Y')
        new_date = date_time_obj.date()

    elif re.search(re_date3,date):
        # FORM OF 05.25.2019
        date_time_obj = datetime.datetime.strptime(date, '%m.%d.%Y')
        new_date = date_time_obj.date()

    else:
        print('Date format not found')
        new_date = 'NODATE'

    return new_date

def add_values_to_db(value, date, game):
    query = ''' UPDATE vod
    SET date = '%s', game = '%s'
    WHERE vod_title = '%s';
    ''' % (date,game, value.strip())
    execute_query(connection, query)


def get_db_entry():
    read_from_db_file()
    with open(filename,'r') as f:
        for line in f:
            date, game = parse_title(line.strip())
            
            date = change_date_format(date)
            print('Game: ', game)
            print('Date: ', date,'\n')
            add_values_to_db(line, date, game)

def assign_series_in_db(SERIES_NUM, GAME_NAME, url):
    query ='''
    insert into playlist (playlist_id,playlist_title,playlist_link) 
    VALUES ( '%s', '%s', '%s');
    ''' % (SERIES_NUM, GAME_NAME, url)

    try: 
        execute_query(connection, query)
    except:
        print('Adding series failed')

if __name__ == '__main__':
    
    pass

    # test_string = '[Grand Theft Auto V] "NoPixel | Yung Dab - !EU" (03/11/2019)'
    # date_test = '2020-03-13'
    # add_values_to_db(test_string, date_test)
    
    # date, game = parse_title(test_string.strip())
    # date= change_date_format(date)
    # print('Game: ', game)
    # print('Date: ', date,'\n')




    # test_string2 = 'Clint Stevens - Skyrim (Part 6) [March 18, 2020]'
    # date, game = parse_title(test_string2.strip())
    # date = change_date_format(date)
    # print('Game: ', game)
    # print('Date: ', date,'\n')
    