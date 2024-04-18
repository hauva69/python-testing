#!/usr/bin/python3

def _main():
    fd = open('surname.txt', 'rb')
    for line in fd:
        line = line.decode('iso-8859-1')
        print(line)
    fd.close()

if __name__ == '__main__':
    _main()
