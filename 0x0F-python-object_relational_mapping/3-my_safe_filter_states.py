#!/usr/bin/python3
"""Module containing script for safely displaying states table"""

import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]

    cur.close()
    conn.close()
