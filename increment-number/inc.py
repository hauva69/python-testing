#!/usr/bin/python3

'''
Increment an integer.
'''

def increment(number: int, format='06') -> str:
    '''Increment an integer and return it as a formatted string.'''
    incremented = number + 1

    return f'{incremented:{format}}'

def _main():
    print(f'incremented={increment(1000)}')
    print(f'incremented={increment(1000, "08")}')
    print(f'incremented={increment(1000, 4)}')

if __name__ == '__main__':
    _main()
