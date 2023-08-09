#!/usr/bin/python3
for i in range(ord('Z'), ord('A') - 1, -1):
    if not(i % 2):
        c = chr(i + 32)
    else:
        c = chr(i)
    print('{}'.format(c), end='')
