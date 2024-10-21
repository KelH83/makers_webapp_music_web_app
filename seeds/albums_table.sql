-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS books;
DROP SEQUENCE IF EXISTS books_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS books_id_seq;
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_name VARCHAR(255)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO books (title, author_name) VALUES ('Invisible Cities', 'Italo Calvino');
INSERT INTO books (title, author_name) VALUES ('The Man Who Was Thursday', 'GK Chesterton');
INSERT INTO books (title, author_name) VALUES ('Bluets', 'Maggie Nelson');
INSERT INTO books (title, author_name) VALUES ('No Place on Earth', 'Christa Wolf');
INSERT INTO books (title, author_name) VALUES ('Nevada', 'Imogen Binnie');

DROP TABLE IF EXISTS albums;

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year int,
    artist_id int
);

INSERT INTO albums (title, release_year, artist_id) VALUES ('Vulgar display of power', 1992, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Cowboys from hell', 1990, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Follow the leader', 1998, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Untouchables', 2002, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Bloody kisses', 1993, 3);