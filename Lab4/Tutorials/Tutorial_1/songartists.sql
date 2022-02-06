USE Lab4_songs;

CREATE TABLE Songs_artist (
    id		INT NOT NULL auto_increment,
    song		VARCHAR(100) NOT NULL,
    artist 		VARCHAR(100) NOT NULL,
    primary key (id)
);

