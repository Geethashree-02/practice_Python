#  SINGLE INHERITANCE

class Addition:
    def add(self):
        a=int(input("Enter the value for a :"))
        b=int(input("Enter the value for b :"))
        c = a+b
        print("Addition :",c)

class Subtraction(Addition):
    def sub(self):
        self.add()
        a=int(input("Enter the value for a :"))
        b=int(input("Enter the value for b :"))
        c = a-b
        print("Subtraction :",c)

obj = Subtraction()
obj.sub()
