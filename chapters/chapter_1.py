from utils import *
from rich.console import Console
import sys, os, time, inquirer


def main():
    with open(f'./saves/save.json', 'r') as f:
        data = f.read()
    # parse the json data
    data = eval(data)
    player = data['name']

    console = Console()
    console.rule("Chapter 1: New Beginnings")
    typewrite(
        "It's another normal day in the Litochoro Village. The villagers are busy preparing for the upcoming village festival.",
        "The annual village festival is celebrated to thank the agriculture god Tapu Bulu for good crop yield.",
        "You wake up, stretch your body and go outside to see the village lively with visitors from different districts of Olympia.",
        "<WAIT>",
        "'So beautiful...' you think to yourself as you stare at the lush green grass and the colorful flowers contrasting with the deep blue sky.",
        "<PAUSE>",
        "Suddenly you hear a loud booming sound followed by sounds of footsteps..."
        f"{(player + player[-1]*3).upper()}! WAAAKEE UPPPPP!!!",
        "You: It's mom! I must have overslept...Wait a sec!",
        "An idea suddenly flashes in your mind...You get up, wash your face and sit down at your study table with a book in hand!",
        "Mom: Oh, you're awake! I thought you overslept again, but you're diligently studying!",
        "Mom: There was a letter for from Prof. Tumin. He said he'll be visiting us during the festival. Isn't that nice?",
        "     And that's why I want you to do a little shopping for dinner. You'll go right? Ofcourse you will!",
        "You: Alright sure! I'd love a chance to talk about Pokemon with him on dinner! I'll be heading off right away!!",
        "Mom: Oh, you're so sweet! I'll be waiting for you.",
        
        "",     
        
        
    )

    typewrite("<INPUT>")
