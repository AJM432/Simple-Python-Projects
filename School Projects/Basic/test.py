import time


def msg():
    num = .3
    print('Y')
    time.sleep(num)
    print(' o')
    time.sleep(num)
    print('  u')
    time.sleep(num)
    
    print('L')
    time.sleep(num)
    print(' o')
    time.sleep(num)
    print('  s')
    time.sleep(num)
    print('   e')
    time.sleep(num)
    print(':(  :(')





guess = input('Enter a number: ')
num = 5

if int(guess) == num:
    msg()

else:
    print('You lose')
