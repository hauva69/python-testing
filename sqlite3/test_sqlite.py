#!/usr/bin/python3

'''
Sqlite testing.
'''

import logging
import os
import os.path
import sqlite3
import unittest

logging.basicConfig(level=logging.DEBUG)

DB_NAME = 'requests.db'

class TestInsert(unittest.TestCase):
    def _get_connection(self):
        return sqlite3.connect(DB_NAME)

    def test_remove(self):
        '''Tests removing the database.'''
        try:
            os.remove(DB_NAME)
        except FileNotFoundError:
             pass

    def test_init_database(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        sql = '''CREATE TABLE requests(UID, RESPONSIBILITY, CREATED)'''
        try:
            cursor.execute(sql)
        except sqlite3.OperationalError:
            pass
        cursor.close()
        conn.close()

    def _test_table_does_not_exist(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        sql = """SELECT uid, responsibility, created FROM requests WHERE uid = 'hauva'"""
        with self.assertRaises(sqlite3.OperationalError):
            cursor.execute(sql)
            result = cursor.fetchone()
        cursor.close()
        conn.close()

    def test_user_exists(self):
        responsibility = 'kändivästüü'
        conn = self._get_connection()
        cursor = conn.cursor()
        sql = '''CREATE TABLE requests(UID, RESPONSIBILITY, CREATED)'''
        cursor.execute(sql)
        sql = """INSERT INTO requests (uid, responsibility, created) VALUES ('hauva', '{0}', current_timestamp)""".format(responsibility)

        try:
            cursor.execute(sql)
            conn.commit()
        except sqlite3.OperationalError as ex:
            logging.error(ex)
        except Exception as ex:
            logging.error(ex)

        # sql = """SELECT uid, responsibility, created FROM requests WHERE uid = 'hauva'"""
        sql = "SELECT * FROM requests"
        cursor.execute(sql)
        result = cursor.fetchall()
        logging.debug('result=%s', result)
        self.assertEqual(result[0][0], 'hauva', 'Should be "hauva"')
        self.assertEqual(result[0][1], responsibility, 'Should be "{0}"'.format(responsibility))
        cursor.close()
        conn.close()

if __name__ == '__main__':
        unittest.main()

