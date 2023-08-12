#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    len_arg = len(sys.argv)
    if len_arg == 1:
        print('0 arguments.')
    else:
        a = 1
        print('{:d} arguments:'.format(len_arg - 1))
        argv = sys.argv[1:]
        for i in argv:
            print('{:d}: {}'.format(a, i))
            a = a + 1
