#!/usr/bin/python3

'''
Tests for entify.

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

import unittest

from entify import entify

CONVERSION = {
    'Á': '&#xC1;',
    'á': '&#xE1;',
    'É': '&#xC9;',
    'é': '&#xE9;',
    'È': '&#xC8;',
|   'è': '&#xE8;',
    'Ò': '&#xD2;',
    'ò': '&#xF2;',
    'Ó': '&#xD3;',
    'ó': '&#xF3;',
    'Ü': '&#xDC;',
    'ü': '&#xFC;',
    'å': '&#xE5',
    'Å': '&#xC5;',
    'Ä': '&#xC4;',
    'ä': '&#xE4;',
    'ö': '&#xF6;',
    'Ö': '&#xD6;',
'''
}

class TestEntify(unittest.TestCase):
    def test_entify(self):
        test_string = 'Åke Bjärne Österman. Äldre konstapel.'
        expected = '&#xC5;ke Bj&#xC5;rne &#xF6;sterman'
        self.assertEqual(entify(test_string), expected, 'expected {0}'.format(expected))

if __name__ == '__main__':
    unittest.main()
