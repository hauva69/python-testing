#!/usr/bin/python3

'''Testing sqlite3 module'''

import logging
import sqlite3

logging.basicConfig(level=logging.DEBUG)

DB_NAME = 'tutorial.db'
CREATE_SQL = 'CREATE TABLE movie(title, year, score)'
INSERT_SQL = """
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
"""
SELECT_SQL = "SELECT score FROM movie"

def _main():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute(CREATE_SQL)
    except sqlite3.OperationalError as ex:
        logging.warning(ex)
    result = cursor.execute("SELECT name FROM sqlite_master WHERE name = 'spam'")
    logging.info('result=%s', result.fetchone())
    cursor.execute(INSERT_SQL)
    conn.commit()
    result = cursor.execute(SELECT_SQL)
    logging.info(result.fetchall())

if __name__ == '__main__':
    _main()
