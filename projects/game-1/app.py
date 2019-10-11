import random


class enemy:
    def __init__(self, type, health, attack):
        self.type = type
        self.heath = health
        self.attack = attack


class player:
    def __init__(self, health, attack, money):
        self.heath = health
        self.attack = attack
        self.money = money


class item:
    def __init__(self, type, price, effect):
        self.type = type
        self.effect = effect


player = player(100, 50, 1000)
boss = enemy('boss', 1000, 50)
dragon = enemy('dragon', 500, 25)
solder = enemy('soldier', 100, 50)
health_potion = item('health', 100, 200)
fireball = item('attack', 50, 150)
money_multiplier = item('money', 75, 100)
player_inventory = ''
player_stats = ''


def game():
    player_name = input('What is your name: ')
    print('Hello, ' + player_name + ' welcome to the game')
    print('')
    print('There is a soldier in the distance time to start your first match!')

    fight()


def fight():

    opt_1 = ['A', 'run away']
    opt_2 = ['B', 'fight enemy']
    opt_3 = ['C', 'hide by a near by rock']

    win = False
    while win == False:
        print(opt_1[0] + ': ' + opt_1[1])
        print(opt_2[0] + ': ' + opt_2[1])
        print(opt_3[0] + ': ' + opt_3[1])

        fight_option = input('Enter one of the above: ')

        if fight_option == 'A':
            print('')
            print('-----------')
            print('Another soldier ambushed you!')
            print('Try again')
            win = False
            print('-----------')
        elif fight_option == 'B':
            print('')
            print('-----------')
            print('The knight has more health than you')
            print('You died!')
            win = False
            print('-----------')
        elif fight_option == 'C':
            print('-----------')
            print('You were able to successfully ambush and defeat the soldier')
            print('You won! Time to move on')
            print('-----------')
            win == True


def menu():
    print("""
    play: Continue to game
    item: Goes to item list
    inventory: Shows inventory
    stats: Shows stats
""")
    player_input = input('Enter Command From List: ')

    if player_input == 'item':
        print("""
    Health potion: 
        price: $100
        effect: +200 health

    Fireball:
        price: $50
        effect: +150 attack
    
    Money multiplier:
        price: $75
        effect: +100 money/enemy killed
""")

    elif player_input == 'inventory':
        print(player_inventory)

    elif player_input == 'stats':
        print(player_stats)

    elif player_input == 'play':
        game()


menu()
