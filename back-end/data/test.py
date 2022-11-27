import sqlite3


con = sqlite3.connect("project.db")
c = con.cursor()
# c.execute("""CREATE TABLE Users (
#             first text,
#             pay integer
#             )""")
# c.execute("INSERT INTO Users VALUES ('Matt', 50000)")
# con.commit()
c.execute("SELECT * FROM Users")
con.commit()
con.close()