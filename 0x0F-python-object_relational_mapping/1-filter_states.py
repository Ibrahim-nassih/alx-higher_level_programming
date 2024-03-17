#!/usr/bin/python3
"""
Every state in the database hbtn_0e_0_usa is listed in this module.
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE\
             'N%' ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
