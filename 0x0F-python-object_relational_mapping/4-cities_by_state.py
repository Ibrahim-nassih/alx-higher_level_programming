#!/usr/bin/python3
"""
All cities in the database hbtn_0e_4_usa are listed in this module.
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id,cities.name,states.name FROM cities\
                LEFT JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
