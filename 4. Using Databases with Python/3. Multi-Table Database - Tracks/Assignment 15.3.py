import sqlite3
import xml.etree.ElementTree as ET


# Function that we'll use to find the content of a specific field.
def find_field(track, wanted_field):
    """This function gets two parameters: track, a dictionary containing all
    the XML tags of a certain song, and wanted_field, a string representing the
    title of the tag we want to obtain.
    It works by finding a key tag with the text {wanted_field}, and
    returning the content of the following tag. If wanted_field doesn't
    match any tag, it returns a False"""

    # Variable we'll use to indicate when we've found wanted_field
    found = False

    for tag in track:
        if not found:
            # Looking for the wanted field
            if(tag.tag == "key" and tag.text == wanted_field):
                found = True
        else:
            # After founding it, we return the content of the following
            # tag (the one with its value)
            return tag.text

    return False


conn = sqlite3.connect('tracks.sqlite')
cur = conn.cursor()

cur.executescript("""
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album; 
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Track
    """)


cur.executescript(''' CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


data_source = open("tracks/Library.xml")
data = data_source.read()
xml_data = ET.fromstring(data)

tracks_data = xml_data.findall("dict/dict/dict")

for track in tracks_data:
    title = find_field(track, "Name")
    artist = find_field(track, "Artist")
    genre = find_field(track, "Genre")
    album = find_field(track, "Album")
    length = find_field(track, "Total Time")
    count = find_field(track, "Play Count")
    rating = find_field(track, "Rating")

    # Artist
    if (artist):
        artist_statement = """INSERT INTO Artist(name) SELECT ? WHERE NOT EXISTS 
            (SELECT * FROM Artist WHERE name = ?)"""
        SQLparams = (artist, artist)
        cur.execute(artist_statement, SQLparams)

    # Genre
    if (genre):
        genre_statement = """INSERT INTO Genre(name) SELECT ? WHERE NOT EXISTS 
            (SELECT * FROM Genre WHERE name = ?)"""
        SQLparams = (genre, genre)
        cur.execute(genre_statement, SQLparams)

    # Album
    if (album):
        artistID_statement = "SELECT id from Artist WHERE name = ?"
        cur.execute(artistID_statement, (artist, ))
        artist_id = cur.fetchone()[0]

        album_statement = """INSERT INTO Album(title, artist_id) 
            SELECT ?, ? WHERE NOT EXISTS (SELECT * FROM Album WHERE title = ?)"""
        SQLparams = (album, artist_id, album)
        cur.execute(album_statement, SQLparams)

    # Track
    if (title):
        genreID_statement = "SELECT id from Genre WHERE name = ?"
        cur.execute(genreID_statement, (genre, ))
        try:
            genre_id = cur.fetchone()[0]
        except TypeError:
            genre_id = 0

        albumID_statement = "SELECT id from Album WHERE title = ?"
        cur.execute(albumID_statement, (album, ))
        try:
            album_id = cur.fetchone()[0]
        except TypeError:
            album_id = 0

        track_statement = """INSERT INTO Track(title, album_id, genre_id, len,
            rating, count) SELECT ?, ?, ?, ?, ?, ?
                WHERE NOT EXISTS (SELECT * FROM Track WHERE title = ?)"""
        SQLparams = (title, album_id, genre_id, length, rating, count, title)
        cur.execute(track_statement, SQLparams)


conn.commit()
cur.close()
