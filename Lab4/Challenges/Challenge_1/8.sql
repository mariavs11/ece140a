SELECT COUNT(SongName) FROM Songs
WHERE tempo > (
    SELECT AVG(tempo)
    FROM Songs
);
