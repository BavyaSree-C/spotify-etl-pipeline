import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import mysql.connector

#SETTING UP SPOTIFY API CREDENTIALS
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='ENTER CLIENT HERE',
    client_secret='ENTER SECRET KEY'
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


# Read track URLs from file
file_path='track_urls.txt'
with open(file_path,'r') as file:
    track_urls= file.readlines()

#Process each URL
for track_url in track_urls:
    track_url=track_url.strip()  #Remove any leading/trailing whitespaces
    try:
        #Extract track ID from URL
        track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)


        #Fetch track details from Spotify API
        track = sp.track(track_id)
        
        #Extract meta data
        track_data= {
            'Track Name': track['name'],
            'Artist': track['artists'][0]['name'],
            'Album': track['album']['name'],
            'Popularity': track['popularity'],
            'Duration (minutes)': track['duration_ms'] / 60000
        }

        #Insert Data into MySQL

        insert_query = '''
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

        print(f" Inserted: {track_data['Track Name']} by {track_data['Artist']}")

    except Exception as e:
        print(f"Error processing URL: {track_url}, Error: {e}")


#Close the connection
cursor.close()
connection.close()

print("All tracks have been processed and inserted into database.")