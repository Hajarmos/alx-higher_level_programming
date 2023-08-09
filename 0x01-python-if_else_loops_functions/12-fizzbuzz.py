#!/usr/bin/python3
def fizzbuzz():
    f = 'Fizz'
    b = 'Buzz'
    for i in range(1, 101):
        if not(i % 3) and not(i % 5):
            print('{}{}'.format(f, b), end=' ')
        elif not(i % 3):
            print('{}'.format(f), end=' ')
        elif not(i % 5):
            print('{}'.format(b), end=' ')
        else:
            print('{}'.format(i), end=' ')
