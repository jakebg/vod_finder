# Must have google-api-python-client installed
# pip3 install --upgrade google-api-python-client

import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "AIzaSyBDHdoNCwm5I_Q46ngYsI4q1qQzqEzrFm0")

def yt_playlist_lister(url, STREAMER='NONE'):
    query = parse_qs(urlparse(url).query)
    playlist_query = query["list"][0]

    request = youtube.playlistItems().list(
        playlistId = playlist_query,
        part = "snippet",
    )

    playlist_info = []
    while request is not None:
        response = request.execute()
        playlist_info += response["items"]
        request = youtube.playlistItems().list_next(request, response)

    playlist_output = open('ytplaylist.txt','w')

    for i in playlist_info:

        # find_apos finds apostrophe in string and adds 2nd apostrophe
        # for usage in sql (cannot have apostrophe or string ruins INSERT into the table)
        # OLD WAY { playlist_output.write(f'{i["snippet"]["title"]};') }
        find_apos = f'{i["snippet"]["title"]};'
        try: 
            find_apos.index("'")
        except:
            playlist_output.write(find_apos)
        else:
            count = find_apos.index("'")
            found = find_apos[:count]+ "'" + find_apos[count:]
            playlist_output.write(found)

        #SETS STREAMER ID
        playlist_output.write(STREAMER)
        playlist_output.write(f'https://www.youtube.com/watch?v={i["snippet"]["resourceId"]["videoId"]}\n')

