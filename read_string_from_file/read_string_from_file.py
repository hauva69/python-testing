#!/usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG)

def _main():
    fd = open('password.txt')
    line = fd.read()
    fd.close()
    line = line.strip()

    logging.debug(line)

if __name__ == '__main__':
    _main()
