import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
# films_db.sqlite
result = cur.execute("""SELECT title FROM films WHERE duration <= 85""").fetchall()
for elem in result:
    print(elem[0])
con.close()
