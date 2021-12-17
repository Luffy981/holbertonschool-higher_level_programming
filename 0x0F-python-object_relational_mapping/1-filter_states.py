#!/usr/bin/python3
from sys import argv
import MySQLdb


def connectDB():
    try:
        db_connection = MySQLdb.connect(host="localhost", port=3306,
                                        user=argv[1], password=argv[2],
                                        db=argv[3], charset="utf8")
    except:
        print("Can't connect to database")
        return 0
    print("Connected...")
    cur = db_connection.cursor()
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db_connection.close()


connectDB()
