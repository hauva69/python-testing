#!/usr/bin/python3

'''Creates bash script from input and the contents of the configuration file.'''

import logging
import sys

import configlib

logging.basicConfig(level=logging.DEBUG)

def _create_xml():
    conf = configlib.getconfiguration('props.ini')
    interpreter = conf['create_xml']['interpreter']
    shebang = f'#!{interpreter}'
    cmd = conf['create_xml']['cmd']

    print(f'{shebang}\n')

    for line in sys.stdin:
        sys.stdout.write(f'{cmd} {line}')

def _run_xml():
    conf = configlib.getconfiguration('props.ini')
    interpreter = conf['run_xml']['interpreter']
    shebang = f'#!{interpreter}'
    cmd = conf['run_xml']['cmd']

    print(f'{shebang}\n')

    for line in sys.stdin:
        sys.stdout.write(f'{cmd} {line}')

def _main():
    cmd = sys.argv[1]

    if cmd == 'create':
        _create_xml()
    elif cmd == 'run':
        _run_xml()
    else:
        raise ValueError(f'unexpected command value: {cmd}')

if __name__ == '__main__':
    _main()
