class Album:
    def __init__(self, artist_id, title, release_year, id=None):
        self.artist_id = artist_id
        self.title = title
        self.release_year = release_year
        self.id = id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Album(Title:{self.title}, Release year:{self.release_year}, Artist ID:{self.artist_id})"