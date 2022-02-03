# contains main code

from utils import *
from rich.console import Console
import os, sys, inquirer
import initial


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
        initial.initiate()
        # new_game()

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
    style="yellow on blue")

    # show the game menu
    menu()


if __name__ == '__main__':
    # initialising run.py
    clear()

    main()
    