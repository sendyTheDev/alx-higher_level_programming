#!/usr/bin/python3
"""
List all cities of a given state from the database hbtn_0e_4_usa, sorted in
ascending order by cities
"""
import sys
import MySQLdb

if __name__ == "__main__":
    state = sys.argv[4]

    db = MySQLdb.connect(
      host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
      port=3306)

    c = db.cursor()
    c.execute("""
        SELECT
            *
        FROM
            cities
            INNER JOIN
                states
                ON cities.state_id = states.id
        ORDER BY
            cities.id ASC
    """)

    # Output.
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == state]))
