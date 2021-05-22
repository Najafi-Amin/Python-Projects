'''
@author Amin Najafi
05/21/21
Description: The following program is a game which
asks the user questions and responds depending on the
user's input.
'''

import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro(enemy, weapon, magic_taken):
    print_pause("You find yourself standing in an open field, ")
    print_pause("filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + enemy + " is somewhere around here,")
    print_pause(" and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty but not very")
    print_pause(" effective " + weapon + ".")


def valid_input(prompt, enemy, weapon, magic_taken):
    response = input(prompt)
    if response == "1":
        house(enemy, weapon, magic_taken)
    elif response == "2":
        cave(enemy, weapon, magic_taken)
    else:
        print_pause("sorry, I don't understand.")
        valid_input('''\nEnter 1 to knock on the door of the house.\n
        Enter 2 to peer into the cave.\n
        What would you like to do?\n
        Please enter 1 or 2\n''', enemy, weapon, magic_taken)


def play_again():
    response1a = input("would you like to play again?(Y/N)")
    response1a = response1a.upper()
    if response1a == "Y":
        print("Excellent! restarting the game...")
        play_game()
    elif response1a == "N":
        print("Thanks for playing! See you next time!")
        exit()
    else:
        print("Wrong input! Please try again!")
        play_again()


def house(enemy, weapon, magic_taken):
    print_pause("you approach the door of the house")
    print_pause("you are about to knock, when the door opens and")
    print_pause(" out steps a " + enemy + ".")
    print_pause("Eep! this is the " + enemy + "'s house!")
    print_pause("The "+enemy+" attacks you!")
    print_pause("You feel a bit under-prepared for this, ")
    if magic_taken is False:
        print_pause("what with only having a " + weapon + ".")
    response1 = input("would you like to (1) fight or (2) run away?")
    if response1 == "1":
        fight(enemy, weapon, magic_taken)
    elif response1 == "2":
        runaway(enemy, weapon, magic_taken)


def fight(enemy, weapon, magic_taken):
    if magic_taken is False:
        print_pause("you do your best...")
        print_pause("but your " + weapon + " is no match for the troll.")
        print_pause("you have been defeated!")
    if magic_taken is True:
        print_pause("As the "+enemy+" moves to ")
        print_pause("attack, you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your ")
        print_pause("hand as you brace yourself for the attack.")
        print_pause("But the "+enemy+" takes one look at your")
        print_pause(" shiny new toy and runs away!")
        print_pause("You have rid the town of the "+enemy)
        print_pause(". You are victorious!")
    play_again()


def runaway(enemy, weapon, magic_taken):
    print_pause("You run back into the field. Luckily,")
    print_pause(" you don't seem to have been followed.")
    valid_input("""Enter 1 to knock on the door of the house.\n
    Enter 2 to peer into the cave.\n
    What would you like to do?\n
    Please enter 1 or 2\n""", enemy, weapon, magic_taken)


def cave(enemy, weapon, magic_taken):
    print_pause("you peer cautiously into the cave.")
    if magic_taken is False:
        print_pause("It turns out to be only a very small cave.")
        print_pause("your eye catches a glint of metal behind a rock")
        print_pause("you have found the Magical sword of ogoroth!")
        print_pause("you discard your " + weapon)
        print_pause(" and take the sword with you!")
        magic_taken = True
    else:
        print_pause("You've been here before, and gotten all")
        print_pause(" the good stuff. It's just an empty cave now")
    print_pause("you walk back out to the field!")
    valid_input("""Enter 1 to knock on the door of the house.\n
    Enter 2 to peer into the cave.\n
    What would you like to do?\n
    Please enter 1 or 2\n""", enemy, weapon, magic_taken)
    play_again()


def play_game():
    magic_taken = False
    num = random.randint(0, (len(enemies) - 1))
    enemy = enemies[num]
    num = random.randint(0, (len(weapons) - 1))
    weapon = weapons[num]
    intro(enemy, weapon, magic_taken)
    valid_input('''Enter 1 to knock on the door of the house.\n
    Enter 2 to peer into the cave.\n
    What would you like to do?\n
    Please enter 1 or 2\n''', enemy, weapon, magic_taken)


enemies = ["ghoul", "pirate", "cyclone", "troll", "wicked fairie", "gorgon"]
weapons = ["sword", "silly old dagger", "shotgun", "RPG"]
play_game()
