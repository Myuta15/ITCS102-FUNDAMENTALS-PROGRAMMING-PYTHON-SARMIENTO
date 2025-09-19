#activity15
#name1 = 'russel'
#name2 = 'david'
#name3 = 'sarmiento'

#print("my name is", name1," ", name2," ", name3)
#print(f"my name is {name1} {name2} {name3}")

odd = 0
for i in range(1, 11, 1):
    num = eval(input(f"{i} - Enter a number - - > "))

    if num % 2 == 1:
        odd += num

print(f"The sum of all the ODD numbers given is:", {odd})