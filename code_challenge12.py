for z in range(1, 7):
    for x in range(7, z, -1):
        print(" ", end=" ")
    for y in range(z, 0, -1):
        print(y, end=" ")
    for v in range(1, z):
        print(1+v, end=" ")
    print()