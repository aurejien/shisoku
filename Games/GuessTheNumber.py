#python 3.7.1
#GuessTheNumber
import time
from random import randint
print("-----------------------------------")
print("         Code by åurejien          ")
print("        github.com/aurejien        ")
print("-----------------------------------")
print()
print()
print("----------------------------------------------\n")
print("               Guess the number                 ")
print("                  4 levels                     \n")
print("----------------------------------------------\n")
print()
name = input("Your name?. . \n→ ")
name = name.title()
print()
print("Choose your level:")
level = int(input("{1} Easy \n{2} Hard \n{3} Extrem \n{4} Lucky \n{X} Coming Soon \n→ "))
print()
if level == 1:
  print("Easy level, \nGuess one number between 1 & 100 \nOnly 6 try\n")
  x = 6
  a = randint(1, 100)
  level_num = 100
  nun = int(input("{1} Ready?\n→ "))
  print("----------------------------------------------\n")
elif level == 2:
  print("Hard level, \nGuess one number between 1 & 500 \nOnly 10 try\n")
  x = 10
  a = randint(1, 500)
  level_num = 500
  nun = int(input("{1} Ready?\n→ "))
  print("----------------------------------------------\n")
elif level == 3:
  print("Extrem level, \nGuess one number between 1 & 1000 \nOnly 10 try\n")
  x = 10
  a = randint(1, 1000)
  level_num = 1000
  nun = int(input("{1} Ready?\n→ "))
  print("----------------------------------------------\n")
elif level == 4:
  print("Well done you choose the Lucky version, \nGuess one number between 1 & 200 \nWith a random try among 5 & 10\n")
  x = randint(5,10)
  a = randint(1, 200)
  level_num = 200
  nun = int(input("{1} Ready?\n→ "))
  print("----------------------------------------------\n")
print("{0} Open the menu")
print()

while x != 0:
  try:
    if x == 1:
      print("Last try")
    else:
      print(x, "try")
    n = int(input("Guess?  → "))
    x += -1
    if n == a:
      print("You won...")
      print("Well done", name)
      print("----------------------------------------------\n")
      print(name, "Play again? ")
      restart = int(input("{1} yes\n{0} no\n→ "))
      print()
      if restart == 1:
        if level == 1:
          x = 6
          a = randint(1, 100)
          level_num = 100
        elif level == 2:
          x = 10
          a = randint(1, 500)
          level_num = 500
        elif level == 3:
          x = 10
          a = randint(1, 1000)
          level_num = 1000
        elif level == 4:
          x = randint(5,10)
          a = randint(1, 200)
          level_num = 200
        print("{0} Open the menu")
        print()
        print("----------------------------------------------\n")
      else:
        print("----------------------------------------------\n")
        print("Thanks for playing\nGoodbye", name,".\n")
        print("----------------------------------------------\n")
        break
    elif n == 0:
      print()
      print("----------------------------------------------\n")
      menu = int(input("{1} Change the difficulty\n{2} Win more try\n{3} Change your name\n{4} Leave the game\n→ "))
      if menu == 1:  
        print("Choose your level:")
        level = int(input("{1} Easy\n{2} Hard \n{3} Extrem \n{4} Lucky \n→ "))
        print()
        if level == 1:
          print("Easy level, \nGuess one number between 1 & 100 \nOnly 6 try")
          x = 6
          a = randint(1, 100)
          level_num = 100
          nun = int(input("{1} Ready?\n→ "))
          print("----------------------------------------------\n")
          print("{0} Open the menu")
          print() 
        elif level == 2:
          print("Hard level, \nGuess one number between 1 & 500 \nOnly 10 try")
          x = 10
          a = randint(1, 500)
          level_num = 500
          nun = int(input("{1} Ready?\n→ "))
          print("----------------------------------------------\n")
          print("{0} Open the menu")
          print()
        elif level == 3:
          print("Extrem level, \nGuess one number between 1 & 1000 \nOnly 10 try")
          x = 10
          a = randint(1, 1000)
          level_num = 1000
          nun = int(input("{1} Ready?\n→ "))
          print("{0} Open the menu")
          print()
          print("----------------------------------------------\n") 
        elif level == 4:
          print("Well done you choose the Lucky version, \nGuess one number between 1 & 200 \nWith a random try among 5 & 10\n")
          x = randint(5,10)
          a = randint(1, 200)
          level_num = 200
          nun = int(input("{1} Ready?\n→ "))
          print("----------------------------------------------\n")
          print("{0} Open the menu")
          print()
      elif menu == 2:
        print()
        print("----------------------------------------------\n")
        print("Mini gane.")
        print("Win the game with the higher card\n")
        nun = int(input("{1} Ready?\n→ "))
        miniH = randint(1, 20)
        miniO = randint(1, 20)
        print("Your card", miniH, "- the computer", miniO)
        if miniH >= miniO:
          x += 6
          print(name, "you won")
          print("You own 5 try more")
          print("----------------------------------------------\n")
          nun = int(input("{1} Back to the game\n→ "))
          print("----------------------------------------------\n")
          print()
        else:
          x += 1
          print(name, "you lost")
          print("Sorry try again")
          print("----------------------------------------------\n")
          nun = int(input("{1} Back to the game\n→ "))
          print("----------------------------------------------\n")
          print()
      elif menu == 3:
        x += 1
        print(name, "you want to change your name ?")
        name = input("The new one:\n→")
        name = name.title()
        print()
        print("Well", name, "is your new name")
        nun = int(input("{1} Ready?\n→ "))
        print("----------------------------------------------\n")
        print() 
      else:
        print("----------------------------------------------\n")
        print("Thanks for playing\nGoodbye", name,".")
        print()
        print("----------------------------------------------\n")
        break
    elif x == 0:
      print("You lost the number was", a)
      print()
      print("----------------------------------------------\n")
      print(name, "play again? ")
      restart = int(input("{1} yes\n{0} no\n→ "))
      print()
      if restart == 1:
        if level == 1:
          x = 6
          a = randint(1, 100)
          level_num = 100
        elif level == 2:
          x = 10
          a = randint(1, 500)
          level_num = 500
        elif level == 3:
          x = 10
          a = randint(1, 1000)
          level_num = 1000
        elif level == 4:
          x = randint(5,10)
          a = randint(1, 200)
          level_num = 200
        print("{0} Open the menu")
        print()
        print("----------------------------------------------\n")
      else:
        print("----------------------------------------------\n")
        print("Thanks for playing\nGoodbye", name,".\n")
        print("----------------------------------------------\n")
        break
    elif n < 1 or n > level_num:
      print("Only a number between 1 &",level_num,".")
      x += 1
    elif n < a:
      print("Higher")
      print()
    elif n > a:
      print("Smaller")
      print()
  except ValueError:
    print("Value Error")
    print()
    continue
