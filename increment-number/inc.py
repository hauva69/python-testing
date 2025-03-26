#!/usr/bin/python3

'''
Increment an integer.
'''

import csv
import logging
import sys

logging.basicConfig(level=logging.DEBUG)

FIELDS = [1, 3, 4, 5]

def increment(number: int, format='06') -> str:
    '''Increment an integer and return it as a formatted string.'''
    incremented = number + 1

    return f'{incremented:{format}}'

def _test():
    print(f'incremented={increment(1000)}')
    print(f'incremented={increment(1000, "08")}')
    print(f'incremented={increment(1000, 4)}')

def _main():
    with open('numbers.in', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        writer = csv.writer(sys.stdout, delimiter=';', quotechar='|')
        index = 0

        for row in reader:
            data = None

            for field in row:
                if index in FIELDS:
                    if index == 1:
                        start, data = row[index].split('-')
                        incremented = start + '-' + increment(int(data), '04')
                        logging.debug('incremented=%s type=%s', data, type(data))
                        row[index] = incremented
                    elif index == 5:
                        email = row[index]
                        logging.debug('email=%s', email)
                        replaced = email[1:6]
                        incremented = increment(int(replaced), '')
                        email = email.replace(replaced, incremented)
                        logging.debug('replaced=%s incremented=%s', replaced, incremented)
                        logging.debug('email=%s', email)
                        row[index] = email
                    else:
                        data, end = row[index].split('_')
                        incremented = 'f' + increment(int(data[1:]), '') + '_' + end
                        logging.info('incremented_else=%s', incremented)
                        row[index] = incremented

                index += 1
            
            logging.info(row)
            writer.writerow(row)

if __name__ == '__main__':
    _main()
