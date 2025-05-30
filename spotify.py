import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt
import re

# Setting up client credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='ENTER CLIENT HERE',
    client_secret='ENTER SECRET KEY'
))

#full track url(example:  Señorita by Shawn Mendes)
track_url = "https://open.spotify.com/track/6v3KW9xbzN5yKLt9YKDYA2"

#Extract  track ID directly from url using regex
track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

#fetch track details
track = sp.track(track_id)
print(track)

#Extract metadata
track_data = {
    'Track Name': track['name'],
    'Artist': track['artists'][0]['name'],
    'Album': track['album']['name'],
    'Popularity': track['popularity'],
    'Duration (minutes)': track['duration_ms']/60000

}

#Display metadata
print(f"\nTrack name: {track_data['Track Name']}")
print(f"\nArtist: {track_data['Artist']}")
print(f"\nAlbum: {track_data['Album']}")
print(f"\nPopularity: {track_data['Popularity']}")
print(f"\nDuration: {track_data['Duration (minutes)']:.2f}minutes")

#convert metadata to DataFrame
df=pd.DataFrame([track_data])
print("\nTrack Data as DataFrame:")
print(df)

#Save metadata to csv 
df.to_csv( 'spotify_track_data.csv', index=False)

#Visualize Track data
features = ['Popularity', 'Duration (minutes)']
values = [track_data['Popularity'], track_data['Duration (minutes)']]

plt.figure(figsize=(8, 5))
plt.bar(features, values, color='skyblue', edgecolor='black')
plt.title(f"Track Metadata for '{track_data['Track Name']}'")
plt.ylabel('Value')
plt.show()