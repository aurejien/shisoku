import os
from random import randint
from math import ceil

monney = 2000
play_again = True
print("-----------------------------------")
print()
print(f"Welcome to the Zcasino \n you start with {monney} .-\nGood luck and enjoy your game.")
print()
print("-----------------------------------")
player_name = input("Your name?:\n->   ")
player_name = player_name.title() #Move the first letter to Capital letter
print()
print("Rules\nYou have to give bet on one number between 0 and 49\nIf number match you multiply your bet by 3\nIf not match you will earn 0.5 more if it the same color.")
print("-----------------------------------")
while play_again:
    #number asking
    print(f"Your credit: {monney}.")
    print()
    num_bet = -1
    while num_bet < 0:
        num_bet = input("Choose the number btw 0 and 49:\n->   ")
        try:
            num_bet = int(num_bet)
            if num_bet < 0 or num_bet > 49:
                raise ValueError
            elif num_bet % 2:
                print(f"{num_bet} Black")
            else:
                print(f"{num_bet} Red")
        except ValueError:
            print("Erreur des données.")
            num_bet = -1
    #bet asking
    bet = -1
    while bet <= 0 or bet >= monney +1:
        bet = input("Your bet:\n->   ")
        try:
            bet = int(bet)
            if bet <= 0 or bet >= monney +1:
                raise ValueError
        except ValueError:
            print("Erreur des données.")
            bet = -1
    #Random winning number
    winning_num = randint(0,49)
    if winning_num % 2:
        color = "Black"
    else:
        color = "Red"
    if num_bet == winning_num:
        earn_bet = bet * 3
        monney += earn_bet
        print()
        print(f"Yours {num_bet} {color}, Roulette {winning_num} {color}")
        print(f"You are lucky {player_name} you earn {earn_bet}.")
        print("-----------------------------------")
    elif num_bet % 2 == winning_num % 2:
        earn_bet_color = bet + ceil(bet * 0.4)
        monney += earn_bet_color
        print()
        print(f"Yours {num_bet} {color}, Roulette {winning_num} {color}")
        print(f"Well donne same color {player_name} you earn {earn_bet_color}.")
        print("-----------------------------------")
    else:
        monney -= bet
        print()
        print(f"Yours {num_bet} {color}, Roulette {winning_num} {color}")
        print(f"Sorry {player_name} you lost.")
        print("-----------------------------------")
    
    if monney <= 0:
        print(f"Sorry {player_name} your credit's {monney}\nYour are in ruined.")
        follow = input(f"Add more money?\n Yes or No\n->   ")
        if "yes" == follow or "Yes" == follow or "YES" == follow or "Y" == follow or "y" == follow:
            monney = -1
            while monney < 0:
                monney = input(f"How many you want to add?\n->   ")
                try:
                    monney = int(monney)
                    if monney <= 1 or monney >= 1001:
                        raise ValueError
                    print(f"Thanks {player_name} you add {monney}.\nGood luck.")
                except ValueError:
                        print("We can't accept more than 1000.-")
                        monney = -1
        else:
            print(f"Goodbye {player_name}")
            play_again = False
os.system("pause")