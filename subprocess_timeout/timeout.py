#!/usr/bin/python3

'''
Testime subprocess.check_output().
'''

import logging
import subprocess

logging.basicConfig(level=logging.DEBUG)

def _timeout(sleep: str, timeout: int):
    subprocess.check_output(['/usr/bin/sleep', sleep], stderr=subprocess.STDOUT, timeout=timeout)

if __name__ == '__main__':
    sleep = '2'
    timeout = 5
    logging.info('timeout sleep=%s timeout=%s', sleep, timeout)
    _timeout('2', 5)

    sleep = '5'
    timeout = 2
    logging.info('timeout sleep=%s timeout=%s', sleep, timeout)
    
    try:
        _timeout('5', 2)
    except subprocess.TimeoutExpired as ex:
        logging.error(ex)
