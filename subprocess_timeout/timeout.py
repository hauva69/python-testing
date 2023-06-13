#!/usr/bin/python3

'''
Testime subprocess.check_output().
'''

import subprocess

def _timeout_5_success():
    subprocess.check_output(['/usr/bin/sleep', '2'], stderr=subprocess.STDOUT, timeout=5)

if __name__ == '__main__':
    _timeout_5_success()
