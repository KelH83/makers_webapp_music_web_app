from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    # Read
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["title"], row["release_year"],row["artist_id"])
            albums.append(item)
        return albums

    # Create 
    def create(self, album):
        self._connection.execute('INSERT INTO albums (artist_id,title, release_year) VALUES (%s, %s, %s)', [
                        album.artist_id,album.title, album.release_year])
        return None
