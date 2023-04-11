#!/usr/bin/python3

'''
Transform accented characters to entities.

| Merkki | Entiteetti |
| ------ | ---------- |
| Á      | &#xC1;     |
| á      | &#xE1;     |
| É      | &#xC9;     |
| é      | &#xE9;     |
| È      | &#xC8;     |
| è      | &#xE8;     |
| Ò      | &#xD2;     |
| ò      | &#xF2;     |
| Ó      | &#xD3;     |
| ó      | &#xF3;     |
| Ü      | &#xDC;     |
| ü      | &#xFC;     |
| å      | &#xE5;     |
| Å      | &#xC5;     |
| Ä      | &#xC4;     |
| ä      | &#xE4;     |
| ö      | &#xF6;     |
| Ö      | &#xD6;     |
'''

import logging
import sys

logging.basicConfig(level=logging.DEBUG)

CONVERSION = {
    'Á': '&#xC1;',
    'á': '&#xE1;',
    'É': '&#xC9;',
    'é': '&#xE9;',
    'È': '&#xC8;',
    'è': '&#xE8;',
    'Ò': '&#xD2;',
    'ò': '&#xF2;',
    'Ó': '&#xD3;',
    'ó': '&#xF3;',
    'Ü': '&#xDC;',
    'ü': '&#xFC;',
    'å': '&#xE5;',
    'Å': '&#xC5;',
    'Ä': '&#xC4;',
    'ä': '&#xE4;',
    'ö': '&#xF6;',
    'Ö': '&#xD6;',
}

def entify(string: str) -> str:
    '''Transforms accented characters of a string to entities.'''
    entified = string

    for key, value in CONVERSION.items():
        logging.debug('key=%s value=%s', key, value)
        entified = entified.replace(key, value)

    return entified

if __name__ == '__main__':
    print(entify('Åke Bjärne Österman. Äldre konstapel.'))
