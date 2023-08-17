-- Script that uses the hbtn_0d_tvshows database to list all genres not linked

SELECT
  DISTINCT `name`
FROM
  `tv_genres` AS n
  INNER JOIN `tv_show_genres` AS s ON n.`id` = s.`genre_id`
  INNER JOIN `tv_shows` AS t ON s.`show_id` = t.`id`
WHERE
  n.`name` NOT IN (
    SELECT
      `name`
    FROM
      `tv_genres` AS n
      INNER JOIN `tv_show_genres` AS s ON g.`id` = s.`genre_id`
      INNER JOIN `tv_shows` AS t ON s.`show_id` = t.`id`
    WHERE
      t.`title` = "Dexter"
  )
ORDER BY
  n.`name`;
