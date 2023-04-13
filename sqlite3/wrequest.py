#!/usr/bin/python3

'''Checks whether the user exists in the database and has same priviledges.'''

import logging

logging.basicConfig(level=logging.INFO)

def will_soap_be_posted(cursor, uid: str, responsibility: str, primary_position) -> bool:
    '''Will the SOAP request be posted?'''
    sql = 'SELECT responsibility, primary_position FROM requests WHERE uid = ? ORDER BY created DESC' # pylint: disable=line-too-long
    cursor.execute(sql, (uid, ))
    result = cursor.fetchone()
    logging.debug('uid=%s responsibility=%s primary_position=%s',
                  uid, responsibility, primary_position)
    logging.debug('result=%s', result)

    if result and len(result) == 2 and result[0] == responsibility and result[1] == primary_position:
        logging.debug('len(result)=%s', len(result))
        logging.error('The SOAP request for user "%s" not posted. Check the user.', uid)
        return False

    return True

def _main():
    print('hello, world')

if __name__ == '__main__':
    _main()
