#!/usr/bin/python3

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

def _main():
    print('#!/usr/bin/python3\n')
    print("'''Please do change the first \"elif\" to \"if\".'''\n")
    print("def get_entity_from_ord(value: int):")
    print("    '''Returns an XML entity from the ord of a character.'''")
    print("    data = ''")
    print('    byte = 32\n')

    for k, v in CONVERSION.items():
        _, value, entity = k, ord(k), v

        print(f'    elif byte == {value}:')
        print(f"        data += '{entity}'")

if __name__ == '__main__':
    _main()
