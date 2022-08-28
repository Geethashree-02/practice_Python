#swap numbers without using 3rd vairable
#Method_1
class fun:
    def M1(self):
        a=7
        b=5
        print("Method_1")
        print("Before swapping a : ",a," and b : ",b)
        a,b=b,a
        print("After swapping a : ",a," and b : ",b)


#swap numbers without using 3rd vairable
#Method_2

    def M2(self):
        a=7
        b=3
        print("Method_2")
        print("Before swapping a : ",a," and b : ",b)
        a=a+b
        b=a-b
        a=a-b
        print("After swapping a = ",a," and b = ",b)


        
obj=fun()
obj.M1()
obj.M2()

#swap string without using 3rd vairable
#Method_3
def M3():
        a="SITA"
        b="RAM"
        print("Method_1")
        print("Before swapping a : ",a," and b : ",b)
        a,b=b,a
        print("After swapping a : ",a," and b : ",b)

M3()

