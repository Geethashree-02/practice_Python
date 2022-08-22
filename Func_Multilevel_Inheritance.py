# Multilevel Inheritance

class Addition:
    def add(self):
        a = int(input("Enter the value for a : "))
        b = int(input("Enter the value for b : "))
        c = a+b
        print("Addition : ",c)

class Subtraction(Addition):
    def sub(self):
        a = int(input("Enter the value for a :"))
        b = int(input("Enter the value for b :"))
        c = a-b
        print("Subtraction : ",c)

class callfn(Subtraction):
    def func(self):
        self.add()
        self.sub()
        
obj = callfn()
obj.func()
