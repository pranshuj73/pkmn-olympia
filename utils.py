from math import floor
import os, time, sys, importlib

# contains utility functions
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def loader(message, n):
    for i in range(4):
        print(f"\r{message}{'.' * i}", end="\r")
        time.sleep(n)
    print()

def wait(n):
    time.sleep(floor(n))

def typewrite(*argv):
  for arg in argv:
    if arg == '<INPUT>':
      input("Press enter to continue...")
      print(f"\033[A{' ' * 50}\033[A") # move cursor up 2 lines
    elif arg == '<PAUSE>':
      time.sleep(0.7)
      print()
    else:
      # each arg will be a sentence
      for char in arg:
        time.sleep(0.04) # go to sleep for 0.04 secs
        sys.stdout.write(char) # prints char on screen (somehow differently?)
        sys.stdout.flush() # flushes char from ram memory using voodoo magic
      
      print() # This print exists to separate lines from one another
      time.sleep(0.1) # sleep before printing another sentence

def read_savefile():
    with open(f'./saves/save.json', 'r') as f:
        data = f.read()
    
    # parse the json data
    data = eval(data)
    
    return data['chapter'], data['name']


def save_game(chapter, name):
    # save the game
    # chapter: chapter number
    # name: player name
    
    # save the chapter and player name to json file in the saves directory
    with open(f'./saves/save.json', 'w') as f:
        f.write(f'{{\n\t"chapter": {chapter},\n\t"name": "{name}"\n}}')

def load_game():
    # load the game
    # returns chapter and player name
    
    # load the chapter and player name from json file in the saves directory
    while True:
        # check player's current progress
        chapter, name = read_savefile()
        
        try:
            clear()
            # dynamically import the main function of chapter module
            main = getattr(importlib.import_module(f"chapters.chapter_{chapter}"), "main")
            main()

            next_chapter = int(chapter) + 1
            save_game(next_chapter, name)

            print()
            loader("Saving the Game", 0.2)
            typewrite("Successfully Saved the Game!", "<INPUT>")
            clear()

        except ModuleNotFoundError:
            clear()
            typewrite(
                "Oh no! You've reached the end of the game!",
                "Thank you for playing Pokemon!",
                "<INPUT>"
            )
            break
        
        except Exception as e:
            clear()
            typewrite(
                f"Oh no! There was an error loading the game. Please try again later.",
                "<PAUSE>"
            )
            break

        

    clear()
    # back to the main menu
    lobby = getattr(importlib.import_module(f"run"), "main")    
    lobby()
