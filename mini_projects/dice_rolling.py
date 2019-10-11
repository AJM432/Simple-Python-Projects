
#!/usr/bin/env python
import random
import time
import datetime
'''
def roll():
    run = None
    enter = input('do you want to roll the die Y/N: ')
    if enter == 'Y':
        run = True

    while run:
        x = random.randint(1, 6)
        print(x)
        x = input('do you want to roll again? Y/N: ')
        if x == 'N':
            run = False

roll()

'''
def dice():
    x = int(input('How many times do you want to roll the die: '))
    y = 0
    one = two = three = four = five = six = 0
    while x != y:
        z = random.randint(1, 6)
        print(z)
        y+=1
        if z == 1:
            one += 1

        elif z == 2:
            two += 1

        elif z == 3:
            three += 1

        elif z == 4:
            four += 1

        elif z == 5:
            five += 1
        
        elif z == 6:
            six += 1
        
        if x == y:
            print('one = ' + str(one))
            print('two = ' + str(two))
            print('three = ' + str(three))
            print('four = ' + str(four))
            print('five = ' + str(five))
            print('six = ' + str(six))




dice()

