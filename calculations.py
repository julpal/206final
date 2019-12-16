import sqlite3
import json

#get connection and cursor for database
conn = sqlite3.connect('final_project.sqlite')
curr = conn.cursor()

#creates new table of spotify data from JOIN
curr.execute("""CREATE TABLE spotify AS
            SELECT tracks.track, tracks.uri, tracks.popularity, audio.danceability, audio.tempo
            FROM tracks
            INNER JOIN audio ON tracks.uri=audio.uri; 
""")

#SPOTIFY CALCULATIONS
#create empty list
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




#YELP CALCULATIONS

#finds number of restaurants with the respective ratings
curr.execute("SELECT rating FROM restaurants")
result = curr.fetchall()

count3 = 0
count35 = 0
count4 = 0
count45 = 0
for x in result:
    if x[0] == 3:
        count3 += 1
    if x[0] == 3.5:
        count35 += 1
    if x[0] == 4:
        count4 +=1
    if x[0] == 4.5:
        count45 +=1



#finds whether restaurants have many, some, or not many reviews
curr.execute("SELECT review_count FROM reviews")
result2 = curr.fetchall()

many_reviews = 0
some_reviews = 0
not_many = 0
for x in result2:
    if x[0] > 500:
        many_reviews += 1
    if x[0] >= 100 and x[0] < 500:
        some_reviews += 1
    if x[0] < 100:
        not_many +=1




#writes calculations out to a file
with open('calculations.txt', 'w') as f: 
    #spotify 
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
    f.write('\n\n')

    #yelp
    f.write('Ratings\n')
    f.write('Rating, Count\n')
    for x in result:
        rating = x[0]
        if x[0] == 3:
            count = count3
        if x[0] == 3.3:
            count = count35
        if x[0] == 4:
            count = count4
        if x[0] == 4.5:
            count = count45
        f.write('{},{}\n'.format(rating, count))
    f.write('\n\n')
    f.write('Numner of Reviews\n')
    f.write('Review Count, Review Amount\n')
    for x in result2:
        review_count = x[0]
        if x[0] > 500:
            reviews = 'many reviews'
        if x[0] >= 100 and x[0] < 500:
            reviews = 'some reviews'
        if x[0] < 100:
            reviews = 'not many reviews'
        f.write('{},{}\n'.format(review_count, reviews))
    f.write('\n\n')




conn.commit()
conn.close()