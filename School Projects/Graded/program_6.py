T = 200
L = 100
Q = 25
D = 10
N = 5
P = 1

c = int(input('How much did the item cost?: '))

#number of toonies = input / 200
#print(number)
#input = input%200
numT = c // T
print(str(numT) + ' Toonies')
c = c%T

numL = c // L
print(str(numL) + ' Loonies')
c = c%L

numQ = c // Q
print(str(numQ) + ' Quarters')
c = c%Q

numD = c //D
print(str(numD) + ' Dimes')
c = c%D

numN = c // N
print(str(numN) + ' Nickles')
c = c%N

numP = c // P
print(str(numP) + ' Pennies')
