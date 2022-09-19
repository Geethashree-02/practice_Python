user = list(input("Enter the string : "))
user2=user
print(user2)
word = user2[ : :-1]
count=0
word2=word
print(word2)
"""for i in user2:
    for j in word:
        if user[i]==word[j]:
            count+=1
            print(count)
        else:
            print("no match")
#wrong ansr
"""

"""for i in range(len(user2)):
    print(user2[i],end=" ")
print()
for j in range(len(word2)):
    print(word2[j],end=" ")
    if(user2[i]==word2[j]):
        count+=1
        print(count)
    else:
        print("Not  match")
#crt ansr
"""
for i in range(len(user2)):
    #print(user2[i],end=" ")
#print()
    for j in range(len(word2)):
        #print(word2[j],end=" ")
        if(user2[i]==word2[j]):
            count=count+1
            print(count)
        else:
        
        #print("Not  match")
           break
