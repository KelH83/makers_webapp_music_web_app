import os
from flask import Flask, request
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/albums', methods=['POST'])
def post_album():
    connection = get_flask_database_connection(app) 
    title = request.form['title']
    release_year = request.form['release_year']
    artist = request.form['artist_id']
    repository = AlbumRepository(connection)

    repository.create(Album(artist, title, release_year))

    return 'Created'


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

