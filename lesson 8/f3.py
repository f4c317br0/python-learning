import sqlite3

con = sqlite3.connect('music_db.sqlite')
cur = con.cursor()
# films_db.sqlite
result = cur.execute("""SELECT DISTINCT album.title
FROM album
INNER JOIN track ON album.AlbumId = track.AlbumId
INNER JOIN genre ON track.GenreId = genre.GenreId
WHERE genre.Name = ?
ORDER BY album.ArtistId, album.title""", (input(),)).fetchall()
for elem in result:
    print(elem[0])

con.close()