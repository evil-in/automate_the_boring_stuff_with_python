# -*- coding: utf-8 -*-
"""
Chapter 2 Exercises
Q9) Write code that :
    prints Hello if 1 stored in spam,
    prints Howdy is 2 stored in spam, 
    prints Greetings! if anythhing else is stored in spam
"""

spam = int(input('Enter a number.\n'))

if spam==1:
    print('Hello')
elif spam==2:
    print('Howdy')
else:
    print('Greetings!')