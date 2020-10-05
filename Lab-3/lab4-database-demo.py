#!/usr/bin/env python3
# built on tutorial: scienceprog.com/working-with-sqlite-in-raspberry-pi-using-python-3/
import sqlite3

#some initial data
id = 4
temperature = 0.0
date = '2014-01-05'
#connect to database file
dbconnect = sqlite3.connect("my.db")


#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
# dbconnect.row_factory = sqlite3.Row
cursor = dbconnect.cursor()
cursor.execute("CREATE TABLE temperature(id INTEGER PRIMARY KEY, temp TEXT, date DATETIME)")

for i in range(10):
    #execute insert statement
    id += 1
    temperature += 1.1
    cursor.execute("insert into temperature values (?, ?, ?)",(id, temperature, date))

dbconnect.commit()
#print data
for row in cursor.execute('SELECT * FROM temperature'):
    print(row)


#close the connection
dbconnect.close()

# New Code for Lab3
def create_sensor(conn, sensor):
    """
    Create a new row in sensors table
    :param conn: Connection object
    :param sensor: tuple (type, zone)
    :return:
    """
    curs = conn.cursor()
    curs.execute("INSERT INTO sensors (type, zone) VALUES(?,?)", sensor)


# establish connection
conn = sqlite3.connect("my.db")
cursor = conn.cursor()

# create new table in database
cursor.execute("CREATE TABLE IF NOT EXISTS  sensors(sensorID INTEGER PRIMARY KEY, type TEXT, zone TEXT)")

# Add rows to sensors table
create_sensor(conn, ("door", "kitchen"))
create_sensor(conn, ("temperature", "kitchen"))
create_sensor(conn, ("door", "garage"))
create_sensor(conn, ("motion", "garage"))
create_sensor(conn, ("temperature", "garage"))

for row in cursor.execute('SELECT * FROM sensors'):
    print(row)

conn.commit()
conn.close()
