import json
import requests
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

conn = sqlite3.connect('new_yelp.sqlite')
curr = conn.cursor()

curr.execute("SELECT rating FROM restaurants")

result = curr.fetchall()

# for x in result:
#     print (x[0])


#finds number of restaurants with the respective ratings
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

print("There are " + str(count3) + " 3 star restaurants in Ann Arbor")
print("There are " + str(count35) + " 3.5 star restaurants in Ann Arbor")
print("There are " + str(count4) + " 4 star restaurants in Ann Arbor")
print("There are " + str(count45) + " 4.5 star restaurants in Ann Arbor")





curr.execute("SELECT review_count FROM reviews")

result2 = curr.fetchall()

# for x in result2:
#     print (x[0])


#finds whether restaurants have many, some, or not many reviews
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

print(str(many_reviews) + " restaurants in Ann Arbor have more than 500 reviews.")
print(str(some_reviews) + " restaurants in Ann Arbor have more than 100 reviews.")
print(str(not_many) + " restaurants in Ann Arbor have less than 100 reviews.")





# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()


ratings = ('3', '3.5', '4', '4.5')
y_pos = np.arange(len(ratings))
restaurants = (count3, count35, count4, count45)


error = np.random.rand(len(ratings))

ax.barh(y_pos, restaurants, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(ratings)
ax.invert_yaxis() 
ax.set
ax.set_ylabel("Rating")
ax.set_xlabel('Number of Restaurants')
ax.set_title('Ann Arbor Restaurant Ratings')

ax.barh(y_pos, restaurants, color=('red', 'green', 'yellow', 'blue'))

plt.show()


# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
number_reviews = ('<100', '100-500', '<500')
y_pos = np.arange(len(number_reviews))
restaurants = (not_many, some_reviews, many_reviews)

error = np.random.rand(len(number_reviews))

ax.barh(y_pos, restaurants, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(number_reviews)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_ylabel("Number of Reviews")
ax.set_xlabel('Number of Restaurants')
ax.set_title('Ann Arbor Restaurant Review Count')

ax.barh(y_pos, restaurants, color=('red', 'green', 'yellow'))

plt.show()




with open('spotify_calculations.txt', 'w') as f:  
    f.write('Ratings\n')
    f.write('Rating, Count\n')
    for x in results:
        rating = x[0]
        if x[0] == 3:
            count = count3
        if x[0] == 3.3:
            count = count35
        if x[0] == 4:
            count = count4
        if x[0] == 4.5:
            count = count45
    f.write('{},{},{}\n'.format(rating, count))
    f.write('There are '+ str(count3) + ' 3 star restaurants in Ann Arbor')
    f.write('There are '+ str(count35) + ' 3.5 star restaurants in Ann Arbor')
    f.write('There are '+ str(count4) + ' 4 star restaurants in Ann Arbor')
    f.write('There are '+ str(count45) + ' 4.5 star restaurants in Ann Arbor')
    f.write('\n\n')











