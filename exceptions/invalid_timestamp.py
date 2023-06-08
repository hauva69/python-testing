#!/usr/bin/python3

'''Exception testing.'''

import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

class InvalidTimeStampException(Exception):
    pass

def _value_error():
    try:
        now = datetime.datetime.now()
        if now.second % 2  == 0:
            raise ValueError('this is the original ValueError')
    except ValueError as ex:
        logging.debug('original_exception=%s', ex)
        now = datetime.datetime.utcnow().isoformat()
        raise InvalidTimeStampException(f'timestamp {now} has invalid format')
    
    raise ValueError('REST API returned an error')

if __name__ == '__main__':
    try:
        _value_error()    
    except InvalidTimeStampException as ex:
        logging.error(ex)
    except ValueError as ex:
        logging.error(ex)
