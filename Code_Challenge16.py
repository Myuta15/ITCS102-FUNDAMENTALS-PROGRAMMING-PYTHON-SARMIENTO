import os

student_records = {}

while True: 
    print("Select from the options: \nA - Add Information\nB - Search a Record\nC - Delete a Record\nD - Modify a Record\nE - Exit ").upper()

    choice = input("Your Choice - - - - > ")

    if choice == 'A':
        print("ADDING STUDENT INFORMATION")
        print("= = = = = = = = = = = = = = =")
        
        search_code = input("Key search for this student - - - > ").upper()
        first_name = input("Type the Student's First name - - > ").upper()
        last_name = input("Type the Student's Last name - - - > ").upper()
        course = input("Type the Student's Course - - - > ").upper()
        email = input("Type the Student's email address - - - > ")
        isSingle= input("ARE YOU AN MC OR TARNISH? (M / T) - - - >")

        student_records = {search_code : [first_name, last_name, course, email]}
        print("DATA SAVED")

        os.system('cls')
        continue

    elif choice == 'B':
        os.system('cls')
        code = input("Type the search code - - - > ")
        
        for j in student_records.keys():
            if code in student_records.keys():
                print("Record Found . . . ")