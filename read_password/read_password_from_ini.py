#!/usr/bin/python3

'''
Read usernames and passwords for QA and PRD environments from a configuration file.
'''

# https://www.deepanseeralan.com/tech/checking-file-permissions-in-python/
# https://www.tutorialspoint.com/How-to-check-the-permissions-of-a-file-using-Python

import logging
import os
import stat
import sys

import configlib

logging.basicConfig(level=logging.DEBUG)

CONFIG = 'credentials.ini'

def read_credentials(env: str, ini_file: str):
    '''Reads credentials from an ini file.'''
    _check_permissions(ini_file)
    config = None
    try:
        config = configlib.getconfiguration(ini_file)
    except FileNotFoundError as ex:
        logging.critical(ex)
        sys.exit(1)

    # pylint: disable=redefined-outer-name
    username = config[env]['username']
    password = config[env]['password']

    return username, password

def _check_permissions(filename: str):
    status = os.stat(filename)
    mode = stat.filemode(status.st_mode)
    logging.debug('status=%s mode=%s', status, mode)
    user_only_mode = '-rw-------'

    if mode != user_only_mode:
        raise ValueError(f'file {filename} must have permission 600 {user_only_mode}')

if __name__ == '__main__':
    username, password = read_credentials('QA', CONFIG)
    logging.debug('username=%s password=%s', username, password)
    username, password = read_credentials('PRD', CONFIG)
    logging.debug('username=%s password=%s', username, password)
