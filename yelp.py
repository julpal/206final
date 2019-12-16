import json
import requests
import sqlite3


api_key = 'YgZQoqt8gAna0G0koZRFZrCoUgDOA14QK3zMYEYfgEzwzbtLqXRuanUqQdtlnqjQtRRhpNx1E-KBnyQrAqtSsjaH1-GI-Bi0DdqApdgcUbuIz6cj4SwnAcXoSUXlXXYx'
url = 'https://api.yelp.com/v3/businesses/search' 

#authorization from Yelp
headers = {'Authorization': 'Bearer %s' % api_key,}

#change the final 'term' each time you run the code to a cuisine of your choice
#limited to 20 results each time
params = {'is_closed': 'false', 'location': 'Ann Arbor', 'limit': 20, 'term': 'restaurants', 'term': 'american'}

#request to the API
req = requests.get(url, params=params, headers=headers)
print(req.status_code)

#turn data into json
parsed = json.loads(req.text)

#prints json
# print(json.dumps(parsed, indent=4))

#prints list of restaurants with their ratings and addresses
businesses = parsed["businesses"]
# for restaurant in businesses:
#     print("Name:", restaurant["name"])
#     print("Rating:", restaurant["rating"])
#     print("Address:", " ".join(restaurant["location"]["display_address"]))



#set up database
conn = sqlite3.connect('final_project.sqlite')
curr = conn.cursor()


# #creates table

# curr.execute("""CREATE TABLE restaurants(
#     name text unique,
#     rating integer,
#     address text
# )""")

results = []

#parses through data to add to table
i = 0
for restaurant in businesses:
    name = businesses[i]['name']
    rating = businesses[i]['rating']
    address = businesses[i]['location']['display_address']
    tup = (str(name), str(rating), str(address))
    results.append(tup)
    i += 1

#inserts data into table
for tup in results:
    curr.execute("INSERT OR REPLACE INTO restaurants VALUES (?,?,?)", tup)




# #creates table

# curr.execute("""CREATE TABLE reviews(
#     name text unique,
#     review_count integer,
#     phone text
# )""")



results2 = []

#parses through data to add to table
i = 0
for restaurant in businesses:
    name = businesses[i]['name']
    review_count = businesses[i]['review_count']
    phone = businesses[i]['phone']
    tup2 = (str(name), str(review_count), str(phone))
    results2.append(tup2)
    i += 1

#inserts data into table
for tup2 in results2:
    curr.execute("INSERT OR REPLACE INTO reviews VALUES (?,?,?)", tup2)


conn.commit()
conn.close
