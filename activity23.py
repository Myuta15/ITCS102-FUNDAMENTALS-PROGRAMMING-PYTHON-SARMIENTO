months = ["jan", "feb", "mar", "apr", "may", "jun",]

#adding/appending item
months.append("aug")
print(months)

#remove/pop last item
months.pop()
print(months)

#removing a specific item
months.remove("mar")
print(months)

#insert a new item at index 2
months.insert(2, "dec")
print(months)

#the length
lenlist = len(months)
print("Length of the list:",lenlist)

#sorting alphabetically
months.sort()
print("Sorted list:", months)

# iteration
for m in months:
    print(f"{m},2025")


x = 'Dummy name'

#list slicing 

print(x[::-1])