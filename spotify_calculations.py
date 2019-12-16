import sqlite3
import json

#get connection and cursor for database
conn = sqlite3.connect('final_project.sqlite')
curr = conn.cursor()

# #creates new table of spotify data from JOIN
# curr.execute("""CREATE TABLE spotify AS
#             SELECT tracks.track, tracks.uri, tracks.popularity, audio.danceability, audio.tempo
#             FROM tracks
#             INNER JOIN audio ON tracks.uri=audio.uri; 
# """)


#create empty dictionary
song_list = []

#SELECT items from new joined table and add to dictionary
spotify_data = conn.execute("SELECT uri, track, popularity, danceability, tempo from spotify")

#create a list of used uris
saved_uris = []

#iterates through pieces of data from new spotify table and adds to python dictionary
for row in spotify_data:
    uri = row[0]
    name = row[1]
    popularity = row[2]
    tempo = row[4]

    if uri not in saved_uris:
        song_dict = {'name': name, 'popularity':int(popularity), 'tempo':int(tempo)}
        song_list.append(song_dict)
        saved_uris.append(uri)

#gets top 10 and bottom 10 songs based on popularity stat
top_15_songs = sorted(song_list, key=lambda x: x['popularity'], reverse=True)[0:16]
bottom_15_songs = sorted(song_list, key=lambda x: x['popularity'])[0:16]

#finds average tempo of most popular songs
total_tempo_top = 0
for dic in top_15_songs:
    total_tempo_top += dic['tempo']
average_tempo_top = total_tempo_top / 15

#finds average tempo of least popular songs
total_tempo_bottom = 0
for dic in bottom_15_songs:
    total_tempo_bottom += dic['tempo']
average_tempo_bottom = total_tempo_bottom / 15


#writes calculations out to a file
with open('spotify_calculations.txt', 'w') as f:
    f.write('Top\n')
    f.write('Name, Popularity, Tempo\n')
    for song in top_15_songs:
        name = song['name']
        popularity = str(song['popularity'])
        tempo = str(song['tempo'])
        f.write('{},{},{}\n'.format(name, popularity, tempo))
    f.write('Average Tempo for Top 15 Songs: ' + str(average_tempo_top))
    f.write('\n\n')

    f.write('Bottom\n')
    f.write('Name, Popularity, Tempo\n')
    for song in bottom_15_songs:
        name = song['name']
        popularity = str(song['popularity'])
        tempo = str(song['tempo'])
        f.write('{},{},{}\n'.format(name, popularity, tempo))
    f.write('Average Tempo for Bottom 15 Songs: ' + str(average_tempo_bottom))




conn.commit()
conn.close()