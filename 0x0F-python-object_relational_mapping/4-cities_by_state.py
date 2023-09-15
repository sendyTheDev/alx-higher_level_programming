#!/usr/bin/python3
"""
Lists all cities of the database hbtn_0e_4_usa, sorted in ascending and
order by cities.id.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
      host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
      port=3306)

    c = db.cursor()
    c.execute("""
      SELECT
         states.name,
         cities.id,
         cities.name
      FROM
         cities
         INNER JOIN
            states
            ON cities.state_id = states.id
      ORDER BY
         cities.id ASC
      """)
    for row in c.fetchall():
        print(row)
