
import os

# This will serve as the stopping point of the program/code.
# What is "Def": def [vname]: [built in function]
def pause():
    input("\nPress ENTER to continue...")


name = input("Person using. . . ?: ")
#INTRODUCTION
print(" = = = = = = = = = = = = = = = = = = = = = = = = = =")
print("WELCOME TO MY CODE COMPILER :D", "[", name, "]")
print("= = = = = = = = = = = = = = = = = = = = = = = = = = =")

#Basics Codes here (print, variables, operators, conditionals, etc)
#List all of the functions, Then create the menu so you can correct it simpler!!.

def pyprintbasic():
    print("\n= = = = = = = = = = = = = = = = = = = = = =")
    print("== BASIC FUNCTION OF PRINT ==")
    print("Hello World!!")
    print("- - - - - - - - - - - - -")
    print("Line: print('Hello World!!')")
    pause()
    os.system("cls")
def pyprintbasic2():
    print("\n= = = = = = = = = = = = = = = = = = = = = =")
    print("== What are the Variables? ==")
    print("For this we have: name = 'Johan' ")
    name = "Johan"
    print("Then line the code like this: print('My name is', name)")
    print("My name is", name)
    pause()

def pyprintbasic3():
    print("\n= = = = = = = = = = = = = = = = = = = = = =")
    print("== Variable W Print ==")
    print("Variable = 16")
    baria = 16
    print("Alex is", baria, "years old.")
    pause()
    os.system("cls")
# I'll be back with some progress. [Marked: 4:14 pm 12/12/25] 

def pyprintbasicsub():
    while True:
        print("==================================")
        print("= = PRINT FUNCTIONS = = ")
        print("==================================")
        print("[1]-BASIC EXAMPLE OF PRINT")
        print("==================================")
        print("[2]-WHAT ARE VARIABLES")
        print("==================================")
        print("[3]-VARIABLE AND PRINT")
        print("==================================")
        print("[0]-RETURN TO MAIN MENU")
        print("==================================")

        printchoice = input("Selection: ")

        if printchoice == "1":
            pyprintbasic()
        elif printchoice == "2":
            pyprintbasic2()
        elif printchoice == "3":
            pyprintbasic3()
        elif printchoice == "0":
            break
        else:
            print("INVALID . . . SELECT A NUMBER")
        os.system("cls")
# PRINT FUNCTION DONE [MARKED: 4:56PM 12/12/25]
# -----------------------------------------------------------------------
def pyvariablebasic():
    print("\n= = = = = = = = = = = = = = = = = = = = = =")
    print("== Variables ==")
    print("Variables can be anything, like x = 3 or y = johan")
    pause()
    os.system("cls")

def pyvariablebasic2():
        print("== Variables Application ==")
        xerov = "johan"
        yuta = "3"
        print("The boy named", xerov, "is", yuta, "years old")
        pause()
        os.system("cls")

def pyvariablebasicsub():
    while True:
        print("==================================")
        print("= = VARIABLE FUNCTIONS = = ")
        print("==================================")
        print("[1]-VARIABLES")
        print("==================================")
        print("[2]-VARIABLES APPLICATION")
        print("==================================")
        print("[3]-RETURN TO MAIN MENU")
        print("==================================")
    
        variablechoice = input("Selection: ")

        if variablechoice == "1":
            pyvariablebasic()
        elif variablechoice  == "2":
            pyvariablebasic2()
        elif variablechoice  == "3":
            break
        else:
            print("INVALID . . . SELECT A NUMBER")
        os.system("cls")
# VARIABLE FUNCTION DONE [MARKED: 5:56PM 12/12/25]
# -----------------------------------------------------------------------
def pyoperatorbasic():
    print("== ARITMETIC OPERATORS ==")
    print("\n+ = addition \n- = subtraction \n* = multiplication \n/ = division \n% = modulus \n** = exponentiation \n// = Floor Division")

def pyoperatorbasic2():
    print("== ARITMETIC APPLICATION ==")
    x = 3
    y = 40
    print("x = 3, y = 40")
    print("x + y =", x + y)
    print("x - y =", x - y)
    print("x * y =", x * y)
    print("x / y =", x / y)
    print("x // y =", x // y)
    print("x % y =", x % y)
    print("x ** y =", x ** y)
    pause()
    os.system("cls")
def pyoperatorbasic3():
    print("== COMPARISON OPERATORS ==")
    print("\n== = equals \n!= = not equal \n> = greater than \n< = less than \n>= = greater or equal \n<= = less than or equal")

def pyoperatorbasic4():
     print("== COMPARISON APPLICATION ==")
     print("The operators will respond with true or false.") 
     king = 100
     commoner = 15
     print("king = 100, commoner = 15")
     print("king == commoner =", king == commoner)
     print("king != commoner =", king != commoner)
     print("king > commoner =", king > commoner)
     print("king < commoner =", king < commoner)
     print("king >= commoner =", king >= commoner)
     print("king <= commoner =", king <= commoner)
     pause()
     os.system("cls")
def pyoperatorbasic5():
    print("== LOGICAL OPERATORS ==")
    print("and, or, not")
    print("The operators will determine if the variables are true or false.") 
    print("example: x = 100, x > 50 = True")

def pyoperatorbasic6():
    print("== LOGICAL APPLICATION ==")
    judy = 100
    john = 400
    jacob = 500
    print("judy = 100, john = 400, jacob = 500")
    print("=================================")
    print("judy < john and john < jacob")
    print("V---------------------------------")
    print(judy < john and john < jacob)
    print("==================================")
    print("john == jacob and judy < john")
    print("V---------------------------------")
    print(john == jacob or judy < john)
    print("==================================")
    print("(not(judy != john and judy > jacob))")
    print("V---------------------------------")
    print(not(judy != john and judy > jacob))
    print("==================================")
    pause()
    os.system("cls")
def pyoperatorbasicsub():
    while True:
        print("==================================")
        print("\n= = OPERATORS FUNCTIONS = = ")
        print("==================================")
        print("[1]-ARITHMETIC OPERATOR")
        print("==================================")
        print("[2]-LOGICAL OPERATOR")
        print("==================================")
        print("[3]-COMPARISON OPERATOR")
        print("==================================")
        print("[0]-RETURN TO MAIN MENU")
        print("==================================")

        operatorchoice = input("SELECTION: ")
        if operatorchoice == "1":
         pyoperatorbasicsub2()
        elif operatorchoice =="2":
         pyoperatorbasicsub3()
        elif operatorchoice == "3":
         pyoperatorbasicsub4()
        elif operatorchoice == "0":
         break
        else:
         print("INVALID . . . SELECT A NUMBER")
    os.system("cls")
def pyoperatorbasicsub2():
    while True:
        print("==================================")
        print("\n== ARITHMETIC FUNCTIONS ==")
        print("==================================")
        print("[1]-ARITHMETIC OPERATOR")
        print("==================================")
        print("[2]-ARITHMETIC APPLICATION")
        print("==================================")
        print("[0]-RETURN")
        print("==================================")

        operatorchoice1 = input("SELECTION: ")
        if operatorchoice1 == "1":
         pyoperatorbasic()
        elif operatorchoice1 =="2":
         pyoperatorbasic2()
        elif operatorchoice1 == "0":
         break  
        else:
         print("INVALID . . . SELECT A NUMBER")
    os.system("cls")
def pyoperatorbasicsub3():
    while True:
     print("==================================")
     print("\n== LOGICAL FUNCTIONS ==")
     print("==================================")
     print("[1]-LOGICAL OPERATOR")
     print("==================================")
     print("[2]-LOGICAL APPLICATION")
     print("==================================")
     print("[0]-RETURN")
     print("==================================")

     operatorchoice2 = input("SELECTION: ")
     if operatorchoice2 == "1":
         pyoperatorbasic3()
     elif operatorchoice2 =="2":
         pyoperatorbasic4()
     elif operatorchoice2 == "0":
         break
     else:
         print("INVALID . . . SELECT A NUMBER")
    os.system("cls")
def pyoperatorbasicsub4():
    while True:
     print("==================================")
     print("\n== COMPARISON FUNCTIONS ==")
     print("==================================")
     print("[1]-COMPARISON OPERATOR")
     print("==================================")
     print("[2]-COMPARISON APPLICATION")
     print("==================================")
     print("[0]-RETURN")
     print("==================================")

     operatorchoice3 = input("SELECTION: ")
     if operatorchoice3 == "1":
         pyoperatorbasic5()
     elif operatorchoice3 =="2":
         pyoperatorbasic6()
     elif operatorchoice3 == "0":
         break
     else:
         print("INVALID . . . SELECT A NUMBER")
    os.system("cls")
# OPERATORS FUNCTION DONE [MARKED: 7:33PM 12/12/25]
# ----------------------------------------------------------------------- 
def pyconditionalbasic():
    print("== EXAMPLE OF IF / CONDITIONALS FUNCTIONS ==")
    print("It's similar to logical operators (and, or, not)")
    print("But it serves as a statement, 'Condition' as it is called")
    print("it will only perform the action IF the condition is met.")
    print("==================================")
    print("variables: x = 30, y = 3, z = 0")
    print("==================================")
    print("statement: if x * y < z \nprint:('Greater')")
    print("==================================")
    x = 30 
    y = 3
    z = 0
    if x * y < z:
        print("Greater")
    pause()
    os.system("cls")

def pyconditionalbasic2():
    print("== EXAMPLE OF ELIF / CONDITIONALS FUNCTIONS ==")
    print("This condition is a addon to the list of conditions")
    print("IF is the main/start of the condition list, while ELIF is the following/added conditions.")
    print("==================================")
    print("variables: x = 30, y = 3, z = 0")
    print("==================================")
    print("statement: if x * y > z \nprint:('Greater') \nelif x / y == y: \nprint('Possible')")
    x = 30 
    y = 3
    z = 0
    if x * y > z:
        print("Greater")
    elif x / y == y:
        print("Possible")
    pause()
    os.system("cls")

def pyconditionalbasic3():
    print("== EXAMPLE OF ELSE / CONDITIONALS FUNCTIONS ==")
    print("This condition will serve as the checkpoint for the rest of the conditions.")
    print("If an input or result didn't meet the conditions, this condition will be executed.")
    print("==================================")
    print("Conditions: \nIf dummy == 'apple': print('same :D') \nelif dummy == 'guava': print('No way :o') \nelse: print('meh :/')")
    print("==================================")
    print("what's your favorite fruit?")
    print("==================================")

    dummy = input("what's your favorite fruit? ")
    if dummy == "apple":
        print("same :D")
    elif dummy == "guava":
        print("No way :o")
    else: 
        print("meh :/")
    pause()
    os.system("cls")

def pyconditionalbasicsub():
 while True:
    print("==================================")
    print("\n== CONDTIONAL FUNCTIONS ==")
    print("==================================")
    print("[1]-IF CONDITION")
    print("==================================")
    print("[2]-ELIF CONDITION")
    print("==================================")
    print("[3]-ELSE CONDITION")
    print("==================================")
    print("[0]-RETURN")
    print("==================================")

    conditionalchoice = input("SELECTION: ")
    if conditionalchoice == "1":
        pyconditionalbasic()
    elif conditionalchoice == "2":
        pyconditionalbasic2()
    elif conditionalchoice == "3":
        pyconditionalbasic3()
    elif conditionalchoice == "0":
        break
    else:
        print("INVALID . . . SELECT A NUMBER")
# OPERATORS FUNCTION DONE [MARKED: 8:53PM 12/12/25]
# ----------------------------------------------------------------------- #

def pyloopsbasic1():
    print("== FOR LOOP FUNCTIONS ==")
    print("Loop is used for iterating over a sequence (list, a tuple, a dictionary, a set, or a string)")
    print("It will repeat until it reach the chosen range. ranging from 0 to infinity")
    print("\t\tfor [variable] in [list/sequence]:")
    print("List: box = [cat, dog, mouse, snake, goat, hamster] \nVariable: For x in box:")
    pause()
    

def pyloopsbasic2():
    print("== FOR LOOP APPLICATION ==")
    box = ["cat", "dog", "mouse", "snake", "goat", "hamster"]
    for x in box:
        print(x)
    print("To stop the loop use 'break'")
    print("if x == 'mouse': \n\tbreak")
    print("output:\ncat \ndog \nmouse")
    pause()
    

def pyloopsbasic3():
    print("== WHILE LOOP FUNCTION ==")
    print("It will repeat a statement as long as the condition is true/met")
    print("This can be as simple as a counter or timer")
    print("[variable] = 1, \nWhile [variable] < 10: \nprint([variable]) \n[variable] +=1")
    pause()
    os.system("cls")
def pyloopbasic4():
    print("\n== WHILE LOOP APPLICATION ==")
    print("f = 1 \nwhile f <= 10: \nprint(f) \nf += 1")
    f = 1
    while f <= 10:
        print(f)
        f += 1
    pause()
    os.system("cls")



def pyloopbasic5():
    print("== WHILE NESTED LOOP FUNCTION ==")
    print("Same as the others loop but this one is nested or grouped with or within a loop")
    print("Example: \nitem1 =['Cat', 'mouse', 'man', 'Plant'] \nitem2=['Pet', 'Pet', 'Owner', 'Household']")
    print("for y in item1:")
    print("for x in item2:")
    print("\nprint(y,x)")
    print("\nThose variables with brackets can be found on the LIST FUNCTION")
    pause()
    os.system("cls")

def pyloopbasic6():
    print("== NESTED LOOP APPLICATION ==")
    item1 = ["Cat", "mouse", "man", "Plant"]
    item2 = ["Pet", "Pet", "Owner", "Household"]
    for y in item1:
        for x in item2:
            print(y,x)
    pause()
    os.system("cls")

def pyloopbasicsub(): #MAIN MENU OF LOOP = = =  = = = = ====================================================================
 while True:
     print("==================================")
     print("[1]-FOR LOOP FUNCTION")
     print("==================================")
     print("[2]-WHILE LOOP FUNCTION")
     print("==================================")
     print("[3]-NESTED LOOP FUNCTION")
     print("==================================")
     print("[4]-RETURN TO MAIN MENU")
     print("==================================")

     loopchoice = input("SELECTION: ")

     if loopchoice == "1":
        pyloopbasicsub2()
     elif loopchoice == "2":
        pyloopbasicsub3()
     elif loopchoice == "3":
        pyloopbasicsub4()
     elif loopchoice == "4": 
        break
     
def pyloopbasicsub2():
 while True:
    print("==================================")
    print("[1]-FOR LOOP FUNCTION")
    print("==================================")
    print("[2]-FOR LOOP APPLICATION")
    print("==================================")
    print("[3]-RETURN")
    print("==================================")
    loopchoice2 = input("SELECTION: ")
    if loopchoice2 == "1":
     pyloopsbasic1()
    elif loopchoice2 == "2":
     pyloopsbasic2()
    elif loopchoice2 == "3":
     break
    os.system("cls")

def pyloopbasicsub3():
 while True:
    print("==================================")
    print("[1]-WHILE LOOP FUNCTION")
    print("==================================")
    print("[2]-WHILE LOOP APPLICATION")
    print("==================================")
    print("[3]-RETURN")
    print("==================================")
    loopchoice3 = input("SELECTION: ")
    if loopchoice3 == "1":
     pyloopsbasic3()
    elif loopchoice3 == "2":
     pyloopbasic4()
    elif loopchoice3 == "3":
     break
    os.system("cls")
def pyloopbasicsub4():
    while True:
        print("==================================")
        print("[1]-NESTED LOOP FUNCTION")
        print("==================================")
        print("[2]-NESTED LOOP APPLICATION")
        print("==================================")
        print("[3]-RETURN")
        print("==================================")
        loopchoice3 = input("SELECTION: ")
        if loopchoice3 == "1":
         pyloopbasic5()
        elif loopchoice3 == "2":
         pyloopbasic6()
        elif loopchoice3 == "3":
         break
        os.system("cls")
# LOOP FUNCTIONS DONE [MARKED: 11:21PM 12/12/25] 

def pylistsbasic():
    
    print("=== WHAT IS A LIST..? ===")
    print("A 'List' is a collection of objects that can be arranged or changed")
    print("It is able to store multiple items or objects inside a 'single' variable ")
    print("Example: \nbasket =['bread', 'fruits', 'jars', 'cups', 'towels'] print(basket) \nprintinghere = 'I am' \nprintinghere2 = 'Johan' \nconclusion = 'Smirnoff' \norderlyfunction = [printinghere, printinghere2, conclusion,] \nprint(orderlyfunction)")
    print("OUTPUT: ['bread', 'fruits', 'jars', 'cups', 'towels'] \n['I am', 'Johan', 'Smirnoff']")
    pause()
    os.system("cls")

def pylistsbasic2():
   print("=== LIST APPLICATION ===")
   print("These are the different things you can do to change a list")
   print("• APPEND = To add an object at the end of the list")
   print("• CLEAR = Removes all the elements from the list")
   print("• COPY = Returns a copy of the list")
   print("• COUNT =	Returns the number of elements with the specified value")
   print("• Extend = Add the elements of a list or any iterable, to the end of the list")
   print("• Index = Returns the index of the first element with the specified value")
   print("• Insert = Adds an element at a specified position")
   print("• Pop	= Removes an element at a specified position")
   print("• Remove = Removes the first item with the specified value")
   print("• Reverse = Reverses the order of the list")
   print("• Sort = Sorts the list")
   print("\nexamplelist=['Johan', 'Adam', 'Yuri', 'Nick', 'Alex', 'Bert']")
   print("============================================================|")
   print("APPEND:                                                     |")
   print("examplelist.append('Chris')                                 |")
   print("============================================================|")
   print("Output: ['Johan', 'Adam', 'Yuri', 'Nick', 'Alex', 'Bert', 'Chris']🔨(^u^ )")
   print("============================================================|")
   print("                                                            |")
   print("CLEAR:                                                      |")
   print("examplelist.clear()                                         |")
   print("============================================================|")
   print("Output: []                                                  |")
   print("============================================================|")
   print("                                                            |")
   print("COPY:                                                       |")
   print("newlist = examplelist.copy()                                |")
   print("============================================================|")
   print("Output:                                                     |")
   print("newlist = ['Johan', 'Adam', 'Yuri', 'Nick', 'Alex', 'Bert'] |")
   print("============================================================|")
   print("                                                            |")
   print("COUNT:                                                      |")
   print("examplelist.count('Adam')                                   |")
   print("============================================================|")
   print("Output: 1                                                   |")
   print("============================================================|")
   print("                                                            |")
   print("EXTEND:                                                     |")
   print("examplelist.extend(['Liam', 'Noah'])                        |")
   print("============================================================|")
   print("Output: ['Johan', 'Adam', 'Yuri', 'Nick', 'Alex', 'Bert', 'Liam', 'Noah']🔨(0v0 )")
   print("============================================================|")
   print("                                                            |")
   print("INDEX:                                                      |")
   print("examplelist.index('Alex')                                   |")
   print("============================================================|")
   print("Output: 4                                                   |")
   print("============================================================|")
   print("                                                            |")
   print("INSERT:                                                     |")
   print("examplelist.insert(2, 'Emma')                               |")
   print("============================================================|")
   print("Output: ['Johan', 'Adam', 'Emma', 'Yuri', 'Nick', 'Alex', 'Bert']🔨(•̀ ᗜ •́ )")
   print("============================================================|")
   print("                                                            |")
   print("POP:                                                        |")
   print("examplelist.pop(1)                                          |")
   print("============================================================|")
   print("Output: ['Johan', 'Yuri', 'Nick', 'Alex', 'Bert']           |")
   print("============================================================|")
   print("                                                            |")
   print("REMOVE:                                                     |")
   print("examplelist.remove('Nick')                                  |")
   print("============================================================|")
   print("Output: ['Johan', 'Adam', 'Yuri', 'Alex', 'Bert']           |")
   print("============================================================|")
   print("                                                            |")
   print("REVERSE:                                                    |")
   print("examplelist.reverse()                                       |")
   print("============================================================|")
   print("Output: ['Bert', 'Alex', 'Nick', 'Yuri', 'Adam', 'Johan']   |")
   print("============================================================|")
   print("                                                            |")
   print("SORT:                                                       |")
   print("examplelist.sort()                                          |")
   print("============================================================|")
   print("Output: ['Adam', 'Alex', 'Bert', 'Johan', 'Nick', 'Yuri']   |")
   print("============================================================|")

   print("Extra: the value of the list starts from 0 not 1. so in this list example: Johan is 0 and Adam is 1.")
   pause()
   os.system("cls")

def pylistsbasicsub():
 while True:
    print("[1]-WHAT IS A LIST FUNCTION")
    print("[2]-LIST APPLICATION")
    print("[3]-RETURN TO MAIN MENU")

    listchoice =input("SELECTION: ")
    if listchoice == '1':
     pylistsbasic()
    elif listchoice == '2':
     pylistsbasic2()
    elif listchoice == '3':
     os.system("cls")
     break
    else: 
       print("INVALID!!!!!!")
# LIST FUNCTIONS DONE [MARKED: 12:58PM 12/13/25] 
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #
def pyfunctionsbasic():
   print("=== WHAT IS A FUNCTION? ===")
   print("It is a block of code which only runs when it is called.")
   print("it helps avoiding code repetition and a lengthy code.")
   print("it uses the word 'def' to define the function.")
   print("So as an example: \n def 'pyfunctionsbasic(): \nprint('HELLO WORLD') ")
   pause()
   os.system("cls")
def pyfunctionsbasic2():
   print("=== FUNCTION APPLICATION ===")
   print("def quickmathz(num): \nreturn (num * 140 - 60 \nprint(quickmathz(22)) \nprint(quickmathz(50)) \nprint(quickmathz(400))" )
   print("RESULT: ")
   def quickmathz(num): 
      return (num * 140 - 60)
   print(quickmathz(22))
   print(quickmathz(50))
   print(quickmathz(400))
   
   print("Extra: If you need to create a function placeholder without any code, use 'pass'")
   pause()
   os.system("cls")

def pyfunctionsbasicsub():
 while True:
   print("==================================")
   print("[1]-WHAT IS A FUNCTION?")
   print("==================================")
   print("[2]-FUNCTION APPLICATION")
   print("==================================")
   print("[3]-RETURN")
   print("==================================")
   
   functionchoice = input("SELECTION: ")

   if functionchoice == '1':
      pyfunctionsbasic()
   elif functionchoice == '2':
      pyfunctionsbasic2()
   elif functionchoice == '3':
      os.system("cls")
      break
   

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #
# = = = = = = = MENU HERE = = = = = ! ! = ! ! = = = = ! ! = = = = #

def mainmenu():
    while True:
        print("============= MAIN MENU ==========")
        print("\t[1] - Print Statements")
        print("==================================")
        print("\t[2] - Variables")
        print("==================================")
        print("\t[3] - Operators")
        print("==================================")
        print("\t[4] - Conditional")
        print("==================================")
        print("\t[5] - Loops")
        print("==================================")
        print("\t[6] - Lists")
        print("==================================")
        print("\t[7] - Functions")
        print("==================================")
        print("\t[E] - EXIT")
        print("==================================")
        mainchoice = input("Selection: ")

        if mainchoice == "1":
            pyprintbasicsub()
        elif mainchoice == "2":
            pyvariablebasicsub()
        elif mainchoice  == "3":
            pyoperatorbasicsub()
        elif mainchoice  == "4":
            pyconditionalbasicsub()
        elif mainchoice  == "5":
            pyloopbasicsub()
        elif mainchoice == "6":
            pylistsbasicsub()
        elif mainchoice  == "7":
            pyfunctionsbasicsub()
        elif mainchoice  == "E":
            print('\nEXITING THANK YOU FOR USING MY PROGRAM!!!')
            break
        else: 
            print(" INVALID CHOICE !!!")
mainmenu()


# Notes:
# Errors that occured: 29 [ 11:21pm ] 12/12/2025
# -Repeating Menu 
# -Fail to Run
# -Starting print vanishing 
# -Nullified conditions (not accepting or low opacity text)
# Cause: Improper alignment and unexpected index. 

