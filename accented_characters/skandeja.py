#!/usr/bin/python3

def _main():
    fd_latin1 = open('skandeja-latin1.txt')
    # latin1 = fd_latin1.read()
    fd_latin1.close()
    fd_utf8 = open('skandeja-utf8.txt')
    utf8 = fd_utf8.read()
    fd_utf8.close()
    # print(latin1)
    print(utf8)

if __name__ == '__main__':
    _main()
