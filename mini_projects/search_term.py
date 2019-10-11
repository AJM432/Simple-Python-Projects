import webbrowser as wb

def open(url):
    run = 0
    while run != leng:
        wb.open_new(url + term_list[run])
        run+=1

url1 = 'https://www.merriam-webster.com/dictionary/'
#url2 = 'https://www.dictionary.com/browse/'
term_list = []

leng = int(input('Enter length of list: '))
print('Enter the terms: ')

for x in range(leng):
    term = input()
    term_list.append(term)

if leng > 10:
    print('Opening more than 5 tabs will slow down do you want to continue?')
    option = input('y/n: ')
    if option == 'n':
        quit()
open(url1)
    
##error = input('Does the link work? [y/n]: ')
##
##if error == 'n':
##    open(url2)

