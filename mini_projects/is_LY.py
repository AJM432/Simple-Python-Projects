
#!/usr/bin/env python3

# This project is now in testing phase
# error non syntax related
# ERROR: All years 0-2999 are seen as not leap years including real leap years

def leapYear(year):
    run = True
    leap = None
    while run == True:
        # year = int(input('enter a year: '))
        
        if year % 4 != 0 or year % 100 != 0:
            leap = False

        
        if year % 4 == 0 and year % 100 == 0 and year & 400 == 0:
            leap = True
        return leap
                

        #if leap == True:
            #print('This year IS a leap year')

        #else:
            #print('This year is NOT a leap year')
        

x = 0
while x != 3000:
    leapYear(x)
    x+=1
    if leapYear == True:
        print(x + ' is a leap year!')
    if x == 2999:
        print('somethings wrong here')

    
