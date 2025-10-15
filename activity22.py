
import random

print("Let's guess the number")

random_number = random.randint(1, 100)
tries = 0
con = True

while True:
    num = int(eval(input("Input an integer number - - - > ")))

    con += 1 

    if num == random_number: 
        print("CORRECT!")
        print(f"Only took {con} tries")
        break
    else:
        print("WRONG! TRY AGAIN!!!")
        print("CONTINUE...")
        continue