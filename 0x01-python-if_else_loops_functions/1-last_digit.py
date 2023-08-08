#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_dgt = (-1 * number) % 10
else:   
    last_dgt = number % 10
stri = 'Last digit of {} is {}'.format(number,last_dgt)
if last_dgt > 5:
    print('{} and is greater than 5'.format(stri))
elif last_dgt == 0:
    print('{} and is 0'.format(stri))
else:
    print('{} and is less than 6 and not 0'.format(stri))
