#The summation of odd numbers / Code_Challenge_8.py 
print("The Summation of ODD NUMBERS")
num = int(input("Enter a number: "))

result = 0

for i in range(10):
    if num % 2 == 1:
        oddsum += num  

print("The total of all the ODD numbers - - - > ", result)
