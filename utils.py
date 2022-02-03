from math import floor
import os, time, sys
from turtle import end_fill

# contains utility functions
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def loader(message, n):
    for i in range(4):
        print(f"\r{message}{'.' * i}", end="\r")
        time.sleep(0.5)
    print()

def wait(n):
    time.sleep(floor(n))

def typewrite(*argv):
  for arg in argv:
    if arg == '<INPUT>':
      input("Enter any key to continue...")
      print("\033[A                             \033[A") # move cursor up 2 lines
    if arg == '<PAUSE>':
      time.sleep(0.7)
    else:
      # each arg will be a sentence
      for char in arg:
        time.sleep(0.05) # go to sleep for 0.05 secs
        sys.stdout.write(char) # prints char on screen (somehow differently?)
        sys.stdout.flush() # flushes char from ram memory using voodoo magic
      
      print() # This print exists to separate lines from one another
      time.sleep(0.1) # sleep before printing another sentence