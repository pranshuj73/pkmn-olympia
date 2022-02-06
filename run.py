# contains main code

from utils import *
from rich.console import Console
import os, sys, inquirer


def exit():
    print("Exiting Game...")
    sys.exit(0)

def menu():
    question = [
        inquirer.List(
            'menu',
            message = "What do you want to do?",
            choices = ['Load Game', 'New Game', 'About', 'Exit'],
        )
    ]
    answer = inquirer.prompt(question)

    if answer['menu'] == 'Exit':
        exit()
    elif answer['menu'] == 'Load Game':
        load_game()
    elif answer['menu'] == 'New Game':
        save_game(0, '')
        load_game()
        

def main():
    # printing the game title
    console = Console()
    console.print(
"""

█▀█ █▀█ █▄▀ █▀▀ █▀▄▀█ █▀█ █▄░█
█▀▀ █▄█ █░█ ██▄ █░▀░█ █▄█ █░▀█

█▀█ █░░ █▄█ █▀▄▀█ █▀█ █ ▄▀█
█▄█ █▄▄ ░█░ █░▀░█ █▀▀ █ █▀█

""",
    style="yellow",
    justify="center",)

    # show the game menu
    menu()


if __name__ == '__main__':
    # initialising run.py
    clear()

    main()
