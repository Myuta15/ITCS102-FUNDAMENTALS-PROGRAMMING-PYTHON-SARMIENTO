
i = eval(input("Enter a number: "))

for i in range(1, 11, 1):
    for y in range(1, i, 1):
        print(" ",end=" ")
    for z in range(10, i, -1):
        print("*", end= " ")
    print() 

#spaces in the ("") can affect the spacing. so if i were to remove the space
#in y's print it'd be a triangle