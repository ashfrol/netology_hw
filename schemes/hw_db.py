import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost:5432/music2')
# print(engine.table_names())

connection = engine.connect()

# Найти количество исполнителей в каждом жанре;
# sel = connection.execute("""
# SELECT g.name, COUNT(b.id) FROM genre g
# JOIN genreband gb ON g.id = gb.genre_id
# JOIN band b ON gb.band_id = b.id
# GROUP BY g.name;""").fetchall()
# pprint(sel)

# количество треков, вошедших в альбомы 2019-2020 годов;
# sel = connection.execute("""
# SELECT a.name, COUNT(t.id) from track t
# JOIN album a ON t.album_id = a.id
# WHERE a.year >= '01-01-2018' AND year < '01-01-2020'
# GROUP BY a.name;
# """).fetchall()
# pprint(sel)

# средняя продолжительность треков по каждому альбому;
# sel = connection.execute("""
# SELECT a.name, AVG(t.time) from track t
# JOIN album a ON t.album_id = a.id
# GROUP BY a.name;
# """).fetchall()
# pprint(sel)

# все исполнители, которые не выпустили альбомы в 2020 году;
# sel = connection.execute("""
# SELECT b.name FROM band b
# JOIN bandalbum ba ON ba.band_id = b.id
# JOIN album a ON ba.album_id = a.id
# WHERE a.year NOT BETWEEN '01-01-2020' AND '01-01-2021'
# ;
# """).fetchall()
# pprint(sel)

# названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
# sel = connection.execute("""
# SELECT c.name FROM collection c
# JOIN collectiontrack ct ON ct.collection_id = c.id
# JOIN track t ON ct.track_id = t.id
# JOIN album a ON t.album_id = a.id
# JOIN bandalbum ba ON a.id = ba.album_id
# JOIN band b ON ba.band_id = b.id
# WHERE b.name LIKE 'Mordor';
# """).fetchall()
# pprint(sel)

# название альбомов, в которых присутствуют исполнители более 1 жанра;
# sel = connection.execute("""
# SELECT a.name FROM album a
# JOIN bandalbum ba ON a.id = ba.album_id
# JOIN band b ON ba.band_id = b.id
# JOIN genreband gb ON b.id = gb.band_id
# JOIN genre g ON gb.genre_id = g.id
# GROUP BY a.id, b.id
# HAVING COUNT(gb.band_id) > 1
# ;""").fetchall()
# pprint(sel)

# наименование треков, которые не входят в сборники;
# sel = connection.execute("""
# SELECT t.name from track t
# LEFT JOIN collectiontrack ct ON t.id = ct.track_id
# WHERE ct.track_id IS NULL;
# """).fetchall()
# pprint(sel)

# исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
# sel = connection.execute("""
# SELECT b.name FROM band b
# JOIN bandalbum ba ON b.id = ba.band_id
# JOIN album a ON ba.album_id = a.id
# JOIN track t ON a.id = t.album_id
# WHERE t.time = (
#     SELECT MIN(time) FROM track
# );
# """).fetchall()
# pprint(sel)

# название альбомов, содержащих наименьшее количество треков.
# sel = connection.execute("""
# SELECT a.name from album a
# JOIN track t ON a.id = t.album_id
# GROUP BY a.id
# HAVING COUNT(t.album_id) = (
#     SELECT COUNT(t.album_id) from album a
#     JOIN track t ON a.id = t.album_id
#     GROUP BY a.id
#     ORDER BY COUNT(t.album_id) ASC
#     LIMIT 1
# )
# ;
# """).fetchall()
# pprint(sel)
