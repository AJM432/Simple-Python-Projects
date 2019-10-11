def calc():
    a = int(input('Enter num 1: '))
    b = int(input('Enter num 2: '))

    operator = input('Enter operator add/sub/mul/div: ')

    if operator == 'add':
        result = a + b
    
    elif operator == 'sub':
        result = a - b
    
    elif operator == 'mul':
        result = a * b
    
    elif operator == 'div':
        result = a / b
    
    print(result)
     

calc()
