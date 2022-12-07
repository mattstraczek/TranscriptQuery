#connect db
#query DB to get the transcript col
#get the trancripts with the correct queries and results

import sqlite3
from dataFormatter import *
import sys

# /Users/heetparikh/Desktop/TranscriptQuery/
con = sqlite3.connect("back-end/data/project.db") 
c = con.cursor()

#ChannelName
#DateRange
#Query
ChannelName = "SpaceX"
DataRangeStart = "2022"
DateRangeEnd = "2016"
query = "Music"

query = sys.argv[1]
ChannelName = sys.argv[2]
DataRangeStart = sys.argv[3]
DateRangeEnd = sys.argv[4]

sqlQuery = "SELECT Link, VideoName, Transcript FROM Users WHERE ChannelName =" + "'" + ChannelName + "'" + " AND " + "Transcript like"+ "'" + "%" + query + "%' LIMIT 1"
# print(sqlQuery)
# print(sqlQuery)

c.execute(sqlQuery)
# c.execute('''SELECT Link, VideoName, Transcript FROM Users WHERE ChannelName = ? ''',(ChannelName))
con.commit()
rows = c.fetchall()

for row in rows:
    actualData = row[2]
    splitData = actualData.split(",")
    print(len(splitData))

con.close()