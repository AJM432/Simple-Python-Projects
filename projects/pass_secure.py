import random
import time

def encode():
    key = random.randint(10, 100)
    print('The key is ' + str(key))

    output = []
    words = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
  
    password = input('Enter password (words only): ')
    pass_num = []

    for x in password:
        if x in words:
            pass_num.append(words.index(x))

    for x in pass_num:
        output.append(key * int(x))
        
    print('Your secure key is: ')
    print(output)


def crack():
    key1 = int(input('Enter the key: '))
    words = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    output1 = []
    output2 = []
    while True:
        inpt = input('Enter each item in encoded list: ')
        output1.append(inpt)
        if '' in output1:
            del(output1[-1])
            break
    for x in output1:
        output2.append(int(x) // key1)
    for x in output2:
        time.sleep(.5)
        print(words[x])
                    

option = input('Enter "crack" or "encode": ')
if option == 'encode':
    encode()

elif option == 'crack':
    crack()




'''
words = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    key1 = input('What is the key: ')
    pass_num1 = []
    output1 = []
    while True:
        inpt = input('Enter each item from endoded list: ')
        pass_num1.append(inpt)
        if '' in pass_num1:
            del(pass_num1[-1])
            for x in pass_num1:
                output1.append(str(int(x//key1))
                print(output1)

            for x in output1:
                print(words[x])
'''    

