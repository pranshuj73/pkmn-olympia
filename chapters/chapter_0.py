from utils import *
from rich.console import Console
import sys, os, time, inquirer


def main():
    console = Console()
    loader('Game is loading', 0.3)
    clear()
    typewrite(
        "Hello and welcome to the world of Pokemon!",
        "Pokemon are wonderful creatures that live in the world and fight each other.",
        "<PAUSE>",
        "My name is Professor Tumin. I'm a Pokemon Researcher and that is simply to say I like studying Pokemon!",
        "Ah...I forgot to ask you, what's your name?"
    )

    askName = [
        inquirer.List(
            'name',
            message = "My name is",
            choices = ['New Name', 'Jayden','Ash', 'Red',]
        ),
    ]
    name = inquirer.prompt(askName)['name']
    if name == "New Name":
        name = input("Please enter your name: ")
    
    askGender = [
        inquirer.List(
            'gender',
            message = "And I am a",
            choices = ['Boy', 'Girl']
        )
    ]
    gender = inquirer.prompt(askGender)['gender']
    save_game(1, name)
    typewrite(
        f"Very well! Pleased to make acquaintance with you you {name}, you're a wonderful {gender.lower()}!",
        "Now then! Shall we embark on this journey together?",
        "Let's enter the world of Pokemon, where the dreams become reality!",
        "<INPUT>"
    )
