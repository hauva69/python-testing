#!/usr/bin/python3

'''Test reading and writing binary.'''

import logging

logging.basicConfig(level=logging.DEBUG)

def write_binary_file(filename: str, data):
    logging.debug('data.__class__=%s', data.__class__)
    fd = open(filename, 'wb')
    fd.write(data)
    fd.close()

def write_binary_file_with_bytearray(filename: str, data):
    logging.debug('bytearray_data=%s', data)
    badata = bytearray(data)
    logging.debug('badata=%s', badata)
    fd = open(filename, 'wb')
    fd.write(badata)
    fd.close()

def _main():
    latin1_fd = open('binary-latin1.txt', 'rb')
    latin1 = latin1_fd.read()
    latin1_fd.close()
    logging.debug('latin1=%s', latin1)
    write_binary_file('binary_out.txt', latin1)
    write_binary_file_with_bytearray('babinary_out.txt', latin1)

if __name__ == '__main__':
    _main()
