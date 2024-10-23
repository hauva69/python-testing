#!/usr/bin/python3

'''Parses a javascript file for associative array keys.'''

import re

def _main():
    pattern = r'\["([^"]+)'
    prog = re.compile(pattern)

    fd = open('associative-array.js')
    for line in fd:
        line = line.rstrip()
        match = prog.search(line)
        if match:
            print(match.group(1))

    fd.close()

if __name__ == '__main__':
    _main()
