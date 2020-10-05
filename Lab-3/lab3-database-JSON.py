import requests
import json
import sqlite3
from sqlite3 import DatabaseError

# The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa


# As of October 2015, you need an API key.
# I have registered under my Carleton email.
apiKey = "a808bbf30202728efca23e099a4eecc7"

# Query the user for a city
city = input("Enter the name of a city whose weather you want: ")

# Build the URL parameters
payload = {"q":city, "units":"imperial", "APPID":apiKey }


# Get the weather information
r = requests.get("http://api.openweathermap.org/data/2.5/weather", params=payload)

print (r.url)

# Get data as json dictionary
data = r.json()

print (data)

# Print the results

current = data["main"]
degreeSym = chr(176)

temperature = current["temp"]
humidity = current["humidity"]
pressure = current["pressure"]

print ("Temperature: %d%sF" % (temperature, degreeSym ))
print ("Humidity: %d%%" % humidity)
print ("Pressure: %d" % pressure )

current = data["wind"]
print ("Wind : %d" % current["speed"])

# establish connection
conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()


# create new table in database
cursor.execute("CREATE TABLE IF NOT EXISTS weather (id INTEGER PRIMARY KEY, city TEXT, temperature INTEGER, humidity INTEGER, pressure INTEGER, wind INTEGER)")

# insert data into table
values = (city, temperature , humidity, pressure, current["speed"])
cursor.execute("INSERT INTO weather(city, temperature, humidity, pressure, wind) VALUES(?,?,?,?,?)", values)
for row in cursor.execute('SELECT * FROM weather'):
    print(row)
conn.commit()
conn.close()