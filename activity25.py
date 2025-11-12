from activity25_1 import *
from actvitity25_2 import *


name = input("Hi, what's your name ? > ")
print(f"Welcome {name}, to my compiler program")

iscontinue=True

while iscontinue == True:
    print("Select a program")
    print("A -activity1\nB - activity2\nC activity15\nD - Factorial\nE-Exit")

    choose = input("What program / code do you want to select?").lower()

    if choose == 'a':
    activity1()
    continue

    elif choose == 'b':
    activity2()
    continue

    elif choose == 'c':
    activity15()
    continue

    elif choose == 'd':
    print("factorial program")
    num = input("Input a number - - - > ")
    print(f"The factorial of {num} is {factorial (num)}")
    continue

    elif choose == 'e':
    print("Exiting the program . . .")
    break



#activity25_1.py

