#Removal all characters from a string except integers

user = input("Enter the string : ")
print("".join(filter(str.isdigit,user)))
