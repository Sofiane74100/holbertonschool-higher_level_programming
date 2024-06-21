#!/usr/bin/python3
"""
lists all states with a name starting with N from the database
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'\
                   ORDER BY id ASC")
    stats = cursor.fetchall()
    for stat in stats:
        if stat[1].startswith("N"):
            print(stat)
    cursor.close()
    connection.close()