print("ADDING DATA TO DICTIONARY")
print(" = = = = = = = = = = = = = = = = = = = = = = =")
tuloy = True
empty_dictionary ={}

def print_anime():
   if i,j in empty_dictionary.items():
      print(f"CODE = {i} \nTITLE= {j}")

def pang_search(key):
   print("Searching. . . ")
   print(f"Result shows {empty_dictionary[keys]} on our database")

while tuloy == True: 
    keys = input("Keys for this anime - - - > ").lower()
    value = input("Enter anime title  - - - > ").lower()
    
    empty_dictionary[keys] = value
    
    choice = input("Would you like to continue adding anime \n(y = Yes/n = No) \n(p = print)\n(s = Search) \n : ").lower()
    
    if choice == "y":
       print("Continuing . . . ")
       continue

    elif choice == "n":
       print("Exiting . . . . ")
       break
    elif choice == "p":
        print("Printing your list. . . . ")
        print_anime()
        continue
    elif choice == "s":
       code = input("Input the code of the anime: ")
       pang_search(code)
       continue
    else: 
       print("INPUT SOMETHING VALID")
       
print(empty_dictionary)


#The Search Won't Function Right
