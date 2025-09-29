Clean = True 

while Clean == True:
    qst = input("Are the clothes clean ? (y/n): ")

    if qst.lower() == "y":
        print("Loop Continue")
        continue 

     
    else:
        print("Loop Stops")
        break