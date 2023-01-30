#!/usr/bin/env -S python3

import logging
import random
import os

player_1_score = 0
player_2_score = 0
# SAME = True  # What is this for?
NAME_1 = ''
NAME_2 = ''


def dice_roll():  # the function generates 2 dice rolls and if they are equal adds a third then the total is checked and if it is even then it adds 10 more to the total otherwise it removes 5 point from the total
    """Generate the dice roll."""
    dice1 = random.randint(1, 6)  # rolls dice no.1
    dice2 = random.randint(1, 6)  # rolls dice no.2
    dice3 = random.randint(1, 6)  # rolls dice no.3
    if dice1 == dice2:  # checks if dice 1 and 2 are equal
        total = dice1 + dice2 + dice3  # adds dice 3 if so
    else:
        total = dice1 + dice2  # if not adds dice 1 and 2
    if total in (-5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29):  # checks if total is odd
        final_total = total - 5  # minuses 5 if odd
    else:
        final_total = total + 10  # adds 10 if even
    return final_total  # returns the total


filename_1 = 'player_1.txt'
filename_2 = 'player_2.txt'

# https://github.com/rokejulianlockhart/20-hour-project-dice-game/issues/2
while True:  # https://stackoverflow.com/a/20337522/9731176
    os.system('cls' if os.name == 'nt' else 'clear')
    response = input('Do you wanţ to authenticate or overwrite the previous credentials? (authenticate/overwrite): ')
    os.system('cls' if os.name == 'nt' else 'clear')
    if response == 'authenticate':
        try:
            mode = 'AUTHENTICATION'
            print(mode + ' MODE')
            with open(filename_1, 'r+', encoding='utf-8', errors='strict') as file:
                player = 1
                type_of_input = 'username'
                verify_username_1 = str(input('Player ' + str(player) + ', enter your ' + type_of_input + ': '))
                logging.warning(file.readline())
                if verify_username_1 == str(file.readlines()[0]).strip():
                    print('Correct username.')
                else:
                    print('Incorrect username.')
                type_of_input = 'password'
                verify_password_1 = str(input('Player ' +  str(player) + ', enter your ' + type_of_input + ': '))
                logging.warning(file.readline(2))
                if verify_password_1 == file.readlines()[1].strip():
                    print('Correct password.')
                else:
                    print('Incorrect password.')
                os.system('cls' if os.name == 'nt' else 'clear')
                print(mode + ' MODE')
                player = 2
                type_of_input = 'username'
                verify_username_2 = str(input('Player ' + player + ', enter your ' + type_of_input + ': '))
                if verify_username_2 == file.readline(1):
                    print('Correct username.')
                else:
                    print('Incorrect username.')
                type_of_input = 'password'
                verify_password_2 = str(input('Player ' + player + ', enter your ' + type_of_input + ': '))
                if verify_password_2 == file.readline(2):
                    print('Correct password.')
                else:
                    print('Incorrect password.')
            break
        except ValueError:
            while True:
                incorrect_encodement_response = input('Incorrect encodement. Overwrite? (y/n): ')
                if incorrect_encodement_response == 'y':
                    print('REPLACEMENT MODE')
                    create_username_1 = str(input('Player 1, enter your user: '))
                    create_password_1 = str(input('Player 1, enter your password: '))
                    with open(filename_1, 'w', encoding='utf-8', errors='strict') as file:
                        file.write("username='" + create_username_1 + "'\n")
                        file.write("password='" + create_password_1 + "'\n")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('REPLACEMENT MODE')
                    create_username_2 = str(input('Player 2 enter your user: '))
                    create_password_2 = str(input('Player 2 enter your password: '))
                    with open(filename_2, 'w', encoding='utf-8', errors='strict') as file:
                        file.write("username='" + create_username_2 + "'\n")
                        file.write("password='" + create_password_2 + "'\n")
                    break
                elif incorrect_encodement_response == 'n':
                    raise SystemExit(0) from ValueError
                else:
                    break
    elif response == 'overwrite':
        print('REPLACEMENT MODE')
        create_username_1 = str(input('Player 1, enter your user: '))
        create_password_1 = str(input('Player 1, enter your password: '))
        with open(filename_1, 'w', encoding='utf-8', errors='strict') as file:
            file.write("username='" + create_username_1 + "'\n")
            file.write("password='" + create_password_1 + "'\n")
        os.system('cls' if os.name == 'nt' else 'clear')
        print('REPLACEMENT MODE')
        create_username_2 = str(input('Player 2 enter your user: '))
        create_password_2 = str(input('Player 2 enter your password: '))
        with open(filename_2, 'w', encoding='utf-8', errors='strict') as file:
            file.write("username='" + create_username_2 + "'\n")
            file.write("password='" + create_password_2 + "'\n")
        break
    else:
        print('Invalid response.')
        input('Press any key to recommence authentication.')

with open(filename_1, 'w+', encoding='utf-8', errors='strict') as file:

    end_of_file = False
    while not end_of_file:
        USERNAME = file.readline().strip()
        PASSWORD = file.readline().strip()  # https://ch-nabarun.medium.com/how-to-encrypt-and-decrypt-application-password-using-python-15893cd28bef if you can!

        if verify_username_1 == USERNAME and verify_password_1 == PASSWORD:
            login = True
        else:
            print('Incorrect details.')
            raise SystemExit(1)  # remediate: needs to be while loop
        
        if USERNAME == '':
            end_of_file = True

    with open(filename_1, 'w+', encoding='utf-8', errors='strict') as file:

        end_of_file = False
        while not end_of_file:
            USERNAME = file.readline().strip()
            PASSWORD = file.readline().strip()

            if verify_username_2 == USERNAME and verify_password_2 == PASSWORD:
                login = True
            elif verify_username_1 != USERNAME or verify_password_1 != PASSWORD:
                print('Incorrect details.')
                raise SystemExit(1)  # remediate: needs to be while loop
            
            if USERNAME == '':
                end_of_file = True

os.system('cls' if os.name == 'nt' else 'clear')
NAME_1 = input('Player 1, enter your preffered name: ')
NAME_2 = input('Player 2, enter your preffered name: ')
os.system('cls' if os.name == 'nt' else 'clear')

for i in range(0, 5):  # For loop that loops this 5 times

    input('Player 1, press enter to roll your dices!')
    os.system('cls' if os.name == 'nt' else 'clear')  # clears the console
    score_1 = dice_roll()

    if score_1 < 0:
        score_1 = 0

    player_1_score = player_1_score + score_1
    print(NAME_1, 'you rolled', score_1, 'points!')  # displays the points player 1 rolls
    print(NAME_1, 'has a score of ', player_1_score, 'points!')  # displays player 1's total score
    print(NAME_2, 'has a score of ', player_2_score, 'points!')  # displays player 2's total score
    input('Player 2, press enter to roll your dices!')
    os.system('cls' if os.name == 'nt' else 'clear')  # clears the console
    score_2 = dice_roll()

    if score_2 < 0:
        score_2 = 0

    player_2_score = player_2_score + score_2
    print(NAME_2, 'you rolled', score_2, 'points!')  # displays the points player 2 rolls
    print(NAME_1, 'has a score of', player_1_score, 'points!')  # displays player 1's total score
    print(NAME_2, 'has a score of', player_2_score, 'points!')  # displays player 2's total score

if player_1_score > player_2_score:
    print(NAME_1, 'WINS!')
    input('Press enter to close program.')
    os.system('cls' if os.name == 'nt' else 'clear')  # clears the console
    raise SystemExit(0)  # ends program

elif player_2_score > player_1_score:
    print(NAME_2, 'WINS!')
    input('Press enter to close program.')
    os.system('cls' if os.name == 'nt' else 'clear')
    raise SystemExit(0)  # ends program

else:

    while player_1_score == player_2_score:
        winning_dice_1 = random.randint(1, 6)
        winning_dice_2 = random.randint(1, 6)
        input('You both drew, so now you will roll 1 die and highest wins!')
        print(NAME_1, 'rolled', winning_dice_1,)
        print(NAME_2, 'rolled', winning_dice_2,)

        if winning_dice_1 > winning_dice_2:  # compares the winning dice
            print(NAME_1, 'WINS!')
            input('Press enter to close program.')
            os.system('cls' if os.name == 'nt' else 'clear')  # clears the console
            raise SystemExit(0)  # ends program

        elif winning_dice_2 > winning_dice_1:  # compares the winning dice
            print(NAME_2, 'WINS!')
            input('Press enter to close program.')
            os.system('cls' if os.name == 'nt' else 'clear')  # clears the console
            raise SystemExit(0)  # ends program
