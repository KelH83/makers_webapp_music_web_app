"""
POST /albums
Parameters:
    title=Voyage
    release_year=2022
    artist_id=2
Expected response (200 OK)
"""
def test_post_album(web_client):
    response = web_client.post('/albums', data={'title':'Voyage','release_year':'2022','artist_id':'2'})
    assert response.status_code == 200

"""
GET /artists
Parameters:None
Expected response (200 OK)
"""
def test_get_artists(web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    expected_output = '["Artist(Name:Pixies, Genre:Indie)","Artist(Name:Abba, Genre:Pop)","Artist(Name:Taylor Swift, Genre:Pop)","Artist(Name:Nina Simone, Genre:Jazz)"]'
    actual_output = response.data.decode('utf-8').strip()
    assert expected_output == actual_output

"""
POST /artists
Parameters:
    name=Wild nothing
    genre=Indie
Expected response (200 OK)
"""
def test_post_artist(web_client):
    response = web_client.post('/artists', data={'name':'Wild nothing','genre':'Indie'})
    assert response.status_code == 200

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    expected_output = '["Artist(Name:Pixies, Genre:Indie)","Artist(Name:Abba, Genre:Pop)","Artist(Name:Taylor Swift, Genre:Pop)","Artist(Name:Nina Simone, Genre:Jazz)","Artist(Name:Wild nothing, Genre:Indie)"]'
    actual_output = get_response.data.decode('utf-8').strip()
    assert expected_output == actual_output