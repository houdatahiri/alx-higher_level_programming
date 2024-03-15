#!/usr/bin/python3
""" lists all state from db """
import MYSQLdb
import sys


if __name__ == "__main__":
     b = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
     cur = db.cursor()
     cur.execute("Select * FROM states")
     rows = cur.fetchall()
     for row in rows:
	 print (row)
     cur.close()
     db.close()
