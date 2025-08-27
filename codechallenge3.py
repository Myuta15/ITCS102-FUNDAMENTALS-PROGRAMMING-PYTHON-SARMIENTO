username = "MTS"
pin = "akg15"

name = input("please input your username > ")
password = input("Password?")

if password.lower() == pin and username == name:
		print("ACCESS GRANTED")

else: 
	print("ACCESS DENIED")
