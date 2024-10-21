from lib.artist_repository import ArtistRepository
from lib.artist import Artist


def test_get_all_artists(db_connection): 
    db_connection.seed("seeds/albums_table.sql") 
    repository = ArtistRepository(db_connection) 

    artists = repository.all() 

    assert artists == [
        Artist('Pixies', 'Indie'),
        Artist('Abba', 'Pop'),
        Artist('Taylor Swift', 'Pop'),
        Artist('Nina Simone', 'Jazz')
    ]


def test_create_artist(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = ArtistRepository(db_connection)

    repository.create(Artist("Slayer", "Metal"))

    result = repository.all()
    assert result == [
        Artist('Pixies', 'Indie'),
        Artist('Abba', 'Pop'),
        Artist('Taylor Swift', 'Pop'),
        Artist('Nina Simone', 'Jazz'),
        Artist('Slayer', 'Metal')
    ]
