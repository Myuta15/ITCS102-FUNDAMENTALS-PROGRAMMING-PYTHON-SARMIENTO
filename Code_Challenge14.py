
name = input("Enter your name")
print("Hi what is your name ? - - > ", name)
print("= = = = = = = = = = = = = = = = = = = = = = = = = =")
print("ODD NUMBER COMPILER, TYPE '0' TO TERMINATE THE LOOP ")
sum = 0
odd = ""

con = True

while con == True: 
    num = eval(input("Enter a number - - - > "))

    if num % 2 == 1:
        print("ODD NUMBER DETECTED")
        odd += str(num) + ","
        sum += num
        continue
    elif num == 0: 
        print("Terminated")
        break
    else: 
        if num % 2 == 0:
            print("EVEN NUMBER DETECTED, SKIPPING. . . ")
        else:
            print("INVALID NUMBER")
        continue


print(f"Hi {name}, the sum of all ODD number is {sum}")