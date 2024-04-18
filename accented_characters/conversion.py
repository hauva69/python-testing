#!/usr/bin/python3

'''Please do change the first "elif" to "if".'''

def get_entity_from_ord(value: int):
    '''Returns an XML entity from the ord of a character.'''
    data = ''
    byte = 32

    if byte == 193:
        data += '&#xC1;'
    elif byte == 225:
        data += '&#xE1;'
    elif byte == 201:
        data += '&#xC9;'
    elif byte == 233:
        data += '&#xE9;'
    elif byte == 200:
        data += '&#xC8;'
    elif byte == 232:
        data += '&#xE8;'
    elif byte == 210:
        data += '&#xD2;'
    elif byte == 242:
        data += '&#xF2;'
    elif byte == 211:
        data += '&#xD3;'
    elif byte == 243:
        data += '&#xF3;'
    elif byte == 220:
        data += '&#xDC;'
    elif byte == 252:
        data += '&#xFC;'
    elif byte == 229:
        data += '&#xE5;'
    elif byte == 197:
        data += '&#xC5;'
    elif byte == 196:
        data += '&#xC4;'
    elif byte == 228:
        data += '&#xE4;'
    elif byte == 246:
        data += '&#xF6;'
    elif byte == 214:
        data += '&#xD6;'
