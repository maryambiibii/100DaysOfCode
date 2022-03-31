import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

CLIENT_ID = yours_ID
CLIENT_SECRET = yours_SECRET
URL = "https://www.officialcharts.com/charts/singles-chart/"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
# Write your code below this line 👇

response = requests.get(URL)
top_100_songs = response.text

soup = BeautifulSoup(top_100_songs, "html.parser")
song_title = soup.findAll(name="div", class_="title")
song_title = [song.getText() for song in song_title]

songs_title_list = [title.strip('\n').title() for title in song_title]
print(songs_title_list)

song_uris = []
for song_name in songs_title_list:
    try:
        searchResults = sp.search(q=f"{song_name}", type="track")
        uri = searchResults['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print("Song Not Found")

print(song_uris)

# Create New Playlist
new_playlist = sp.user_playlist_create(
    user_id,
    'Top 100 Songs of All the Time',
    public=False,
    description='Takes top 100 music and creates Spotify playlist.'
)

# Add items to New Playlist
sp.playlist_add_items(playlist_id=new_playlist['id'], items=song_uris)
