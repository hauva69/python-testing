#!/usr/bin/python3

'''
Testime subprocess.check_output().
'''

import subprocess

def _timeout(sleep: str, timeout: int):
    subprocess.check_output(['/usr/bin/sleep', sleep], stderr=subprocess.STDOUT, timeout=timeout)

if __name__ == '__main__':
    _timeout('2', 5)
