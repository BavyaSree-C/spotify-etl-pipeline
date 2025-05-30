import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

#SETTING UP SPOTIFY API CREDENTIALS
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='895b413cdcad4ca3a70f8a55cf8aefba',
    client_secret='fb20ec8664a54294a4e7449162215767'
))

# MySQL Database Connectiom
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'spotify_db'
}

#Connect to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

#Full track URL (Example:  Señorita by Shawn Mendes)
track_url = "https://open.spotify.com/track/6v3KW9xbzN5yKLt9YKDYA2"

#Extract track ID directly from URL
track_id = re.search(r'track/([a-zA-Z0-9]+)',track_url).group(1)

#Fetch track details
track = sp.track(track_id)

#Extract metadata
track_data = {
    'Track Name': track['name'],
    'Artist': track['artists'][0]['name'],
    'Album': track['album']['name'],
    'Popularity': track['popularity'],
    'Duration (minutes)': track['duration_ms'] / 60000
}

#Insert data onto MySQL
insert_query='''
INSERT INTO spotify_tracks (track_name, artist, album, popularity, duration_minutes)
VALUES (%s, %s, %s, %s, %s)
'''
cursor.execute(insert_query,(
    track_data['Track Name'],
    track_data['Artist'],
    track_data['Album'],
    track_data['Popularity'],
    track_data['Duration (minutes)']
))

connection.commit()

print(f"Track '{track_data['Track Name']}' by {track_data['Artist']} inserted into the database.")

#Close the connection
cursor.close()
connection.close()