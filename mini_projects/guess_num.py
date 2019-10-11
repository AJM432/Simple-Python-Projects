import random

def user():
    run = True  
    x = random.randint(1, 100)
    guess = int(input('Enter a number: '))

    while run == True:
        print(x)
        try:
            if guess < x:
                guess = int(input('Too low, Enter a number: '))
            
            elif guess > x:
                guess = int(input('Too high, Enter a number: '))

            elif guess == x:
                print(f'you guessed {guess} and the answer was {x}')
                run = False
        except ValueError:
            guess = int(input('You entered a letter, Enter a number: '))

def comp():
    y = random.randint(1, 100)
    #num_range = 100
    on = True
    n = 0
    comp_guess = 0
    while on == True:
    
        if comp_guess == y:
            print('computer won in ' + n + ' times')
            on = False
        
        #elif comp_guess < y:
            
        #elif comp_guess > y:
           
            
user()



    
