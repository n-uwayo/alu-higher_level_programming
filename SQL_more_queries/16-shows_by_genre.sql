-- Lists all shows and genres linked to the show from the
-- database hbtn_0d_tvshows.
-- Records are ordered by ascending show title and genre name.
SELECT s.title, g.name
FROM tv_shows s LEFT OUTER JOIN tv_show_genres sg
  ON s.id = sg.show_id
  LEFT OUTER JOIN tv_genres g
  ON sg.genre_id = g.id
ORDER BY s.title, g.name;

