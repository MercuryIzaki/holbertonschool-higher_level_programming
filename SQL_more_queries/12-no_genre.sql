-- Lists all shows contained in hbtn_0d_tvshows without a genre linked
-- Displays: tv_shows.title
-- Results sorted by tv_shows.title
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title ASC;
