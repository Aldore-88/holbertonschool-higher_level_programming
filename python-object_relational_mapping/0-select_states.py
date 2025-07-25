#!/usr/bin/python3
"""0.Get all states"""

import MySQLdb
import sys

"""hello"""

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd="",
    db=sys.argv[3]
    )
"""here?"""
cur = db.cursor()
"""here?"""
cur.execute("SELECT * FROM states ORDER BY id ASC;")
rows = cur.fetchall()
for row in rows:
    print(row)
"""here?"""
cur.close()
db.close()
