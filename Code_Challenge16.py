import os
import json

os.system("cls")
print("STUDENT INFORMATION SYSTEM")
print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")

student_records = {}

while True: 
    print("Select from the options: \nA - Add Information\nB - PRINT ALL Record\nC - SEARCH STUDENT RECORD\nD - DELETE A STUDENT Record\nE - EDIT STUDENT RECORD\nF - EXPORT DATA\n G - IMPORT DATA\n0- EXIT")
    print("MUST BE CAPITALIZED")
    choice = input("Your Choice - - - - > ").upper()

    if choice == 'A':
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
        student_records = {student_id: [first_name, last_name, course, email]}
        for id,record in student_records.items():
            print(f"Student ID {id} in STUDENT RECORD {record}")
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
            break
        continue

    elif choice == 'E':
        print("EDIT / MODIFY DATA . . .")

        search_id = input("TYPE THE SEARCH ID - ").upper()
        if search_id in student_records.keys():
            print("RECORD FOUND")
            for i in student_records[student_id]:
                print(f"- - {i}")

        student_id = input("NEW Key search for this student - - - > ").upper()
        first_name = input("Type the NEW Student's First name - - > ").upper()
        last_name = input("Type the NEW Student's Last name - - - > ").upper()
        course = input("Type the NEW Student's Course - - - > ").upper()
        email = input("Type the NEW Student's email address - - - > ")

        student_records[search_id][0] = first_name
        student_records[search_id][1] = last_name
        student_records[search_id][2] = course
        student_records[search_id][3] = email

        print("DATA UPDATED . .")
        continue
    elif choice == 'F':
        os.system("cls")
        print("EXPORTING DATA . . .") 

        with open("student_record.json","w") as new_file:
            json.dump(student_records,new_file,indent=4)
            print("DATA EXPORTED TO JASON")
            continue
    elif choice == "G":
        os.system("cls")
        print("IMPORTING DATA . . . ")
        
        with open("student_record.json","r") as new_file:
            student_json = json.load(new_file)
            print("Data Exported to json")

        
    
    elif choice == "0":
            
            print("EXITING THE PROGRAM. . .")
            break
    else:
        print("= = = INPUT [ I N V A L I D ]  = = = ")
        continue
