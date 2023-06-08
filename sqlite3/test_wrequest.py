#!/usr/bin/python3

'''
Sqlite testing.
'''

import logging
import pathlib
import sqlite3
import time
import unittest

import wrequest

logging.basicConfig(level=logging.INFO)

DB_NAME = pathlib.Path('/tmp/db', 'requests.db')

class TestWrequest(unittest.TestCase):
    '''Test whether the SOAP request will be posted.'''

    @staticmethod
    def _get_connection():
        return sqlite3.connect(DB_NAME)

    def _init_database(self):
        responsibility = 'kändivästüü'
        conn = self._get_connection()
        cursor = conn.cursor()
        sql = f"""
INSERT INTO requests (uid, responsibility, primary_position, created) VALUES
('hauva', '{responsibility}', 2200, current_timestamp)"""
        logging.debug('sql=%s', sql)

        try:
            cursor.execute(sql)
        except sqlite3.OperationalError as ex:
            logging.error(ex)

        time.sleep(1)
        responsibility = 'vastuu'
        sql = f"""
INSERT INTO requests (uid, responsibility, primary_position, created) VALUES
('hauva', '{responsibility}', 5651, current_timestamp)"""
        logging.debug('sql=%s', sql)

        try:
            cursor.execute(sql)
        except sqlite3.OperationalError as ex:
            logging.error(ex)

        conn.commit()
        cursor.close()
        conn.close()

    def test_will_soap_be_posted(self):
        '''Tests whether the SOAP request will be posted.'''
        self._init_database()
        conn = self._get_connection()
        cursor = conn.cursor()
        uid = 'foo'
        responsibility = 'responsibility'
        primary_position = 1111
        self.assertTrue(wrequest.will_soap_be_posted(cursor, uid, responsibility, primary_position),
                        "should be True")
        uid = 'hauva'
        responsibility = 'vastuu'
        primary_position = 5651
        self.assertFalse(wrequest.will_soap_be_posted(
            cursor,
            uid,
            responsibility,
            primary_position),
            "should be False")
        cursor.close()
        conn.close()

if __name__ == '__main__':
    unittest.main()
