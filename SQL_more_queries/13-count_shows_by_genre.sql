-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- Displays: <TV Show genre> - <Number of shows linked to this genre>
-- Only genres with at least one show linked are listed
-- Results sorted by the number of shows linked in descending order
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
