-- lists all shows from hbtn_0d_tvshows_rate by their rating
-- lists all rows of a table by the sul of a linked row
SELECT title, SUM(tv_show_ratings.rate) 'rating'
from tv_shows.id
GROUP BY title
ORDER BY rating DESC;
