-- Script that lists all shows from hbtn_0d_tvshows_rate by their rating

SELECT
  DISTINCT `title`
FROM
  `tv_shows` AS t
  LEFT JOIN `tv_show_genres` AS s ON s.`show_id` = t.`id`
  LEFT JOIN `tv_genres` AS n ON n.`id` = s.`genre_id` 
WHERE
  t.`title` NOT IN (
    SELECT
      `title`
    FROM
      `tv_shows` AS t
      INNER JOIN `tv_show_genres` AS s ON s.`show_id` = t.`id`
      INNER JOIN `tv_genres` AS n ON n.`id` = s.`genre_id`
    WHERE
      n.`name` = "Comedy"
  )
ORDER BY
  `title`;
