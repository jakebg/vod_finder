import mysql.connector
from mysql.connector import Error
from itertools import islice
from mysql_vod import *

import re

# September 4, 2020 (1/2)
# Clint Steven Vods
# ((January)?|(February)?|(March)?|(April)?|(May)?|(June)?|(July)?|(August)?|(September)?|(October)?|(November)?|(December)?)?\D?(\d{1,2}\D?)?\D?(19[7-9]\d|20\d{2})\s(\(\d{1,2}\/\d\))?

# (04/25/2019)
# MoonMOON
# [0-9]{2}\/[0-9]{2}\/[0-9]{4}

re_date1 = "[0-9]{2}\/[0-9]{2}\/[0-9]{4}"
re_date2 = '((January)?|(February)?|(March)?|(April)?|(May)?|(June)?|(July)?|(August)?|(September)?|(October)?|(November)?|(December)?)?\D?(\d{1,2}\D?)?\D?(19[7-9]\d|20\d{2})\s?(\(\d{1,2}\/\d\))?'
re_list = [re_date1, re_date2]

filename = 'test_get_db.txt'
game_list = ['Grand Theft Auto V', 'Skyrim', 'Tony Hawk\'s Pro Skater']




def parse_title(parse_line):
    print(parse_line)

    if any((match := string) in parse_line for string in game_list):
        print('Game: ', match)
        game_result = 'yes'
    else:
        game_result = 'NOGAME'
        print('NO GAME')

    for x in re_list:
        result = re.search(x,parse_line)
        if result:
            date = result.group(0)
            print('Date found: ', date)
            break;
        else:
            date = 'NODATE'
            #print('Date not found.')


    #result = re.search(date_pattern,parse_line)
    # result = False
    # if result:
    #     date = result.group(0)
    #     print('Date found: ', date)
    # else:
    #     date = 'NODATE'
    #     print('Date not found.')
    print('\n')


    return date, game_result

# [Grand Theft Auto V] "NoPixel | Yung Dab - !EU" (03/11/2019)
def read_from_db_file():
    query = '''SELECT vod_title FROM vod;'''

    test = read_query(connection, query)
    print(type(test))
    with open(filename, 'w') as f:
        for listitem in test:
            f.write('%s\n'%listitem)
    pass

if __name__ == '__main__':
    with open(filename,'r') as f:
        for line in f:
            parse_title(line.strip())

    pass