-- SQLite

DROP TABLE IF EXISTS Users;

CREATE TABLE Users(
                ChannelName VARCHAR(255) NOT NULL,
                DateRange VARCHAR(255) NOT NULL,
                VideoName VARCHAR(255) NOT NULL,
                Transcript TEXT(1024) NOT NULL,
                Timestamp TEXT(255) NOT NULL,
                PRIMARY KEY(ChannelName, DateRange)
            );


INSERT INTO Users (ChannelName,DateRange,VideoName, Transcript, Timestamp) 
VALUES('YouTube Channel', '01/01/2022 - 01/01/2023', 'Video Title', 
'Transcript', CURRENT_TIMESTAMP);

SELECT * FROM Users;

-- Storing Data

-- Transcript labeled with Video Name, Time Stamps, 
-- and Strings of the actual transcript.

-- List of tuples (time stamp, phrase) (1:00, cs410 is cool)

-- sqlite3 project.db
-- sqlite> .header on
-- sqlite> .mode column
-- sqlite> .timer on
-- sqlite> SELECT * FROM Users;