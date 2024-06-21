#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table
 of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]
    connection = MySQLdb.connect(host="localhost", port=3306, user=username,
                                 passwd=password, db=database)
    cursor = connection.cursor()
    query = ("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY\
              id ASC".format(state_name))
    cursor.execute(query)
    states = cursor.fetchall()
    for value in states:
        print(value)
    cursor.close()
    connection.close()