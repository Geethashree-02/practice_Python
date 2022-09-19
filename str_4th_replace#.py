strg = input("Enter the string : ")
#print(strg.replace(" ","#"))
word = strg.maketrans(" ","#")
print(strg.translate(word))