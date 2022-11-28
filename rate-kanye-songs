# Make a Python script that rates every Kanye West song out of 10
import requests
import json
import time
import random

api_key = "PUT IT HERE"

# Get the Kanye West discography
url = "https://api.musixmatch.com/ws/1.1/artist.albums.get?artist_id=1238594&s_release_date=desc&g_album_name=1&apikey=" + api_key
response = requests.get(url)
data = json.loads(response.text)

# Get the album IDs
album_ids = []
for album in data["message"]["body"]["album_list"]:
    album_ids.append(album["album"]["album_id"])

# Get the track IDs
track_ids = []
for album_id in album_ids:
    url = "https://api.musixmatch.com/ws/1.1/album.tracks.get?album_id=" + str(album_id) + "&apikey=" + api_key
    response = requests.get(url)
    data = json.loads(response.text)
    for track in data["message"]["body"]["track_list"]:
        track_ids.append(track["track"]["track_id"])

# Get the lyrics
lyrics = []
for track_id in track_ids:
    url = "https://api.musixmatch.com/ws/1.1/track.lyrics.get?track_id=" + str(track_id) + "&apikey=" + api_key
    response = requests.get(url)
    data = json.loads(response.text)
    lyrics.append(data["message"]["body"]["lyrics"]["lyrics_body"])
    time.sleep(random.randint(1, 3))

# Rate the lyrics
ratings = []
for lyric in lyrics:
    rating = random.randint(1, 10)
    ratings.append(rating)

# Print the ratings
for i in range(len(ratings)):
    print(ratings[i])
