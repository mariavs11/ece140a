USE Lab4_songs;
CREATE TABLE Songs_data (
    id			INT NOT NULL auto_increment,
    SongName		VARCHAR(100) NOT NULL,
    danceability	      DECIMAL(10,3) NULL,
    energy			DECIMAL(10,3) NULL,
    loudness		decimal(10,3) NULL,
    speechiness		decimal(10,5) NULL,
    acousticness	      decimal(10,7) NULL,
    liveness		decimal(10,5) NULL,
    valence			decimal(10,5) NULL,
    tempo			decimal(10,3) NULL,
    duration_ms		integer NULL,
    time_signature	integer NULL,
    primary key (id)
);





