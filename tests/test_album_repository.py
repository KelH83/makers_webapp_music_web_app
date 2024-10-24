from lib.album_repository import AlbumRepository
from lib.album import Album


def test_get_all_albums(db_connection): 
    db_connection.seed("seeds/albums_table.sql") 
    repository = AlbumRepository(db_connection) 

    albums = repository.all() 

    assert albums == [
        Album('Vulgar display of power', 1992, 1),
        Album('Cowboys from hell', 1990, 1),
        Album('Follow the leader', 1998, 2),
        Album('Untouchables', 2002, 2),
        Album('Bloody kisses', 1993, 3)
    ]


def test_create_album(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(2, "Korn", 1994))

    result = repository.all()
    assert result == [
        Album('Vulgar display of power', 1992, 1),
        Album('Cowboys from hell', 1990, 1),
        Album('Follow the leader', 1998, 2),
        Album('Untouchables', 2002, 2),
        Album('Bloody kisses', 1993, 3),
        Album("Korn", 1994, 2)
    ]

