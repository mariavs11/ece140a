SELECT AVG(speechiness),artist
FROM Songs
GROUP BY artist
HAVING COUNT(SongName) > 3;
