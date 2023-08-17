-- script that lists all genres in the database hbtn_0d_tvshows_rate

SELECT
  `name`,
  SUM(`rate`) AS `rating`
FROM
  `tv_genres` AS n
  INNER JOIN `tv_show_genres` AS s ON s.`genre_id` = n.`id`
  INNER JOIN `tv_show_ratings` AS r ON r.`show_id` = s.`show_id`
GROUP BY
  `name`
ORDER BY
  `rating` DESC;
