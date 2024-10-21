
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

DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    genre VARCHAR(255)
    
);

INSERT INTO artists (name, genre) VALUES ('Pixies', 'Indie');
INSERT INTO artists (name, genre) VALUES ('Abba', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Taylor Swift', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Nina Simone', 'Jazz');
