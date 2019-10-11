deposit = float(input('How much money did you want to deposit?: '))

year1 = round(deposit * 1.04, 2)
year2 = round(year1 * 1.04, 2)
year3 = round(year2 * 1.04, 2)


print('In 1 year you will get ' + str(year1))
print('In 2 years you will get ' + str(year2))
print('In 3 years you will get ' + str(year3))
