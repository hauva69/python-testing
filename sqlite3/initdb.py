#!/usr/bin/python3

'''
Init the database.
'''

import logging
import pathlib
import sqlite3
import sys

logging.basicConfig(level=logging.INFO)

DB_NAME = pathlib.Path('/tmp/db/', 'requests.db')

def _get_connection():
    return sqlite3.connect(DB_NAME)

def _main():
    conn = _get_connection()
    cursor = conn.cursor()
    sql = '''CREATE TABLE requests(UID, ENVIRONMENT, RESPONSIBILITY, PRIMARY_POSITION, CREATED)'''

    try:
        cursor.execute(sql)
    except sqlite3.OperationalError as ex: # pylint: disable=redefined-outer-name
        logging.warning(ex)

    cursor.close()
    conn.close()

if __name__ == '__main__':
    try:
        _main()
    except sqlite3.OperationalError as ex:
        logging.critical(ex)
        sys.exit(1)
