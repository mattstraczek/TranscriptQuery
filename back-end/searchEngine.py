#connect db
#query DB to get the transcript col
#get the trancripts with the correct queries and results

import sqlite3
from dataFormatter import *
import sys

# /Users/heetparikh/Desktop/TranscriptQuery/
con = sqlite3.connect("/Users/vrushpatel/Desktop/TranscriptQuery/back-end/data/project.db") 
c = con.cursor()

#ChannelName
#DateRange
#Query
ChannelName = "SpaceX"
DataRangeStart = "2022"
DateRangeEnd = "2016"
query = "great to be"

# query = sys.argv[1]
# ChannelName = sys.argv[2]
# DataRangeStart = sys.argv[3]
# DateRangeEnd = sys.argv[4]

sqlQuery = "SELECT Link, VideoName, Transcript FROM Users WHERE ChannelName =" + "'" + ChannelName + "'" + " AND " + "Transcript like"+ "'" + "%" + query + "%' LIMIT 100"
# print(sqlQuery)
# print(sqlQuery)

c.execute(sqlQuery)
# c.execute('''SELECT Link, VideoName, Transcript FROM Users WHERE ChannelName = ? ''',(ChannelName))
con.commit()
rows = c.fetchall()

for row in rows:
    actualData = row[2]
    # print(actualData[1])
    splitData = actualData.split("; ")
    # print(splitData[0])
    query = query.lower()
    videoLinkList = []
    myDict = {}
    timestampsList = [] 
    for i in splitData:
        if query in i:
            timestampsList.append(i[1:i.find(',')])
    myDict[row[0]] = timestampsList
    print(myDict)
con.close()