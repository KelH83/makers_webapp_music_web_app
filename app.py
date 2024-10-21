import os
from flask import Flask, request
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.database_connection import get_flask_database_connection
from lib.artist import Artist
from lib.artist_repository import ArtistRepository

app = Flask(__name__)

@app.route('/albums', methods=['POST'])
def post_album():
    connection = get_flask_database_connection(app) 
    title = request.form['title']
    release_year = request.form['release_year']
    artist = request.form['artist_id']
    repository = AlbumRepository(connection)

    repository.create(Album(artist, title, release_year))

    return 'Created'

@app.route('/artists', methods=['GET'])
def get_artist():
    connection = get_flask_database_connection(app) 
    repository = ArtistRepository(connection)
    all_artists = repository.all()
    return_list = []
    for artist in all_artists:
        return_list.append(str(artist))
        print('HERE: ',return_list)
    return return_list

@app.route('/artists', methods=['POST'])
def post_artist():
    connection = get_flask_database_connection(app) 
    name = request.form['name']
    genre = request.form['genre']
    repository = ArtistRepository(connection)

    repository.create(Artist(name, genre))

    return 'Created'


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

