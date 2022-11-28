# Create a Python script which changes my Spotify song every second
import spotipy
import spotipy.util as util
import time

# Spotify API credentials
username = 'your_username'
client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'your_redirect_uri'

# Get the user's Spotify authorization token
token = util.prompt_for_user_token(username,
                                   scope='user-modify-playback-state',
                                   client_id=client_id,
                                   client_secret=client_secret,
                                   redirect_uri=redirect_uri)

# Create the Spotify object
spotify = spotipy.Spotify(auth=token)

# Get the user's device ID
devices = spotify.devices()
device_id = devices['devices'][0]['id']

# Get the user's saved tracks
saved_tracks = spotify.current_user_saved_tracks()

# Create a list of the user's saved tracks
track_list = []
for item in saved_tracks['items']:
    track = item['track']
    track_list.append(track['id'])

# Play the first track in the list
spotify.start_playback(device_id=device_id, uris=[track_list[0]])

# Change the song every second
while True:
    for track in track_list:
        spotify.start_playback(device_id=device_id, uris=[track])
        time.sleep(1)
