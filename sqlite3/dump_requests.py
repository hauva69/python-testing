#!/usr/bin/python3

'''
Dump the request database to the standard output.
'''

import logging
import pathlib
import sqlite3
# import sys

logging.basicConfig(level=logging.DEBUG)

DB_NAME = pathlib.Path('/tmp/db', 'requests.db')

def _get_connection():
    return sqlite3.connect(DB_NAME)

def _main():
    conn = _get_connection()
    cursor = conn.cursor()
    sql = 'SELECT uid, responsibility, primary_position, created FROM requests ORDER BY created, uid DESC' # pylint: disable=line-too-long
    cursor.execute(sql)

    while True:
        result = cursor.fetchone()
        if not result:
            break
        print(f'{result[0]};{result[1]};{result[2]};{result[3]}')

    cursor.close()
    conn.close()

if __name__ == '__main__':
    _main()
