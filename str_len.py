# find the length of the string
#Method_2

class strg:
    def m1(self):
        print("Method_1")
        strg="SHREE"
        print("The count is ")
        print(len(strg))

#Method_2
    def m2(self):
        print("Method_2")
        string="Geetha"
        count=0
        for i in string:
            count=count+1
        print("The count is ",count)

call=strg()
call.m1()
call.m2()
