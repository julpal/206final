import requests
import json
import spotipy
import spotipy.util as util
import sys
import os
import webbrowser
import sqlite3

#Uses client id and client secret to acsess a spotify authorization token
CLIENT_ID = "c3778bbf65c74861b4cd4e4b4338ee2d" 
CLIENT_SECRET = "85f8095f71dd42d68ae94f1a869a7d5d"

grant_type = 'client_credentials'
body_params = {'grant_type' : grant_type}

url = 'https://accounts.spotify.com/api/token'
response = requests.post(url, data=body_params, auth = (CLIENT_ID, CLIENT_SECRET)) 

token_raw = json.loads(response.text)
token = token_raw["access_token"]

#Create spotipy Object
sp = spotipy.Spotify(auth=token)

#establishes connection and creates cursor for database
conn = sqlite3.connect('final_project.sqlite')
curr = conn.cursor()

# # creates table for tracks in database. Comment out after first run of code.
# curr.execute("""CREATE TABLE tracks(
#             track text,
#             uri text unique,
#             album_name text,
#             album_release_date text,
#             artist text,
#             popularity integer
#             ) """)

# #creates table for tracks audio features. Comment out after first run of code.
# curr.execute("""CREATE TABLE audio(
#             uri text unique,
#             danceability integer,
#             tempo integer
#             ) """)


#create an empty list to store items to be stored to database
results_data_list = []

#creates empty list to store uris in
uri_list = []

#search queries: 'christmas', 'winter', 'holiday', 'mistletoe', 'santa', 'xmas'
#get search results for tracks with each search query in the United States. Limits results to 20. Change q parameter each time you run code.
tracks_results = sp.search('xmas', type='track', limit=20, market='US')

#pull pieces of data from API json results for each searched track and appends them in tuple form to results_data_list
for track_dictionary in tracks_results['tracks']['items']:
    track = track_dictionary.get('name', None)
    trackuri = track_dictionary['uri']
    uri_list.append(trackuri)
    album = track_dictionary['album']['name']
    release_date = track_dictionary['album']['release_date']
    artist = track_dictionary['artists'][0]['name']
    popularity = track_dictionary['popularity']
    tup = (track, trackuri, album, release_date, artist, int(popularity))
    results_data_list.append(tup)


#creates an empty list for audio analysis information
audio_features_data = []
for uri in uri_list:
    analysis_results = sp.audio_features(uri)

    danceability = analysis_results[0]['danceability']
    tempo = analysis_results[0]['tempo']
    uri = analysis_results[0]['uri']
    analysis_tup = (uri, danceability, tempo)
    audio_features_data.append(analysis_tup)

#loop through tracks data in results_data_list and add to tracks table in database
for tup in results_data_list:
    curr.execute("INSERT OR REPLACE INTO tracks VALUES (?, ?, ?, ?, ?, ?)", tup)

#loop through tracks data in audio_features_data and add to audio table in database
for tup in audio_features_data:
    curr.execute("INSERT OR REPLACE INTO audio VALUES (?, ?, ?)", tup)

#saves changes to database
conn.commit()
conn.close()