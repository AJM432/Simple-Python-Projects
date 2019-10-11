shapes = ['0', '1', '2', 'triangle', 'square', 'pentagon', 'hexagon', 'septagon', 'octoagon', 'nonagon', 'decagon']
num_sides = int(input('Enter the number of sides (3-10): '))

if num_sides > 10 or num_sides < 2:
    print('You must enter a number between [3] and [10].')

else:
    print('A shape with ' + str(num_sides) + ' sides is a ' + str(shapes[num_sides]) + '.')
