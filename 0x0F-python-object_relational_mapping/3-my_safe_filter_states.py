#!/usr/bin/python3
"""Module containing script for safely displaying states table"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = '%s' ORDER BY id ASC",
                [sys.argv[4]])
    query_rows = cur.fetchall()
    for row in query_row:
        print(row)

    cur.close()
    conn.close()
