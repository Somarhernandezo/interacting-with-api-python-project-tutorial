import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import seaborn as sns
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()

# Get credential values

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
print(f'El ID es: {client_id}')

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

id_artista = '5K4W6rqBFWDnAN6FQUkS6x'

results = spotify.artist_top_tracks(artist_id=id_artista)
canciones = []

for track in results['tracks']:
    canciones.append(
        {'name':track['name'],
        'popularity' : track['popularity'],
        'duration_min': track['duration_ms'] / 60000}
    )

tracks_df = pd.DataFrame(canciones)

print(tracks_df.head(3))

plt.scatter(tracks_df['duration_min'], tracks_df['popularity'])
plt.xlabel('Duration (minutes)')
plt.ylabel('Popularity')
plt.title('Relationship between duration and popularity')
plt.show()
