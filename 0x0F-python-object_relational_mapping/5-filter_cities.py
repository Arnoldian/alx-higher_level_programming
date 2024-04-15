#!/usr/bin/python3
"""
Module lists all states from hbtn_0e_0_usa db
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)

    check = sys.argv[4]
    c = db.cursor()
    c.execute("SELECT cities.name FROM cities INNER JOIN states 
            ON states.id=cities.state_id WHERE states.name=%s", (check, ))
    rows = c.fetchall()

    for row in rows:
        print(row)

    c.close()
    db.close()
