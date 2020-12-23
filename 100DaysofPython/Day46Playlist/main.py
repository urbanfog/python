import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Retrieve date from user
date = input(
    "What date would you like to generate a playlist for? Please use yyyy-mm-dd format. ")

# Scrape Billboard & generate song_title list
response = requests.get(
    f"https://www.billboard.com/charts/hot-100/{date}").text
soup = BeautifulSoup(response, "html.parser")
songs = soup.find_all(
    name="span", class_="chart-element__information__song text--truncate color--primary")
song_titles = [song.getText() for song in songs]

# Use Spotipy to create playlist based on Billboard Top 100
# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                                               client_secret=os.getenv(
                                                   "SPOTIFY_CLIENT_SECRET"),
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify playlist-modify-private user-read-private",
                                               show_dialog=True))
user_id = sp.current_user()['id']

# Create blank playlist
playlist = sp.user_playlist_create(user=user_id,
                                   name=f"Billboard Top 100: {date}",
                                   public=True,
                                   collaborative=False,
                                   description="A generated playlist from the Billboard Top 100 of a specified date.")

# Search songs and get song uris
song_year = date.split("-")[0]
song_uris = []
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{song_year}", type='track')
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Add tracks to playlist
sp.user_playlist_add_tracks(
    user=user_id, playlist_id=playlist['id'], tracks=song_uris)

# Enjoy
