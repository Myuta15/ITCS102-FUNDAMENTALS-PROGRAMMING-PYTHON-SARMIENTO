import os

os.system("cls")
print("STUDENT INFORMATION SYSTEM")
print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")

student_records = {}

while True: 
    print("Select from the options: \nA - Add Information\nB - PRINT ALL Record\nC - SEARCH STUDENT RECORD\nD - DELETE A STUDENT Record\nE - EDIT STUDENT RECORD\nF - EXPORT DATA\n 0- EXIT")
    print("MUST BE CAPITALIZED")
    choice = input("Your Choice - - - - > ")

    if choice == 'A':
        os.system("cls")
        print("ADDING STUDENT INFORMATION")
        print("= = = = = = = = = = = = = = =")
        
        student_id = input("Key search for this student - - - > ").upper()
        first_name = input("Type the Student's First name - - > ").upper()
        last_name = input("Type the Student's Last name - - - > ").upper()
        course = input("Type the Student's Course - - - > ").upper()
        email = input("Type the Student's email address - - - > ")
        

        student_records = {student_id: [first_name, last_name, course, email]}
        print("DATA SAVED")

        os.system('cls')
        continue

    elif choice == 'B':
        print("PRINTING STUDENT RECORDS")
        for id,record in student_records.items():
            print(F"Student ID {id} in STUDENT RECORD {record}")
        else: 
            print("NO RECORD FOUND . . . ")
        continue

    elif choice =='C':
        os.system('cls')
        search_id = input("TYPE THE ID TO SEARCH - ").upper()
        for id in student_records.keys():
            if search_id in student_records.keys():
                print("RECORD FOUND")
                for i in student_records[search_id]:
                    print(f"-- {i}")
        else: 
            print("NO RECORD FOUND")
        continue

    elif choice == 'D':
        os.system("cls")
        print("DELETING EXISTING RECORD . . . ")

        search_id = input("TYPE THE SEARCH ID - ").upper()
        if search_id in student_records.keys():
            print("RECORD FOUND")
            for i in student_records[student_id]:
                print(f"- - {i}")
            
            student_records.pop(search_id)
            print("RECORD REMOVED")
        else: 
            print(" NO RECORD FOUND ")
        continue

    elif choice == '0':
        print("SYSTEM EXIT")
        break
    elif choice == "P":
       pass
       continue
    else:
        print("\nINVALID CHOICE, PLEASE RE-ENTER YOUR CHOICE")
        continue