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
    typewrite(
        "Hello and welcome to the world of Pokemon!",
        "Pokemon are wonderful creatures that live in the world and fight each other.",
        "<PAUSE>",
        "My name is Professor Tumin. I'm a Pokemon Researcher and that is simply to say I like studying Pokemon!",
        "Ah...I forgot to ask you, what's your name?"
    )

    askInfo = [
        inquirer.Text('name', message = "My name is"),
        inquirer.List(
            'gender',
            message = "And I am a",
            choices = ['Boy', 'Girl']
        )
    ]
    info = inquirer.prompt(askInfo)
    name, gender = info['name'], info['gender']
    typewrite(
        f"Very well! Pleased to make acquaintance with you you {name}, you're a wonderful {gender.lower()}!",
        "Now then! Shall we embark on this journey together?",
        "Let's enter the world of Pokemon, where the dreams become reality!",
        "<INPUT>"
    )
