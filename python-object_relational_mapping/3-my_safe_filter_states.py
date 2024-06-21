#!/usr/bin/python3
"""takes in arguments and displays all values in the states table
 of hbtn_0e_0_usa where name matches the argument. But this time,
   write one that is safe from MySQL injections!
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    data = argv[3]
    state_name = argv[4]
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=username, passwd=password, db=data)
    cursor = connection.cursor()
    query = ("SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC")
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()
    for values in states:
        print(values)
    cursor.close()
    connection.close()
    