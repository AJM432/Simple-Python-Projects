
phone = int(input('Enter number of minutes on phone: '))
text = int(input('Enter number of messages sent: '))
print('Base Charge: $15')

add_phone = round((phone - 50) * .25, 2)
add_text = round((text - 50) * .15, 2)
if phone > 50 and text > 50:
    print('Additional phone charge: $' + str(add_phone))
    print('Additional texts charge: $' + str(add_text))

print('Additional 911 fee: $0.44')
total = round((15.0 + add_phone + add_text + 0.44)* 1.13, 2)
print('Your total is $' + str(total))

 
    
