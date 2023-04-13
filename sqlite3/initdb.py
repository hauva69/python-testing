#!/usr/bin/python3

'''
Init the database.
'''

import logging
import sqlite3

logging.basicConfig(level=logging.INFO)

DB_NAME = 'requests.db'

def _get_connection():
    return sqlite3.connect(DB_NAME)

def _main():
    conn = _get_connection()
    cursor = conn.cursor()
    sql = '''CREATE TABLE requests(UID, RESPONSIBILITY, PRIMARY_POSITION, CREATED)'''

    try:
        cursor.execute(sql)
    except sqlite3.OperationalError as ex:
        logging.warning(ex)

    cursor.close()
    conn.close()

if __name__ == '__main__':
    _main()
