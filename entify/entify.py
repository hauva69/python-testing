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

import sys


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
    return 'FIXME'

if __name__ == '__main__':
    entify('Åke Bjärne Österman. Äldre konstapel.')
