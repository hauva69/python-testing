#!/usr/bin/python3

def _main():
    fd = open('surname.txt', encoding='iso-8859-1')
    for line in fd:
        latin1bytes = line.encode('iso-8859-1')
        print(latin1bytes.decode('iso-8859-1').encode('utf-8').decode('utf-8'))
    fd.close()

if __name__ == '__main__':
    _main()
