T = 200
L = 100
Q = 25
D = 10
N = 5
P = 1

#numT = numL = numQ = numD = numN = numP = 0

change = int(input('Enter the amount of change: '))

numT = change // T
numL = (change % numT) // L
numQ = (change % numL) // Q
numD = (change % numQ) // D
numN = (change % numD) // N
numP = (change % numN) // P
print(numT)
print(numL)
print(numQ)
print(numD)
print(numN)
print(numP)





