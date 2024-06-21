#!/usr/bin/python3
"""takes in the name of a state as an argument
 and lists all cities of that state
, using the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    data = argv[3]
    state_name = argv[4]
    connection = MySQLdb.connect(host="localhost", port=3306, user=username,
                                 passwd=password, db=data)
    cursor = connection.cursor()
    cursor.execute("SELECT cities.name FROM cities INNER JOIN states ON\
                cities.state_id=states.id WHERE states.name = %s\
                    ORDER BY cities.id ASC", (state_name,))
    states = cursor.fetchall()
    for index, state in enumerate(states):
        if index < len(states) - 1:
            print('{}, '.format(state[0]), end="")
        else:
            print('{}'.format(state[0]), end="")
    print()
    cursor.close()
    connection.close()
    