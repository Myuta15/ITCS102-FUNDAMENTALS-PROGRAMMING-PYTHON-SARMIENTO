print(" = = = = = = = = = ANIME ARCHIVE LIST = = = = = = = = = = = = = = = = = = ")
listed = []
while True:
    user = input("ENTER AN ANIME TITLE (type 'x' to exit): ")

    if user.lower() == "x":
         print("EXITING . . . ")
         break
    else: 
        listed.append(user)   
        print(f"{user} HAS BEEN ADDED. .")
    
print("ANIME ARCHIVED ARE THE FOLLOWING:")
for title in listed:
    print(f"• {title}")