v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
y = ('y','Y')
x = input('Enter a letter: ')

if x in v:
    print('You entered a vowel')

elif x in y :
    print('Y is sometimes a vowel')

else:
    print('You did not enter a vowel')
