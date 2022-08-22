#  MULTIPLE INHERITANCE(Method1)

class Addition:
    def add(self):
        a=int(input("Enter the value for a :"))
        b=int(input("Enter the value for b :"))
        c = a+b
        print("Addition :",c)

class Subtraction:
    def sub(self):
        a=int(input("Enter the value for a :"))
        b=int(input("Enter the value for b :"))
        c = a-b
        print("Subtraction :",c)
class Input(Addition,Subtraction):
    def base(self):
        self.add()
        self.sub()

obj=Input()
obj.base()
