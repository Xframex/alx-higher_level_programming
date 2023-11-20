#!/usr/bin/python3
"""name of a state as an argument and lists
    all cities of that state, database hbtn_0e_4_usa]
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states\
                 ON state_id = states.id WHERE states.name = %s ORDER BY\
                 cities.id ASC;", (argv[4],))
    rows = cur.fetchall()
    separator = ', '
    print(separator.join(row[0] for row in rows))
    cur.close()
    db.close()
