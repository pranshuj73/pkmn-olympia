# contains main code

from utils import *
import sys
import inquirer

def new_game():
    print("Starting New Game...", end="\r" )
    
    # chapter_1()

def exit():
    print("Exiting Game...")
    sys.exit(0)

def menu():
    question = [
        inquirer.List(
            'menu',
            message="What do you want to do?",
            choices = ['New Game', 'Load Game', 'About', 'Exit'],
        )
    ]
    answer = inquirer.prompt(question)

    if answer['menu'] == 'Exit':
        exit()
    elif answer['menu'] == 'New Game':
        new_game()

def main():
    # printing the game title
    print(
"""
█▀█ █▀█ █▄▀ █▀▀ █▀▄▀█ █▀█ █▄░█
█▀▀ █▄█ █░█ ██▄ █░▀░█ █▄█ █░▀█

█▀█ █░░ █▄█ █▀▄▀█ █▀█ █ ▄▀█
█▄█ █▄▄ ░█░ █░▀░█ █▀▀ █ █▀█
"""
    )

    # show the game menu
    menu()


if __name__ == '__main__':
    main()