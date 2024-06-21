#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    data = argv[3]
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=username, passwd=password, db=data)
    cursor = connection.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                   JOIN states ON cities.state_id = states.id\
                   ORDER BY cities.id ASC")
    states = cursor.fetchall()
    for values in states:
        print(values)
    cursor.close()
    connection.close()
    