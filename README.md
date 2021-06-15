# vod_finder

Uses:
  Python
  MySQL
  Youtube API

https://dbdiagram.io/embed/60a2c533b29a09603d154366

This series of programs helps create a database of VODs(videos on demand) of twitch streamer previous streams that were reuploaded to youtube.


yt_playlist_lister.py - Retrieves data from a given Youtube playlist using the Youtube API. Returns a text file that can then be used in the insert_to_db.py to input to database

get_db_entry.py - This program finds the name of the game and date (typcially in the title of the VOD) and updates the database given the values found.

insert_to_db.py - Inserts the values from the text file into the database. Uses mysql for python

mysql_vod.py - Main driver function.

helper.py - Creates a lists of lists out of a text file
