<!-- Single Table Design Recipe Template -->

## 1. Extract nouns from the user stories or specification

```
As a music lover,
So I can organise my records,
I want to keep a list of albums' titles.
Albums > title

As a music lover,
So I can organise my records,
I want to keep a list of albums' release years.
Albums > release_year
```

```
Nouns:

Albums, title, release year
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| Albums                | title, release year |

Name of the table (always plural): `albums`

Column names: `title`, `release_year`

## 3. Decide the column types

```
# EXAMPLE:

id: SERIAL
title: VARCHAR(255)
release_year: int
```

## 4. Write the SQL

```sql
-- file: albums_table.sql

-- Replace the table name, column names and types.

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  release_year int
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 music_web < albums_table.sql
```

<!-- Plain Route Design Recipe -->

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)
```

## 2. Create Examples as Tests


```python
# EXAMPLE

# POST /albums
#  Expected response (200 OK):
"""
Adds an album
"""
```

## 3. Test-drive the Route

```python

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
```

