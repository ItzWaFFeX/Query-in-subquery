import sqlite3 

database = 'database (2).sqlite'

conn = sqlite3.connect(database)

print('Its Skibidi')

import pandas as pd

tables = pd.read_sql("""
     SELECT * FROM sqlite_master WHERE type = "table";
""",conn)

print(tables)



teams = pd.read_sql("""
SELECT * FROM Team;
""",conn)

team_name = pd.read_sql("""
SELECT Team_Name AS CLUBS FROM Team;
""",conn)

print(teams)


season = pd.read_sql("""
SELECT * FROM Season;
""",conn)


Batsman_Scored = pd.read_sql("""
SELECT Match_Id, Runs_Scored as Total_Runs
From Batsman_Scored WHERE Total_Runs > 5 AND Match_Id IN
(SELECT Match_Id FROM Match WHERE Season_Id == 8);

""",conn)

match = pd.read_sql("""
SELECT Match_Id FROM Match WHERE Season_Id == 8;
""",conn)

print(match)



print (Batsman_Scored)








