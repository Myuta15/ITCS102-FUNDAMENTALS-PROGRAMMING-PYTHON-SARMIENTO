#1 to 20 cold
#21 to 30 lukewarm 
#31 to 40 warm 
#41 to 50 hot 
#51 and above boiling hot

temp = eval(input("Enter Temperature - - - > "))

if temp >= 1 and temp <= 20:
	print("The Temperature is Cold") 

elif temp >= float("-inf"):
	print("The temparature is a Freezing Cold")

elif temp >= 21 and temp <= 30:
	print("The Temperature is LukeWarm")

elif temp >= 31 and temp <= 40:
	print("The Temperature is Warm")

elif temp >= 41 and temp <= 50:
	print("The Temperature is Hot")

elif temp >= 51:
	print("The temparature is Boiling Hot")

else: 

	print("invalid temperature")