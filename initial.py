from email import message
from random import choices
from typing import TYPE_CHECKING
from utils import *
from rich.console import Console
import sys, os, time, inquirer

# initialising
if not os.path.exists('./saves'):
    os.makedirs('./saves')




def initiate():
    console = Console()
    clear()
    loader('Game is loading', 1)
    clear()
    typewrite("Welcome to the game!")
    wait(2)
    clear()
    typewrite("Hello! I am Professor Tumin! And I welcome you to the world of Pokemon.")

    # Asking for name
    typewrite("Sorry I am little old so I forget, can you tell me your name again?")
    askInfo = [
        inquirer.Text('name', message = "My name is"),
        inquirer.List(
            'gender',
            message = "And I am a",
            choices = ['Boy', 'Michael Scott', 'Apache Helikopter', 'Dishwasher']
        )
    ]
    info = inquirer.prompt(askInfo)
    name, gender = info['name'], info['gender']
    typewrite(f"Very well! So nice to meet you {name}, a {gender}!")