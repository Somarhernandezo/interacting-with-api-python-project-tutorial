import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import seaborn as sns
import spotipy
import spotipy as spotify

# load the .env file variables
load_dotenv()

# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
print(f'El ID es: {client_id}')

# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

id_artista = '2DaxqgrOhkeH0fpeiQq2f4'

results = spotipy.Spotify.artist_top_tracks(self, artist_id=id_artista)
canciones = []

for track in results['tracks']:
    canciones.append(
        {'name':track['name']},
        {'popularity' : track['popularity']}
    )

print(track)